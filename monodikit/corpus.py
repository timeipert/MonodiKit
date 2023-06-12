import glob
import random
import os

from .document import Chant
from .genre_specific import ProperTropeComplex


class Corpus:
    def __init__(self, directory, sample=0, filter_options={}):
        self.directory = directory
        self.documents = self.load_corpus(sample)
        self.filter = filter_options

    def load_corpus(self, sample):
        if not sample:
            return list(filter([create_document(entry, self.filter) for source in glob.glob(self.directory)
                                for entry in
                                [directory for directory in glob.glob(os.path.join(source, "*")) if
                                 os.path.isdir(directory)]
                                if check_files_exist(entry)]))  # ! Error when there are missing files?
        else:
            entries = [entry for source in glob.glob(self.directory)
                       for entry in
                       [directory for directory in glob.glob(os.path.join(source, "*")) if os.path.isdir(directory)]
                       ]
            return list(filter(None, [create_document(entry, self.filter)
                                      for entry in random.sample(entries, sample)
                                      if check_files_exist(entry)]))

    # TODO It should be possible to filter the collection of documents and create multiple "sub corpora"


def create_document(entry, filter_options={}):
    """
    Creates a new instance of a document. At first checks for a specific type and assigns a genre-specific subclass
    (for example TropeComplex()). If no suitable subclass is found, it returns a generic Document() instance.
    """
    meta = Chant.get_meta(entry)


    # Now checks only for substring
    for key, value in filter_options.items():
        if value not in meta[key]:
            return None

    if meta.gattung1 == "Tropus":
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
