# FAF (Frequently Asked Functions)
## Get Overview over Corpus
You can get a Dataframe of the Corpus documents and source metadata:
```python
import pandas as pd
import monodikit
corpus = monodikit.Corpus(dir)
document_meta = pd.DataFrame.from_records(corpus.document_metadata)
source_meta = pd.DataFrame.from_records(corpus.source_metadata)
```

So you can list all document metadata of genre "Tropus" 
or you can get all liturgical play
(which are groups of documents that are identified by the *liturgical_play_id*)

```python
# Show metadata of all tropes
print(document_meta.loc[document_meta["genre"] == "Tropus"]) 

# Show IDs of all liturgical plays (for example to build a sub corpora out of one or all of them)
print(document_meta.loc[document_meta["liturgical_play_id"] != None].value_counts())
```