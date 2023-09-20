# Examples

## Get an overview over corpus
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

## Corpus filtering by metadata
````python
subcorpus = monodikit.Corpus("../data/*", filters=lambda doc, source: source.herkunftsort == "Paris")
````


## Get a single chant by id
```python
import monodikit
monodikit.Corpus("data/*")
document_id = "Aa 13-7v-7"
chant = next((chant for chant in corpus.documents if chant.meta.document_id == chant_id), None)
print(chant)
```

## Search for pitch pattern
The goal is to search for chants based on a specific musical pattern represented by the search_string.
```python
import monodikit
corpus = monodikit.Corpus("data/*")

search_string = "A4C5B4A4"
chants_found = []
for chant in corpus.documents:
    neume_components = chant.flat_neume_components
    pitches = "".join([neume.pitch for neume in neume_components])
    if search_string in pitches:
        chants_found.append((chant.meta.document_id, pitches))
print(chants_found)
```
* We iterate through each chant in the loaded corpus (corpus.documents).
* For each chant, we obtain the neume components (neume_components) and extract their pitches.
* We concatenate the pitches into a string.
* We check if the search_string (our desired pattern) is present in the concatenated pitches for the current chant.
* If the pattern is found in the chant, we append a tuple containing the chant's document ID and the pitches to the list chants_found.