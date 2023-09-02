import glob
import random
import os

from .document import Chant
from .source import create_source, Source
from .genre_specific import ProperTropeComplex


class Corpus:
    """
    A collection of chants loaded from a directory.

    Parameters:
    -----------
    directory : str
        The input directory that holds the data.

    sample : int, optional
        The number of chants that are given as a sample. Defaults to None.

    filter_options : dict or callable, optional
        If a dict is provided, it does a substring match.

        If a callable object is provided, it calls it for every document and creates the document
        if True is returned.

    Returns:
    --------
    Corpus
        A Corpus object containing the chants loaded from the directory.

    Examples:
    ---------
    Load chants with a specific substring match:
    ```
    subcorpus1 = Corpus("../data/*", filter_options={"gattung1": "Sequenz"})
    ```

    Load chants using a custom filtering function:
    ```
    subcorpus2 = Corpus("../data/*", filter_options=lambda chant: chant.gattung1 == "Tropus" or chant.gattung1 == "Sequenz")
    ```
    """

    def __init__(self, directory, sample=0, filters=None):
        if filters is None:
            filters = {}
        self.directory = directory
        self.filters = filters
        self.documents = []
        self.sample = False
        sources = [create_source(source) for source in glob.glob(self.directory)]
        self.sources = {source.quellensigle: source for source in sources}
        self.load_corpus(sample)


    def load_corpus(self, sample):
        if not sample:
            self.sample = False
            self.documents = list(filter(None, [create_document(entry,
                                                                filters=self.filters,
                                                                sources=self.sources)
                                                for source in glob.glob(self.directory)
                                                for entry in
                                                [directory for directory in
                                                 glob.glob(os.path.join(source, "*")) if
                                                 os.path.isdir(directory)]
                                                if check_files_exist(entry)]))  # ! Error when there are missing files?
        else:
            self.sample = True
            entries = [entry for source in glob.glob(self.directory)
                       for entry in
                       [directory for directory in glob.glob(os.path.join(source, "*"))
                        if os.path.isdir(directory)]]
            return list(filter(None, [create_document(entry, filters=self.filters)
                                      for entry in random.sample(entries, sample)
                                      if check_files_exist(entry)]))




def create_document(entry, filters, sources = None):
    """
    Creates a new instance of a document.
    At first checks for a specific type and assigns a genre-specific subclass
    (for example TropeComplex()).
     If no suitable subclass is found, it returns a generic Document() instance.
    """
    document_meta = Chant.get_meta(entry)
    source_meta = sources.get(document_meta.source_id, None)


    if callable(filters):
        if not filters(document_meta, source_meta):
            return None
    else:
        # Now checks only for substring
        for key, value in filters.items():
            if value not in document_meta.__getattribute__(key):
                return None

    if document_meta.genre == "Tropus":
        return ProperTropeComplex(entry)
    # ... other genres
    else:
        return Chant(entry)


def check_files_exist(path):
    meta_file = os.path.join(path, 'meta.json')
    data_file = os.path.join(path, 'data.json')

    if os.path.isfile(meta_file) and os.path.isfile(data_file):
        return True
    else:
        return False
