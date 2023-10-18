import glob
import random
import os

from .document import Chant
from .source import create_source
import pickle


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
        self.sources = {source.sigle: source for source in sources}
        self.load_corpus(sample)

    # TODO: One should create subcorpora without the need to reload the whole corpus

    def __init__(self, directory=None, sample=0, filters=None, use_pkl=None):
        if use_pkl and os.path.exists(use_pkl):
            #print("pkl exists, use pkl..")
            with open(use_pkl, "rb") as f:
                corpus_data = pickle.load(f)
                self.directory = corpus_data.directory
                self.filters = corpus_data.filters
                self.documents = corpus_data.documents
                self.sample = corpus_data.sample
                self.sources = corpus_data.sources

        elif directory:
           # print("pkl does not exist.")

            self.directory = directory
            self.filters = filters
            self.documents = []
            self.sample = False
            sources = [create_source(source) for source in glob.glob(self.directory)]
            self.sources = {source.sigle: source for source in sources}
            self.load_corpus(sample)
            if use_pkl:
                print("save pkl.")
                with open(use_pkl, "wb") as f:
                    pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        #print("end __init__")
            # TODO: One should create subcorpora without the need to reload the whole corpus

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

    def filter(self, filters):
        if not callable(filters):
            Exception("Error  in filter(): argument has to be a callable")
        if self.filters:
            filters = lambda document_meta, source_meta: filters(document_meta, source_meta) and self.filters(document_meta, source_meta)
        filtered_corpus = Corpus()
        filtered_corpus.documents = [document for document in self.documents if filters(document.meta, self.sources[document.meta.source_id])]
        filtered_corpus.sources = self.sources
        filtered_corpus.filters = filters
        filtered_corpus.sample = self.sample
        return filtered_corpus



    @property
    def document_metadata(self):
        return [document.meta.as_record for document in self.documents]

    @property
    def source_metadata(self):
        return [source.meta.as_record for source in self.sources]


from .genre_specific import ProperTropeComplex


def create_document(entry, filters = None, sources=None):

    """
    Creates a new instance of a document.
    At first checks for a specific type and assigns a genre-specific subclass
    (for example TropeComplex()).
     If no suitable subclass is found, it returns a generic Document() instance.
     Example:
         ```
         document = create_document("./data/manuscriptid/documentid")
         ```
    """
    document_meta = Chant.get_meta(entry)
    if sources:
        source_meta = sources.get(document_meta.source_id, None)
    if filters:
        if callable(filters):
            if not filters(document_meta, source_meta):
                return None
        else:
            Exception("Filters have to be a callable")
   # else:
        # Now checks only for substring
       # for key, value in filters.items():
        #    if value not in document_meta.__getattribute__(key):
         #       return None

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
