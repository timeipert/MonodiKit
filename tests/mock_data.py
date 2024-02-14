from dataclasses import dataclass
import uuid

# Mock data for Accidental
accidental_data = {
    "uuid": str(uuid.uuid4()),
    "base": "A",
    "liquescent": "some_liquescent_value",
    "noteType": "Flat",
    "octave": 4,
    "focus": True,
    "index": (1, 2)
}


notes_data = {"spaced":
                  [{"nonSpaced":
                              [{"grouped":
                                             [{"uuid": "e617f59f-2de8-4fc8-be24-8aac161cbbe3",
                                                      "noteType": "Normal",
                                                      "base": "C",
                                                      "liquescent": False,
                                                      "octave": 4,
                                                      "focus": False
                                                      }
                                                     ]
                                         }
                                        ]
                          }
                         ]}

notes_flat_data = {"spaced":
                  [{"nonSpaced":
                              [{"grouped":
                                             [{"uuid": "e617f59f-2de8-4fc8-be24-8aac161cbbe3",
                                                      "noteType": "Flat",
                                                      "base": "C",
                                                      "liquescent": False,
                                                      "octave": 4,
                                                      "focus": False
                                                      }
                                                     ]
                                         }
                                        ]
                          }
                         ]}

# Mock data for NeumeComponent
neume_component_data = {
    "uuid": str(uuid.uuid4()),
    "base": "B",
    "liquescent": True,
    "noteType": "Normal",
    "octave": 5,
    "focus": False,
    "index": (2, 3)
}

meta_data = {
  "id" : "0b1fa521-57a7-4409-91c9-79d998f49a21",
  "quelle_id" : "Aa 13",
  "dokumenten_id" : "Aa 13-157v-14",
  "gattung1" : "Sequenz",
  "gattung2" : "Textiert",
  "festtag" : "Iohannes Evangelista",
  "feier" : "Messe",
  "textinitium" : "Iohannes Iesu Christo",
  "bibliographischerverweis" : "AH 53, 168",
  "druckausgabe" : "CM III",
  "zeilenstart" : "14",
  "foliostart" : "157v",
  "kommentar" : "",
  "editionsstatus" : "ediert",
  "additionalData" : {
    "Melodiennummer_Katalog" : "",
    "Editor" : "andreas.pfisterer@uni-wuerzburg.de",
    "Bezugsgesang" : "",
    "Melodie_Standard" : "Romana",
    "Endseite" : "158",
    "Startposition" : "",
    "Zusatz_zu_Textinitium" : "",
    "Referenz_auf_Spiel" : "",
    "Endzeile" : "1",
    "Nachtragsschicht" : "A",
    "Überlieferungszustand" : "",
    "Melodie_Quelle" : ""
  }
}
data_data ={
  "uuid" : "a5b06c68-1cba-4720-8850-8a1b78494ad7",
  "children" : [
    {
      "uuid" : "f733d4d1-2171-4dc5-bef3-834ea9d59e8f",
      "children" : [
        {
          "uuid" : "28aef807-ff53-4d3e-a40e-54804865964f",
          "text" : "DE SANCTO IOHANNE EVANGELISTA (f. 157v)",
          "retro" : False,
          "paratextType" : "Festtag",
          "comment" : None,
          "kind" : "ParatextContainer"
        }
      ],
      "data" : [
      ],
      "kind" : "FormteilContainer"
    },
    {
      "uuid" : "c623f645-c89d-46f3-a7d2-f7c1fa28f61f",
      "children" : [
        {
          "uuid" : "37b91708-ab12-465e-b45b-88faabfc194d",
          "children" : [
            {
              "uuid" : "9a95fc5b-3783-4fad-99ea-113000c2900b",
              "children" : [
                {
                  "uuid" : "12adaa1d-bd6a-4b1f-83e8-dd7fde97289f",
                  "text" : "Io-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "e617f59f-2de8-4fc8-be24-8aac161cbbe3",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "bac36058-bc17-46fc-9db4-e953b41d24f3",
                  "text" : "han-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "cfec5748-642b-4aac-b12b-3ec6b49a8bd6",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "2eda7e82-b7b0-4543-a6d6-373720c72018",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : True,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "5c8cd1d5-93e9-4a41-87bd-a7a56e40e6d6",
                  "text" : "nes",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "5a05ba3d-c169-4757-86a4-d18e4552b0e9",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "0a215f7c-9edd-4562-a36f-05579c9bd28b",
                  "text" : "Ie-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "36d3479b-69a6-4ae5-966b-5bd70fb3a197",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "82aa7afa-c96f-4c16-b586-85539073b976",
                  "text" : "su",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "d489b659-864a-4277-864d-7c39613e3ecb",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "4be1028b-4c22-41fe-b8d5-931e5c57e431",
                  "text" : "Chri-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "7b26f073-0d59-4168-9d17-020b2eea0add",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "461d3458-b973-4a5a-a289-6aa91800ac4d",
                  "text" : "sto",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "3b458e51-724b-41c7-a54e-f6683194c689",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "29945796-fcaa-4070-9efe-bb10b1d39b14",
                  "text" : "mul-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "c9b0ede4-9910-4035-b26b-82bbd53efbb2",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "5f5ca5da-b800-43ae-8d12-b6a0457c498d",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : True,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "bbf22995-cdf4-4e74-996d-092ad5ec0f69",
                  "text" : "tum",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "3abfb8ab-3974-4816-a14f-513146d9072f",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "b0ca2fe4-23ed-428f-86f9-4fa9daea94d6",
                  "text" : "di-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "6ee1d815-d4e6-41cc-8a8b-24d9710a5ee6",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "916f2c27-36ff-4a99-b21c-eafa583b570a",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "e310cbf3-2f8f-4ceb-acbd-119dc2a76ed0",
                  "text" : "le-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "42a41b2f-1af8-4834-9722-c1a971a0300d",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "104c4c1b-68ce-4d38-b3f3-6bbfa3c2525c",
                  "text" : "cte",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "dd530ca1-38e4-4ada-928e-7619448e1dad",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "2e7ebe57-3da5-4fdd-8785-938a58f1ecf1",
                  "text" : "uir-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "f97062bd-2b8d-49a9-b682-17f6e85465bd",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "a2a32e3b-d58e-4649-b15b-e17f1b6c5bc7",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : True,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "a80708d2-31b7-40dc-b0ba-4b0935dbcae0",
                  "text" : "go",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "8dd7d423-bf15-4a5c-9b8f-65f6f1459ace",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : ""
            }
          ],
          "kind" : "FormteilContainer"
        }
      ],
      "data" : [
        {
          "name" : "Signatur",
          "data" : "1"
        }
      ],
      "kind" : "FormteilContainer"
    },
    {
      "uuid" : "4a6b21ce-3885-4168-bfca-4984c1e0813e",
      "children" : [
        {
          "uuid" : "a6c95dc9-b484-42e1-9ad9-c7523fc39350",
          "children" : [
            {
              "uuid" : "942548b4-b3b4-4b2a-8ac4-fa43f7091e44",
              "children" : [
                {
                  "uuid" : "5220549e-ebea-4b4b-a202-bf6da6553b73",
                  "text" : "Tu",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "7c4d700e-f188-4641-b07d-ef9a3e843775",
                                "base" : "F",
                                "octave" : 4,
                                "noteType" : "Normal",
                                "focus" : False,
                                "liquescent" : False
                              },
                              {
                                "uuid" : "ab39430c-9ef3-4910-9fd7-c5caea409b03",
                                "base" : "A",
                                "octave" : 4,
                                "noteType" : "Normal",
                                "focus" : False,
                                "liquescent" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "3ff00509-5a0a-45fe-99a9-d4959395dbaf",
                  "text" : "ei-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "b2d50199-5101-40f3-b0dd-72585a82dfa4",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "2740f2bc-801a-405a-82a6-8047eff74eff",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : True,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "b03b03fe-d7eb-4066-86d1-c1a59916936b",
                  "text" : "us",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "9d4fa022-38fe-42df-bf7a-37a92056005a",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "14b92e33-c9ee-40f8-b572-85cbbbd65be2",
                  "text" : "a-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "aab78d88-8737-4cbd-9a65-0bd113c89957",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "69844621-bc20-4df6-8ded-fd1e13ae7867",
                  "text" : "mo-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "de95d61f-406b-415d-8ca4-0db36da3a8c2",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "86a6bab0-c1e8-4eda-8e99-e296bcd98078",
                  "text" : "re",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "8e488469-c5be-4451-b607-4ec5a19c48fc",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "83c9e646-7743-4481-8217-f9f85832afcf",
                  "text" : "car-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "d7fe93d0-5fc8-4c1a-9c19-633b9e5414c8",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "8f2ad2b5-af19-4e1a-8918-ab8b67c631ad",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "f73d5fea-474e-4e5f-a70b-e49a82bca285",
                  "text" : "na-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "bda6339d-152a-4b07-b698-c430ba6bac57",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "3373f543-f52d-4173-bc4a-5ee7008a1dc8",
                  "text" : "lem",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "86642cd7-eeda-4983-94f4-e0554caee5e0",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : "a"
            }
          ],
          "kind" : "FormteilContainer"
        },
        {
          "uuid" : "966ba4cf-6629-4dfa-bc31-44b562090919",
          "children" : [
            {
              "uuid" : "463cfadd-bb6a-415b-b6ed-c03a787ef26e",
              "children" : [
                {
                  "uuid" : "3d92344f-14dc-4431-a33e-2504103c9f6f",
                  "text" : "In",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "88e2ac83-f995-4685-88f2-ce63160e606a",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "37b4588e-9ce2-4bf4-94d8-0abddf2e2090",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "ddf88410-fbbc-480c-9268-49bf5fd968fa",
                  "text" : "na-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "bcf27800-8837-4e2c-9380-faa07466e5bc",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "807029f2-ec5b-4338-9491-2cc52c249f72",
                  "text" : "ui",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "f54460cf-135f-4a98-98a4-55f52db9e93a",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "c7ee219a-867e-44e2-bf54-d6fb62bc4da3",
                  "text" : "pa-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "9db1c090-ca19-476f-8b91-25fb7ba46698",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "c43ffcaa-ed5e-4759-a651-3357fe0c232d",
                  "text" : "ren-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "ab615d24-0387-4c89-81d1-d7958447199a",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "c2c90822-5124-4ae6-b30c-edcd0c0a033a",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : True,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "e4ae9d51-3376-441e-bba8-569aa7f3733a",
                  "text" : "tem",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "da354f5e-5129-49e3-843d-419ff5e73ded",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "5eb2f7f1-bab4-4535-8ad7-859150ebbaea",
                  "text" : "li-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "6499314c-6687-4c09-a0e7-e89c08b64c22",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "adc48e08-ef70-4f65-a267-b767575ae572",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "22221228-de0c-49eb-84d3-255437e5e8d1",
                  "text" : "qui-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "37833321-1ff4-4505-aae3-aadb7b3cc6ec",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "b9c0a9c5-81d8-4de7-baec-779bb4b0f584",
                  "kind" : "LineChange",
                  "focus" : True
                },
                {
                  "uuid" : "02685a29-6cfa-495f-8961-d1adca3bd734",
                  "text" : "sti",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "8dcc430b-54c5-470e-b83d-7610cbbdccfd",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : "b"
            }
          ],
          "kind" : "FormteilContainer"
        }
      ],
      "data" : [
        {
          "name" : "Signatur",
          "data" : "2"
        }
      ],
      "kind" : "FormteilContainer"
    },
    {
      "uuid" : "6bb4c43e-d32f-42f1-b8e8-f9feb2783f7b",
      "children" : [
        {
          "uuid" : "1a13b391-7627-4063-9167-afe0683cc9af",
          "children" : [
            {
              "uuid" : "0d053276-6f06-42c1-8564-8dc9b823c8c4",
              "children" : [
                {
                  "uuid" : "8460e422-bf81-4729-8b76-6f6bf35a47c3",
                  "text" : "Tu",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "cb315d21-23be-4eab-ba86-b51bf65df19e",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "da15db16-3719-4dd2-92fa-68a0369951f0",
                  "text" : "le-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "fa1b5e30-b983-470e-892a-837cef89f606",
                                "noteType" : "Normal",
                                "base" : "E",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "89aaa341-908e-4ca6-a628-71e540101f67",
                                "noteType" : "Oriscus",
                                "base" : "E",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "833ed1c4-6538-41a3-9408-5ca4e686cace",
                  "text" : "ue",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "a56d599d-c0ce-4495-8903-785f770a679f",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "41d5b8ce-df02-4786-8c1f-37defd0bde1f",
                  "text" : "con-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "6497596b-32f4-4ee5-8225-30e1007860b7",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "61e89965-5cae-498f-9b99-875ede9981da",
                  "text" : "iu-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "a8a0d770-8c60-40ea-a2b2-52184d2b38cd",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "4460d88a-bf48-4161-9164-2667d25a3a0a",
                  "text" : "gis",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "071a350a-aca8-4aa2-9242-4cf199daf2e0",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "f08d0c1d-78da-4a68-916e-057a375f8f4d",
                  "text" : "pe-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "acb96cfd-feba-4335-ad04-efebdf5bb6a6",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "0a6bd78a-a3b6-4e7a-b259-41ee8e39036e",
                  "text" : "ctus",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "a57d610b-3c11-4269-9ba0-c0912b43adee",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "fefb3879-f3d8-44d7-90ee-c8e28d8f036b",
                  "text" : "re-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "76afe2a2-fe8a-42da-ade4-70526779770e",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "58b55141-0a86-432c-a75d-9ba4866bcd92",
                  "text" : "spu-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "1c616e44-c4b5-4c56-bc12-128cf14f1aaf",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "820217bb-2a77-43e2-8686-6ceb23cdb1e8",
                  "text" : "i-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "903fb2cb-8c4a-4e58-938d-41a225c1ecf6",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "085334d8-d6c7-4357-84f8-9b9f8cfbe63e",
                  "text" : "sti",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "2d5c38f8-104e-497c-b52f-a166df11f9f7",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "1e6ec77b-93e2-4291-93c8-f662008fee27",
                  "text" : "mes-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "612d9b6e-9ab2-4018-b1f7-19f7c576e659",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "cc763cc3-f939-40e9-909f-b915d8cc830c",
                  "text" : "si-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "33b2022c-e7dd-4122-b61d-5a7d3a8ce3d1",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "f3a13779-7222-44ff-943a-0993fe892bc0",
                  "text" : "am",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "6bf2013a-a50e-4d96-a6ea-3539fcaa1be2",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "acd082d0-ed89-4612-8308-dd306e855e73",
                  "text" : "se-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "44f49df5-c114-4602-8a99-df31b1dae172",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "3e06e621-c0ce-440c-a053-7ebfab4f5914",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "e0e76bd3-2167-43ee-b06a-e8527d9a6ccf",
                  "text" : "cu-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "6905aaf4-45fe-4ee5-b8c7-3ed8d0a6b4ea",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "fc082d8c-2b63-4735-bf4d-00f52b450592",
                  "text" : "tus",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "b7ba5c28-6d8c-4089-89db-194355b7239f",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : "a"
            }
          ],
          "kind" : "FormteilContainer"
        },
        {
          "uuid" : "e2cc4a60-d983-4225-9ebf-7d4d5f648865",
          "children" : [
            {
              "uuid" : "92ac25cd-e97c-4633-9a54-dd36d2a4aab2",
              "children" : [
                {
                  "uuid" : "505016d0-2519-4d6d-a95b-bb5d459102e3",
                  "text" : "Vt",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "722e5bf1-d43d-4b9e-b125-4aec9ee7fa45",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "d0be2d41-550f-403c-afd8-6afbef03181e",
                  "text" : "ei-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "2c41ebe6-9201-48e5-825a-61514f2c641c",
                                "noteType" : "Normal",
                                "base" : "E",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "fd75b696-8342-4a01-869c-bfd289142464",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : True,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "4ee13a87-da2e-409f-937f-43e74a402ef1",
                  "text" : "us",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "1ea14fad-26f9-4fd4-9e58-7332807f8e2a",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "383aecd3-48a6-4eb5-ad2a-e0bed67983ab",
                  "text" : "pe-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "6ff9d082-7c5e-42bb-8ad0-034ab4d5ceeb",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "6c12dbb5-640a-4524-80c3-51c75b7a215d",
                  "text" : "cto-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "2bc1071e-f399-40ab-8d04-dab1dce29673",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "96042045-c4b6-45ef-b1f6-b2bc31fda325",
                  "text" : "ris",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "5625fa15-4d12-4535-a0ea-0c159e931c0a",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "40c5e319-8ad8-4247-8694-f5b9249dba9b",
                  "text" : "sa-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "1bf19b7f-4d19-4b5a-bc05-dc6eeb114374",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "5ec65bc3-e515-435e-93e2-8649e569ffac",
                  "text" : "cra",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "5a71c79a-24e5-43b2-91ca-2b6f1f5446e7",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "d29019f1-f5d6-4e42-8cd7-b1ce32693e56",
                  "text" : "me-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "9736c279-7cef-4630-9443-797c512f6a5d",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "d043db1c-7918-474a-8caa-439abde8cb54",
                  "text" : "ru-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "53ff626e-b072-469f-9d58-97f7b04813c3",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "4e4665e0-ad57-4b51-b0c6-fda38009ed32",
                  "text" : "is-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "21064d6d-b309-4ed3-befc-e73dc904a13f",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "635d2995-8020-41c1-85fc-bcbd7e03d17d",
                  "text" : "ses",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "19f84b85-03f1-4a1a-8798-780bf4fda8d0",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "5bd6455c-e8f1-47ec-9c1c-e4215ae4a1c0",
                  "kind" : "LineChange",
                  "focus" : False
                },
                {
                  "uuid" : "0d04b920-e3ba-4bbc-a434-30141a965cf7",
                  "kind" : "Syllable",
                  "text" : "flu-",
                  "syllableType" : "Normal",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "5eef0ad0-681e-4314-99ce-06397b5aef0a",
                                "base" : "A",
                                "liquescent" : False,
                                "noteType" : "Normal",
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  }
                },
                {
                  "uuid" : "e6dfa10f-b678-456d-98af-08e2eff6794d",
                  "kind" : "Syllable",
                  "text" : "en-",
                  "syllableType" : "Normal",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "635a29d8-775c-4f00-8cca-a4dbe86cce2a",
                                "base" : "G",
                                "liquescent" : False,
                                "noteType" : "Normal",
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  }
                },
                {
                  "uuid" : "dcb28689-a096-463b-a9d0-0ca9d9d1fe61",
                  "kind" : "Syllable",
                  "text" : "ta",
                  "syllableType" : "Normal",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "636de5b2-ccd9-4295-a11b-18b9d6cc49fb",
                                "base" : "F",
                                "liquescent" : False,
                                "noteType" : "Normal",
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  }
                },
                {
                  "uuid" : "86c0832a-cb2f-4a7a-ab66-e4b24aa53790",
                  "text" : "po-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "13d9335a-3496-4611-83a6-7969a2324299",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "af757362-a145-4acc-94cd-9879502642c6",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "5fd8a3c0-b446-4072-aecc-c4198b00e73c",
                  "text" : "ta-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "9d30c75d-0f71-4bff-8e5b-2061048c19bd",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "b573de04-3aeb-459b-94e3-2f29fc55a567",
                  "text" : "re",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "eeb145f3-ecdb-46cd-910e-6366a2c72eb1",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : "b"
            }
          ],
          "kind" : "FormteilContainer"
        }
      ],
      "data" : [
        {
          "name" : "Signatur",
          "data" : "3"
        }
      ],
      "kind" : "FormteilContainer"
    },
    {
      "uuid" : "4908e769-3824-4a23-9fa5-c042d0c1245e",
      "children" : [
        {
          "uuid" : "2c7e661c-2238-4bfa-9de2-fe401ed8987a",
          "children" : [
            {
              "uuid" : "200a15d2-f8df-4232-8780-d8c885274f0c",
              "children" : [
                {
                  "uuid" : "3d6301bb-e0cb-4078-b5fb-fb33c5ee4a53",
                  "text" : "Tu-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "3c26040b-baf5-4077-8bd3-7688bdc15977",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "e0722de2-ced8-4038-b98c-5263300bfd5d",
                  "text" : "que",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "643ae966-8d12-43af-9b0a-0cb972d1a0fa",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "c4b544ec-fd14-4596-b703-ada9174934df",
                  "text" : "in",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "b9df3494-dd9e-4b14-a72c-e7d02aa7a9ff",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "01136af2-ac36-49fb-900f-c1d79c760b7f",
                  "text" : "ter-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "1d47e5eb-9ff2-4a3f-b9de-e3b5adf80b38",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "8260ff5c-2828-4d74-83df-417154ce851f",
                  "text" : "ra",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "525f27a8-af83-4637-8818-29c5bc5946e8",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "226efa74-d2b1-4662-b4e6-25ab3fe54560",
                  "text" : "po-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "928e429e-e535-4dcd-894b-e2e1559accd5",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "0ffea0b4-7895-4b8e-809b-bb3647e6fb02",
                  "text" : "si-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "246c308c-6909-403a-a31e-f33876d73726",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "6cc9d66d-6821-4f8e-b927-f2cdfb7b58fd",
                  "text" : "tus",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "04280fc5-508b-4011-ad73-363cdcc96df6",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "1106ccd5-780f-44c0-b167-4bd820fe38b6",
                  "text" : "glo-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "f35a28f9-c0f4-4609-8a94-6924b9abe86e",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "ba1f449b-01f3-4489-a14f-7cc3cd018b97",
                  "text" : "ri-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "47aada34-bf77-4595-90d8-45b58556cb93",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "9ba13336-4c87-4f22-991f-5410b673a603",
                  "text" : "am",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "a46427fd-456e-41c2-947a-c9ce0c88c2b3",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "d67f3ccf-e340-4a06-a77e-1b237d017368",
                  "text" : "con-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "dddc5435-3e6f-4cf2-beed-4f899e8e180d",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "f36c113c-51e6-4b02-b8cb-d5aeda416df6",
                  "text" : "spe-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "09a7ba59-4139-41e2-863d-af6cddf5b4c3",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "6e54ed46-1452-4f4b-8d2d-6a63b9348020",
                  "text" : "xi-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "ea7f65ec-b8a1-4858-85c1-443352b35516",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "72a0066a-4df5-4a03-85ee-2d4df93b6720",
                  "text" : "sti",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "89e06429-02e2-4369-acac-a67cb4c94a47",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "1e9c318f-5cd7-429b-ac36-fa30ccaf4a48",
                  "text" : "fi-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "e0d09205-9c82-4027-bca7-c49e312ac92b",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "d9473973-432f-48b1-afc4-13232bd18f23",
                  "text" : "li-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "272ab426-1756-4ada-9219-d577d752fe99",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "f04936d4-b51b-49fd-bf9f-398551379d9b",
                  "text" : "i",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "23920c55-f39e-4395-9a52-fd825135a631",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "378a1952-7ba2-428a-822c-dc0e8782e559",
                  "text" : "de-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "78e48145-2ea9-40ed-a2ca-3ad39d031a00",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "108f62d5-4618-420d-87c1-0864cece86a5",
                  "text" : "i",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "192301bf-7c5e-439d-bc0b-eff3f72772fe",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : "a"
            }
          ],
          "kind" : "FormteilContainer"
        },
        {
          "uuid" : "ecbca23d-c9ba-4cb2-82f3-5b9c9bd101db",
          "children" : [
            {
              "uuid" : "b19f8363-a9ab-40e2-95df-57bf4db3780c",
              "children" : [
                {
                  "uuid" : "17cabff1-5db6-4cb4-96e5-5e242ee94951",
                  "text" : "Que",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "6ab9306f-375c-4050-a0ed-e7414dad57cf",
                                "noteType" : "Normal",
                                "base" : "F",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "68307435-5a60-4775-afa1-fd615bb8ed22",
                  "text" : "so-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "72a978f3-e8d6-4fcc-84bb-60f57915204f",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "7f91ef50-0ce1-484e-ae09-2b8571b1ffe1",
                  "text" : "lum",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "e68b9943-89d8-4b1d-8a51-23b48e09f7c9",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "1d05129a-49de-4c47-94fa-c49e5d956ef4",
                  "text" : "san-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "5f8361da-d169-4681-8a32-230cc8f5937b",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              },
                              {
                                "uuid" : "f8967fe6-e4d8-4a11-abc0-d29bc6008e35",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : True,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "7c1293a0-f26f-4e5f-8454-a7c775b15d52",
                  "text" : "ctis",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "0f283450-b28c-44f0-89fc-922319733517",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "fb9c5239-97aa-4a47-99bd-6410225d0777",
                  "text" : "in",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "397dd30f-4b67-47c2-82fe-6100fae69e88",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "c253d28c-28a1-4b71-b833-dc0426d1eaf9",
                  "text" : "ui-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "4354522d-5da9-44b5-85f1-dfe1c54c0508",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "526fc412-9c84-4acc-88c2-cfaf94015d59",
                  "text" : "ta",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "25b8dbc2-2ed2-4b0f-aa49-fcd710c3ccfa",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "29c79fea-67f4-4de0-aeee-47b574b37740",
                  "kind" : "LineChange",
                  "focus" : False
                },
                {
                  "uuid" : "dd36a5ff-d040-4367-b157-df77cdd84b46",
                  "text" : "cre-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "ab20ec6a-39ef-43ef-a49a-5a0867ebc178",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "7363ce3b-cc45-4c56-9c3d-b0df4b3daa1b",
                  "text" : "di-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "e0491657-11f5-4f43-aae9-2ced7673a5cd",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "5bd6bc14-2aa8-45b4-b88e-cfd68da00785",
                  "text" : "tur",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "c75f73b9-ec0a-49be-b66b-d5817cfe9694",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "94002078-0de4-4887-bfd7-c41e48787736",
                  "text" : "con-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "fba207ed-22a4-48b4-a5be-2e1ff4d64615",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "2c9ff034-56fc-4101-8a79-114b8533ddce",
                  "text" : "tu-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "a463010a-4762-4ee1-a678-65d8f8fd8d31",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "a3c472ab-5364-4eb7-a0ca-7563b735ce71",
                  "text" : "en-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "5def52d6-2ea2-48e6-af10-aea4d09d3217",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "5073be52-0414-4f00-a2de-85473ef42612",
                  "text" : "da",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "8e5b8749-bc5f-4ca8-965e-4bb9a36d616d",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "93fb5c64-a829-4803-afc8-027f32e38480",
                  "text" : "es-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "f79a54d3-03e6-4db1-80a1-426e56055cb9",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "3ef26977-4df8-4baf-ac96-116cf2e35d61",
                  "text" : "se",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "eae789b2-6fc5-4a38-9e3f-5d1aa05674f5",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "f8f7ccfd-f5d1-460a-a51c-dc56e8b9d32e",
                  "text" : "per-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "04931b47-9a3a-490b-9e06-f6e383de1008",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "e9f15ded-6541-4299-91c9-4616048cc635",
                  "text" : "hen-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "c941daa6-fe17-42a6-b0c5-0ebeaa430a8f",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              },
                              {
                                "uuid" : "c291f6a0-4a33-46b8-a329-3c12e88bdd4b",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : True,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "4e4ea497-22df-44a3-9d77-4873e56b9c2a",
                  "text" : "ni",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "0bc422d2-b248-4944-a39c-337a52b71094",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : "b"
            }
          ],
          "kind" : "FormteilContainer"
        }
      ],
      "data" : [
        {
          "name" : "Signatur",
          "data" : "4"
        }
      ],
      "kind" : "FormteilContainer"
    },
    {
      "uuid" : "c43748fa-dd9d-4c54-9d98-760c488609f9",
      "children" : [
        {
          "uuid" : "ea33e3ec-bb5e-4d22-96a5-14804c756345",
          "children" : [
            {
              "uuid" : "1134e6ba-3db4-4205-b70a-d9b924b392c6",
              "children" : [
                {
                  "uuid" : "3ac04e46-0366-4b1b-8b7b-30ad7a9b4b77",
                  "text" : "Te",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "8f86d5f4-a9eb-4f87-8c5f-08574c1973e9",
                                "base" : "A",
                                "octave" : 4,
                                "noteType" : "Strophicus",
                                "focus" : False,
                                "liquescent" : False
                              }
                            ]
                          },
                          {
                            "grouped" : [
                              {
                                "uuid" : "460d3e12-787c-4ac8-9f0e-28daa4761d74",
                                "base" : "A",
                                "octave" : 4,
                                "noteType" : "Strophicus",
                                "focus" : False,
                                "liquescent" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "70f14e9d-8291-4e99-bdf5-5868710e69a0",
                  "text" : "Chri-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "760a4832-78f5-4aca-b241-9ac2c35aaab1",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "244859b0-d66b-48e9-b1e3-4b74f590b73f",
                  "text" : "stus",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "b7444c4c-dc6a-4496-92a1-4f963282bca8",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "33091889-ff86-4ae6-9bdb-9a5f3b71c7af",
                  "text" : "in",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "406e3346-8f26-4e15-8e45-b307c79b44d2",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "c6b4a3f5-ceaf-4456-adc6-d43604eb9cbe",
                  "text" : "cru-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "35c239ae-c00d-407d-a99f-7d5bd45bbc6b",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "bcda0719-81cb-42de-869c-9b8fdbd345dd",
                  "text" : "ce",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "05820a5b-040f-4c7c-a5e3-d66452e9f3fc",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "064ce33e-d6ad-488b-8311-f0066bcac7bb",
                  "text" : "tri-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "742b5488-8bbf-4970-9c5a-12250052348d",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "0fa85cd6-7bc0-4566-b903-0a440312e79b",
                  "text" : "um-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "66be278c-a7ec-4d54-9765-fdb02b6c8f0e",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              },
                              {
                                "uuid" : "373c723b-083b-47da-be13-f126830eb398",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : True,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "cd5773f1-ec98-40ff-a4e1-2bb286bfc888",
                  "text" : "phans",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "34140841-1ebb-4df0-b832-05d9bb7adc73",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "c08a2366-3c84-4308-8b4b-48d6cb3823df",
                  "text" : "ma-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "e07a9ab6-608a-454f-8c13-00616f43c6da",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "0dd5d04c-2b00-44d5-a3de-6cd505d48652",
                  "text" : "tri",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "9dc0a6d3-6d67-442e-8f15-5cf40209410a",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "7ae54ea1-c190-42f6-9f15-c584c21c99fb",
                  "text" : "su-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "93626d25-480a-4bb3-b1c8-4d0b32f59c30",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "091dcfc2-bf3f-453f-ab05-435b2c22894a",
                  "text" : "e",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "3ff099bc-bef9-4076-8ff6-91552c128016",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "0d5a3280-1d6c-422a-8cbe-ebba400a3ac6",
                  "text" : "de-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "135eb1ce-6308-410d-9b9c-200d0803c4ef",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "092dd8ff-4367-4744-bae7-8080d087f0c9",
                  "text" : "dit",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "31ccce28-c56c-4b9e-8f08-a3f7dc29cc89",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "5f26ce7e-9a50-45ec-934c-a136859dd162",
                  "text" : "cu-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "378aa646-f99b-4dba-8fa1-36440ab07a63",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "e077d0da-23ca-4232-9bf1-950720b9e050",
                  "text" : "sto-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "09775aeb-4750-457b-bf97-7d4404b02663",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "d0b984bb-7fc0-43bf-8060-0941217f06ed",
                  "text" : "dem",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "93e7ea92-177f-476a-be95-8a1f139080b6",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : "a"
            }
          ],
          "kind" : "FormteilContainer"
        },
        {
          "uuid" : "a8d4c6c5-6f24-48f5-98cb-b1c18f0c5756",
          "children" : [
            {
              "uuid" : "ff02ed07-9a97-4066-be94-71d2305cc06e",
              "children" : [
                {
                  "uuid" : "4fabfd27-c1ff-4fc0-98de-d36cf52698ea",
                  "kind" : "LineChange",
                  "focus" : True
                },
                {
                  "uuid" : "f094236a-a1ae-4a5a-bc8d-e0ffa07280b6",
                  "text" : "Ut",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "0ca00c42-0cec-4582-8a9d-caa3c48a0669",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "d002b01b-8b4b-4c0b-ba0c-d5804572bfba",
                  "text" : "uir-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "1267a323-1e7a-4019-8ae9-7167f6ca79d9",
                                "base" : "G",
                                "octave" : 4,
                                "noteType" : "Normal",
                                "focus" : False,
                                "liquescent" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "89451f3d-2fbd-4984-bf96-707b5961b69a",
                  "text" : "go",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "37504cd2-f0dd-4f82-92ba-5d6b689447bd",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "f97cca50-c179-4229-a97e-9c41f68c331a",
                  "text" : "uir-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "487915b1-5f59-4eac-93b8-63a1a7892198",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "74ed7039-1cec-42c4-aa74-6a97c73f2b84",
                  "text" : "gi-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "a562dbc9-265f-4008-8e83-7d1250352996",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "64985b2a-3177-41a6-9c71-310619423f33",
                  "text" : "nem",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "03d16ea6-b9ae-4378-852a-f5704d36ba8e",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "1a931581-b4c2-42bb-a002-49653ce10552",
                  "text" : "ser-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "2119291c-5cd0-4e00-8b84-5d6a6e9b976c",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "33a04ca2-594c-4ceb-8165-aa64442c5c77",
                  "text" : "ua-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "8042aa74-f0d3-4656-918f-5e7aa6b48d17",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "7d5ca991-11d1-4594-bacc-14b6d5761ddd",
                  "text" : "res",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "49de9286-e8d5-44f8-bb29-e4919309f2ec",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "05142fd1-c438-4cb7-b6ff-116ca2f69ebc",
                  "text" : "at-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "cc632f18-5df8-42cc-8471-83b4016b74ee",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "4c5785ef-8644-42c9-a28a-606569011034",
                  "text" : "que",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "c897810a-e0c8-414c-847c-c2d4dcc81c63",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "29eb8cb3-3184-430c-b5e6-85935dd36fbf",
                  "text" : "cu-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "7f9d150c-1223-4337-a2ad-71c398061bed",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "01fa3c46-8832-4e68-8959-d6e5639ead76",
                  "text" : "ram",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "167c624c-f52d-44ca-87d6-fd37c61a11ed",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "f277f30d-8eca-47dc-9d48-6f1d5c32a001",
                  "text" : "sup-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "50010952-49a5-407e-ba47-a110fb3832cb",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "0e4c74e9-986b-4423-9010-e4a44e134ede",
                  "text" : "pe-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "1d70d51e-b779-496f-8f86-2be559be6161",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "8bdae090-b6b2-46b8-80b8-5089387b6120",
                  "text" : "di-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "91060862-ea0d-473f-bcab-1a770d19dc40",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "ae4106a0-0635-4371-8ec6-6ea663936fef",
                  "text" : "ta-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "b6356be3-243d-45d2-898f-cc27d0f4d07c",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "b825471d-d09c-4741-b4a1-938565e84ab5",
                  "text" : "res",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "87bb5f2c-edbe-412b-ab70-bc271d5051e3",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : "b"
            }
          ],
          "kind" : "FormteilContainer"
        }
      ],
      "data" : [
        {
          "name" : "Signatur",
          "data" : "5"
        }
      ],
      "kind" : "FormteilContainer"
    },
    {
      "uuid" : "776c4d95-955c-4a86-a9ca-f35d058680f0",
      "children" : [
        {
          "uuid" : "004ac51e-3611-4bad-a7d2-46c83d8db857",
          "children" : [
            {
              "uuid" : "c8e1e93b-b3d2-4fa5-8ddd-b439820b417e",
              "children" : [
                {
                  "uuid" : "4b3cf255-6392-4bfd-b389-984b95174099",
                  "text" : "Tu-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "6d8f7b32-a0b8-4e14-9103-d855bc220ddc",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "dd7c7076-a3bf-402e-9a07-a2f4e2a49f38",
                                "noteType" : "Oriscus",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "9972099c-35c5-4633-a614-553e23d1b80d",
                  "text" : "te",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "7930b76a-1b74-4ff0-94fa-6147dba48075",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "4377adf1-8343-451a-988d-bf0edc4d145f",
                  "text" : "car-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "a6210c69-f8fa-44a5-8efc-f714503286f5",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "03ede5eb-6870-4c17-8cf2-84f52e697e28",
                  "text" : "ce-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "e7aa8c56-64ac-4a40-9dd7-68914f27bacf",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "b3bdf7ea-50e4-4e1c-80f4-d549ebc22fae",
                  "text" : "re",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "b4dfa9a0-67d6-4cc8-85e5-5aa61220be8f",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "8646106d-7548-4955-9229-ba4fd649cbd7",
                  "text" : "fla-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "d58756d3-9955-4546-b33c-d3231d940350",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "24c089a4-5f67-4558-b4a6-630824856c0d",
                  "text" : "gris-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "cdaae01d-c085-43a0-ae3d-d989c5e316b8",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "acf198af-d993-4650-85ea-a64ee4086da3",
                  "text" : "que",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "8309bb3e-1d5c-4023-9c92-e713a3d9bced",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "e39c53c3-8441-485a-b280-beb72b846578",
                  "text" : "fra-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "fa0eec67-9195-4901-90cd-cdaf59c8793f",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "7fc35263-107d-455e-a88a-5c65f0e9201a",
                  "text" : "ctus",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "33837952-daf9-4061-87e3-49bba86c25c0",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "ce14e756-372b-4cbf-b225-cd04021b32fe",
                  "text" : "te-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "96305761-cca0-4362-a58f-021a3cebf5b4",
                                "noteType" : "Normal",
                                "base" : "E",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "6e3c80a6-d6ec-41f9-9697-00ee81c1841b",
                  "text" : "sti-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "d08bdb7d-84fd-4deb-9a2e-2c15fff449e6",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "c2405e8d-f282-407e-bd96-cb293ecc3942",
                  "text" : "mo-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "a8bd3593-762d-4350-9c57-2036c833b8b2",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "b8450000-5a9c-4a59-8685-4fe6459efdde",
                  "text" : "ni-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "890b287c-fee5-49eb-966e-46a7779131b1",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "d0d4d614-2698-4922-ad65-b8e7d1451b54",
                  "text" : "o",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "cc18abfc-057c-46f3-8b2b-3b7de1fcfebb",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "5eed0813-ed98-404e-8c99-7765f91f61ae",
                  "kind" : "LineChange",
                  "focus" : False
                },
                {
                  "uuid" : "a0bffbda-fd23-4247-a8dd-0fe456354f65",
                  "text" : "pro",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "e9f90b3c-a4bf-4119-a8f7-2e04cace4524",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "a4661856-60fe-4db1-a2de-b27caddf2811",
                  "text" : "Chri-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "ca57cc7f-3169-4456-8323-f3015b796cc4",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "134d1193-7d7c-45d8-ba8d-a9fcc7e142e7",
                  "text" : "sti",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "2884eb8e-9415-4f41-ade2-255d405a976e",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "8bcb4524-8236-4078-9453-cb4cb4b610e7",
                  "text" : "es",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "8dcf5b75-9c38-413c-89e1-fb97d3e0acd0",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "fa02aaaf-ef00-4e81-98cd-c5c05cb2bca6",
                  "text" : "ga-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "52e06ce0-6878-49bd-979e-04663e27892d",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "50e389c4-cf63-4fba-a07a-c48e6ac1df62",
                  "text" : "ui-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "8f34165b-251f-4e10-8e3f-cae265afdeba",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "aa390c07-1bba-4383-a50b-e7a82e81a977",
                  "text" : "sus",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "215c73a5-7607-4a25-8ce7-6c29bbcd6463",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : "a"
            }
          ],
          "kind" : "FormteilContainer"
        },
        {
          "uuid" : "082f1076-34d7-42ba-a6e2-016641324188",
          "children" : [
            {
              "uuid" : "61a0ed01-3952-4e2d-a78c-da51ceed10b3",
              "children" : [
                {
                  "uuid" : "f2f646d3-01b8-4727-a731-a7831dca49ac",
                  "text" : "I-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "7aea19b3-cad6-41bf-a249-da489b6723a7",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "4524e257-226a-4ab8-8f50-2508e3422d59",
                  "text" : "dem",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "76cd5a2c-521c-40c9-a3e5-16a32b00c828",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "9a4e3569-206d-4597-ad3d-7cd5f733ccb4",
                  "text" : "mor-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "570053f8-810d-42aa-8412-d7064167eed3",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "477e4fca-fea2-4b01-82db-a0bbcbab1cf2",
                  "text" : "tu-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "bc86b4fc-b2c0-4e77-bc44-3a1419af2bb7",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "8030611f-3935-4211-bc43-8d1f37293e8b",
                  "text" : "os",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "3ce68d5e-255a-4b68-bd94-3335297be5ca",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "d635fbce-e042-433b-8803-5f4e95f48b73",
                  "text" : "sus-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "2805d4a6-b4bb-44a6-8cb6-82459ae68179",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "2df42e63-c15b-432c-92e7-a35d3bbcdd78",
                  "text" : "ci-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "c46abbc1-12ab-4cd1-ac0b-e5cf182a7930",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "1595f391-9730-4dbe-bbc0-0c1f64b0c4a7",
                  "text" : "tans",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "d8e4e5dd-d1f3-4b10-be63-35f4d1d56f4d",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "e18ef5b7-9e28-43e0-a67f-3867816cf452",
                  "text" : "in-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "9633b236-494f-4330-aadc-03ea650dd221",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "fbaf223f-c74d-4a46-b017-378a6489be41",
                  "text" : "que",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "6af8a1ab-ef5a-4473-b41d-b826b997edb3",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "8a2c6b49-7f42-4c9b-a60d-45c3c28adbcd",
                  "text" : "Ie-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "fdfb84c4-64e2-4a13-9fc5-01f63b87b181",
                                "noteType" : "Normal",
                                "base" : "E",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "9bb52849-1531-48bb-b1f7-14c888fcf8b4",
                  "text" : "su",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "de2b6986-c8f6-4251-a17c-7b93949f0f82",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "c3a50fcf-a3ab-43ee-9528-d0643388beaf",
                  "text" : "no-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "cf3f7734-b16e-4a90-8989-c07acfddc16d",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "5c778e18-c1d4-4f42-9a90-956fc9a24b61",
                  "text" : "mi-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "2209bb77-1be1-4e78-a406-0f4c29c57935",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "b8f63222-77a6-43a1-a2cc-cb01623cd13f",
                  "text" : "ne",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "09b3bf99-4dba-4e78-b905-9cec670f2f73",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "ad95de92-b313-4764-bead-72c5f8513a51",
                  "text" : "ue-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "528dc3c5-7587-4c42-9b1a-b7a825ab2d29",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "d23183fe-63b8-49a0-8261-01fd6b1139b4",
                  "text" : "ne-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "304d5db8-6d27-4101-8234-d9f58ae34a69",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "bf537e3d-dd67-40a5-b875-b4b6ed62a578",
                  "text" : "num",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "ce8676e6-b488-4f51-b6b5-f0f9eb2f1a40",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "8264c77e-967b-4b79-a854-cda508278415",
                  "text" : "for-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "9bc77240-73bc-42d4-825d-6619b6ab5522",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "a3f38bcd-fc16-4ba5-af45-dc9581169938",
                  "text" : "te",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "2b4ecc54-8055-485d-8b2e-09ed1f356232",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "b5dbfcd6-a439-4ec5-879c-7d692c0aef77",
                  "text" : "uin-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "596abd6c-2bb7-4e57-b7af-84d59c931147",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "7bbb72ea-8677-47ea-a6f3-b767702f859f",
                  "text" : "cis",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "1730a256-fcfb-46ca-ab8d-5ceddcf7e4c2",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : "b"
            }
          ],
          "kind" : "FormteilContainer"
        }
      ],
      "data" : [
        {
          "name" : "Signatur",
          "data" : "6"
        }
      ],
      "kind" : "FormteilContainer"
    },
    {
      "uuid" : "0be2359c-fd3b-49a3-8e28-516f826488b9",
      "children" : [
        {
          "uuid" : "14df776f-e681-4ef0-a5cb-1f612d5f922f",
          "children" : [
            {
              "uuid" : "685c0b74-ec53-4105-b020-6e0b779b755b",
              "children" : [
                {
                  "uuid" : "674851a1-7b76-4db1-8f3a-d08cffc593d1",
                  "text" : "Ti-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "7e071f9f-462d-43be-bb8a-51f282805013",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "3bdd0d8f-f3a7-41f5-9a77-d0dfaa04c916",
                  "text" : "bi",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "189ee907-77b2-42af-b79a-c7684c77ab8f",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "fc900d70-9b6a-4d5e-9fb1-4f967aa84461",
                  "text" : "sum-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "246a867b-5603-4096-a03d-8d8312cda649",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              },
                              {
                                "uuid" : "28067247-dbc1-4cf7-a719-d75dc0bd52f8",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : True,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "f78d1516-4799-4b9b-ad21-6fa25dee77db",
                  "text" : "mus",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "c04cde86-fc1d-4d12-a06e-e488336dabbd",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "4b3687aa-cf3f-471d-aa65-21db972fe174",
                  "kind" : "LineChange",
                  "focus" : False
                },
                {
                  "uuid" : "11ccd092-e35f-40be-bc28-448a93e2a39d",
                  "text" : "ta-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "78e0845e-7c1d-449f-b01e-3a37568de2f6",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "fa02e5e0-f82b-4dae-8d81-8e91aece2d2b",
                  "text" : "ci-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "3e35f17f-5406-497b-8369-4e64d68017a6",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "f1707410-6cc2-4c89-bf4c-b183fbbe7713",
                  "text" : "tum",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "2c2e21c3-ebe6-455b-8b08-65826604f1c9",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "e4a6703c-18f7-4e39-82e9-40337a7cd2da",
                  "text" : "ce-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "1eb3f163-1c4a-4367-9a51-57b36f663042",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "763b7690-71f9-4dbf-b1d0-a891b546a8d4",
                  "text" : "te-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "ab2a16e1-e956-4a11-ae42-66f0fdfba935",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "b4c2c937-48db-4108-a30f-f849ac7e0456",
                  "text" : "ris",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "f9451353-f4e6-496a-8580-9e130de626e5",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "34c5f7fb-738a-4c31-bd0a-67049ba57792",
                  "text" : "uer-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "8679ca69-5a73-46f0-8668-7cea5bdf5c89",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "b7c53d56-3eae-4caf-ba6b-91694b63477b",
                  "text" : "bum",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "5e862697-06d4-4eab-bb8d-4078f32ebe4f",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "85d2f3df-433d-44d8-b8d3-23d2a77c42ee",
                  "text" : "su-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "4180f1ad-04a2-43c8-b8fa-263323b0e43b",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "ef704ae0-03e0-44c5-98b8-013319811b28",
                  "text" : "um",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "b68df425-f97b-4425-b508-916ef2d086e5",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "845b94c3-7e51-4006-b651-6ae10feb048d",
                  "text" : "pa-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "33960b60-7e56-420b-a185-d28ff8fb6b7d",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "98ba8b7d-e47d-4281-a536-08410de3dd51",
                  "text" : "ter",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "a40f291b-36f7-481b-9ddf-0c89101ace1e",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "76aca6b9-8e75-4f76-81f1-68354e6c5b61",
                  "text" : "re-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "da3f4c9c-e4d9-4db8-922f-b9b787142344",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "f17b17d4-68c8-41fc-b6bd-ba6053302163",
                  "text" : "ue-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "21bbc6ab-d65a-4caf-a95a-bec52d4ee12e",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "fc5c5d77-81e5-493f-b419-3cd392f5742e",
                  "text" : "lat",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "aaba74a2-b47b-42fb-b4d8-4894cefd1393",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : "a"
            }
          ],
          "kind" : "FormteilContainer"
        },
        {
          "uuid" : "6b6d4ec6-93f3-4501-be9f-71e470e38ac0",
          "children" : [
            {
              "uuid" : "de0bf03d-d266-49fe-93c1-3280274878c8",
              "children" : [
                {
                  "uuid" : "576d191f-043f-4f64-a076-098751002e9e",
                  "text" : "Tu",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "1c4c3308-ca72-4a2a-93d1-6c5b0cc95844",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "16e6b378-29f2-4fb8-9aa6-88b52bb4987b",
                  "text" : "nos",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "84c5cc46-f792-45b7-9bfd-747534fc260b",
                                "base" : "A",
                                "octave" : 4,
                                "noteType" : "Normal",
                                "focus" : False,
                                "liquescent" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "97d20582-2ee3-45bf-971b-bec2f1dcca0f",
                  "text" : "om-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "2e348836-8b93-40ce-923e-2b0de437213f",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              },
                              {
                                "uuid" : "39ba820b-9a3b-4696-8850-fc2a62260740",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : True,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "8d6a7638-bda9-42f1-bc3e-b0f166e6f4e3",
                  "text" : "nes",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "762f895c-f177-4040-9b06-a7193171e084",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "2133cf0a-43c3-4540-a1a5-03dfff4e5a0c",
                  "text" : "se-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "0e54b049-a7bb-490c-8a14-3bc3b6ad2461",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "19331aca-0402-49f1-8831-5a5e95eecdad",
                  "text" : "du-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "f1739c7e-9c45-4356-8252-1474d9d6006b",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "0a0f6a91-9e2b-4aaf-b2fc-ca8d52ab419d",
                  "text" : "lis",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "e42b3a90-23f0-4df3-99ff-39b5cc3b6587",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "e600417d-7bb3-4ac3-a61a-71816851165a",
                  "text" : "pre-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "eca3eb54-29bd-4a0a-9847-f437d9dff479",
                                "noteType" : "Normal",
                                "base" : "D",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "691fc105-7164-44fa-bf03-55b0e672d2d0",
                  "text" : "ci-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "169fba3c-4c8d-45b2-8d12-4716178f45a2",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "3321b269-6a1e-4caf-9198-89a414d54b02",
                  "text" : "bus",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "8ae31e68-531e-4c3c-bfb1-3be01a9e2c19",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "269feb97-2ae2-4130-9b0b-cdfa1ec02d9b",
                  "text" : "a-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "e96b4f91-563a-4bbb-8e9f-177e32e03f59",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "e5a88968-f4c4-41ae-8cdc-aadef9fa6110",
                  "text" : "pud",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "dcb24711-d893-4104-8ef9-361d759699de",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "a3b6432f-c7d5-4ea2-b361-a721bf51ef26",
                  "text" : "de-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "a580db3c-2c96-4b5c-81c8-af465d8a55b9",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "48798a40-8933-4baf-9ae1-b9c8a16fbe64",
                  "text" : "um",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "da86a77e-a1e3-46ea-b03d-894e5f6e3ce4",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "16d089c5-ecf1-4b8b-b253-a9fab0c21f74",
                  "text" : "sem-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "20056cf5-ba31-40ca-97d9-e84d8668cc44",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "96b81395-166a-4c8d-a936-de6e13b91034",
                  "text" : "per",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "5386b64e-a6c9-4617-afe3-4b04d745653f",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "974fd944-5974-4ec6-a911-258d2c3e17a6",
                  "kind" : "FolioChange",
                  "focus" : False,
                  "text" : "f. 158"
                },
                {
                  "uuid" : "f31d3a55-ce1e-4c60-bd47-4ee4660531f8",
                  "text" : "com-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "98d6a2e1-5366-4413-8356-9e25746af01b",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "14c87e05-4017-466a-80b9-2c719aac9226",
                  "text" : "men-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "b99cd9ec-491f-404a-a9d3-3a6cf3d73677",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              },
                              {
                                "uuid" : "09456f74-c2d3-4b34-8e72-75577eef7693",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : True,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "e95ff479-8faa-438b-8917-5c1de486b25a",
                  "text" : "da",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "51420055-f942-4c4b-afba-6c2ad30eb878",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : "b"
            }
          ],
          "kind" : "FormteilContainer"
        }
      ],
      "data" : [
        {
          "name" : "Signatur",
          "data" : "7"
        }
      ],
      "kind" : "FormteilContainer"
    },
    {
      "uuid" : "e4170b77-187a-42ce-8b37-b0fedbaa96c9",
      "children" : [
        {
          "uuid" : "9b175fde-2cac-4c31-8d4d-3fc716cc8935",
          "children" : [
            {
              "uuid" : "e1737575-33ca-4e4a-9c31-b2b6ae523026",
              "children" : [
                {
                  "uuid" : "b47c3213-5ab6-42b8-81ee-ef560b2d07ba",
                  "text" : "Io-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "fcb34937-23e6-41e9-8789-aa4db7758139",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "cdf352be-20eb-4f9c-afb4-5a9047adac9b",
                  "text" : "han-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "53df7498-415f-4add-a084-6af178c0a628",
                                "noteType" : "Normal",
                                "base" : "G",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "1e4efa18-e5dc-4ee5-9105-1f343c766091",
                  "text" : "nes",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "59bfb991-f9da-4289-bbc7-66431a3b3ace",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "a18c3d95-24c4-497e-a10f-0d678cff97f6",
                  "text" : "Chri-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "2f3f2412-23e3-4a22-859f-122affbd0ec6",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "9fe9627c-d4ee-4e4b-8b2f-996e8fbb442e",
                  "text" : "sti",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "088235db-434e-440e-b587-0a2b73bd5107",
                                "noteType" : "Normal",
                                "base" : "C",
                                "liquescent" : False,
                                "octave" : 5,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "61fd91a7-3912-4e50-ba59-5e6d0d88cef1",
                  "text" : "ca-",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "0e959f5e-dac4-4e9b-ac62-330e5a614ff3",
                                "noteType" : "Normal",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              },
                              {
                                "uuid" : "bfa33005-255d-4b03-bac8-60634707de16",
                                "noteType" : "Oriscus",
                                "base" : "B",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : False
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                },
                {
                  "uuid" : "03991eb1-3b64-4629-9b32-20a5a5764c52",
                  "text" : "re",
                  "notes" : {
                    "spaced" : [
                      {
                        "nonSpaced" : [
                          {
                            "grouped" : [
                              {
                                "uuid" : "95f1aab8-4080-4fb2-959a-1890f4586f72",
                                "noteType" : "Normal",
                                "base" : "A",
                                "liquescent" : False,
                                "octave" : 4,
                                "focus" : True
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  },
                  "syllableType" : "Normal",
                  "kind" : "Syllable"
                }
              ],
              "kind" : "ZeileContainer"
            }
          ],
          "data" : [
            {
              "name" : "Signatur",
              "data" : ""
            }
          ],
          "kind" : "FormteilContainer"
        }
      ],
      "data" : [
        {
          "name" : "Signatur",
          "data" : "8"
        }
      ],
      "kind" : "FormteilContainer"
    }
  ],
  "comments" : [
    {
      "startUUID" : "e617f59f-2de8-4fc8-be24-8aac161cbbe3",
      "endUUID" : "916f2c27-36ff-4a99-b21c-eafa583b570a",
      "text" : "Iohannes Iesu Christo multum di-] korrigiert aus Lesart.",
      "lines" : [
        {
          "uuid" : "e868c56b-8e86-4c6b-9b0c-4b0490baa8ae",
          "kind" : "ZeileContainer",
          "children" : [
            {
              "uuid" : "12adaa1d-bd6a-4b1f-83e8-dd7fde97289f",
              "text" : "Io-",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "e617f59f-2de8-4fc8-be24-8aac161cbbe3",
                            "noteType" : "Normal",
                            "base" : "D",
                            "liquescent" : False,
                            "octave" : 4,
                            "focus" : False
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            },
            {
              "uuid" : "bac36058-bc17-46fc-9db4-e953b41d24f3",
              "text" : "han-",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "cfec5748-642b-4aac-b12b-3ec6b49a8bd6",
                            "noteType" : "Normal",
                            "base" : "F",
                            "liquescent" : False,
                            "octave" : 4,
                            "focus" : False
                          },
                          {
                            "uuid" : "2eda7e82-b7b0-4543-a6d6-373720c72018",
                            "noteType" : "Normal",
                            "base" : "E",
                            "liquescent" : True,
                            "octave" : 4,
                            "focus" : False
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            },
            {
              "uuid" : "5c8cd1d5-93e9-4a41-87bd-a7a56e40e6d6",
              "text" : "nes",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "5a05ba3d-c169-4757-86a4-d18e4552b0e9",
                            "noteType" : "Normal",
                            "base" : "D",
                            "liquescent" : False,
                            "octave" : 4,
                            "focus" : False
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            },
            {
              "uuid" : "0a215f7c-9edd-4562-a36f-05579c9bd28b",
              "text" : "Ie-",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "36d3479b-69a6-4ae5-966b-5bd70fb3a197",
                            "noteType" : "Normal",
                            "base" : "D",
                            "liquescent" : False,
                            "octave" : 4,
                            "focus" : False
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            },
            {
              "uuid" : "82aa7afa-c96f-4c16-b586-85539073b976",
              "text" : "su",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "d489b659-864a-4277-864d-7c39613e3ecb",
                            "noteType" : "Normal",
                            "base" : "E",
                            "liquescent" : False,
                            "octave" : 4,
                            "focus" : True
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            },
            {
              "uuid" : "4be1028b-4c22-41fe-b8d5-931e5c57e431",
              "text" : "Chri-",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "7b26f073-0d59-4168-9d17-020b2eea0add",
                            "noteType" : "Normal",
                            "base" : "F",
                            "liquescent" : False,
                            "octave" : 4,
                            "focus" : False
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            },
            {
              "uuid" : "461d3458-b973-4a5a-a289-6aa91800ac4d",
              "text" : "sto",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "3b458e51-724b-41c7-a54e-f6683194c689",
                            "noteType" : "Normal",
                            "base" : "E",
                            "liquescent" : False,
                            "octave" : 4,
                            "focus" : False
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            },
            {
              "uuid" : "29945796-fcaa-4070-9efe-bb10b1d39b14",
              "text" : "mul-",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "c9b0ede4-9910-4035-b26b-82bbd53efbb2",
                            "noteType" : "Normal",
                            "base" : "G",
                            "liquescent" : False,
                            "octave" : 4,
                            "focus" : False
                          },
                          {
                            "uuid" : "5f5ca5da-b800-43ae-8d12-b6a0457c498d",
                            "noteType" : "Normal",
                            "base" : "F",
                            "liquescent" : True,
                            "octave" : 4,
                            "focus" : False
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            },
            {
              "uuid" : "bbf22995-cdf4-4e74-996d-092ad5ec0f69",
              "text" : "tum",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "3abfb8ab-3974-4816-a14f-513146d9072f",
                            "noteType" : "Normal",
                            "base" : "E",
                            "liquescent" : False,
                            "octave" : 4,
                            "focus" : True
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            },
            {
              "uuid" : "b0ca2fe4-23ed-428f-86f9-4fa9daea94d6",
              "text" : "di-",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "6ee1d815-d4e6-41cc-8a8b-24d9710a5ee6",
                            "base" : "E",
                            "octave" : 4,
                            "noteType" : "Normal",
                            "focus" : False,
                            "liquescent" : False
                          },
                          {
                            "uuid" : "7140329e-e33b-4f16-86f5-c3835051505b",
                            "base" : "A",
                            "octave" : 4,
                            "noteType" : "Normal",
                            "focus" : False,
                            "liquescent" : False
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            }
          ]
        }
      ]
    },
    {
      "startUUID" : "dddc5435-3e6f-4cf2-beed-4f899e8e180d",
      "endUUID" : "89e06429-02e2-4369-acac-a67cb4c94a47",
      "text" : "conspexisti] korrigiert aus Lesart.",
      "lines" : [
        {
          "uuid" : "dcd4e0ff-ffc8-48cb-8f72-6456b3517978",
          "kind" : "ZeileContainer",
          "children" : [
            {
              "uuid" : "d67f3ccf-e340-4a06-a77e-1b237d017368",
              "text" : "con-",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "dddc5435-3e6f-4cf2-beed-4f899e8e180d",
                            "noteType" : "Normal",
                            "base" : "D",
                            "liquescent" : False,
                            "octave" : 5,
                            "focus" : False
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            },
            {
              "uuid" : "f36c113c-51e6-4b02-b8cb-d5aeda416df6",
              "text" : "spe-",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "09a7ba59-4139-41e2-863d-af6cddf5b4c3",
                            "noteType" : "Normal",
                            "base" : "C",
                            "liquescent" : False,
                            "octave" : 5,
                            "focus" : False
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            },
            {
              "uuid" : "6e54ed46-1452-4f4b-8d2d-6a63b9348020",
              "text" : "xi-",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "ea7f65ec-b8a1-4858-85c1-443352b35516",
                            "noteType" : "Normal",
                            "base" : "B",
                            "liquescent" : False,
                            "octave" : 4,
                            "focus" : False
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            },
            {
              "uuid" : "72a0066a-4df5-4a03-85ee-2d4df93b6720",
              "text" : "sti",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "89e06429-02e2-4369-acac-a67cb4c94a47",
                            "noteType" : "Normal",
                            "base" : "C",
                            "liquescent" : False,
                            "octave" : 5,
                            "focus" : True
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            }
          ]
        }
      ]
    },
    {
      "startUUID" : "93e7ea92-177f-476a-be95-8a1f139080b6",
      "endUUID" : "93e7ea92-177f-476a-be95-8a1f139080b6",
      "text" : "-dem] emendiert nach 5b.",
      "emendation" : True,
      "lines" : [
        {
          "uuid" : "e37ed976-8090-4c5e-9377-2c53814b0b27",
          "kind" : "ZeileContainer",
          "children" : [
            {
              "uuid" : "d0b984bb-7fc0-43bf-8060-0941217f06ed",
              "text" : "dem",
              "notes" : {
                "spaced" : [
                  {
                    "nonSpaced" : [
                      {
                        "grouped" : [
                          {
                            "uuid" : "93e7ea92-177f-476a-be95-8a1f139080b6",
                            "noteType" : "Normal",
                            "base" : "B",
                            "liquescent" : False,
                            "octave" : 4,
                            "focus" : True
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              "syllableType" : "Normal",
              "kind" : "Syllable"
            }
          ]
        }
      ]
    }
  ],
  "documentType" : "Level2",
  "version" : None,
  "kind" : "RootContainer"
}

chant_data = {
    "entry_path": "../../data/Aa 13/0cf5420e-a94d-4b23-aaac-ac5f27ba07e7"
}


@dataclass
class Neume:
    uuid: str
    spaced_element: dict
    index: tuple


# Create mock Neume data
neume_data = {
    "uuid": str(uuid.uuid4()),
    "spaced_element": {
        "noteType": "Normal",
        "base": "C",
        "liquescent": False,
        "octave": 4,
        # ... other neume attributes
    },
    "index": (0, 0)  # Example index
}


@dataclass
class Syllable:
    uuid: str
    kind: str
    index: tuple
    text: str
    syllableType: str
    notes: dict
    endsWord: bool
    focus: bool
    hasNotes: bool
    neumes: list


# Create mock Syllable data
syllable_data = {
    "uuid": str(uuid.uuid4()),
    "kind": "some_kind",
    "index": (0, 0),  # Example index
    "text": "Example Text",
    "syllableType": "Normal",
    "notes": {
        "spaced": [
            {"noteType": "Normal", "base": "C", "liquescent": False, "octave": 4},
            # Add more notes as needed
        ]
    },
    "endsWord": False,
    "focus": False,
    "hasNotes": True,
    "neumes": []  # List of Neume instances
}
source_meta_mock = {
  "id" : "Apt 17",
  "quellensigle" : "Apt 17",
  "herkunftsregion" : "Quellen aquitanischer Herkunft",
  "herkunftsort" : "Apt",
  "herkunftsinstitution" : "",
  "ordenstradition" : "",
  "quellentyp" : "Tropar, Prosar",
  "bibliotheksort" : "Apt",
  "bibliothek" : "Archive Basilique de Sainte Anne",
  "bibliothekssignatur" : "Ms. 17",
  "kommentar" : "",
  "datierung" : "11. Jh Mitte",
  "status" : "true",
  "jahrhundert" : "11.",
  "manifest" : "",
  "foliooffset" : -1,
  "publish": True,
  "unknownvalue": "test"
}

doc_meta_mock = {
  "id" : "0de145d0-1435-40d5-95d4-78ff9e8c1f1e",
  "quelle_id" : "Apt 17",
  "dokumenten_id" : "Apt 17-326-4",
  "gattung1" : "Tropus",
  "unknownvalue": "test",
  "gattung2" : "Offertorium-Tropus",
  "festtag" : "Omnes sancti",
  "feier" : "Messe",
  "textinitium" : "O quam mellifluum",
  "bibliographischerverweis" : "O quam gloriosum off 1 A 2^CM B (CT X)",
  "druckausgabe" : "II-3",
  "zeilenstart" : "4",
  "foliostart" : "326",
  "kommentar" : "nicht d8a37389-3554-467e-ac5b-0e18485527ac",
  "editionsstatus" : "ediert",
  "additionalData" : {
    "Melodiennummer_Katalog" : "",
    "Editor" : "david.catalunya@uni-wuerzburg.de",
    "Bezugsgesang" : "(O quam gloriosum)",
    "Melodie_Standard" : "",
    "Endseite" : "326",
    "Startposition" : "",
    "Zusatz_zu_Textinitium" : "",
    "Referenz_auf_Spiel" : "",
    "Endzeile" : "8",
    "Nachtragsschicht" : "",
    "Überlieferungszustand" : "",
    "Melodie_Quelle" : ""
  }
}