#!/usr/bin/env python


ethnets = [
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_50-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 50
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_383-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 383
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_230-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 230
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_491-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 491
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_192-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 192
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_414-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 414
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_347-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 347
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_283-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 283
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_493-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 493
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_12-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 12
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_2-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 2
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_186-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 186
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_490-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 490
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_92-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 92
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_286-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 286
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_374-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 374
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_196-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 196
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_110-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 110
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_306-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 306
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_36-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 36
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_174-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 174
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_69-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 69
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_191-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 191
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_386-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 386
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_30-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 30
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_267-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 267
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_41-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 41
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_292-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 292
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_308-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 308
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_451-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 451
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_219-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 219
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_391-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 391
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_259-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 259
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_232-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 232
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_167-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 167
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_322-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 322
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_292-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 292
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_417-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 417
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_67-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 67
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_77-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 77
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_289-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 289
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_104-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 104
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_337-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 337
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_446-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 446
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_195-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 195
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_262-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 262
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_209-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 209
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_250-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 250
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_14-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 14
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_482-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 482
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_84-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 84
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_196-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 196
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_52-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 52
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_206-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 206
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_455-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 455
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_131-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 131
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_46-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 46
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_308-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 308
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_194-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 194
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_401-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 401
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_87-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 87
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_483-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 483
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_481-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 481
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_184-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 184
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_188-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 188
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_467-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 467
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_463-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 463
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_380-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 380
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_492-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 492
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_408-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 408
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_261-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 261
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_457-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 457
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_160-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 160
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_321-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 321
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_366-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 366
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_335-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 335
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_134-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 134
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_486-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 486
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_211-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 211
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_178-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 178
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_479-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 479
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Untagged",
        "name": "1Network",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 0
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_396-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 396
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_165-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 165
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_158-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 158
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_113-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 113
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_318-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 318
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_40-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 40
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_375-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 375
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_14-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 14
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_109-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 109
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_207-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 207
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_381-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 381
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_445-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 445
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_182-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 182
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_159-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 159
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_418-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 418
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_86-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 86
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_458-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 458
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_49-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 49
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_331-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 331
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_312-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 312
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_234-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 234
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_311-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 311
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_401-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 401
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_8-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 8
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_44-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 44
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_497-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 497
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_429-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 429
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_447-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 447
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_417-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 417
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_55-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 55
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_109-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 109
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_358-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 358
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_320-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 320
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_30-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 30
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_189-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 189
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_264-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 264
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_118-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 118
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_125-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 125
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_7-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 7
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_62-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 62
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_328-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 328
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_393-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 393
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_272-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 272
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_242-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 242
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_434-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 434
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_444-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 444
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_56-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 56
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_101-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 101
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_369-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 369
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_476-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 476
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_495-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 495
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_64-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 64
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_310-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 310
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_187-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 187
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_366-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 366
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_213-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 213
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_427-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 427
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_178-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 178
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_379-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 379
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_140-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 140
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_262-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 262
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_285-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 285
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_136-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 136
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_96-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 96
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_374-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 374
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_269-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 269
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_425-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 425
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_210-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 210
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_330-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 330
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_489-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 489
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_142-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 142
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_399-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 399
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_159-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 159
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_247-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 247
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_277-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 277
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_495-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 495
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_13-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 13
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_95-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 95
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_8-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 8
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_93-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 93
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_47-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 47
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_471-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 471
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_61-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 61
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_224-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 224
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_139-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 139
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_250-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 250
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_279-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 279
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_266-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 266
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_42-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 42
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_223-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 223
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_456-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 456
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_419-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 419
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_465-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 465
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_330-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 330
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_242-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 242
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_256-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 256
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_296-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 296
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_477-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 477
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_98-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 98
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_123-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 123
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_499-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 499
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_441-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 441
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_129-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 129
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_421-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 421
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_327-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 327
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_309-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 309
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_336-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 336
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_357-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 357
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_249-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 249
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_478-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 478
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_310-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 310
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_410-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 410
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_313-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 313
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_130-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 130
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_70-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 70
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_391-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 391
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_457-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 457
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_263-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 263
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_85-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 85
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_426-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 426
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_183-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 183
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_276-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 276
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_254-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 254
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_283-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 283
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_148-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 148
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_438-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 438
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_482-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 482
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_154-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 154
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_167-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 167
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_112-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 112
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_293-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 293
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_212-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 212
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_260-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 260
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_57-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 57
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_129-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 129
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_54-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 54
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_270-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 270
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_236-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 236
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_301-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 301
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_317-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 317
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_160-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 160
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_349-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 349
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_395-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 395
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_191-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 191
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_315-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 315
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_17-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 17
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_392-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 392
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_135-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 135
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_42-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 42
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_370-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 370
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_11-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 11
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_111-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 111
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_26-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 26
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_232-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 232
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_248-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 248
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_45-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 45
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_227-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 227
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_233-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 233
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_282-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 282
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_105-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 105
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_179-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 179
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_350-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 350
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_103-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 103
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_130-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 130
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_415-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 415
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_74-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 74
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_274-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 274
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_52-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 52
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_185-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 185
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_147-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 147
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_439-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 439
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_260-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 260
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_91-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 91
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_290-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 290
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_31-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 31
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_294-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 294
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_428-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 428
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_236-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 236
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_27-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 27
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_185-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 185
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_487-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 487
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_414-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 414
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_208-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 208
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_177-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 177
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_29-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 29
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_252-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 252
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_10-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 10
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_119-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 119
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_297-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 297
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_382-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 382
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_7-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 7
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_258-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 258
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_75-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 75
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_204-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 204
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_301-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 301
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_83-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 83
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_24-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 24
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_193-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 193
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_347-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 347
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_316-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 316
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_445-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 445
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_350-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 350
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_329-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 329
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_82-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 82
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_142-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 142
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_314-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 314
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_89-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 89
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_377-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 377
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_258-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 258
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_137-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 137
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_344-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 344
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_307-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 307
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_493-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 493
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_372-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 372
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_438-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 438
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_108-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 108
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_82-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 82
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_161-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 161
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_370-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 370
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_299-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 299
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_211-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 211
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_3-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 3
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_297-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 297
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_67-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 67
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_239-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 239
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_319-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 319
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_127-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 127
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_29-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 29
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_18-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 18
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_90-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 90
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_161-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 161
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_141-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 141
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_422-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 422
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_102-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 102
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_338-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 338
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_251-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 251
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_28-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 28
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_79-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 79
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_386-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 386
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_488-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 488
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_265-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 265
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_61-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 61
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_150-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 150
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_107-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 107
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_62-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 62
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_363-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 363
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_376-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 376
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_58-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 58
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_49-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 49
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_25-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 25
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_276-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 276
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_424-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 424
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_189-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 189
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_332-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 332
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_264-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 264
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_198-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 198
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_39-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 39
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_452-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 452
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_31-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 31
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_25-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 25
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_265-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 265
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_229-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 229
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_483-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 483
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_344-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 344
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_201-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 201
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_399-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 399
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_442-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 442
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_365-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 365
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_233-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 233
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_427-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 427
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_97-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 97
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_192-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 192
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_54-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 54
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_420-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 420
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_437-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 437
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_155-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 155
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_487-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 487
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_143-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 143
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_286-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 286
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_111-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 111
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_407-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 407
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_389-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 389
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_221-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 221
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_452-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 452
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_466-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 466
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_99-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 99
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_58-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 58
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_405-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 405
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_106-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 106
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_133-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 133
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_362-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 362
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_152-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 152
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_302-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 302
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_175-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 175
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_71-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 71
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_376-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 376
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_469-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 469
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_430-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 430
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_334-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 334
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_336-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 336
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_368-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 368
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_484-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 484
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_155-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 155
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_158-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 158
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_50-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 50
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_137-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 137
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_405-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 405
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_332-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 332
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_73-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 73
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_238-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 238
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_68-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 68
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_268-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 268
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_117-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 117
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_56-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 56
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_6-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 6
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_491-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 491
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_157-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 157
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_305-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 305
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_157-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 157
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_355-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 355
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_126-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 126
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_355-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 355
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_335-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 335
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_298-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 298
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_224-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 224
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_114-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 114
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_21-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 21
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_78-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 78
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_153-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 153
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_378-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 378
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_372-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 372
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_87-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 87
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_432-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 432
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_104-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 104
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_259-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 259
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_299-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 299
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_378-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 378
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_339-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 339
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_199-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 199
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_172-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 172
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_168-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 168
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_103-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 103
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_324-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 324
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_51-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 51
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_65-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 65
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_173-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 173
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_156-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 156
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_32-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 32
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_115-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 115
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_210-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 210
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_302-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 302
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_68-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 68
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_113-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 113
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_177-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 177
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_96-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 96
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_410-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 410
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_362-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 362
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_348-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 348
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_293-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 293
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_240-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 240
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_101-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 101
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_446-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 446
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_175-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 175
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_388-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 388
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_18-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 18
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_16-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 16
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_183-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 183
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_494-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 494
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_145-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 145
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_271-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 271
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_304-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 304
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_398-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 398
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_440-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 440
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_88-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 88
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_231-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 231
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_360-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 360
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_411-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 411
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_240-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 240
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_173-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 173
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_181-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 181
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_363-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 363
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_346-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 346
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_19-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 19
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_105-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 105
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_444-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 444
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_430-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 430
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_377-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 377
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_80-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 80
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_450-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 450
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_423-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 423
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_373-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 373
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_168-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 168
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_143-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 143
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_422-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 422
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_456-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 456
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_70-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 70
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_463-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 463
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_108-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 108
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_180-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 180
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_359-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 359
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_384-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 384
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_63-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 63
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_360-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 360
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_255-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 255
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_373-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 373
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_449-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 449
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_40-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 40
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_361-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 361
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_176-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 176
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_214-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 214
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_309-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 309
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_453-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 453
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_500-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 500
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_190-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 190
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_333-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 333
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_100-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 100
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_220-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 220
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_128-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 128
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_317-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 317
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_190-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 190
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_431-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 431
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_384-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 384
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_448-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 448
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_416-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 416
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_294-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 294
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_246-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 246
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_473-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 473
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_385-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 385
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_79-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 79
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_437-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 437
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_403-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 403
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_57-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 57
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_412-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 412
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_352-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 352
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_215-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 215
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_55-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 55
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_471-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 471
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_291-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 291
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_426-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 426
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_174-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 174
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_11-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 11
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_275-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 275
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_33-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 33
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_331-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 331
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_20-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 20
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_402-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 402
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_284-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 284
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_2-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 2
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_431-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 431
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_231-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 231
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_396-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 396
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_170-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 170
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_200-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 200
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_323-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 323
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_274-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 274
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_73-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 73
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_179-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 179
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_28-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 28
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_397-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 397
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_93-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 93
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_343-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 343
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_279-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 279
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_66-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 66
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_199-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 199
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_217-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 217
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_367-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 367
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_126-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 126
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_169-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 169
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_436-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 436
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_470-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 470
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_9-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 9
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_35-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 35
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_186-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 186
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_122-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 122
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_149-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 149
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_162-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 162
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_15-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 15
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_97-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 97
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_287-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 287
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_497-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 497
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_395-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 395
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_115-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 115
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_26-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 26
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_188-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 188
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_16-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 16
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_209-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 209
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_352-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 352
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_228-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 228
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_98-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 98
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_163-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 163
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_221-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 221
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_251-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 251
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_235-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 235
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_171-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 171
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_475-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 475
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_298-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 298
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_22-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 22
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_22-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 22
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_267-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 267
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_151-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 151
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_200-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 200
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_141-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 141
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_59-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 59
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_345-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 345
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_319-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 319
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_201-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 201
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_406-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 406
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_325-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 325
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_466-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 466
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_458-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 458
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_307-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 307
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_206-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 206
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_60-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 60
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_257-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 257
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_489-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 489
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_353-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 353
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_472-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 472
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_263-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 263
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_124-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 124
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_461-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 461
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_187-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 187
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_51-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 51
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_467-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 467
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_223-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 223
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_181-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 181
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_222-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 222
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_138-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 138
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_59-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 59
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_149-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 149
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_24-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 24
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_429-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 429
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_148-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 148
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_440-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 440
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_316-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 316
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_225-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 225
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_15-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 15
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_305-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 305
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_300-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 300
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_36-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 36
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_203-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 203
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_76-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 76
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_390-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 390
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_138-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 138
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_280-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 280
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_6-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 6
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_116-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 116
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_184-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 184
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_37-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 37
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_269-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 269
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_334-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 334
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_496-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 496
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_443-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 443
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_474-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 474
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_34-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 34
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_10-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 10
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_69-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 69
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_90-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 90
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_480-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 480
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_381-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 381
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_337-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 337
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_357-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 357
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_13-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 13
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_476-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 476
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_333-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 333
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_418-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 418
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_169-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 169
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_346-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 346
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_80-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 80
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_490-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 490
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_343-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 343
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_365-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 365
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_204-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 204
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_222-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 222
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_244-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 244
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_424-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 424
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_278-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 278
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_124-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 124
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_132-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 132
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_38-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 38
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_202-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 202
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_484-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 484
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_128-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 128
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_291-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 291
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_83-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 83
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_409-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 409
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_277-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 277
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_44-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 44
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_85-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 85
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_140-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 140
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_464-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 464
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_423-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 423
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_473-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 473
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_182-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 182
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_341-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 341
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_324-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 324
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_455-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 455
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_94-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 94
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_454-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 454
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_485-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 485
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_20-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 20
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_48-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 48
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_193-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 193
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_139-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 139
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_361-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 361
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_84-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 84
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_486-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 486
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_367-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 367
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_100-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 100
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_207-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 207
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_398-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 398
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_387-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 387
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_32-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 32
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_102-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 102
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_121-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 121
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_479-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 479
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_400-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 400
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_76-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 76
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_413-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 413
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_326-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 326
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_257-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 257
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_72-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 72
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_127-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 127
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_326-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 326
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_241-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 241
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Untagged",
        "name": "2Network",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": False,
        "vlanId": 0
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_114-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 114
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_312-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 312
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_404-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 404
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_205-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 205
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_74-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 74
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_244-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 244
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_494-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 494
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_205-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 205
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_107-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 107
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_120-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 120
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_132-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 132
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_439-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 439
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_459-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 459
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_202-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 202
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_278-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 278
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_313-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 313
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_327-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 327
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_287-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 287
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_371-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 371
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_134-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 134
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_323-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 323
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_409-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 409
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_342-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 342
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_459-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 459
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_245-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 245
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_43-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 43
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_195-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 195
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_385-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 385
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_460-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 460
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_225-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 225
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_472-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 472
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_164-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 164
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_172-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 172
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_153-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 153
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_375-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 375
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_256-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 256
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_485-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 485
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_338-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 338
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_9-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 9
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_461-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 461
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_470-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 470
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_218-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 218
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_304-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 304
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_356-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 356
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_388-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 388
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_328-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 328
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_435-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 435
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_488-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 488
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_255-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 255
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_212-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 212
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_237-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 237
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_197-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 197
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_442-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 442
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_249-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 249
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_241-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 241
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_60-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 60
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_496-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 496
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_288-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 288
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_48-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 48
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_351-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 351
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_464-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 464
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_371-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 371
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_89-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 89
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_227-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 227
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_383-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 383
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_45-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 45
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_500-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 500
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_41-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 41
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_125-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 125
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_432-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 432
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_118-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 118
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_117-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 117
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_216-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 216
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_43-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 43
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_268-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 268
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_246-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 246
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_234-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 234
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_448-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 448
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_368-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 368
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_419-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 419
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_229-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 229
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_288-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 288
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_226-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 226
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_281-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 281
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_230-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 230
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_318-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 318
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_415-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 415
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_359-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 359
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_121-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 121
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_441-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 441
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_19-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 19
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_340-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 340
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_75-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 75
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_354-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 354
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_53-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 53
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_392-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 392
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_208-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 208
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_152-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 152
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_110-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 110
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_213-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 213
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_382-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 382
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_311-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 311
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_99-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 99
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_460-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 460
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_295-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 295
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_468-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 468
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_290-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 290
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_478-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 478
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_306-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 306
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_266-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 266
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_394-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 394
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_325-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 325
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_435-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 435
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_387-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 387
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_275-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 275
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_498-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 498
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_420-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 420
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_71-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 71
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_63-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 63
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_314-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 314
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_194-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 194
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_226-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 226
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_468-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 468
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_462-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 462
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_451-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 451
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_165-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 165
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_106-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 106
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_23-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 23
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_404-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 404
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_341-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 341
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_271-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 271
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_393-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 393
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_253-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 253
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_273-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 273
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_37-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 37
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_348-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 348
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_220-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 220
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_284-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 284
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_433-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 433
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_329-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 329
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_389-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 389
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_235-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 235
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_285-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 285
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_163-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 163
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_86-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 86
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_282-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 282
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_421-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 421
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_454-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 454
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_144-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 144
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_91-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 91
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_443-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 443
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_411-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 411
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_403-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 403
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_428-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 428
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_217-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 217
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_92-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 92
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_216-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 216
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_243-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 243
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_3-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 3
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_65-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 65
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_219-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 219
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_112-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 112
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_321-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 321
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_245-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 245
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_261-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 261
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_119-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 119
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_450-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 450
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_447-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 447
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_136-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 136
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_38-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 38
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_170-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 170
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_247-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 247
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_353-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 353
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_408-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 408
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_406-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 406
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_154-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 154
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_296-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 296
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_151-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 151
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_380-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 380
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_239-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 239
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_4-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 4
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_339-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 339
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_303-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 303
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_123-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 123
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_295-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 295
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_254-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 254
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_122-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 122
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_146-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 146
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_462-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 462
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_270-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 270
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_176-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 176
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_499-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 499
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_475-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 475
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_166-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 166
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_369-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 369
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_198-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 198
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_402-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 402
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_116-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 116
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_133-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 133
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_469-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 469
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_146-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 146
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_81-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 81
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_21-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 21
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_315-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 315
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_303-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 303
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_289-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 289
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_218-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 218
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_412-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 412
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_243-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 243
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_379-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 379
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_88-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 88
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_436-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 436
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_253-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 253
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_197-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 197
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_364-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 364
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_248-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 248
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_5-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 5
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_498-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 498
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_53-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 53
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_281-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 281
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_228-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 228
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_453-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 453
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_95-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 95
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_340-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 340
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_351-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 351
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_465-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 465
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_413-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 413
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_434-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 434
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_238-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 238
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_425-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 425
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_273-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 273
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_147-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 147
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_180-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 180
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_150-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 150
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_481-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 481
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_47-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 47
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_252-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 252
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_144-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 144
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_94-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 94
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_34-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 34
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_349-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 349
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_394-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 394
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_166-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 166
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_480-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 480
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_23-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 23
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_72-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 72
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_416-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 416
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_17-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 17
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_322-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 322
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_356-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 356
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_474-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 474
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_397-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 397
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_46-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 46
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_492-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 492
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_162-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 162
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_280-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 280
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_215-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 215
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_27-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 27
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_449-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 449
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_12-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 12
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_214-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 214
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_171-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 171
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_64-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 64
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_135-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 135
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_66-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 66
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_477-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 477
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_35-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 35
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_156-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 156
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_33-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 33
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_407-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 407
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_300-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 300
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_237-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 237
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_5-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 5
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_364-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 364
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_320-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 320
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_342-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 342
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_400-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 400
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_78-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 78
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_390-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 390
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_354-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 354
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_145-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 145
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_131-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 131
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_77-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 77
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_164-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 164
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_4-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 4
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_81-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 81
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_39-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 39
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_358-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 358
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_272-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 272
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_120-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 120
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_203-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 203
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_433-O",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 433
    },
    {
        "type": "ethernet-networkV3",
        "ethernetNetworkType": "Tagged",
        "name": "net_345-E",
        "privateNetwork": False,
        "purpose": "General",
        "smartLink": True,
        "vlanId": 345
    }
]

fcnets = [
]

fcoenets = [
]

networkset = [
    {
        "type": "network-set",
        "name": "NetSet_2S1409P9XS_1",
        "nativeNetworkUri": None,
        "networkUris": [
            "net_120-E",
            "net_231-E",
            "net_130-E",
            "net_256-E",
            "net_188-E",
            "net_151-E",
            "net_250-E",
            "net_204-E",
            "net_218-E",
            "net_215-E",
            "net_183-E",
            "net_209-E",
            "net_175-E",
            "net_112-E",
            "net_253-E",
            "net_255-E",
            "net_202-E",
            "net_152-E",
            "net_219-E",
            "net_237-E",
            "net_200-E",
            "net_170-E",
            "net_239-E",
            "net_211-E",
            "net_100-E",
            "net_166-E",
            "net_201-E",
            "net_190-E",
            "net_148-E",
            "net_251-E",
            "net_184-E",
            "net_140-E",
            "net_233-E",
            "net_155-E",
            "net_226-E",
            "net_176-E",
            "net_254-E",
            "net_234-E",
            "net_187-E",
            "net_189-E",
            "net_196-E",
            "net_153-E",
            "net_102-E",
            "net_241-E",
            "net_167-E",
            "net_141-E",
            "net_146-E",
            "net_114-E",
            "net_126-E",
            "net_135-E",
            "net_106-E",
            "net_208-E",
            "net_103-E",
            "net_224-E",
            "net_221-E",
            "net_235-E",
            "net_161-E",
            "net_210-E",
            "net_179-E",
            "net_159-E",
            "net_165-E",
            "net_247-E",
            "net_101-E",
            "net_185-E",
            "net_227-E",
            "net_121-E",
            "net_133-E",
            "net_203-E",
            "net_180-E",
            "net_160-E",
            "net_122-E",
            "net_178-E",
            "net_245-E",
            "net_136-E",
            "net_113-E",
            "net_258-E",
            "net_205-E",
            "net_191-E",
            "net_257-E",
            "net_236-E",
            "net_116-E",
            "net_171-E",
            "net_150-E",
            "net_194-E",
            "net_177-E",
            "net_195-E",
            "net_145-E",
            "net_230-E",
            "net_260-E",
            "net_134-E",
            "net_198-E",
            "net_228-E",
            "net_163-E",
            "net_248-E",
            "net_105-E",
            "net_229-E",
            "net_129-E",
            "net_111-E",
            "net_213-E",
            "net_110-E",
            "net_261-E",
            "net_128-E",
            "net_182-E",
            "net_217-E",
            "net_157-E",
            "net_164-E",
            "net_252-E",
            "net_125-E",
            "net_124-E",
            "net_212-E",
            "net_243-E",
            "net_216-E",
            "net_138-E",
            "net_242-E",
            "net_169-E",
            "net_119-E",
            "net_158-E",
            "net_149-E",
            "net_207-E",
            "net_246-E",
            "net_104-E",
            "net_109-E",
            "net_220-E",
            "net_238-E",
            "net_108-E",
            "net_193-E",
            "net_154-E",
            "net_118-E",
            "net_143-E",
            "net_186-E",
            "net_115-E",
            "net_137-E",
            "net_232-E",
            "net_240-E",
            "net_131-E",
            "net_162-E",
            "net_249-E",
            "net_225-E",
            "net_107-E",
            "net_142-E",
            "net_199-E",
            "net_144-E",
            "net_214-E",
            "net_223-E",
            "net_244-E",
            "net_172-E",
            "net_147-E",
            "net_168-E",
            "net_123-E",
            "net_197-E",
            "net_132-E",
            "net_174-E",
            "net_139-E",
            "net_206-E",
            "net_222-E",
            "net_117-E",
            "net_259-E",
            "net_156-E",
            "net_181-E",
            "net_173-E",
            "net_192-E",
            "net_127-E"
        ]
    },
    {
        "type": "network-set",
        "name": "NetSet_2S1409P9XS_0",
        "nativeNetworkUri": None,
        "networkUris": [
            "net_214-O",
            "net_139-O",
            "net_238-O",
            "net_232-O",
            "net_244-O",
            "net_228-O",
            "net_103-O",
            "net_131-O",
            "net_111-O",
            "net_204-O",
            "net_209-O",
            "net_163-O",
            "net_206-O",
            "net_189-O",
            "net_153-O",
            "net_157-O",
            "net_257-O",
            "net_223-O",
            "net_254-O",
            "net_249-O",
            "net_151-O",
            "net_110-O",
            "net_220-O",
            "net_208-O",
            "net_261-O",
            "net_104-O",
            "net_121-O",
            "net_116-O",
            "net_194-O",
            "net_173-O",
            "net_216-O",
            "net_190-O",
            "net_188-O",
            "net_137-O",
            "net_115-O",
            "net_160-O",
            "net_158-O",
            "net_176-O",
            "net_114-O",
            "net_230-O",
            "net_145-O",
            "net_201-O",
            "net_138-O",
            "net_246-O",
            "net_234-O",
            "net_198-O",
            "net_240-O",
            "net_203-O",
            "net_146-O",
            "net_167-O",
            "net_245-O",
            "net_165-O",
            "net_187-O",
            "net_200-O",
            "net_156-O",
            "net_207-O",
            "net_199-O",
            "net_247-O",
            "net_132-O",
            "net_231-O",
            "net_147-O",
            "net_210-O",
            "net_122-O",
            "net_172-O",
            "net_106-O",
            "net_119-O",
            "net_101-O",
            "net_120-O",
            "net_135-O",
            "net_180-O",
            "net_171-O",
            "net_141-O",
            "net_113-O",
            "net_258-O",
            "net_253-O",
            "net_149-O",
            "net_224-O",
            "net_102-O",
            "net_241-O",
            "net_100-O",
            "net_259-O",
            "net_166-O",
            "net_128-O",
            "net_134-O",
            "net_126-O",
            "net_150-O",
            "net_140-O",
            "net_127-O",
            "net_108-O",
            "net_162-O",
            "net_142-O",
            "net_256-O",
            "net_186-O",
            "net_196-O",
            "net_143-O",
            "net_133-O",
            "net_242-O",
            "net_164-O",
            "net_237-O",
            "net_155-O",
            "net_243-O",
            "net_117-O",
            "net_191-O",
            "net_193-O",
            "net_154-O",
            "net_197-O",
            "net_222-O",
            "net_107-O",
            "net_239-O",
            "net_181-O",
            "net_195-O",
            "net_212-O",
            "net_144-O",
            "net_159-O",
            "net_125-O",
            "net_236-O",
            "net_217-O",
            "net_202-O",
            "net_260-O",
            "net_174-O",
            "net_255-O",
            "net_148-O",
            "net_169-O",
            "net_184-O",
            "net_168-O",
            "net_118-O",
            "net_218-O",
            "net_252-O",
            "net_225-O",
            "net_161-O",
            "net_105-O",
            "net_170-O",
            "net_215-O",
            "net_130-O",
            "net_124-O",
            "net_227-O",
            "net_183-O",
            "net_112-O",
            "net_179-O",
            "net_192-O",
            "net_175-O",
            "net_219-O",
            "net_250-O",
            "net_229-O",
            "net_248-O",
            "net_233-O",
            "net_226-O",
            "net_177-O",
            "net_123-O",
            "net_178-O",
            "net_205-O",
            "net_213-O",
            "net_221-O",
            "net_129-O",
            "net_251-O",
            "net_136-O",
            "net_235-O",
            "net_185-O",
            "net_109-O",
            "net_182-O",
            "net_152-O",
            "net_211-O"
        ]
    }
]

lig = [
    {
        "name": "LIG_2S1409P9XS",
        "ethernetSettings": {
            "enableFastMacCacheFailover": True,
            "enableIgmpSnooping": False,
            "enableNetworkLoopProtection": True,
            "enablePauseFloodProtection": True,
            "igmpIdleTimeoutInterval": 260,
            "interconnectType": "Ethernet",
            "macRefreshInterval": 5
        },
        "interconnectMapTemplate": [
            {
                "enclosure": 1,
                "bay": 2,
                "type": "HP VC Flex-10/10D Module"
            },
            {
                "enclosure": 1,
                "bay": 3,
                "type": "HP VC Flex-10 Enet Module"
            },
            {
                "enclosure": 1,
                "bay": 4,
                "type": "HP VC Flex-10 Enet Module"
            },
            {
                "enclosure": 1,
                "bay": 5,
                "type": "HP VC 8Gb 20-Port FC Module"
            },
            {
                "enclosure": 1,
                "bay": 6,
                "type": "HP VC 8Gb 20-Port FC Module"
            },
            {
                "enclosure": 1,
                "bay": 1,
                "type": "HP VC Flex-10/10D Module"
            }

        ],
        "telemetryConfiguration": {
            "enableTelemetry": True,
            "sampleCount": 300,
            "sampleInterval": 300
        },
        "snmpConfiguration": {
            "enabled": True,
            "readCommunity": "public",
            "snmpAccess": [],
            "systemContact": "",
            "trapDestinations": []
        },
        "uplinkSets": [
        {
            "ethernetNetworkType": "Untagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X7",
                    "enclosure": "1",
                    "bay": "2"
                }
            ],
            "mode": "Auto",
            "name": "2Network",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "2Network"
            ],
            "primaryPort": None
        },
        {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "1",
                    "port": "X4",
                    "enclosure": "1"
                },
                {
                    "speed": "Auto",
                    "bay": "1",
                    "port": "X3",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "OddPipe",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "net_238-O",
                "net_66-O",
                "net_244-O",
                "net_500-O",
                "net_315-O",
                "net_324-O",
                "net_131-O",
                "net_111-O",
                "net_51-O",
                "net_449-O",
                "net_189-O",
                "net_5-O",
                "net_294-O",
                "net_376-O",
                "net_457-O",
                "net_497-O",
                "net_447-O",
                "net_469-O",
                "net_380-O",
                "net_104-O",
                "net_312-O",
                "net_121-O",
                "net_194-O",
                "net_81-O",
                "net_18-O",
                "net_173-O",
                "net_63-O",
                "net_424-O",
                "net_61-O",
                "net_489-O",
                "net_301-O",
                "net_461-O",
                "net_372-O",
                "net_468-O",
                "net_246-O",
                "net_378-O",
                "net_43-O",
                "net_287-O",
                "net_302-O",
                "net_146-O",
                "net_97-O",
                "net_450-O",
                "net_474-O",
                "net_322-O",
                "net_56-O",
                "net_498-O",
                "net_419-O",
                "net_326-O",
                "net_499-O",
                "net_70-O",
                "net_284-O",
                "net_275-O",
                "net_147-O",
                "net_283-O",
                "net_262-O",
                "net_106-O",
                "net_101-O",
                "net_120-O",
                "net_487-O",
                "net_295-O",
                "net_456-O",
                "net_476-O",
                "net_113-O",
                "net_98-O",
                "net_253-O",
                "net_224-O",
                "net_241-O",
                "net_433-O",
                "net_62-O",
                "net_390-O",
                "net_313-O",
                "net_370-O",
                "net_483-O",
                "net_298-O",
                "net_335-O",
                "net_290-O",
                "net_484-O",
                "net_13-O",
                "net_164-O",
                "net_363-O",
                "net_155-O",
                "net_243-O",
                "net_193-O",
                "net_325-O",
                "net_88-O",
                "net_384-O",
                "net_466-O",
                "net_367-O",
                "net_369-O",
                "net_463-O",
                "net_411-O",
                "net_75-O",
                "net_144-O",
                "net_125-O",
                "net_420-O",
                "net_260-O",
                "net_288-O",
                "net_168-O",
                "net_24-O",
                "net_218-O",
                "net_252-O",
                "net_393-O",
                "net_414-O",
                "net_342-O",
                "net_225-O",
                "net_161-O",
                "net_430-O",
                "net_105-O",
                "net_488-O",
                "net_67-O",
                "net_381-O",
                "net_346-O",
                "net_124-O",
                "net_112-O",
                "net_496-O",
                "net_248-O",
                "net_334-O",
                "net_386-O",
                "net_28-O",
                "net_442-O",
                "net_350-O",
                "net_4-O",
                "net_83-O",
                "net_86-O",
                "net_8-O",
                "net_344-O",
                "net_343-O",
                "net_10-O",
                "net_221-O",
                "net_251-O",
                "net_129-O",
                "net_494-O",
                "net_211-O",
                "net_93-O",
                "net_30-O",
                "net_214-O",
                "net_139-O",
                "net_49-O",
                "net_232-O",
                "net_365-O",
                "net_437-O",
                "net_406-O",
                "net_103-O",
                "net_353-O",
                "net_16-O",
                "net_439-O",
                "net_281-O",
                "net_206-O",
                "net_435-O",
                "net_2-O",
                "net_90-O",
                "net_451-O",
                "net_157-O",
                "net_257-O",
                "net_387-O",
                "net_249-O",
                "net_458-O",
                "net_40-O",
                "net_151-O",
                "net_91-O",
                "net_455-O",
                "net_261-O",
                "net_89-O",
                "net_190-O",
                "net_137-O",
                "net_22-O",
                "net_52-O",
                "net_115-O",
                "net_64-O",
                "net_328-O",
                "net_114-O",
                "net_176-O",
                "net_201-O",
                "net_234-O",
                "net_50-O",
                "net_446-O",
                "net_460-O",
                "net_293-O",
                "net_271-O",
                "net_207-O",
                "net_345-O",
                "net_392-O",
                "net_495-O",
                "net_132-O",
                "net_231-O",
                "net_29-O",
                "net_314-O",
                "net_434-O",
                "net_79-O",
                "net_172-O",
                "net_479-O",
                "net_427-O",
                "net_319-O",
                "net_327-O",
                "net_102-O",
                "net_336-O",
                "net_323-O",
                "net_19-O",
                "net_7-O",
                "net_166-O",
                "net_299-O",
                "net_471-O",
                "net_128-O",
                "net_134-O",
                "net_452-O",
                "net_310-O",
                "net_127-O",
                "net_14-O",
                "net_242-O",
                "net_409-O",
                "net_42-O",
                "net_398-O",
                "net_266-O",
                "net_413-O",
                "net_154-O",
                "net_222-O",
                "net_396-O",
                "net_431-O",
                "net_348-O",
                "net_212-O",
                "net_195-O",
                "net_304-O",
                "net_80-O",
                "net_217-O",
                "net_355-O",
                "net_31-O",
                "net_169-O",
                "net_371-O",
                "net_338-O",
                "net_39-O",
                "net_87-O",
                "net_373-O",
                "net_423-O",
                "net_170-O",
                "net_45-O",
                "net_279-O",
                "net_227-O",
                "net_183-O",
                "net_377-O",
                "net_192-O",
                "net_219-O",
                "net_175-O",
                "net_12-O",
                "net_459-O",
                "net_229-O",
                "net_417-O",
                "net_361-O",
                "net_233-O",
                "net_27-O",
                "net_356-O",
                "net_337-O",
                "net_362-O",
                "net_177-O",
                "net_178-O",
                "net_307-O",
                "net_421-O",
                "net_235-O",
                "net_331-O",
                "net_76-O",
                "net_182-O",
                "net_379-O",
                "net_274-O",
                "net_84-O",
                "net_228-O",
                "net_69-O",
                "net_53-O",
                "net_57-O",
                "net_204-O",
                "net_426-O",
                "net_429-O",
                "net_37-O",
                "net_163-O",
                "net_366-O",
                "net_317-O",
                "net_311-O",
                "net_400-O",
                "net_47-O",
                "net_351-O",
                "net_34-O",
                "net_486-O",
                "net_110-O",
                "net_73-O",
                "net_477-O",
                "net_220-O",
                "net_329-O",
                "net_99-O",
                "net_354-O",
                "net_216-O",
                "net_357-O",
                "net_382-O",
                "net_188-O",
                "net_475-O",
                "net_158-O",
                "net_160-O",
                "net_145-O",
                "net_270-O",
                "net_491-O",
                "net_198-O",
                "net_401-O",
                "net_167-O",
                "net_453-O",
                "net_165-O",
                "net_282-O",
                "net_318-O",
                "net_349-O",
                "net_395-O",
                "net_482-O",
                "net_199-O",
                "net_464-O",
                "net_412-O",
                "net_247-O",
                "net_82-O",
                "net_448-O",
                "net_210-O",
                "net_122-O",
                "net_171-O",
                "net_432-O",
                "net_490-O",
                "net_473-O",
                "net_397-O",
                "net_26-O",
                "net_149-O",
                "net_273-O",
                "net_416-O",
                "net_352-O",
                "net_492-O",
                "net_259-O",
                "net_436-O",
                "net_428-O",
                "net_445-O",
                "net_407-O",
                "net_410-O",
                "net_140-O",
                "net_256-O",
                "net_142-O",
                "net_186-O",
                "net_143-O",
                "net_385-O",
                "net_133-O",
                "net_48-O",
                "net_54-O",
                "net_443-O",
                "net_78-O",
                "net_191-O",
                "net_117-O",
                "net_55-O",
                "net_107-O",
                "net_239-O",
                "net_485-O",
                "net_181-O",
                "net_339-O",
                "net_316-O",
                "net_389-O",
                "net_297-O",
                "net_236-O",
                "net_306-O",
                "net_202-O",
                "net_255-O",
                "net_347-O",
                "net_286-O",
                "net_36-O",
                "net_472-O",
                "net_3-O",
                "net_77-O",
                "net_480-O",
                "net_418-O",
                "net_215-O",
                "net_58-O",
                "net_130-O",
                "net_278-O",
                "net_454-O",
                "net_332-O",
                "net_179-O",
                "net_25-O",
                "net_11-O",
                "net_394-O",
                "net_205-O",
                "net_213-O",
                "net_276-O",
                "net_46-O",
                "net_185-O",
                "net_72-O",
                "net_441-O",
                "net_264-O",
                "net_303-O",
                "net_470-O",
                "net_272-O",
                "net_408-O",
                "net_209-O",
                "net_368-O",
                "net_153-O",
                "net_462-O",
                "net_223-O",
                "net_254-O",
                "net_208-O",
                "net_291-O",
                "net_308-O",
                "net_116-O",
                "net_265-O",
                "net_330-O",
                "net_230-O",
                "net_267-O",
                "net_405-O",
                "net_138-O",
                "net_6-O",
                "net_32-O",
                "net_240-O",
                "net_203-O",
                "net_245-O",
                "net_388-O",
                "net_425-O",
                "net_156-O",
                "net_200-O",
                "net_187-O",
                "net_35-O",
                "net_92-O",
                "net_391-O",
                "net_404-O",
                "net_321-O",
                "net_340-O",
                "net_119-O",
                "net_135-O",
                "net_180-O",
                "net_9-O",
                "net_481-O",
                "net_141-O",
                "net_258-O",
                "net_296-O",
                "net_403-O",
                "net_359-O",
                "net_263-O",
                "net_285-O",
                "net_100-O",
                "net_280-O",
                "net_305-O",
                "net_360-O",
                "net_493-O",
                "net_399-O",
                "net_68-O",
                "net_126-O",
                "net_150-O",
                "net_65-O",
                "net_415-O",
                "net_162-O",
                "net_108-O",
                "net_268-O",
                "net_402-O",
                "net_20-O",
                "net_196-O",
                "net_237-O",
                "net_85-O",
                "net_41-O",
                "net_197-O",
                "net_364-O",
                "net_17-O",
                "net_21-O",
                "net_375-O",
                "net_33-O",
                "net_159-O",
                "net_96-O",
                "net_444-O",
                "net_422-O",
                "net_440-O",
                "net_71-O",
                "net_59-O",
                "net_174-O",
                "net_148-O",
                "net_467-O",
                "net_184-O",
                "net_118-O",
                "net_383-O",
                "net_269-O",
                "net_289-O",
                "net_292-O",
                "net_320-O",
                "net_277-O",
                "net_60-O",
                "net_95-O",
                "net_300-O",
                "net_250-O",
                "net_15-O",
                "net_226-O",
                "net_465-O",
                "net_23-O",
                "net_438-O",
                "net_123-O",
                "net_44-O",
                "net_333-O",
                "net_38-O",
                "net_136-O",
                "net_358-O",
                "net_341-O",
                "net_109-O",
                "net_74-O",
                "net_374-O",
                "net_152-O",
                "net_478-O",
                "net_309-O",
                "net_94-O"
            ],
            "primaryPort": None
        },
        {
            "ethernetNetworkType": "Tagged",
            "lacpTimer": "Short",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "bay": "2",
                    "port": "X4",
                    "enclosure": "1"
                },
                {
                    "speed": "Auto",
                    "bay": "2",
                    "port": "X3",
                    "enclosure": "1"
                }
            ],
            "mode": "Auto",
            "name": "EvenPipe",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "net_120-E",
                "net_462-E",
                "net_256-E",
                "net_337-E",
                "net_492-E",
                "net_307-E",
                "net_42-E",
                "net_183-E",
                "net_209-E",
                "net_112-E",
                "net_324-E",
                "net_202-E",
                "net_360-E",
                "net_219-E",
                "net_237-E",
                "net_200-E",
                "net_44-E",
                "net_265-E",
                "net_442-E",
                "net_11-E",
                "net_9-E",
                "net_433-E",
                "net_184-E",
                "net_251-E",
                "net_488-E",
                "net_436-E",
                "net_155-E",
                "net_372-E",
                "net_226-E",
                "net_176-E",
                "net_254-E",
                "net_325-E",
                "net_241-E",
                "net_8-E",
                "net_167-E",
                "net_22-E",
                "net_17-E",
                "net_402-E",
                "net_329-E",
                "net_429-E",
                "net_21-E",
                "net_351-E",
                "net_289-E",
                "net_15-E",
                "net_347-E",
                "net_235-E",
                "net_376-E",
                "net_46-E",
                "net_73-E",
                "net_185-E",
                "net_421-E",
                "net_340-E",
                "net_82-E",
                "net_77-E",
                "net_203-E",
                "net_294-E",
                "net_418-E",
                "net_122-E",
                "net_31-E",
                "net_447-E",
                "net_258-E",
                "net_205-E",
                "net_70-E",
                "net_116-E",
                "net_419-E",
                "net_177-E",
                "net_375-E",
                "net_304-E",
                "net_387-E",
                "net_228-E",
                "net_163-E",
                "net_105-E",
                "net_129-E",
                "net_276-E",
                "net_426-E",
                "net_310-E",
                "net_382-E",
                "net_453-E",
                "net_128-E",
                "net_182-E",
                "net_463-E",
                "net_353-E",
                "net_404-E",
                "net_455-E",
                "net_124-E",
                "net_125-E",
                "net_216-E",
                "net_56-E",
                "net_412-E",
                "net_320-E",
                "net_458-E",
                "net_285-E",
                "net_246-E",
                "net_109-E",
                "net_282-E",
                "net_154-E",
                "net_409-E",
                "net_270-E",
                "net_332-E",
                "net_162-E",
                "net_18-E",
                "net_407-E",
                "net_142-E",
                "net_500-E",
                "net_199-E",
                "net_24-E",
                "net_369-E",
                "net_223-E",
                "net_89-E",
                "net_428-E",
                "net_481-E",
                "net_312-E",
                "net_264-E",
                "net_450-E",
                "net_434-E",
                "net_439-E",
                "net_181-E",
                "net_392-E",
                "net_411-E",
                "net_280-E",
                "net_448-E",
                "net_130-E",
                "net_471-E",
                "net_80-E",
                "net_204-E",
                "net_96-E",
                "net_354-E",
                "net_293-E",
                "net_34-E",
                "net_321-E",
                "net_215-E",
                "net_175-E",
                "net_253-E",
                "net_152-E",
                "net_491-E",
                "net_349-E",
                "net_63-E",
                "net_414-E",
                "net_303-E",
                "net_3-E",
                "net_41-E",
                "net_472-E",
                "net_170-E",
                "net_487-E",
                "net_343-E",
                "net_100-E",
                "net_449-E",
                "net_234-E",
                "net_7-E",
                "net_469-E",
                "net_395-E",
                "net_102-E",
                "net_32-E",
                "net_417-E",
                "net_146-E",
                "net_114-E",
                "net_106-E",
                "net_278-E",
                "net_496-E",
                "net_45-E",
                "net_161-E",
                "net_165-E",
                "net_101-E",
                "net_345-E",
                "net_43-E",
                "net_478-E",
                "net_464-E",
                "net_53-E",
                "net_16-E",
                "net_445-E",
                "net_454-E",
                "net_180-E",
                "net_178-E",
                "net_65-E",
                "net_263-E",
                "net_28-E",
                "net_51-E",
                "net_361-E",
                "net_308-E",
                "net_236-E",
                "net_171-E",
                "net_194-E",
                "net_145-E",
                "net_72-E",
                "net_297-E",
                "net_269-E",
                "net_84-E",
                "net_495-E",
                "net_461-E",
                "net_111-E",
                "net_358-E",
                "net_378-E",
                "net_110-E",
                "net_493-E",
                "net_261-E",
                "net_6-E",
                "net_494-E",
                "net_29-E",
                "net_336-E",
                "net_252-E",
                "net_64-E",
                "net_14-E",
                "net_243-E",
                "net_367-E",
                "net_388-E",
                "net_374-E",
                "net_301-E",
                "net_169-E",
                "net_104-E",
                "net_207-E",
                "net_86-E",
                "net_348-E",
                "net_405-E",
                "net_416-E",
                "net_319-E",
                "net_477-E",
                "net_292-E",
                "net_406-E",
                "net_389-E",
                "net_334-E",
                "net_468-E",
                "net_287-E",
                "net_186-E",
                "net_232-E",
                "net_240-E",
                "net_422-E",
                "net_322-E",
                "net_144-E",
                "net_214-E",
                "net_123-E",
                "net_427-E",
                "net_117-E",
                "net_475-E",
                "net_499-E",
                "net_91-E",
                "net_424-E",
                "net_10-E",
                "net_93-E",
                "net_192-E",
                "net_231-E",
                "net_188-E",
                "net_290-E",
                "net_151-E",
                "net_356-E",
                "net_37-E",
                "net_27-E",
                "net_441-E",
                "net_218-E",
                "net_467-E",
                "net_380-E",
                "net_57-E",
                "net_85-E",
                "net_255-E",
                "net_338-E",
                "net_48-E",
                "net_211-E",
                "net_363-E",
                "net_275-E",
                "net_300-E",
                "net_315-E",
                "net_311-E",
                "net_286-E",
                "net_201-E",
                "net_296-E",
                "net_148-E",
                "net_187-E",
                "net_189-E",
                "net_396-E",
                "net_196-E",
                "net_384-E",
                "net_126-E",
                "net_208-E",
                "net_444-E",
                "net_221-E",
                "net_377-E",
                "net_210-E",
                "net_413-E",
                "net_335-E",
                "net_283-E",
                "net_227-E",
                "net_121-E",
                "net_87-E",
                "net_371-E",
                "net_383-E",
                "net_288-E",
                "net_25-E",
                "net_267-E",
                "net_33-E",
                "net_245-E",
                "net_49-E",
                "net_359-E",
                "net_365-E",
                "net_452-E",
                "net_410-E",
                "net_440-E",
                "net_403-E",
                "net_88-E",
                "net_397-E",
                "net_272-E",
                "net_341-E",
                "net_230-E",
                "net_456-E",
                "net_260-E",
                "net_333-E",
                "net_134-E",
                "net_198-E",
                "net_339-E",
                "net_399-E",
                "net_74-E",
                "net_229-E",
                "net_432-E",
                "net_58-E",
                "net_474-E",
                "net_394-E",
                "net_451-E",
                "net_217-E",
                "net_62-E",
                "net_164-E",
                "net_30-E",
                "net_373-E",
                "net_408-E",
                "net_318-E",
                "net_212-E",
                "net_71-E",
                "net_138-E",
                "net_274-E",
                "net_26-E",
                "net_476-E",
                "net_90-E",
                "net_486-E",
                "net_158-E",
                "net_149-E",
                "net_220-E",
                "net_55-E",
                "net_391-E",
                "net_435-E",
                "net_238-E",
                "net_291-E",
                "net_193-E",
                "net_466-E",
                "net_443-E",
                "net_143-E",
                "net_330-E",
                "net_97-E",
                "net_95-E",
                "net_485-E",
                "net_115-E",
                "net_137-E",
                "net_328-E",
                "net_400-E",
                "net_131-E",
                "net_81-E",
                "net_284-E",
                "net_362-E",
                "net_352-E",
                "net_225-E",
                "net_107-E",
                "net_465-E",
                "net_480-E",
                "net_273-E",
                "net_38-E",
                "net_368-E",
                "net_244-E",
                "net_147-E",
                "net_457-E",
                "net_172-E",
                "net_401-E",
                "net_168-E",
                "net_420-E",
                "net_398-E",
                "net_132-E",
                "net_60-E",
                "net_139-E",
                "net_206-E",
                "net_430-E",
                "net_298-E",
                "net_259-E",
                "net_279-E",
                "net_484-E",
                "net_342-E",
                "net_326-E",
                "net_173-E",
                "net_5-E",
                "net_295-E",
                "net_381-E",
                "net_94-E",
                "net_250-E",
                "net_379-E",
                "net_268-E",
                "net_83-E",
                "net_69-E",
                "net_23-E",
                "net_313-E",
                "net_239-E",
                "net_459-E",
                "net_92-E",
                "net_54-E",
                "net_437-E",
                "net_166-E",
                "net_190-E",
                "net_364-E",
                "net_59-E",
                "net_357-E",
                "net_233-E",
                "net_140-E",
                "net_153-E",
                "net_350-E",
                "net_497-E",
                "net_75-E",
                "net_19-E",
                "net_141-E",
                "net_316-E",
                "net_135-E",
                "net_76-E",
                "net_50-E",
                "net_498-E",
                "net_431-E",
                "net_103-E",
                "net_224-E",
                "net_305-E",
                "net_179-E",
                "net_68-E",
                "net_423-E",
                "net_159-E",
                "net_99-E",
                "net_247-E",
                "net_370-E",
                "net_438-E",
                "net_133-E",
                "net_160-E",
                "net_390-E",
                "net_327-E",
                "net_136-E",
                "net_425-E",
                "net_317-E",
                "net_12-E",
                "net_113-E",
                "net_309-E",
                "net_191-E",
                "net_489-E",
                "net_257-E",
                "net_277-E",
                "net_355-E",
                "net_446-E",
                "net_150-E",
                "net_195-E",
                "net_385-E",
                "net_490-E",
                "net_79-E",
                "net_271-E",
                "net_61-E",
                "net_4-E",
                "net_248-E",
                "net_281-E",
                "net_266-E",
                "net_213-E",
                "net_98-E",
                "net_157-E",
                "net_67-E",
                "net_299-E",
                "net_20-E",
                "net_415-E",
                "net_482-E",
                "net_473-E",
                "net_242-E",
                "net_323-E",
                "net_119-E",
                "net_36-E",
                "net_306-E",
                "net_35-E",
                "net_393-E",
                "net_108-E",
                "net_13-E",
                "net_331-E",
                "net_118-E",
                "net_52-E",
                "net_262-E",
                "net_346-E",
                "net_366-E",
                "net_483-E",
                "net_249-E",
                "net_66-E",
                "net_2-E",
                "net_344-E",
                "net_479-E",
                "net_302-E",
                "net_197-E",
                "net_174-E",
                "net_47-E",
                "net_314-E",
                "net_222-E",
                "net_460-E",
                "net_40-E",
                "net_470-E",
                "net_386-E",
                "net_78-E",
                "net_156-E",
                "net_39-E",
                "net_127-E"
            ],
            "primaryPort": None
        },
        {
            "ethernetNetworkType": "Untagged",
            "lacpTimer": "Long",
            "logicalPortConfigInfos": [
                {
                    "speed": "Auto",
                    "port": "X7",
                    "enclosure": "1",
                    "bay": "1"
                }
            ],
            "mode": "Auto",
            "name": "1Network",
            "nativeNetworkUri": None,
            "networkType": "Ethernet",
            "networkUris": [
                "1Network"
            ],
            "primaryPort": None
        }
        ],
    }
]

encgrp = [
    {
        "name": "EG_2S1409P9XS",
        "type": "EnclosureGroupV200",
        "enclosureTypeUri": "/rest/enclosure-types/c7000",
        "stackingMode": "Enclosure",
        "interconnectBayMappingCount": 8,
        "interconnectBayMappings": [
            {
                "interconnectBay": 1,
                "logicalInterconnectGroupUri": "LIG_2S1409P9XS"
            },
            {
                "interconnectBay": 2,
                "logicalInterconnectGroupUri": "LIG_2S1409P9XS"
            },
            {
                "interconnectBay": 3,
                "logicalInterconnectGroupUri": "LIG_2S1409P9XS"
            },
            {
                "interconnectBay": 4,
                "logicalInterconnectGroupUri": "LIG_2S1409P9XS"
            },
            {
                "interconnectBay": 5,
                "logicalInterconnectGroupUri": "LIG_2S1409P9XS"
            },
            {
                "interconnectBay": 6,
                "logicalInterconnectGroupUri": "LIG_2S1409P9XS"
            },
            {
                "interconnectBay": 7,
                "logicalInterconnectGroupUri": "LIG_2S1409P9XS"
            },
            {
                "interconnectBay": 8,
                "logicalInterconnectGroupUri": "LIG_2S1409P9XS"
            }
        ]
    }
]

profiles = [
    {
        "enclosureBay": 1,
        "hideUnusedFlexNics": True,
        "macType": "Physical",
        "name": "Profile1",
        "connections": [
            {
                "allocatedMbps": 2000,
                "deploymentStatus": "Deployed",
                "functionType": "Ethernet",
                "id": 1,
                "macType": "Physical",
                "maximumMbps": 10000,
                "name": None,
                "portId": "Lom 1:2-a",
                "requestedMbps": "2000",
                "wwnn": None,
                "wwpn": None,
                "networkUri": "NetSet_2S1409P9XS_1"
            },
            {
                "allocatedMbps": 2000,
                "deploymentStatus": "Deployed",
                "functionType": "Ethernet",
                "id": 2,
                "macType": "Physical",
                "maximumMbps": 10000,
                "name": None,
                "portId": "Lom 1:1-a",
                "requestedMbps": "2000",
                "wwnn": None,
                "wwpn": None,
                "networkUri": "NetSet_2S1409P9XS_0"
            }
        ],
        "serverHardwareUri": "VC-BVT-BACKUP, bay 1",
        "enclosureGroupUri": "EG_2S1409P9XS",
        "enclosureUri": "VC-BVT-BACKUP",
        "type": "ServerProfileV5",
        "serialNumberType": "Physical"
    }
]

encs = [
    {
        "enclosureGroupUri": "EG_2S1409P9XS",
        "forceInstallFirmware": False,
        "licensingIntent": "OneViewNoiLO"
    }
]

servers = [
    {
        "formFactor": "HalfHeight",
        "licensingIntent": "OneViewNoiLO",
        "memoryMb": 8192,
        "model": "ProLiant BL460c G7",
        "mpFirmwareVersion": "1.80 Jul 11 2014",
        "mpModel": "iLO3",
        "name": "VC-BVT-BACKUP, bay 1",
        "partNumber": "603718-B21",
        "position": 1,
        "powerLock": False,
        "powerState": "On",
        "processorCoreCount": 4,
        "processorCount": 1,
        "processorSpeedMhz": 2400,
        "processorType": "Intel(R) Xeon(R) CPU E5620 @ 2.40GHz",
        "refreshState": "NotRefreshing",
        "romVersion": "I27 07/02/2013",
        "serialNumber": "USE303TB64",
        "shortModel": "BL460c G7",
        "state": "ProfileApplied",
        "stateReason": "NotApplicable",
        "status": "OK",
        "type": "server-hardware-4"
    }
]

default_variables = {
        'encgrp': encgrp,
        'encs': encs,
        'ethnets': ethnets,
        'fcnets': fcnets,
        'fcoenets': fcoenets,
        'lig': lig,
        'networkset': networkset,
        'profiles': profiles,
        'servers': servers
}

def get_variables():
    variables = default_variables
    return variables

