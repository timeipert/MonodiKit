# MonodiKit: Medieval Chant Document Analysis and Processing
MonodiKit is a Python library designed to facilitate the analysis 
and processing of medieval chant documents. It was specifically 
tailored to handle data in the monodi+ data format as edited 
by the Corpus Monodicum project. 
The library offers a set of classes that 
provide a wide range of functionalities, 
including parsing and processing of chant documents, 
exploring their hierarchical structure, 
managing metadata, generating musical notation, 
and extracting relevant information.


For Documentation see:

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/timeipert/MonodiKit)

## Key Features
* Parsing and processing of medieval chant documents.
* Access to the hierarchical structure of chant documents.
* Management of metadata associated with chant documents.
* Export to MEI, Volpiano and JSON.
* Extraction of relevant information.

## Usage
To use MonodiKit, follow these steps:

Install monodikit from pip:

```bash
pip install monodikit
```
Import the MonodiKit library into your Python project:

```python
import monodikit
```

If you want to use the data published by Corpus monodicum, you have to download it from [OSF](https://doi.org/10.17605/OSF.IO/MFPKD).
Now you can load the data into monodikit with:

```python
corpus = monodikit.Corpus("./data/*")
print(len(corpus.documents))
```

## Examples
Check out [Examples.md](https://github.com/timeipert/MonodiKit/blob/main/Examples.md) for more examples.

## Version History
* 0.0.1
    * Initial Release
* 0.0.2
  * Updated Data Structure and Exception Handling
* 0.0.3
  * Better Volpiano Support
* 0.0.4
  * Changed MAFFT configuration
  * Supports matrixfile in MAFFT
* 0.0.5
  * Minor Bugfix: Error Handling of Volpiano Parsing 
