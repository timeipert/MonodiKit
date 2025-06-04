import glob
import random
import os
import pickle
import logging
from typing import Any, Callable, Dict, List, Optional

from .document import Chant
from .source import create_source

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Corpus:
    """
    A collection of chants loaded from a directory.

    Parameters:
    -----------
    directory : Optional[str]
        A glob pattern (e.g., "../data/*") pointing to source directories.
        If None and use_pkl is provided, the corpus will be loaded from the pickle file.

    sample : int, optional
        Number of chants to sample at random. Defaults to 0 (no sampling).

    filters : Optional[Callable[[Any, Any], bool]]
        A callable that takes (chant_meta, source_meta) and returns True if the chant
        should be included. Defaults to None (no filtering).

    use_pkl : Optional[str]
        Path to a pickle file. If it exists, load the corpus from it; otherwise,
        build the corpus and save it to this path.
    """

    def __init__(
        self,
        directory: Optional[str] = None,
        sample: int = 0,
        filters: Optional[Callable[[Any, Any], bool]] = None,
        use_pkl: Optional[str] = None,
    ) -> None:
        # If a pickle path is given and exists, load from pickle
        if use_pkl and os.path.exists(use_pkl):
            try:
                with open(use_pkl, "rb") as f:
                    corpus_data = pickle.load(f)
                self.directory = corpus_data.directory
                self.filters = corpus_data.filters
                self.documents = corpus_data.documents
                self.sample = corpus_data.sample
                self.sources = corpus_data.sources
                return
            except Exception as e:
                logger.warning(f"Failed to load Corpus from pickle '{use_pkl}': {e}")

        # Otherwise, build from directory (if provided)
        if directory:
            self.directory = directory
            self.filters = filters
            self.documents: List[Chant] = []
            self.sample = bool(sample)
            # Discover sources
            source_paths = glob.glob(self.directory)
            sources = [create_source(path) for path in source_paths]
            # Map by source.sigle
            self.sources: Dict[str, Any] = {src.sigle: src for src in sources if hasattr(src, "sigle")}
            # Load documents
            self._load_corpus(sample)
            # Save to pickle if requested
            if use_pkl:
                try:
                    with open(use_pkl, "wb") as f:
                        pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
                    logger.info(f"Corpus saved to pickle '{use_pkl}'.")
                except Exception as e:
                    logger.warning(f"Failed to save Corpus to pickle '{use_pkl}': {e}")
        else:
            # Neither directory nor valid pickle: initialize empty corpus
            self.directory = ""
            self.filters = filters
            self.documents = []
            self.sample = False
            self.sources = {}

    def _load_corpus(self, sample: int) -> None:
        """
        Internal: populate self.documents based on self.directory, self.filters, and sample.
        """
        # Find all candidate entries: for each source directory, look for subdirectories with meta.json & data.json
        all_entries = [
            entry
            for source_dir in glob.glob(self.directory)
            for entry in glob.glob(os.path.join(source_dir, "*"))
            if os.path.isdir(entry) and check_files_exist(entry)
        ]

        if sample:
            # Take a random sample of the entries
            try:
                sampled = random.sample(all_entries, k=sample)
            except ValueError:
                sampled = all_entries[:]
            entries_to_load = sampled
            self.sample = True
        else:
            entries_to_load = all_entries
            self.sample = False

        loaded_docs: List[Chant] = []
        for entry in entries_to_load:
            doc = create_document(entry, filters=self.filters, sources=self.sources)
            if doc:
                loaded_docs.append(doc)
        self.documents = loaded_docs

    def filter(self, filter_func: Callable[[Any, Any], bool]) -> "Corpus":
        """
        Return a new Corpus containing only documents for which filter_func(meta, source_meta) is True.
        The original filters (if any) are combined with filter_func via logical AND.

        Raises:
            ValueError: if filter_func is not callable.
        """
        if not callable(filter_func):
            raise ValueError("filter(): argument must be callable")

        # Combine existing filters with the new one
        if self.filters:
            def combined(doc_meta: Any, source_meta: Any) -> bool:
                return bool(self.filters(doc_meta, source_meta)) and bool(filter_func(doc_meta, source_meta))
        else:
            combined = filter_func

        # Create a new Corpus instance without invoking __init__
        filtered = object.__new__(Corpus)
        filtered.directory = self.directory
        filtered.filters = combined
        filtered.sources = self.sources
        filtered.sample = self.sample
        # Filter documents in place
        filtered.documents = [
            doc for doc in self.documents
            if combined(doc.meta, self.sources.get(doc.meta.source_id))
        ]
        return filtered

    @property
    def document_metadata(self) -> List[Dict[str, Any]]:
        """
        Return a list of metadata records (dict) for each document.
        """
        return [doc.meta.as_record for doc in self.documents]

    @property
    def source_metadata(self) -> List[Dict[str, Any]]:
        """
        Return a list of metadata records (dict) for each source.
        """
        return [source.meta.as_record for source in self.sources.values()]


def create_document(
    entry: str,
    filters: Optional[Callable[[Any, Any], bool]] = None,
    sources: Optional[Dict[str, Any]] = None,
) -> Optional[Chant]:
    """
    Creates a new Chant (or subclass) instance for the given entry directory.

    First loads metadata (Chant.get_meta). If filters is provided, it must be callable:
        - If filters(meta, source_meta) is False, returns None.
    Then dispatches to a genre-specific subclass if available; otherwise returns a generic Chant.

    Example:
        document = create_document("./data/manuscriptid/documentid")
    """
    try:
        document_meta = Chant.get_meta(entry)
    except Exception as e:
        logger.warning(f"Failed to load meta for entry '{entry}': {e}")
        return None

    source_meta = None
    if sources:
        source_meta = sources.get(document_meta.source_id)

    if filters:
        if not callable(filters):
            raise ValueError("Filters must be a callable")
        try:
            if not filters(document_meta, source_meta):
                return None
        except Exception as e:
            logger.warning(f"Filter raised an exception for entry '{entry}': {e}")
            return None

    # Dispatch based on genre
    if document_meta.genre == "Tropus":
        try:
            from .genre_specific import ProperTropeComplex
            return ProperTropeComplex(entry)
        except Exception as e:
            logger.warning(f"Failed to create ProperTropeComplex for '{entry}': {e}")
            return None

    # ... other genre-specific branches can be added here ...

    # Default to generic Chant
    try:
        return Chant(entry)
    except Exception as e:
        logger.warning(f"Failed to create Chant for '{entry}': {e}")
        return None


def check_files_exist(path: str) -> bool:
    """
    Check that both 'meta.json' and 'data.json' exist in the given directory.
    """
    meta_file = os.path.join(path, "meta.json")
    data_file = os.path.join(path, "data.json")
    return os.path.isfile(meta_file) and os.path.isfile(data_file)
