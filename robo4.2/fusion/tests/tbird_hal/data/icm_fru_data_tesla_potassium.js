{
    "Name": "Interconnect",
    "Parsed": {
        "GraphicsInfo": {
            "Image": [
                {
                    "File": "HPICMPotassium_Front.1.0.0.svgz",
                    "Source": "FRU",
                    "View": "Front"
                }
            ]
        },
        "IcmInfo": {
            "Capabilities": {
                "EKeyXLinkInfo": [],
                "EkeyGroupMatchReq": [],
                "LLSupport": false,
                "MpInfo": {
                    "ConnInfo": [],
                    "ConnType": "Copper",
                    "MpToEmLL": [],
                    "ResetDisruptsDataFlow": true,
                    "ResetSupported": true,
                    "Speed": "1Gbps",
                    "TechType": "Ethernet"
                },
                "MpSupport": true
            },
            "DnsName": "VC4040F8-0000000010",
            "MediaInfo": [
                {
                    "Comment": "Base-MAC",
                    "MAC": "00:00:00:00:00:01",
                    "MediaId": 1
                },
                {
                    "Comment": "Top-MAC",
                    "MAC": "00:00:00:00:00:02",
                    "MediaId": 2
                },
                {
                    "MediaId": 3,
                    "WWNN": "11:00:00:01:02:03:04:05"
                }
            ],
            "MgmtConfig": [
                {
                    "ConnectType": "EM",
                    "CustomerVisible": true,
                    "LinkRate": "115200",
                    "ProtocolType": "RS232",
                    "SerialParams": {
                        "DataBits": 8,
                        "FlowControl": "None",
                        "Parity": "None",
                        "StopBits": 1
                    }
                },
                {
                    "ConnectType": "RJ45",
                    "CustomerVisible": true,
                    "LinkRate": "115200",
                    "ProtocolType": "RS232",
                    "SerialParams": {
                        "DataBits": 8,
                        "FlowControl": "None",
                        "Parity": "None",
                        "StopBits": 1
                    }
                },
                {
                    "ConnectType": "EM",
                    "CustomerVisible": true,
                    "LinkRate": "1Gbps",
                    "ProtocolType": "Ethernet"
                }
            ],
            "PortMap": [
                {
                    "ConnLoc": "Midplane",
                    "ConnName": "JS1",
                    "ConnType": [
                        "Copper"
                    ],
                    "JSToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6"
                                            ],
                                            "PrName": "TSC27:0"
                                        },
                                        {
                                            "Pin": [
                                                "A9"
                                            ],
                                            "PrName": "TSC27:1"
                                        },
                                        {
                                            "Pin": [
                                                "B9"
                                            ],
                                            "PrName": "TSC27:2"
                                        },
                                        {
                                            "Pin": [
                                                "C9"
                                            ],
                                            "PrName": "TSC27:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6",
                                                "A9"
                                            ],
                                            "PrName": "TSC27:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "B9",
                                                "C9"
                                            ],
                                            "PrName": "TSC27:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6",
                                                "A9",
                                                "B9",
                                                "C9"
                                            ],
                                            "PrName": "TSC27:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "B",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6"
                                            ],
                                            "PrName": "TSC26:0"
                                        },
                                        {
                                            "Pin": [
                                                "D9"
                                            ],
                                            "PrName": "TSC26:1"
                                        },
                                        {
                                            "Pin": [
                                                "E9"
                                            ],
                                            "PrName": "TSC26:2"
                                        },
                                        {
                                            "Pin": [
                                                "F9"
                                            ],
                                            "PrName": "TSC26:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6",
                                                "D9"
                                            ],
                                            "PrName": "TSC26:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "E9",
                                                "F9"
                                            ],
                                            "PrName": "TSC26:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6",
                                                "D9",
                                                "E9",
                                                "F9"
                                            ],
                                            "PrName": "TSC26:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Midplane",
                    "ConnName": "JS2",
                    "ConnType": [
                        "Copper"
                    ],
                    "JSToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6"
                                            ],
                                            "PrName": "TSC29:0"
                                        },
                                        {
                                            "Pin": [
                                                "A9"
                                            ],
                                            "PrName": "TSC29:1"
                                        },
                                        {
                                            "Pin": [
                                                "B9"
                                            ],
                                            "PrName": "TSC29:2"
                                        },
                                        {
                                            "Pin": [
                                                "C9"
                                            ],
                                            "PrName": "TSC29:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6",
                                                "A9"
                                            ],
                                            "PrName": "TSC29:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "B9",
                                                "C9"
                                            ],
                                            "PrName": "TSC29:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6",
                                                "A9",
                                                "B9",
                                                "C9"
                                            ],
                                            "PrName": "TSC29:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "B",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6"
                                            ],
                                            "PrName": "TSC28:0"
                                        },
                                        {
                                            "Pin": [
                                                "D9"
                                            ],
                                            "PrName": "TSC28:1"
                                        },
                                        {
                                            "Pin": [
                                                "E9"
                                            ],
                                            "PrName": "TSC28:2"
                                        },
                                        {
                                            "Pin": [
                                                "F9"
                                            ],
                                            "PrName": "TSC28:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6",
                                                "D9"
                                            ],
                                            "PrName": "TSC28:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "E9",
                                                "F9"
                                            ],
                                            "PrName": "TSC28:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6",
                                                "D9",
                                                "E9",
                                                "F9"
                                            ],
                                            "PrName": "TSC28:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Midplane",
                    "ConnName": "JS3",
                    "ConnType": [
                        "Copper"
                    ],
                    "JSToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6"
                                            ],
                                            "PrName": "TSC31:0"
                                        },
                                        {
                                            "Pin": [
                                                "A9"
                                            ],
                                            "PrName": "TSC31:1"
                                        },
                                        {
                                            "Pin": [
                                                "B9"
                                            ],
                                            "PrName": "TSC31:2"
                                        },
                                        {
                                            "Pin": [
                                                "C9"
                                            ],
                                            "PrName": "TSC31:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6",
                                                "A9"
                                            ],
                                            "PrName": "TSC31:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "B9",
                                                "C9"
                                            ],
                                            "PrName": "TSC31:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6",
                                                "A9",
                                                "B9",
                                                "C9"
                                            ],
                                            "PrName": "TSC31:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "B",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6"
                                            ],
                                            "PrName": "TSC30:0"
                                        },
                                        {
                                            "Pin": [
                                                "D9"
                                            ],
                                            "PrName": "TSC30:1"
                                        },
                                        {
                                            "Pin": [
                                                "E9"
                                            ],
                                            "PrName": "TSC30:2"
                                        },
                                        {
                                            "Pin": [
                                                "F9"
                                            ],
                                            "PrName": "TSC30:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6",
                                                "D9"
                                            ],
                                            "PrName": "TSC30:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "E9",
                                                "F9"
                                            ],
                                            "PrName": "TSC30:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6",
                                                "D9",
                                                "E9",
                                                "F9"
                                            ],
                                            "PrName": "TSC30:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Midplane",
                    "ConnName": "JS4",
                    "ConnType": [
                        "Copper"
                    ],
                    "JSToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6"
                                            ],
                                            "PrName": "TSC01:0"
                                        },
                                        {
                                            "Pin": [
                                                "A9"
                                            ],
                                            "PrName": "TSC01:1"
                                        },
                                        {
                                            "Pin": [
                                                "B9"
                                            ],
                                            "PrName": "TSC01:2"
                                        },
                                        {
                                            "Pin": [
                                                "C9"
                                            ],
                                            "PrName": "TSC01:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6",
                                                "A9"
                                            ],
                                            "PrName": "TSC01:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "B9",
                                                "C9"
                                            ],
                                            "PrName": "TSC01:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6",
                                                "A9",
                                                "B9",
                                                "C9"
                                            ],
                                            "PrName": "TSC01:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "B",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6"
                                            ],
                                            "PrName": "TSC00:0"
                                        },
                                        {
                                            "Pin": [
                                                "D9"
                                            ],
                                            "PrName": "TSC00:1"
                                        },
                                        {
                                            "Pin": [
                                                "E9"
                                            ],
                                            "PrName": "TSC00:2"
                                        },
                                        {
                                            "Pin": [
                                                "F9"
                                            ],
                                            "PrName": "TSC00:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6",
                                                "D9"
                                            ],
                                            "PrName": "TSC00:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "E9",
                                                "F9"
                                            ],
                                            "PrName": "TSC00:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6",
                                                "D9",
                                                "E9",
                                                "F9"
                                            ],
                                            "PrName": "TSC00:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Midplane",
                    "ConnName": "JS5",
                    "ConnType": [
                        "Copper"
                    ],
                    "JSToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6"
                                            ],
                                            "PrName": "TSC03:0"
                                        },
                                        {
                                            "Pin": [
                                                "A9"
                                            ],
                                            "PrName": "TSC03:1"
                                        },
                                        {
                                            "Pin": [
                                                "B9"
                                            ],
                                            "PrName": "TSC03:2"
                                        },
                                        {
                                            "Pin": [
                                                "C9"
                                            ],
                                            "PrName": "TSC03:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6",
                                                "A9"
                                            ],
                                            "PrName": "TSC03:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "B9",
                                                "C9"
                                            ],
                                            "PrName": "TSC03:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6",
                                                "A9",
                                                "B9",
                                                "C9"
                                            ],
                                            "PrName": "TSC03:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "B",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6"
                                            ],
                                            "PrName": "TSC02:0"
                                        },
                                        {
                                            "Pin": [
                                                "D9"
                                            ],
                                            "PrName": "TSC02:1"
                                        },
                                        {
                                            "Pin": [
                                                "E9"
                                            ],
                                            "PrName": "TSC02:2"
                                        },
                                        {
                                            "Pin": [
                                                "F9"
                                            ],
                                            "PrName": "TSC02:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6",
                                                "D9"
                                            ],
                                            "PrName": "TSC02:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "E9",
                                                "F9"
                                            ],
                                            "PrName": "TSC02:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6",
                                                "D9",
                                                "E9",
                                                "F9"
                                            ],
                                            "PrName": "TSC02:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Midplane",
                    "ConnName": "JS6",
                    "ConnType": [
                        "Copper"
                    ],
                    "JSToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6"
                                            ],
                                            "PrName": "TSC05:0"
                                        },
                                        {
                                            "Pin": [
                                                "A9"
                                            ],
                                            "PrName": "TSC05:1"
                                        },
                                        {
                                            "Pin": [
                                                "B9"
                                            ],
                                            "PrName": "TSC05:2"
                                        },
                                        {
                                            "Pin": [
                                                "C9"
                                            ],
                                            "PrName": "TSC05:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6",
                                                "A9"
                                            ],
                                            "PrName": "TSC05:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "B9",
                                                "C9"
                                            ],
                                            "PrName": "TSC05:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A6",
                                                "A9",
                                                "B9",
                                                "C9"
                                            ],
                                            "PrName": "TSC05:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "B",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6"
                                            ],
                                            "PrName": "TSC04:0"
                                        },
                                        {
                                            "Pin": [
                                                "D9"
                                            ],
                                            "PrName": "TSC04:1"
                                        },
                                        {
                                            "Pin": [
                                                "E9"
                                            ],
                                            "PrName": "TSC04:2"
                                        },
                                        {
                                            "Pin": [
                                                "F9"
                                            ],
                                            "PrName": "TSC04:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6",
                                                "D9"
                                            ],
                                            "PrName": "TSC04:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "E9",
                                                "F9"
                                            ],
                                            "PrName": "TSC04:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "D6",
                                                "D9",
                                                "E9",
                                                "F9"
                                            ],
                                            "PrName": "TSC04:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "Mgmt",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "A12",
                                                "B12"
                                            ],
                                            "PrName": "M-GE0/0/0"
                                        }
                                    ],
                                    "PinSp": 1,
                                    "PrSp": 1
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Faceplate",
                    "ConnName": "CXP1",
                    "ConnType": [
                        "Copper"
                    ],
                    "FaceplateToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0"
                                            ],
                                            "PrName": "TSC08:0"
                                        },
                                        {
                                            "Pin": [
                                                "1"
                                            ],
                                            "PrName": "TSC08:1"
                                        },
                                        {
                                            "Pin": [
                                                "2"
                                            ],
                                            "PrName": "TSC08:2"
                                        },
                                        {
                                            "Pin": [
                                                "3"
                                            ],
                                            "PrName": "TSC08:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..1"
                                            ],
                                            "PrName": "TSC08:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "2..3"
                                            ],
                                            "PrName": "TSC08:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..3"
                                            ],
                                            "PrName": "TSC08:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "B",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "4"
                                            ],
                                            "PrName": "TSC07:0"
                                        },
                                        {
                                            "Pin": [
                                                "5"
                                            ],
                                            "PrName": "TSC07:1"
                                        },
                                        {
                                            "Pin": [
                                                "6"
                                            ],
                                            "PrName": "TSC07:2"
                                        },
                                        {
                                            "Pin": [
                                                "7"
                                            ],
                                            "PrName": "TSC07:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "4..5"
                                            ],
                                            "PrName": "TSC07:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "6..7"
                                            ],
                                            "PrName": "TSC07:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "4..7"
                                            ],
                                            "PrName": "TSC07:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "C",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "8"
                                            ],
                                            "PrName": "TSC06:0"
                                        },
                                        {
                                            "Pin": [
                                                "9"
                                            ],
                                            "PrName": "TSC06:1"
                                        },
                                        {
                                            "Pin": [
                                                "10"
                                            ],
                                            "PrName": "TSC06:2"
                                        },
                                        {
                                            "Pin": [
                                                "11"
                                            ],
                                            "PrName": "TSC06:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "8..9"
                                            ],
                                            "PrName": "TSC06:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "10..11"
                                            ],
                                            "PrName": "TSC06:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "8..11"
                                            ],
                                            "PrName": "TSC06:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Faceplate",
                    "ConnName": "CXP2",
                    "ConnType": [
                        "Copper"
                    ],
                    "FaceplateToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0"
                                            ],
                                            "PrName": "TSC11:0"
                                        },
                                        {
                                            "Pin": [
                                                "1"
                                            ],
                                            "PrName": "TSC11:1"
                                        },
                                        {
                                            "Pin": [
                                                "2"
                                            ],
                                            "PrName": "TSC11:2"
                                        },
                                        {
                                            "Pin": [
                                                "3"
                                            ],
                                            "PrName": "TSC11:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..1"
                                            ],
                                            "PrName": "TSC11:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "2..3"
                                            ],
                                            "PrName": "TSC11:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..3"
                                            ],
                                            "PrName": "TSC11:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "B",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "4"
                                            ],
                                            "PrName": "TSC10:0"
                                        },
                                        {
                                            "Pin": [
                                                "5"
                                            ],
                                            "PrName": "TSC10:1"
                                        },
                                        {
                                            "Pin": [
                                                "6"
                                            ],
                                            "PrName": "TSC10:2"
                                        },
                                        {
                                            "Pin": [
                                                "7"
                                            ],
                                            "PrName": "TSC10:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "4..5"
                                            ],
                                            "PrName": "TSC10:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "6..7"
                                            ],
                                            "PrName": "TSC10:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "4..7"
                                            ],
                                            "PrName": "TSC10:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "C",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "8"
                                            ],
                                            "PrName": "TSC09:0"
                                        },
                                        {
                                            "Pin": [
                                                "9"
                                            ],
                                            "PrName": "TSC09:1"
                                        },
                                        {
                                            "Pin": [
                                                "10"
                                            ],
                                            "PrName": "TSC09:2"
                                        },
                                        {
                                            "Pin": [
                                                "11"
                                            ],
                                            "PrName": "TSC09:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "8..9"
                                            ],
                                            "PrName": "TSC09:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "10..11"
                                            ],
                                            "PrName": "TSC09:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "8..11"
                                            ],
                                            "PrName": "TSC09:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Faceplate",
                    "ConnName": "CXP3",
                    "ConnType": [
                        "Copper"
                    ],
                    "FaceplateToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0"
                                            ],
                                            "PrName": "TSC22:0"
                                        },
                                        {
                                            "Pin": [
                                                "1"
                                            ],
                                            "PrName": "TSC22:1"
                                        },
                                        {
                                            "Pin": [
                                                "2"
                                            ],
                                            "PrName": "TSC22:2"
                                        },
                                        {
                                            "Pin": [
                                                "3"
                                            ],
                                            "PrName": "TSC22:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..1"
                                            ],
                                            "PrName": "TSC22:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "2..3"
                                            ],
                                            "PrName": "TSC22:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..3"
                                            ],
                                            "PrName": "TSC22:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "B",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "4"
                                            ],
                                            "PrName": "TSC21:0"
                                        },
                                        {
                                            "Pin": [
                                                "5"
                                            ],
                                            "PrName": "TSC21:1"
                                        },
                                        {
                                            "Pin": [
                                                "6"
                                            ],
                                            "PrName": "TSC21:2"
                                        },
                                        {
                                            "Pin": [
                                                "7"
                                            ],
                                            "PrName": "TSC21:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "4..5"
                                            ],
                                            "PrName": "TSC21:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "6..7"
                                            ],
                                            "PrName": "TSC21:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "4..7"
                                            ],
                                            "PrName": "TSC21:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "C",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "8"
                                            ],
                                            "PrName": "TSC20:0"
                                        },
                                        {
                                            "Pin": [
                                                "9"
                                            ],
                                            "PrName": "TSC20:1"
                                        },
                                        {
                                            "Pin": [
                                                "10"
                                            ],
                                            "PrName": "TSC20:2"
                                        },
                                        {
                                            "Pin": [
                                                "11"
                                            ],
                                            "PrName": "TSC20:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "8..9"
                                            ],
                                            "PrName": "TSC20:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "10..11"
                                            ],
                                            "PrName": "TSC20:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "8..11"
                                            ],
                                            "PrName": "TSC20:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Faceplate",
                    "ConnName": "CXP4",
                    "ConnType": [
                        "Copper"
                    ],
                    "FaceplateToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0"
                                            ],
                                            "PrName": "TSC25:0"
                                        },
                                        {
                                            "Pin": [
                                                "1"
                                            ],
                                            "PrName": "TSC25:1"
                                        },
                                        {
                                            "Pin": [
                                                "2"
                                            ],
                                            "PrName": "TSC25:2"
                                        },
                                        {
                                            "Pin": [
                                                "3"
                                            ],
                                            "PrName": "TSC25:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..1"
                                            ],
                                            "PrName": "TSC25:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "2..3"
                                            ],
                                            "PrName": "TSC25:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..3"
                                            ],
                                            "PrName": "TSC25:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "B",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "4"
                                            ],
                                            "PrName": "TSC24:0"
                                        },
                                        {
                                            "Pin": [
                                                "5"
                                            ],
                                            "PrName": "TSC24:1"
                                        },
                                        {
                                            "Pin": [
                                                "6"
                                            ],
                                            "PrName": "TSC24:2"
                                        },
                                        {
                                            "Pin": [
                                                "7"
                                            ],
                                            "PrName": "TSC24:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "4..5"
                                            ],
                                            "PrName": "TSC24:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "6..7"
                                            ],
                                            "PrName": "TSC24:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "4..7"
                                            ],
                                            "PrName": "TSC24:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        },
                        {
                            "Group": "C",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "8"
                                            ],
                                            "PrName": "TSC23:0"
                                        },
                                        {
                                            "Pin": [
                                                "9"
                                            ],
                                            "PrName": "TSC23:1"
                                        },
                                        {
                                            "Pin": [
                                                "10"
                                            ],
                                            "PrName": "TSC23:2"
                                        },
                                        {
                                            "Pin": [
                                                "11"
                                            ],
                                            "PrName": "TSC23:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "8..9"
                                            ],
                                            "PrName": "TSC23:0:1"
                                        },
                                        {
                                            "Pin": [
                                                "10..11"
                                            ],
                                            "PrName": "TSC23:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 20
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "8..11"
                                            ],
                                            "PrName": "TSC23:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Faceplate",
                    "ConnName": "QSFP+1",
                    "ConnType": [
                        "Copper"
                    ],
                    "FaceplateToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0"
                                            ],
                                            "PrName": "TSC12:0"
                                        },
                                        {
                                            "Pin": [
                                                "1"
                                            ],
                                            "PrName": "TSC12:1"
                                        },
                                        {
                                            "Pin": [
                                                "2"
                                            ],
                                            "PrName": "TSC12:2"
                                        },
                                        {
                                            "Pin": [
                                                "3"
                                            ],
                                            "PrName": "TSC12:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..3"
                                            ],
                                            "PrName": "TSC12:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Faceplate",
                    "ConnName": "QSFP+2",
                    "ConnType": [
                        "Copper"
                    ],
                    "FaceplateToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0"
                                            ],
                                            "PrName": "TSC13:0"
                                        },
                                        {
                                            "Pin": [
                                                "1"
                                            ],
                                            "PrName": "TSC13:1"
                                        },
                                        {
                                            "Pin": [
                                                "2"
                                            ],
                                            "PrName": "TSC13:2"
                                        },
                                        {
                                            "Pin": [
                                                "3"
                                            ],
                                            "PrName": "TSC13:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..3"
                                            ],
                                            "PrName": "TSC13:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Faceplate",
                    "ConnName": "QSFP+3",
                    "ConnType": [
                        "Copper"
                    ],
                    "FaceplateToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0"
                                            ],
                                            "PrName": "TSC14:0"
                                        },
                                        {
                                            "Pin": [
                                                "1"
                                            ],
                                            "PrName": "TSC14:1"
                                        },
                                        {
                                            "Pin": [
                                                "2"
                                            ],
                                            "PrName": "TSC14:2"
                                        },
                                        {
                                            "Pin": [
                                                "3"
                                            ],
                                            "PrName": "TSC14:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..3"
                                            ],
                                            "PrName": "TSC14:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Faceplate",
                    "ConnName": "QSFP+4",
                    "ConnType": [
                        "Copper"
                    ],
                    "FaceplateToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0"
                                            ],
                                            "PrName": "TSC15:0"
                                        },
                                        {
                                            "Pin": [
                                                "1"
                                            ],
                                            "PrName": "TSC15:1"
                                        },
                                        {
                                            "Pin": [
                                                "2"
                                            ],
                                            "PrName": "TSC15:2"
                                        },
                                        {
                                            "Pin": [
                                                "3"
                                            ],
                                            "PrName": "TSC15:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..3"
                                            ],
                                            "PrName": "TSC15:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Faceplate",
                    "ConnName": "QSFP+5",
                    "ConnType": [
                        "Copper"
                    ],
                    "FaceplateToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0"
                                            ],
                                            "PrName": "TSC16:0"
                                        },
                                        {
                                            "Pin": [
                                                "1"
                                            ],
                                            "PrName": "TSC16:1"
                                        },
                                        {
                                            "Pin": [
                                                "2"
                                            ],
                                            "PrName": "TSC16:2"
                                        },
                                        {
                                            "Pin": [
                                                "3"
                                            ],
                                            "PrName": "TSC16:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..3"
                                            ],
                                            "PrName": "TSC16:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Faceplate",
                    "ConnName": "QSFP+6",
                    "ConnType": [
                        "Copper"
                    ],
                    "FaceplateToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0"
                                            ],
                                            "PrName": "TSC17:0"
                                        },
                                        {
                                            "Pin": [
                                                "1"
                                            ],
                                            "PrName": "TSC17:1"
                                        },
                                        {
                                            "Pin": [
                                                "2"
                                            ],
                                            "PrName": "TSC17:2"
                                        },
                                        {
                                            "Pin": [
                                                "3"
                                            ],
                                            "PrName": "TSC17:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..3"
                                            ],
                                            "PrName": "TSC17:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Faceplate",
                    "ConnName": "QSFP+7",
                    "ConnType": [
                        "Copper"
                    ],
                    "FaceplateToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0"
                                            ],
                                            "PrName": "TSC18:0"
                                        },
                                        {
                                            "Pin": [
                                                "1"
                                            ],
                                            "PrName": "TSC18:1"
                                        },
                                        {
                                            "Pin": [
                                                "2"
                                            ],
                                            "PrName": "TSC18:2"
                                        },
                                        {
                                            "Pin": [
                                                "3"
                                            ],
                                            "PrName": "TSC18:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..3"
                                            ],
                                            "PrName": "TSC18:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                },
                {
                    "ConnLoc": "Faceplate",
                    "ConnName": "QSFP+8",
                    "ConnType": [
                        "Copper"
                    ],
                    "FaceplateToPort": [
                        {
                            "Group": "A",
                            "PortInfo": [
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0"
                                            ],
                                            "PrName": "TSC19:0"
                                        },
                                        {
                                            "Pin": [
                                                "1"
                                            ],
                                            "PrName": "TSC19:1"
                                        },
                                        {
                                            "Pin": [
                                                "2"
                                            ],
                                            "PrName": "TSC19:2"
                                        },
                                        {
                                            "Pin": [
                                                "3"
                                            ],
                                            "PrName": "TSC19:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 10
                                },
                                {
                                    "Capabilities": [
                                        {
                                            "Pin": [
                                                "0..3"
                                            ],
                                            "PrName": "TSC19:0:1:2:3"
                                        }
                                    ],
                                    "PinSp": 10,
                                    "PrSp": 40
                                }
                            ]
                        }
                    ],
                    "SerdesType": "FF",
                    "TechType": "Ethernet"
                }
            ]
        },
        "PowerInfo": {
            "FullOn": 240,
            "Vaux": 3
        },
        "Preamble": {
            "CommType": [
                "CANMIC"
            ],
            "EEPROMSize": 1048576,
            "EfuseResetDuration": 0,
            "FactoryTimeStamp": "123456",
            "FruSubType": [
                "Ethernet",
                "Switch",
                "ThermalInfo"
            ],
            "FruType": "ICM",
            "GreenFactor": [
                "Low Halogen"
            ],
            "HwCompliance": [],
            "Language": "en-US",
            "LastModified": "2015-01-17",
            "Model": "HP Potassium Ethernet ICM"
        },
        "ProductInfo": {
            "AssemblyPartNumber": "779226-001",
            "BoardRevCode": "VP1",
            "ManufacturedFor": "HP",
            "Manufacturer": "HP",
            "PCASerialNumber": "00000000000014",
            "PCASparePartNumber": "785339-001",
            "PartNumber": "779224-B21",
            "SerialNumber": "0000000010"
        },
        "Type": "HpIcmFru.1.0.0"
    },
    "Type": "HpEmFru.1.0.0",
    "links": {
        "Raw": {
            "extref": "/rest/v1/InterconnectRawFru/1"
        }
    }
}
