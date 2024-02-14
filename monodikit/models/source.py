import glob, json


class Source:
    id: str
    sigle: str
    region_of_origin: str
    location_of_origin: str
    institution_of_origin: str
    religious_order: str
    type: str
    location_of_library: str
    library: str
    signature: str
    comment: str
    dating: str
    status: str
    century: str
    iiif_manifest_url: str
    iiif_foliooffset: str

    def __init__(self, id, quellensigle, herkunftsregion, herkunftsort, herkunftsinstitution, ordenstradition,
                 quellentyp,
                 bibliotheksort, bibliothek, bibliothekssignatur, kommentar, datierung, status, jahrhundert, manifest,
                 foliooffset, publish, **kw
                 ):
        self.id = id
        self.sigle = quellensigle
        self.region_of_origin = herkunftsregion
        self.location_of_origin = herkunftsort
        self.institution_of_origin = herkunftsinstitution
        self.religious_order = ordenstradition
        self.type = quellentyp
        self.location_of_library = bibliotheksort
        self.library = bibliothek
        self.signature = bibliothekssignatur
        self.comment = kommentar
        self.dating = datierung
        self.status = status
        self.century = jahrhundert
        self.iiif_manifest_url = manifest
        self.iiif_foliooffset = foliooffset
        self.publish = publish
        self.unknown=kw

    def as_record(self):
        return {"id": self.id,
                "sigle": self.sigle,
                "region_of_origin": self.region_of_origin,
                "location_of_origin": self.location_of_origin,
                "institution_of_origin": self.institution_of_origin,
                "religious_order": self.religious_order,
                "type": self.type,
                "location_of_library": self.location_of_library,
                "library": self.library,
                "signature": self.signature,
                "comment": self.comment,
                "dating": self.dating,
                "status": self.status,
                "century": self.century,
                "iiif_manifest_url": self.iiif_manifest_url,
                "iiif_foliooffset": self.iiif_foliooffset
                }


def create_source(path):
    if glob.glob(path + "/meta.json"):
        with open(path + "/meta.json") as f:
            metadata = json.load(f)
            return Source(**metadata)
    else:
        raise Exception(f"Could not load source meta file {path}/meta.json")
