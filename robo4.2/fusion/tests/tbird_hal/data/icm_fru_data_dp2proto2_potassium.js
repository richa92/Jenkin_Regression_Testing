{
    "Name": "Interconnect",
    "Type": "HpEmFru.1.0.0",
    "Parsed": {
        "Type": "Potassium_DP2",
        "Preamble": {
            "SchemaFile": "Potassium_DP2.schema",
            "Model": "HP Ethernet ICM",
            "LastModified": "2014-06-03",
            "FactoryTimeStamp": "123456",
            "EEPROMSize": 1048576,
            "Language": "en-US",
            "HwCompliance": [
                "TAA",
                "NEBS",
                "...TBD"
            ],
            "GreenFactor": [
                "Low Halogen",
                "...TBD"
            ],
            "FruType": "ICM",
            "FruSubType": [
                "Ethernet"
            ],
            "CommType": [
                "RIS",
                "SOAP"
            ]
        },
        "ProductInfo": {
            ".Comment": "Does not support ChassisInfo",
            "Manufacturer": "HP",
            "ManufacturedFor": "HP",
            "SerialNumber": "0000000010",
            "PartNumber": "779224-B21",
            "PCASerialNumber": "00000000000014",
            "PCASparePartNumber": "785339-001",
            "AssemblyPartNumber": "779226-001",
            "BoardRevCode": "DP2"
        },
        "GraphicsInfo": {
            "Image": [
                {
                    "View": "Front",
                    "File": "Icm-front-xyz.1.0.0.svgz",
                    "Source": "FRU"
                },
                {
                    "View": "Back",
                    "File": "Icm-back-xyz.1.0.0.svgz",
                    "Source": "FRU"
                },
                {
                    "View": "Side",
                    "File": "Icm-side-xyz.1.0.0.svgz",
                    "Source": "FRU"
                }
            ]
        },
        "PowerInfo": {
            "FullOn": 20,
            "Vaux": 2
        },
        "IcmInfo": {
            "Capabilities": {
                "XLinkInfo": [
                    {
                        "Id": 1,
                        "SerdesType": "FF"
                    },
                    {
                        "Id": 2,
                        "SerdesType": "FF"
                    },
                    {
                        "Id": 3,
                        "SerdesType": "FF"
                    },
                    {
                        "Id": 4,
                        "SerdesType": "FF"
                    }
                ],
                "EkeyMismatch": "DisableFromPowerOn",
                "EkeyGroupMatchReq": [],
                "MpSupport": true,
                "MpInfo": {
                    "ResetSupported": true,
                    "ResetDisruptsDataFlow": true,
                    "ConnType": "Mux",
                    "ConnInfo": [
                        "CL37"
                    ],
                    "TechType": "Ethernet",
                    "Speed": "1Gbps",
                    "MpToEmLL": [
                        11,
                        22
                    ]
                },
                "LLSupport": true
            },
            "PortMap": [
                {
                    "ConnName": "CXP1",
                    "ConnLoc": "Faceplate",
                    "ConnType": [
                        "Copper"
                    ],
                    "TechType": "Ethernet",
                    "SerdesType": "FF",
                    "FaceplateToPort": [
                        {
                            "PrSp": 10,
                            "PinSp": 10,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "1"
                                    ],
                                    "PrName": "10GE1/0/51:1"
                                },
                                {
                                    "Pin": [
                                        "2"
                                    ],
                                    "PrName": "10GE1/0/51:2"
                                },
                                {
                                    "Pin": [
                                        "3"
                                    ],
                                    "PrName": "10GE1/0/51:3"
                                },
                                {
                                    "Pin": [
                                        "4"
                                    ],
                                    "PrName": "10GE1/0/51:4"
                                },
                                {
                                    "Pin": [
                                        "5"
                                    ],
                                    "PrName": "10GE1/0/52:1"
                                },
                                {
                                    "Pin": [
                                        "6"
                                    ],
                                    "PrName": "10GE1/0/52:2"
                                },
                                {
                                    "Pin": [
                                        "7"
                                    ],
                                    "PrName": "10GE1/0/52:3"
                                },
                                {
                                    "Pin": [
                                        "8"
                                    ],
                                    "PrName": "10GE1/0/52:4"
                                },
                                {
                                    "Pin": [
                                        "9"
                                    ],
                                    "PrName": "10GE1/0/53:1"
                                },
                                {
                                    "Pin": [
                                        "10"
                                    ],
                                    "PrName": "10GE1/0/53:2"
                                },
                                {
                                    "Pin": [
                                        "11"
                                    ],
                                    "PrName": "10GE1/0/53:3"
                                },
                                {
                                    "Pin": [
                                        "12"
                                    ],
                                    "PrName": "10GE1/0/53:4"
                                }
                            ]
                        },
                        {
                            "PrSp": 20,
                            "PinSp": 10,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "1..2"
                                    ],
                                    "PrName": "20GE1/0/51:1"
                                },
                                {
                                    "Pin": [
                                        "3..4"
                                    ],
                                    "PrName": "20GE1/0/51:3"
                                },
                                {
                                    "Pin": [
                                        "5..6"
                                    ],
                                    "PrName": "20GE1/0/52:1"
                                },
                                {
                                    "Pin": [
                                        "7..8"
                                    ],
                                    "PrName": "20GE1/0/52:3"
                                },
                                {
                                    "Pin": [
                                        "9..10"
                                    ],
                                    "PrName": "20GE1/0/53:1"
                                },
                                {
                                    "Pin": [
                                        "11..12"
                                    ],
                                    "PrName": "20GE1/0/52:3"
                                }
                            ]
                        },
                        {
                            "PrSp": 40,
                            "PinSp": 10,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "1..4"
                                    ],
                                    "PrName": "40GE1/0/51"
                                },
                                {
                                    "Pin": [
                                        "5..8"
                                    ],
                                    "PrName": "40GE1/0/52"
                                },
                                {
                                    "Pin": [
                                        "9..12"
                                    ],
                                    "PrName": "40GE1/0/53"
                                }
                            ]
                        },
                        {
                            "PrSp": 100,
                            "PinSp": 25,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "1..4"
                                    ],
                                    "PrName": "100GE1/0/51"
                                },
                                {
                                    "Pin": [
                                        "5..8"
                                    ],
                                    "PrName": "100GE1/0/52"
                                },
                                {
                                    "Pin": [
                                        "9..12"
                                    ],
                                    "PrName": "100GE1/0/53"
                                }
                            ]
                        }
                    ]
                },
                {
                    "ConnName": "SFP+1",
                    "ConnLoc": "Faceplate",
                    "ConnType": [
                        "Copper"
                    ],
                    "TechType": "Ethernet",
                    "SerdesType": "FF",
                    "FaceplateToPort": [
                        {
                            "PrSp": 10,
                            "PinSp": 10,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "1"
                                    ],
                                    "PrName": "10GE1/0/1:1"
                                },
                                {
                                    "Pin": [
                                        "2"
                                    ],
                                    "PrName": "10GE1/0/1:2"
                                },
                                {
                                    "Pin": [
                                        "3"
                                    ],
                                    "PrName": "10GE1/0/1:3"
                                },
                                {
                                    "Pin": [
                                        "4"
                                    ],
                                    "PrName": "10GE1/0/1:4"
                                }
                            ]
                        },
                        {
                            "PrSp": 20,
                            "PinSp": 10,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "1..2"
                                    ],
                                    "PrName": "20GE1/0/1:1"
                                },
                                {
                                    "Pin": [
                                        "3..4"
                                    ],
                                    "PrName": "20GE1/0/1:3"
                                }
                            ]
                        },
                        {
                            "PrSp": 40,
                            "PinSp": 10,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "1..4"
                                    ],
                                    "PrName": "40GE1/0/1"
                                }
                            ]
                        },
                        {
                            "PrSp": 100,
                            "PinSp": 25,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "1..4"
                                    ],
                                    "PrName": "100GE1/0/1"
                                }
                            ]
                        }
                    ]
                },
                {
                    "ConnName": "JS1",
                    "ConnLoc": "Midplane",
                    "ConnType": [
                        "Copper"
                    ],
                    "TechType": "Ethernet",
                    "SerdesType": "FF",
                    "JSToPort": [
                        {
                            "PrSp": 10,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6"
                                    ],
                                    "PrName": "10GE1/0/51:1"
                                },
                                {
                                    "Pin": [
                                        "A9"
                                    ],
                                    "PrName": "10GE1/0/51:2"
                                },
                                {
                                    "Pin": [
                                        "B9"
                                    ],
                                    "PrName": "10GE1/0/51:3"
                                },
                                {
                                    "Pin": [
                                        "C9"
                                    ],
                                    "PrName": "10GE1/0/51:4"
                                },
                                {
                                    "Pin": [
                                        "D6"
                                    ],
                                    "PrName": "10GE1/0/52:1"
                                },
                                {
                                    "Pin": [
                                        "D9"
                                    ],
                                    "PrName": "10GE1/0/52:2"
                                },
                                {
                                    "Pin": [
                                        "E9"
                                    ],
                                    "PrName": "10GE1/0/52:3"
                                },
                                {
                                    "Pin": [
                                        "F9"
                                    ],
                                    "PrName": "10GE1/0/52:4"
                                }
                            ]
                        },
                        {
                            "PrSp": 20,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9"
                                    ],
                                    "PrName": "20GE1/0/51:1"
                                },
                                {
                                    "Pin": [
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "20GE1/0/51:3"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9"
                                    ],
                                    "PrName": "20GE1/0/52:1"
                                },
                                {
                                    "Pin": [
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "20GE1/0/52:3"
                                }
                            ]
                        },
                        {
                            "PrSp": 40,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9",
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "40GE1/0/51"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9",
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "40GE1/0/52"
                                }
                            ]
                        },
                        {
                            "PrSp": 100,
                            "PinSp": 25,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9",
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "100GE1/0/51"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9",
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "100GE1/0/52"
                                }
                            ]
                        },
                        {
                            "PrSp": 100,
                            "PinSp": 25,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "E12",
                                        "D12"
                                    ],
                                    "PrName": "100GE1/0/97"
                                }
                            ]
                        }
                    ]
                },
                {
                    "ConnName": "JS2",
                    "ConnLoc": "Midplane",
                    "ConnType": [
                        "Copper"
                    ],
                    "TechType": "Ethernet",
                    "SerdesType": "FF",
                    "JSToPort": [
                        {
                            "PrSp": 10,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6"
                                    ],
                                    "PrName": "10GE1/0/53:1"
                                },
                                {
                                    "Pin": [
                                        "A9"
                                    ],
                                    "PrName": "10GE1/0/53:2"
                                },
                                {
                                    "Pin": [
                                        "B9"
                                    ],
                                    "PrName": "10GE1/0/53:3"
                                },
                                {
                                    "Pin": [
                                        "C9"
                                    ],
                                    "PrName": "10GE1/0/53:4"
                                },
                                {
                                    "Pin": [
                                        "D6"
                                    ],
                                    "PrName": "10GE1/0/54:1"
                                },
                                {
                                    "Pin": [
                                        "D9"
                                    ],
                                    "PrName": "10GE1/0/54:2"
                                },
                                {
                                    "Pin": [
                                        "E9"
                                    ],
                                    "PrName": "10GE1/0/54:3"
                                },
                                {
                                    "Pin": [
                                        "F9"
                                    ],
                                    "PrName": "10GE1/0/54:4"
                                }
                            ]
                        },
                        {
                            "PrSp": 20,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9"
                                    ],
                                    "PrName": "20GE1/0/53:1"
                                },
                                {
                                    "Pin": [
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "20GE1/0/53:3"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9"
                                    ],
                                    "PrName": "20GE1/0/54:1"
                                },
                                {
                                    "Pin": [
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "20GE1/0/54:3"
                                }
                            ]
                        },
                        {
                            "PrSp": 40,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9",
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "40GE1/0/53"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9",
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "40GE1/0/54"
                                }
                            ]
                        },
                        {
                            "PrSp": 100,
                            "PinSp": 25,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9",
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "100GE1/0/53"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9",
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "100GE1/0/54"
                                }
                            ]
                        },
                        {
                            "PrSp": 100,
                            "PinSp": 25,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "E12",
                                        "D12"
                                    ],
                                    "PrName": "100GE1/0/98"
                                }
                            ]
                        }
                    ]
                },
                {
                    "ConnName": "JS3",
                    "ConnLoc": "Midplane",
                    "ConnType": [
                        "Copper"
                    ],
                    "TechType": "Ethernet",
                    "SerdesType": "FF",
                    "JSToPort": [
                        {
                            "PrSp": 10,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6"
                                    ],
                                    "PrName": "10GE1/0/55:1"
                                },
                                {
                                    "Pin": [
                                        "A9"
                                    ],
                                    "PrName": "10GE1/0/55:2"
                                },
                                {
                                    "Pin": [
                                        "B9"
                                    ],
                                    "PrName": "10GE1/0/55:3"
                                },
                                {
                                    "Pin": [
                                        "C9"
                                    ],
                                    "PrName": "10GE1/0/55:4"
                                },
                                {
                                    "Pin": [
                                        "D6"
                                    ],
                                    "PrName": "10GE1/0/56:1"
                                },
                                {
                                    "Pin": [
                                        "D9"
                                    ],
                                    "PrName": "10GE1/0/56:2"
                                },
                                {
                                    "Pin": [
                                        "E9"
                                    ],
                                    "PrName": "10GE1/0/56:3"
                                },
                                {
                                    "Pin": [
                                        "F9"
                                    ],
                                    "PrName": "10GE1/0/56:4"
                                }
                            ]
                        },
                        {
                            "PrSp": 20,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9"
                                    ],
                                    "PrName": "20GE1/0/55:1"
                                },
                                {
                                    "Pin": [
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "20GE1/0/55:3"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9"
                                    ],
                                    "PrName": "20GE1/0/56:1"
                                },
                                {
                                    "Pin": [
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "20GE1/0/56:3"
                                }
                            ]
                        },
                        {
                            "PrSp": 40,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9",
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "40GE1/0/55"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9",
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "40GE1/0/56"
                                }
                            ]
                        },
                        {
                            "PrSp": 100,
                            "PinSp": 25,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9",
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "100GE1/0/55"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9",
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "100GE1/0/56"
                                }
                            ]
                        },
                        {
                            "PrSp": 100,
                            "PinSp": 25,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "E12",
                                        "D12"
                                    ],
                                    "PrName": "100GE1/0/99"
                                }
                            ]
                        }
                    ]
                },
                {
                    "ConnName": "JS4",
                    "ConnLoc": "Midplane",
                    "ConnType": [
                        "Copper"
                    ],
                    "TechType": "Ethernet",
                    "SerdesType": "FF",
                    "JSToPort": [
                        {
                            "PrSp": 10,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6"
                                    ],
                                    "PrName": "10GE1/0/57:1"
                                },
                                {
                                    "Pin": [
                                        "A9"
                                    ],
                                    "PrName": "10GE1/0/57:2"
                                },
                                {
                                    "Pin": [
                                        "B9"
                                    ],
                                    "PrName": "10GE1/0/57:3"
                                },
                                {
                                    "Pin": [
                                        "C9"
                                    ],
                                    "PrName": "10GE1/0/57:4"
                                },
                                {
                                    "Pin": [
                                        "D6"
                                    ],
                                    "PrName": "10GE1/0/58:1"
                                },
                                {
                                    "Pin": [
                                        "D9"
                                    ],
                                    "PrName": "10GE1/0/58:2"
                                },
                                {
                                    "Pin": [
                                        "E9"
                                    ],
                                    "PrName": "10GE1/0/58:3"
                                },
                                {
                                    "Pin": [
                                        "F9"
                                    ],
                                    "PrName": "10GE1/0/58:4"
                                }
                            ]
                        },
                        {
                            "PrSp": 20,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9"
                                    ],
                                    "PrName": "20GE1/0/57:1"
                                },
                                {
                                    "Pin": [
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "20GE1/0/57:3"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9"
                                    ],
                                    "PrName": "20GE1/0/58:1"
                                },
                                {
                                    "Pin": [
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "20GE1/0/58:3"
                                }
                            ]
                        },
                        {
                            "PrSp": 40,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9",
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "40GE1/0/57"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9",
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "40GE1/0/58"
                                }
                            ]
                        },
                        {
                            "PrSp": 100,
                            "PinSp": 25,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9",
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "100GE1/0/57"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9",
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "100GE1/0/58"
                                }
                            ]
                        },
                        {
                            "PrSp": 100,
                            "PinSp": 25,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "E12",
                                        "D12"
                                    ],
                                    "PrName": "100GE1/0/100"
                                }
                            ]
                        }
                    ]
                },
                {
                    "ConnName": "JS5",
                    "ConnLoc": "Midplane",
                    "ConnType": [
                        "Copper"
                    ],
                    "TechType": "Ethernet",
                    "SerdesType": "FF",
                    "JSToPort": [
                        {
                            "PrSp": 10,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6"
                                    ],
                                    "PrName": "10GE1/0/59:1"
                                },
                                {
                                    "Pin": [
                                        "A9"
                                    ],
                                    "PrName": "10GE1/0/59:2"
                                },
                                {
                                    "Pin": [
                                        "B9"
                                    ],
                                    "PrName": "10GE1/0/59:3"
                                },
                                {
                                    "Pin": [
                                        "C9"
                                    ],
                                    "PrName": "10GE1/0/59:4"
                                },
                                {
                                    "Pin": [
                                        "D6"
                                    ],
                                    "PrName": "10GE1/0/60:1"
                                },
                                {
                                    "Pin": [
                                        "D9"
                                    ],
                                    "PrName": "10GE1/0/60:2"
                                },
                                {
                                    "Pin": [
                                        "E9"
                                    ],
                                    "PrName": "10GE1/0/60:3"
                                },
                                {
                                    "Pin": [
                                        "F9"
                                    ],
                                    "PrName": "10GE1/0/60:4"
                                }
                            ]
                        },
                        {
                            "PrSp": 20,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9"
                                    ],
                                    "PrName": "20GE1/0/59:1"
                                },
                                {
                                    "Pin": [
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "20GE1/0/59:3"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9"
                                    ],
                                    "PrName": "20GE1/0/60:1"
                                },
                                {
                                    "Pin": [
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "20GE1/0/60:3"
                                }
                            ]
                        },
                        {
                            "PrSp": 40,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9",
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "40GE1/0/59"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9",
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "40GE1/0/60"
                                }
                            ]
                        },
                        {
                            "PrSp": 100,
                            "PinSp": 25,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9",
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "100GE1/0/59"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9",
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "100GE1/0/60"
                                }
                            ]
                        }
                    ]
                },
                {
                    "ConnName": "JS6",
                    "ConnLoc": "Midplane",
                    "ConnType": [
                        "Copper"
                    ],
                    "TechType": "Ethernet",
                    "SerdesType": "FF",
                    "JSToPort": [
                        {
                            "PrSp": 10,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6"
                                    ],
                                    "PrName": "10GE1/0/95:1"
                                },
                                {
                                    "Pin": [
                                        "A9"
                                    ],
                                    "PrName": "10GE1/0/95:2"
                                },
                                {
                                    "Pin": [
                                        "B9"
                                    ],
                                    "PrName": "10GE1/0/95:3"
                                },
                                {
                                    "Pin": [
                                        "C9"
                                    ],
                                    "PrName": "10GE1/0/95:4"
                                },
                                {
                                    "Pin": [
                                        "D6"
                                    ],
                                    "PrName": "10GE1/0/96:1"
                                },
                                {
                                    "Pin": [
                                        "D9"
                                    ],
                                    "PrName": "10GE1/0/96:2"
                                },
                                {
                                    "Pin": [
                                        "E9"
                                    ],
                                    "PrName": "10GE1/0/96:3"
                                },
                                {
                                    "Pin": [
                                        "F9"
                                    ],
                                    "PrName": "10GE1/0/96:4"
                                }
                            ]
                        },
                        {
                            "PrSp": 20,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9"
                                    ],
                                    "PrName": "20GE1/0/95:1"
                                },
                                {
                                    "Pin": [
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "20GE1/0/95:3"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9"
                                    ],
                                    "PrName": "20GE1/0/96:1"
                                },
                                {
                                    "Pin": [
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "20GE1/0/96:3"
                                }
                            ]
                        },
                        {
                            "PrSp": 40,
                            "PinSp": 10,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9",
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "40GE1/0/95"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9",
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "40GE1/0/96"
                                }
                            ]
                        },
                        {
                            "PrSp": 100,
                            "PinSp": 25,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A6",
                                        "A9",
                                        "B9",
                                        "C9"
                                    ],
                                    "PrName": "100GE1/0/95"
                                },
                                {
                                    "Pin": [
                                        "D6",
                                        "D9",
                                        "E9",
                                        "F9"
                                    ],
                                    "PrName": "100GE1/0/96"
                                }
                            ]
                        },
                        {
                            "PrSp": 1,
                            "PinSp": 1,
                            "LL": 11,
                            "Capabilities": [
                                {
                                    "Pin": [
                                        "A12",
                                        "B12"
                                    ],
                                    "PrName": "M-GE0/0/0"
                                }
                            ]
                        }
                    ]
                }
            ],
            "MgmtConfig": [
                {
                    "ConnectType": "EM",
                    "ProtocolType": "RS232",
                    "LinkRate": "9600",
                    "SerialParams": {
                        "Parity": "Even",
                        "DataBits": 7,
                        "StopBits": 0,
                        "FlowControl": "None"
                    }
                },
                {
                    "ConnectType": "DB9",
                    "ProtocolType": "RS232",
                    "LinkRate": "9600",
                    "SerialParams": {
                        "Parity": "Even",
                        "DataBits": 7,
                        "StopBits": 0,
                        "FlowControl": "None"
                    }
                },
                {
                    "ConnectType": "EM",
                    "ProtocolType": "Ethernet",
                    "LinkRate": ""
                },
                {
                    "ConnectType": "External",
                    "ProtocolType": "Ethernet",
                    "LinkRate": "1Gbps"
                }
            ],
            "TempInfo": {
                "HasTempSensor": true,
                "TempControl": true,
                "HasLimits": true,
                "TempCriticalLimit": 150,
                "TempAlertLimit": 130,
                "TempWarmLimit": 114
            }
        }
    },
    "links": {
        "Raw": {
            "extref": "/rest/v1/InterconnectRawFru/4"
        }
    }
}