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

## Search in Corpus
With search_in_window you can search for a sequence of pitches or intervals within a certain window size. 
If len(sequence) == window size, it is just a complete match. The following code will give you every segment 
of three pitches that include a E4 and F4 in this order.
```python
results = monodikit.Search.search_in_window(corpus, ["E4", "F4"], 3)
```
You can do the same with intervals, just provide the information in the "preprocess" argument.
```python
results = monodikit.Search.search_in_window(corpus, [1,1,-1,-1,0,0], 6,  preprocess="intervals")
```
You can now create a html file with the results:
```python
with open("result.html", "w") as f:
    f.write(monodikit.Search.visualize_html(results))
```
or view it directly in a jupyter notebook with:
```python
from IPython.display import HTML
HTML(monodikit.Search.visualize_html(results))
```

## Multiple Sequence Alignment with MAFFT
You can also align the found chants (you have to install [MAFFT](https://mafft.cbrc.jp/alignment/software/] locally))

```python
mafft_input = monodikit.Search.to_mafft_input(results[0:10], context=2) # Align the first 10 search results
align = monodikit.Synopsis.run_mafft(mafft_input)
html = monodikit.Synopsis.visualize_alignments(align, highlight=[segment["ids"] for result in results for segment in result["segments"]], offset=2) # visualize and highligh notes that were in the search result window.
```