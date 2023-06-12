from dataclasses import dataclass
import glob, json

@dataclass
class Source:
    id: str
    quellensigle: str
    herkunftsregion: str
    herkunftsort: str
    herkunftsinstitution: str
    ordenstradition: str
    quellentyp: str
    bibliotheksort: str
    bibliothek: str
    bibliothekssignatur: str
    kommentar: str
    datierung: str
    status: str
    jahrhundert: str
    manifest: str
    foliooffset: str

def create_source(path):
    if glob.glob(path + "/meta.json"):
        with open(path + "/meta.json") as f:
            metadata = json.load(f)
            return Source(**metadata)
    else:
        raise Exception(f"Could not load source meta file {path}/meta.json")
