''' Input variables for the test '''

goldenimage_add = [{'name': '',
                    'description': 'goldenimage',
                    'file': "valid_file"},

                   {'name': 'goldenimage_1',
                    'description': 'valid_goldenimage',
                    'file': "valid_file"},

                   {'name': 'goldenimage_1',
                    'description': 'goldenimage duplicate name check',
                    'file': "valid_file"},

                   {'name': 'goldenimage_@#$%',
                    'description': 'goldenimage invalid name check',
                    'file': "valid_file"},

                   {'name': 'goldenimage_invalidfile',
                    'description': 'Invalid file check',
                    'file': "invalid_file"},

                   {'name': 'goldenimage_update',
                    'description': 'goldenimage',
                    'file': "valid_file"},

                   {'name': 'namelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamel',
                    'description': 'Golden Image name length is 255 characters',
                    'file': "valid_file"},

                   {'name': 'namelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelength',
                    'description': 'Golden Image name length greater then 255 characters',
                    'file': "valid_file"},

                   {'name': 'goldenimage_desc_lenghtthousand',
                    'description': 'namelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelength',
                    'file': "valid_file"},

                   {'name': 'goldenimage_desc_lenght_greater_then_thousand',
                    'description': 'namelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelength',
                    'file': "valid_file"},

                   {'name': 'CL RHEL API_GET',
                    'description': 'goldenimage',
                    'file': "valid_file"},

                   {'name': 'cl artifact_for_GET',
                    'description': 'goldenimage',
                    'file': "valid_file"},

                   {'name': 'RHEL-7.2-goldenimage',
                    'description': 'goldenimage',
                    'file': "valid_file"},

                   {'name': '123_goldenimage',
                    'description': 'goldenimage',
                    'file': "valid_file"},

                   {'name': 'goldenimage_456',
                    'description': 'goldenimage',
                    'file': "valid_file"}]


goldenimage_get = [{'name': 'goldenimage_1'},
                   {'description': 'valid_goldenimage'},
                   {'name': 'invalid_goldenimage'},
                   {'id': 'xxxx'}]


goldenimage_update = [{'description': 'gi_update_for_description',
                       'type': 'GoldenImage'},
                      {'name': 'gi_update_for_name',
                       'type': 'GoldenImage'}]


goldenimage_delete = [{'name': 'goldenimage_1'},
                      {'name': 'gi_update_for_name'},
                      {'name': 'namelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamelengthnamel'},
                      {'name': 'goldenimage_desc_lenghtthousand'},
                      {'name': 'xx1234x'},
                      {'name': 'CL RHEL API_GET'},
                      {'name': 'cl artifact_for_GET'},
                      {'name': 'RHEL-7.2-goldenimage'},
                      {'name': '123_goldenimage'},
                      {'name': 'goldenimage_456'}]
