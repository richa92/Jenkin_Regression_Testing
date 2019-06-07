admin_credentials = {'userName': 'Administrator', 'password': 'wpsthpvse1'}
ssh_credentials = {'userName': 'root', 'password': 'hpvse1'}

# Features need to populate the role
populateFeatures = ["OVF167", "OVF2"]
populateCMDs = ["/usr/bin/psql -At -U postgres -d cidb -f /ci/db/schema/authz/install/populate-atlas-scope-roles.sql",
                "/usr/bin/psql -At -U postgres -d cidb -f /ci/db/bin/fusion/authz/populate-fusion-authz.sql"]