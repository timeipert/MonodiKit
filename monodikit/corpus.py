import glob
import random
import os

from document import Document
from genre_specific import ProperTropeComplex
class Corpus:
    def __init__(self, directory, sample=False):
        self.directory = directory
        self.documents = self.load_corpus(sample)

    def load_corpus(self, sample):
        if not sample:
            return [self.create_document(entry) for source in glob.glob(self.directory)
                    for entry in
                    [directory for directory in glob.glob(os.path.join(source, "*")) if os.path.isdir(directory)]]
        else:
            entries = [entry for source in glob.glob(self.directory)
                       for entry in
                       [directory for directory in glob.glob(os.path.join(source, "*")) if os.path.isdir(directory)]]
            return [self.create_document(entry) for entry in random.sample(entries, sample)]

    @staticmethod
    def create_document(entry):
        """
        Creates a new instance of a document. At first checks for a specific type and assigns a genre-specific subclass
        (for example TropeComplex()). If no suitable subclass is found, it returns a generic Document() instance.
        """
        meta = Document.get_meta(entry)
        if meta.gattung1 == "Tropus":
            return ProperTropeComplex(entry)
        # ... other genres
        else:
            return Document(entry)