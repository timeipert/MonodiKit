# Corpus

A collection of chants loaded from a directory.

```python
import monodikit
corpus = monodikit.Corpus("data/*")
```



## Overview

The Corpus class is responsible for managing a collection of chants loaded from a specified directory. It provides functionality to filter and load chants based on specific criteria, allowing users to create subcorpora for further analysis and exploration.


## Key Functionalities

* Loading Chants: The class facilitates loading chants from a specified directory, allowing for the retrieval of either the complete set of chants or a sample based on specified parameters.

* Filtering: Users can filter the chants based on criteria such as genre or other custom parameters, enabling the creation of subcorpora tailored to their needs.

* Metadata Retrieval: The class provides methods to retrieve metadata for both documents and sources in the corpus.


