import sys
sys.path.append('..')
import monodikit

corpus = monodikit.Corpus("../../data/*")
print(monodikit.searchW(corpus, "A4B4C4", 4))