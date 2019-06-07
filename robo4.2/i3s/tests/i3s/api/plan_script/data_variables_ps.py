#from winnt import NULL
from requests.api import patch

planscript = [{
    "type": "PlanScript",
    "description": "Name field valid",
    "name": "EsxiPlanScript",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "# Mount /bootbank area for ESXi 5.5+ \r\n#\r\n# Typical partition layout is:\r\n# 1 - UEFI ESP\r\n# 5 - /bootbank  <= holds ESXi host state to be configured\r\n# 6 - /altbootbank\r\n\r\necho \"########################################\"\r\necho \"Mount ESXi /bootbank\"\r\necho \"########################################\"\r\n\r\n# List structure storage layout found in ESXi Golden Image / OS Volume\r\necho \"Devices:\"\r\n-list-devices\r\necho\r\necho \"Partitions:\"\r\n-list-partitions\r\necho\r\necho \"File systems:\"\r\n-list-filesystems\r\necho\r\n\r\necho \"Mount file systems:\"\r\necho \"/dev/sda5 is assumed to hold ESXi host state configuration\"\r\necho \"mount /dev/sda5\"\r\nmount /dev/sda5 /\r\necho \"File system details for /dev/sda5:\"\r\n-statvfs /\r\necho\r\necho \"########################################\"\r\necho \"Copy out and unpack ESXi host state\"\r\necho \"########################################\"\r\n\r\necho \"Create ImageStreamer temp directory\"\r\n-mkdir /ImageStreamer\r\necho\r\n\r\necho \"Extract ESXi host configuration from Golden Image\"\r\necho \"Copy out boot.cfg\"\r\ndownload /boot.cfg boot.cfg\r\necho \"Copy out state.tgz if present\"\r\n-download /state.tgz state.tgz\r\necho \"Copy out onetime.tgz if present\"\r\n-download /onetime.tgz onetime.tgz\r\necho\r\n\r\necho \"Build esxi_unpack ESXi host state unpack script\"\r\nupload -<<END /ImageStreamer/esxi_unpack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"Finding ESXi host state configuration archive in Golden Image\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Unpack state.tgz\"\r\n    mkdir $DIR/esxi_state\r\n    cd $DIR/esxi_state\r\n    tar xvpzf $DIR/state.tgz\r\n    echo\r\n    echo \"Unpack local.tgz\"\r\n    mkdir $DIR/esxi_local\r\n    cd $DIR/esxi_local\r\n    tar xvpzf $DIR/esxi_state/local.tgz\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Unpack onetime.tgz\"\r\n    mkdir $DIR/esxi_onetime\r\n    cd $DIR/esxi_onetime\r\n    tar xvpzf $DIR/onetime.tgz\r\n    echo\r\nfi\r\n\r\nif [ -e etc/rc.local.d/local.sh ]; then\r\n    cp etc/rc.local.d/local.sh $DIR/local.sh\r\nfi\r\n\r\necho \"Unpacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_unpack ./esxi_unpack\r\necho\r\n\r\necho \"Build esxi_repack ESXi host state repack script\"\r\nupload -<<END /ImageStreamer/esxi_repack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"---------------------------------------------------------------\"\r\necho \"Final ESXi host local.sh content for configuration at first boot:\"\r\ncat $DIR/local.sh\r\necho \"---------------------------------------------------------------\"\r\necho\r\n\r\necho \"Finding ESXi host state configuration archive\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Repack local.tgz\"\r\n    cd $DIR/esxi_local\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/esxi_state/local.tgz *\r\n    echo\r\n    echo \"Repack state.tgz\"\r\n    cd $DIR/esxi_state\r\n    tar cvpzf $DIR/state.tgz *\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Repack onetime.tgz\"\r\n    cd $DIR/esxi_onetime\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/onetime.tgz *\r\n    touch $DIR/state.tgz\r\n    echo\r\nfi\r\necho \"Repacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_repack ./esxi_repack\r\necho\r\n\r\necho \"Run  esxi_repack ESXi host state unpack script\"\r\n!source ./esxi_unpack\r\necho\r\necho \"########################################\"\r\necho \"Configure ssh\"\r\necho \"########################################\"\r\n\r\nupload -<<END /ImageStreamer/esxi_ssh\r\n#!/bin/bash\r\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\r\ncat <<\"EOF\" >>local.sh\r\nvim-cmd hostsvc/enable_esx_shell\r\nvim-cmd hostsvc/start_esx_shell\r\nvim-cmd hostsvc/enable_ssh\r\nvim-cmd hostsvc/start_ssh\r\nservices.sh restart\r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_ssh esxi_ssh\r\necho \"Run esxi_ssh\"\r\n!source ./esxi_ssh\r\necho \"########################################\"\r\necho \"Pack and replace ESXi host state into ESXi host OS Volume\"\r\necho \"########################################\"\r\n\r\necho \"Run  esxi_repack ESXi host state repack script\"\r\n!source ./esxi_repack\r\n\r\necho \"Copy in state.tgz if present\"\r\n-upload state.tgz /state.tgz \r\necho \"Copy in onetime.tgz if present\"\r\n-upload onetime.tgz /onetime.tgz\r\n\r\necho \"Remove Image Streamer temp directory\"\r\nrm-rf /tmp/ImageStreamer\r\necho \"########################################\"\r\necho \"Cleanup and unmount file systems \"\r\necho \"########################################\"\r\n\r\necho \"Remove ImageStreamer temp directory\"\r\nrm-rf /ImageStreamer\r\n\r\necho \"Unmount file systems\"\r\numount /\r\necho"
}, {
    "type": "PlanScript",
    "description": 'Name field null',
    "name": " ",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "# Mount /bootbank area for ESXi 5.5+ \r\n#\r\n# Typical partition layout is:\r\n# 1 - UEFI ESP\r\n# 5 - /bootbank  <= holds ESXi host state to be configured\r\n# 6 - /altbootbank\r\n\r\necho \"########################################\"\r\necho \"Mount ESXi /bootbank\"\r\necho \"########################################\"\r\n\r\n# List structure storage layout found in ESXi Golden Image / OS Volume\r\necho \"Devices:\"\r\n-list-devices\r\necho\r\necho \"Partitions:\"\r\n-list-partitions\r\necho\r\necho \"File systems:\"\r\n-list-filesystems\r\necho\r\n\r\necho \"Mount file systems:\"\r\necho \"/dev/sda5 is assumed to hold ESXi host state configuration\"\r\necho \"mount /dev/sda5\"\r\nmount /dev/sda5 /\r\necho \"File system details for /dev/sda5:\"\r\n-statvfs /\r\necho\r\necho \"########################################\"\r\necho \"Copy out and unpack ESXi host state\"\r\necho \"########################################\"\r\n\r\necho \"Create ImageStreamer temp directory\"\r\n-mkdir /ImageStreamer\r\necho\r\n\r\necho \"Extract ESXi host configuration from Golden Image\"\r\necho \"Copy out boot.cfg\"\r\ndownload /boot.cfg boot.cfg\r\necho \"Copy out state.tgz if present\"\r\n-download /state.tgz state.tgz\r\necho \"Copy out onetime.tgz if present\"\r\n-download /onetime.tgz onetime.tgz\r\necho\r\n\r\necho \"Build esxi_unpack ESXi host state unpack script\"\r\nupload -<<END /ImageStreamer/esxi_unpack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"Finding ESXi host state configuration archive in Golden Image\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Unpack state.tgz\"\r\n    mkdir $DIR/esxi_state\r\n    cd $DIR/esxi_state\r\n    tar xvpzf $DIR/state.tgz\r\n    echo\r\n    echo \"Unpack local.tgz\"\r\n    mkdir $DIR/esxi_local\r\n    cd $DIR/esxi_local\r\n    tar xvpzf $DIR/esxi_state/local.tgz\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Unpack onetime.tgz\"\r\n    mkdir $DIR/esxi_onetime\r\n    cd $DIR/esxi_onetime\r\n    tar xvpzf $DIR/onetime.tgz\r\n    echo\r\nfi\r\n\r\nif [ -e etc/rc.local.d/local.sh ]; then\r\n    cp etc/rc.local.d/local.sh $DIR/local.sh\r\nfi\r\n\r\necho \"Unpacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_unpack ./esxi_unpack\r\necho\r\n\r\necho \"Build esxi_repack ESXi host state repack script\"\r\nupload -<<END /ImageStreamer/esxi_repack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"---------------------------------------------------------------\"\r\necho \"Final ESXi host local.sh content for configuration at first boot:\"\r\ncat $DIR/local.sh\r\necho \"---------------------------------------------------------------\"\r\necho\r\n\r\necho \"Finding ESXi host state configuration archive\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Repack local.tgz\"\r\n    cd $DIR/esxi_local\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/esxi_state/local.tgz *\r\n    echo\r\n    echo \"Repack state.tgz\"\r\n    cd $DIR/esxi_state\r\n    tar cvpzf $DIR/state.tgz *\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Repack onetime.tgz\"\r\n    cd $DIR/esxi_onetime\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/onetime.tgz *\r\n    touch $DIR/state.tgz\r\n    echo\r\nfi\r\necho \"Repacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_repack ./esxi_repack\r\necho\r\n\r\necho \"Run  esxi_repack ESXi host state unpack script\"\r\n!source ./esxi_unpack\r\necho\r\necho \"########################################\"\r\necho \"Configure ssh\"\r\necho \"########################################\"\r\n\r\nupload -<<END /ImageStreamer/esxi_ssh\r\n#!/bin/bash\r\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\r\ncat <<\"EOF\" >>local.sh\r\nvim-cmd hostsvc/enable_esx_shell\r\nvim-cmd hostsvc/start_esx_shell\r\nvim-cmd hostsvc/enable_ssh\r\nvim-cmd hostsvc/start_ssh\r\nservices.sh restart\r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_ssh esxi_ssh\r\necho \"Run esxi_ssh\"\r\n!source ./esxi_ssh\r\necho \"########################################\"\r\necho \"Pack and replace ESXi host state into ESXi host OS Volume\"\r\necho \"########################################\"\r\n\r\necho \"Run  esxi_repack ESXi host state repack script\"\r\n!source ./esxi_repack\r\n\r\necho \"Copy in state.tgz if present\"\r\n-upload state.tgz /state.tgz \r\necho \"Copy in onetime.tgz if present\"\r\n-upload onetime.tgz /onetime.tgz\r\n\r\necho \"Remove Image Streamer temp directory\"\r\nrm-rf /tmp/ImageStreamer\r\necho \"########################################\"\r\necho \"Cleanup and unmount file systems \"\r\necho \"########################################\"\r\n\r\necho \"Remove ImageStreamer temp directory\"\r\nrm-rf /ImageStreamer\r\n\r\necho \"Unmount file systems\"\r\numount /\r\necho"
}, {
    "type": "PlanScript",
    "description": " ",
    "name": " ",
    "hpProvided": 'false',
    "planType": " ",
    "content": " "
}, {
    "type": "PlanScript",
    "description": "valid deploy planscript",
    "name": "Planscript_valid_deploy",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "# Mount /bootbank area for ESXi 5.5+ \r\n#\r\n# Typical partition layout is:\r\n# 1 - UEFI ESP\r\n# 5 - /bootbank  <= holds ESXi host state to be configured\r\n# 6 - /altbootbank\r\n\r\necho \"########################################\"\r\necho \"Mount ESXi /bootbank\"\r\necho \"########################################\"\r\n\r\n# List structure storage layout found in ESXi Golden Image / OS Volume\r\necho \"Devices:\"\r\n-list-devices\r\necho\r\necho \"Partitions:\"\r\n-list-partitions\r\necho\r\necho \"File systems:\"\r\n-list-filesystems\r\necho\r\n\r\necho \"Mount file systems:\"\r\necho \"/dev/sda5 is assumed to hold ESXi host state configuration\"\r\necho \"mount /dev/sda5\"\r\nmount /dev/sda5 /\r\necho \"File system details for /dev/sda5:\"\r\n-statvfs /\r\necho\r\necho \"########################################\"\r\necho \"Copy out and unpack ESXi host state\"\r\necho \"########################################\"\r\n\r\necho \"Create ImageStreamer temp directory\"\r\n-mkdir /ImageStreamer\r\necho\r\n\r\necho \"Extract ESXi host configuration from Golden Image\"\r\necho \"Copy out boot.cfg\"\r\ndownload /boot.cfg boot.cfg\r\necho \"Copy out state.tgz if present\"\r\n-download /state.tgz state.tgz\r\necho \"Copy out onetime.tgz if present\"\r\n-download /onetime.tgz onetime.tgz\r\necho\r\n\r\necho \"Build esxi_unpack ESXi host state unpack script\"\r\nupload -<<END /ImageStreamer/esxi_unpack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"Finding ESXi host state configuration archive in Golden Image\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Unpack state.tgz\"\r\n    mkdir $DIR/esxi_state\r\n    cd $DIR/esxi_state\r\n    tar xvpzf $DIR/state.tgz\r\n    echo\r\n    echo \"Unpack local.tgz\"\r\n    mkdir $DIR/esxi_local\r\n    cd $DIR/esxi_local\r\n    tar xvpzf $DIR/esxi_state/local.tgz\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Unpack onetime.tgz\"\r\n    mkdir $DIR/esxi_onetime\r\n    cd $DIR/esxi_onetime\r\n    tar xvpzf $DIR/onetime.tgz\r\n    echo\r\nfi\r\n\r\nif [ -e etc/rc.local.d/local.sh ]; then\r\n    cp etc/rc.local.d/local.sh $DIR/local.sh\r\nfi\r\n\r\necho \"Unpacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_unpack ./esxi_unpack\r\necho\r\n\r\necho \"Build esxi_repack ESXi host state repack script\"\r\nupload -<<END /ImageStreamer/esxi_repack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"---------------------------------------------------------------\"\r\necho \"Final ESXi host local.sh content for configuration at first boot:\"\r\ncat $DIR/local.sh\r\necho \"---------------------------------------------------------------\"\r\necho\r\n\r\necho \"Finding ESXi host state configuration archive\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Repack local.tgz\"\r\n    cd $DIR/esxi_local\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/esxi_state/local.tgz *\r\n    echo\r\n    echo \"Repack state.tgz\"\r\n    cd $DIR/esxi_state\r\n    tar cvpzf $DIR/state.tgz *\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Repack onetime.tgz\"\r\n    cd $DIR/esxi_onetime\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/onetime.tgz *\r\n    touch $DIR/state.tgz\r\n    echo\r\nfi\r\necho \"Repacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_repack ./esxi_repack\r\necho\r\n\r\necho \"Run  esxi_repack ESXi host state unpack script\"\r\n!source ./esxi_unpack\r\necho\r\necho \"########################################\"\r\necho \"Configure ssh\"\r\necho \"########################################\"\r\n\r\nupload -<<END /ImageStreamer/esxi_ssh\r\n#!/bin/bash\r\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\r\ncat <<\"EOF\" >>local.sh\r\nvim-cmd hostsvc/enable_esx_shell\r\nvim-cmd hostsvc/start_esx_shell\r\nvim-cmd hostsvc/enable_ssh\r\nvim-cmd hostsvc/start_ssh\r\nservices.sh restart\r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_ssh esxi_ssh\r\necho \"Run esxi_ssh\"\r\n!source ./esxi_ssh\r\necho \"########################################\"\r\necho \"Pack and replace ESXi host state into ESXi host OS Volume\"\r\necho \"########################################\"\r\n\r\necho \"Run  esxi_repack ESXi host state repack script\"\r\n!source ./esxi_repack\r\n\r\necho \"Copy in state.tgz if present\"\r\n-upload state.tgz /state.tgz \r\necho \"Copy in onetime.tgz if present\"\r\n-upload onetime.tgz /onetime.tgz\r\n\r\necho \"Remove Image Streamer temp directory\"\r\nrm-rf /tmp/ImageStreamer\r\necho \"########################################\"\r\necho \"Cleanup and unmount file systems \"\r\necho \"########################################\"\r\n\r\necho \"Remove ImageStreamer temp directory\"\r\nrm-rf /ImageStreamer\r\n\r\necho \"Unmount file systems\"\r\numount /\r\necho"
}, {
    "type": "PlanScript",
    "description": "duplicate planscript",
    "name": "Planscript_valid_deploy",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "reboot command"
}, {
    "type": "PlanScript",
    "description": "invalid name",
    "name": "*#$%",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "reboot command"
}, {
    "type": "PlanScript",
    "description": "no plan type planscript",
    "name": "Planscript_no_plantype",
    "hpProvided": "false",
    "planType": " ",
    "content": "reboot command"
}, {
    "type": "PlanScript",
    "description": "invalid plan type planscript",
    "name": "Planscript_invalid_plan_type",
    "hpProvided": "false",
    "planType": "&#*",
    "content": "reboot command"
}, {
    "type": "PlanScript",
    "description": "plan script max characters",
    "name": "planscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplans",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "reboot command"
}, {
    "type": "PlanScript",
    "description": "plan script name greater than 255 chars",
    "name": "planscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanssss",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "reboot command"
}, {
    "type": "PlanScript",
    "description": "planscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplansplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplansplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplansplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplansplanscriptplanscript",
    "name": "descmaxcharas",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "reboot command"
}, {
    "type": "PlanScript",
    "description": "planscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplansplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplansplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplansplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplansplanscriptplanscriptss",
    "name": "psdescgreaterthanmaxchars",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "reboot command"
}, {
    "type": "PlanScript",
    "description": "ps for update",
    "name": "ps_for_update",
    "hpProvided": "false",
    "planType": "general",
    "content": "reboot command"
}, {
    "type": "PlanScript",
    "description": "ps for delete",
    "name": "ps_for_delete",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "reboot command"
}, {
    "type": "PlanScript",
    "description": "ps for get",
    "name": "ps_for_get",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "reboot command"
}, {
    "type": "PlanScript",
    "description": "ps for capture",
    "name": "ps_type_capture",
    "hpProvided": "false",
    "planType": "capture",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\r\n# Script to mount disk in libguesfs virtual appliance for personalizaiton or generalization\r\nmount /dev/sda5 /\r\n\r\n\r\n# creating tmp dir at local filesystem\r\n!mkdir -p ./onetime\r\n!mkdir -p ./state/local\r\n\r\n# copying required files for personalization/generalization to local filesysystem\r\n-copy-out /onetime.tgz .\r\n-copy-out /state.tgz .\r\n-copy-out /boot.cfg .\r\n\r\n# trying to findout whether onetime.tgz will be picked up during booting or state.tgz will be picked\r\n# based on that we can process either onetime.tgz or state.tgz for personalization/generalization\r\n\r\n-!grep \"onetime.tgz\"  ./boot.cfg >./onetime_found\r\n-!grep \"state.tgz\" ./boot.cfg > ./state_found\r\necho \"########################################\"\r\necho \"Generalize host configuration\"\r\necho \"########################################\"\r\n\r\necho \"Empty jumpstrt.tgz archive to remove any configuration left over from install\"\r\nrm /jumpstrt.gz\r\ntouch /jumpstrt\r\ncompress-out gzip /jumpstrt ./jumpstrt.gz\r\nrm /jumpstrt\r\nupload ./jumpstrt.gz /jumpstrt.gz\r\n!rm ./jumpstrt.gz\r\necho\r\n\r\necho \"Empty useropts.gz archive to remove special user configuration\"\r\nrm /useropts.gz\r\ntouch /useropts\r\ncompress-out gzip /useropts ./useropts.gz\r\nrm /useropts\r\nupload ./useropts.gz /useropts.gz\r\n!rm ./useropts.gz\r\necho \r\n\r\necho \"Remove state.tgz archive which holds host configuration\"\r\nrm-f /state.tgz\r\necho \r\n\r\necho \"Download boot.cfg\"\r\ndownload /boot.cfg ./boot.cfg\r\necho\r\n\r\necho \"Construct boot.cfg configuration script\"\r\nupload -<<END /boot_cfg_configure\r\n#!/bin/bash\r\n\r\necho\r\necho \"Original boot.cfg:\"\r\ncat boot.cfg\r\necho\r\n\r\ncp boot.cfg boot.cfg.bak\r\n\r\nsed '/^kernelopt=.*installerDiskDumpSlotSize=/ {\r\n         s/\\(kernelopt=\\).*\\(installerDiskDumpSlotSize=[0-9]*\\).*/\\1 \\2/; n }\r\n     /^kernelopt=/ {\r\n         s/.*/kernelopt=/ }\r\n     /^modules=/ {\r\n         s/--- state.tgz/--- onetime.tgz/ }\r\n    ' < boot.cfg.bak > boot.cfg\r\n\r\nrm boot.cfg.bak\r\n\r\necho \"New boot.cfg:\"\r\ncat boot.cfg\r\necho\r\n\r\necho \"Construct ImageStreamerCapture details file\"\r\necho \"HPE Image Streamer Capture for ESXi 5\" > ./ImageStreamerCapture\r\necho \"Complete generalization by host state removal\" >> ./ImageStreamerCapture\r\ndate >> ./ImageStreamerCapture\r\n\r\nexit 0\r\nEND\r\necho \r\n\r\necho \"Run boot.cfg configuration script\"\r\ndownload /boot_cfg_configure ./boot_cfg_configure\r\n!source ./boot_cfg_configure\r\nrm-f /boot_cfg_configure\r\necho\r\n\r\necho \"Replace boot.cfg\"\r\nupload ./boot.cfg /boot.cfg\r\necho\r\n\r\necho \"Save capture details in Golden Image\"\r\nupload  ./ImageStreamerCapture  /ImageStreamerCapture\r\necho\r\n# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\r\n# Script to Unmount\r\n\r\n-copy-in onetime.tgz /\r\n-copy-in state.tgz /\r\numount /"
}, {
    "type": "PlanScript",
    "description": "",
    "name": "HPE - ESXi 5 - mount",
    "hpProvided": "true",
    "planType": "general",
    "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\r\n# Script to mount disk in libguesfs virtual appliance for personalizaiton or generalization\r\nmount /dev/sda5 /\r\n\r\n\r\n# creating tmp dir at local filesystem\r\n!mkdir -p ./onetime\r\n!mkdir -p ./state/local\r\n\r\n# copying required files for personalization/generalization to local filesysystem\r\n-copy-out /onetime.tgz .\r\n-copy-out /state.tgz .\r\n-copy-out /boot.cfg .\r\n\r\n# trying to findout whether onetime.tgz will be picked up during booting or state.tgz will be picked\r\n# based on that we can process either onetime.tgz or state.tgz for personalization/generalization\r\n\r\n-!grep \"onetime.tgz\"  ./boot.cfg >./onetime_found\r\n-!grep \"state.tgz\" ./boot.cfg > ./state_found"
}, {
    "type": "PlanScript",
    "description": "",
    "name": "HPE - ESXi 5 - unpack state",
    "hpProvided": "true",
    "planType": "general",
    "content": "echo \"########################################\"\r\necho \"Copy out and unpack ESXi host state\"\r\necho \"########################################\"\r\n\r\necho \"Create ImageStreamer temp directory\"\r\n-mkdir /ImageStreamer\r\necho\r\n\r\necho \"Extract ESXi host configuration from Golden Image\"\r\necho \"Copy out boot.cfg\"\r\ndownload /boot.cfg boot.cfg\r\necho \"Copy out state.tgz if present\"\r\n-download /state.tgz state.tgz\r\necho \"Copy out onetime.tgz if present\"\r\n-download /onetime.tgz onetime.tgz\r\necho\r\n\r\necho \"Build esxi_unpack ESXi host state unpack script\"\r\nupload -<<END /ImageStreamer/esxi_unpack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"Finding ESXi host state configuration archive in Golden Image\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Unpack state.tgz\"\r\n    mkdir $DIR/esxi_state\r\n    cd $DIR/esxi_state\r\n    tar xvpzf $DIR/state.tgz\r\n    echo\r\n    echo \"Unpack local.tgz\"\r\n    mkdir $DIR/esxi_local\r\n    cd $DIR/esxi_local\r\n    tar xvpzf $DIR/esxi_state/local.tgz\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Unpack onetime.tgz\"\r\n    mkdir $DIR/esxi_onetime\r\n    cd $DIR/esxi_onetime\r\n    tar xvpzf $DIR/onetime.tgz\r\n    echo\r\nfi\r\n\r\nif [ -e etc/rc.local.d/local.sh ]; then\r\n    cp etc/rc.local.d/local.sh $DIR/local.sh\r\nfi\r\n\r\necho \"Unpacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_unpack ./esxi_unpack\r\necho\r\n\r\necho \"Build esxi_repack ESXi host state repack script\"\r\nupload -<<END /ImageStreamer/esxi_repack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"---------------------------------------------------------------\"\r\necho \"Final ESXi host local.sh content for configuration at first boot:\"\r\ncat $DIR/local.sh\r\necho \"---------------------------------------------------------------\"\r\necho\r\n\r\necho \"Finding ESXi host state configuration archive\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Repack local.tgz\"\r\n    cd $DIR/esxi_local\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/esxi_state/local.tgz *\r\n    echo\r\n    echo \"Repack state.tgz\"\r\n    cd $DIR/esxi_state\r\n    tar cvpzf $DIR/state.tgz *\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Repack onetime.tgz\"\r\n    cd $DIR/esxi_onetime\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/onetime.tgz *\r\n    touch $DIR/state.tgz\r\n    echo\r\nfi\r\necho \"Repacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_repack ./esxi_repack\r\necho\r\n\r\necho \"Run  esxi_repack ESXi host state unpack script\"\r\n!source ./esxi_unpack\r\necho"
}, {
    "type": "PlanScript",
    "description": "",
    "name": "HPE - ESXi 5 - configure management 1st NIC",
    "hpProvided": "true",
    "planType": "deploy",
     "content": "echo \"########################################\"\r\necho \"Configure ESXi host management network\"\r\necho \"########################################\"\r\n\r\necho \"Check Image Streamer capture details\"\r\n-download /ImageStreamerCapture ./ImageStreamerCapture\r\n\r\nupload -<<END /ImageStreamer/check_capture\r\n#!/bin/bash\r\nif [ -f ./ImageStreamerCapture ]; then\r\n    echo \"Capture details:\"\r\n    cat ./ImageStreamerCapture\r\nelse\r\n    echo\r\n    echo \"WARNING: ESXi Golden Image was not captured by Image Streamer.\"\r\n    echo \"Golden Image may not be prepared for correct personalization.\"\r\n    echo \"Recommend deploying Golden Image as is and capturing a new\"\r\n    echo \"Golden Image using Image Streamer via correct capture Build Plan\"\r\n    echo\r\nfi\r\necho\r\nEND\r\ndownload /ImageStreamer/check_capture ./check_capture\r\n!source ./check_capture\r\n\r\n-rm-f /ImageStreamerCapture\r\n\r\nupload -<<END /ImageStreamer/esxi_mgmt_net\r\n#! /bin/bash\r\n\r\ncat <<\"EOF\" >>local.sh\r\n# HPE Image Streamer ESXi host configuration\r\nesxcli system syslog mark --message \"HPE Image Streamer ESXi host configuration for @Hostname@\"\r\n\r\n# Image Streamer management network configuration\r\nesxcli system hostname set --host \"@Hostname@\"\r\nesxcli system hostname set --domain \"@DomainName@\"\r\n\r\nVMK1=vmk2\r\nUPLINK1=`esxcli network nic list | grep -i \"@MgmtNIC.mac@\" | awk '{ print $1 }'`\r\n\r\nesxcli network vswitch standard add --vswitch-name=vSwitch1\r\n\r\nesxcli network vswitch standard portgroup add --portgroup-name=ManangementNetwork1 --vswitch-name=vSwitch1\r\n\r\nesxcli network vswitch standard uplink add --uplink-name=$UPLINK1 --vswitch-name=vSwitch1\r\n\r\nesxcli network ip interface add --interface-name=$VMK1 --portgroup-name=ManangementNetwork1\r\n\r\nEOF\r\n\r\nif [[ \"@MgmtNIC.ipaddress@\" =~ [0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]* ]]; then\r\n\r\necho \"Configure ESXi host management network for static IP\"\r\ncat <<\"EOF\" >>local.sh\r\nesxcli network ip interface ipv4 set --interface-name=$VMK1 --ipv4=@MgmtNIC.ipaddress@ --netmask=@MgmtNIC.netmask@ --type=static\r\n\r\nesxcli network ip route ipv4 add --gateway \"@MgmtNIC.gateway@\" --network default\r\nesxcli network ip dns server add --server=@MgmtNIC.dns1@\r\nesxcli network ip dns server add --server=@MgmtNIC.dns2@\r\n\r\nEOF\r\n\r\nelse\r\n\r\necho \"Configure ESXi host management network for DHCP\"\r\ncat <<\"EOF\" >>local.sh\r\nesxcli network ip  interface ipv4 set --interface-name=$VMK1 --type=dhcp   \r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_mgmt_net ./esxi_mgmt_net\r\necho \"Run esxi_mgmt_net\"\r\n!source ./esxi_mgmt_net\r\necho \"Configure host management complete\""
}, {
    "type": "PlanScript",
    "description": "",
    "name": "HPE - ESXi 5 - simple double managment NIC",
    "hpProvided": "true",
    "planType": "deploy",
    "content": "echo \"########################################\"\r\necho \"Configure ESXi host management 2nd NIC\"\r\necho \"########################################\"\r\n\r\nupload -<<END /ImageStreamer/esxi_mgmt_net\r\n#! /bin/bash\r\n\r\necho \"Configure ESXi host management 2nd NIC\"\r\ncat <<\"EOF\" >>local.sh\r\nVMK2=vmk3\r\nUPLINK2=`esxcli network nic list | grep -i \"@MgmtNIC2.mac@\" | awk '{ print $1 }'`\r\n\r\nesxcli network vswitch standard uplink add --uplink-name=$UPLINK2 --vswitch-name=vSwitch1\r\n\r\nesxcli network ip interface add --interface-name=$VMK2 --portgroup-name=ManangementNetwork1\r\n\r\nEOF\r\n\r\nif [[ \"@MgmtNIC2.ipaddress@\" =~ [0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]* ]]; then\r\n\r\necho \"Configure ESXi host management 2nd NIC for static IP\"\r\ncat <<\"EOF\" >>local.sh\r\nesxcli network ip interface ipv4 set --interface-name=$VMK2 --ipv4=@MgmtNIC2.ipaddress@ --netmask=@MgmtNIC2.netmask@ --type=static\r\n\r\nEOF\r\n\r\nelse\r\n\r\necho \"Configure ESXi host management 2nd NIC for DHCP\"\r\ncat <<\"EOF\" >>local.sh\r\nesxcli network ip  interface ipv4 set --interface-name=$VMK2 --type=dhcp   \r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_mgmt_net ./esxi_mgmt_net\r\necho \"Run esxi_mgmt_net\"\r\n!source ./esxi_mgmt_net\r\necho \"Configure host management complete\""
}, {
    "type": "PlanScript",
    "description": "",
    "name": "HPE - ESXi 5 - set password",
    "hpProvided": "true",
    "planType": "deploy",
     "content": "echo \"########################################\"\r\necho \"Configure host password\"\r\necho \"########################################\"\r\n\r\nupload -<<END /ImageStreamer/esxi_password\r\n#! /bin/bash\r\n\r\ncat <<\"EOF\" >>local.sh\r\n# Image Streamer password configuration\r\necho \"@Password@\" | passwd root --stdin\r\n\r\nEOF\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_password esxi_password\r\necho \"Run esxi_password\"\r\n!source /esxi_password\r\necho"
}, {
    "type": "PlanScript",
    "description": "",
    "name": "HPE - ESXi 5 - configure ssh",
    "hpProvided": "true",
    "planType": "deploy",
    "content": "echo \"########################################\"\r\necho \"Configure ssh\"\r\necho \"########################################\"\r\n\r\nupload -<<END /ImageStreamer/esxi_ssh\r\n#!/bin/bash\r\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\r\ncat <<\"EOF\" >>local.sh\r\nvim-cmd hostsvc/enable_esx_shell\r\nvim-cmd hostsvc/start_esx_shell\r\nvim-cmd hostsvc/enable_ssh\r\nvim-cmd hostsvc/start_ssh\r\nservices.sh restart\r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_ssh esxi_ssh\r\necho \"Run esxi_ssh\"\r\n!source /esxi_ssh"
}, {
    "type": "PlanScript",
    "description": "",
    "name": "HPE - ESXi 5 - repack state",
    "hpProvided": "true",
    "planType": "general",
    "content": "echo \"########################################\"\r\necho \"Pack and replace ESXi host state into ESXi host OS Volume\"\r\necho \"########################################\"\r\n\r\necho \"Run  esxi_repack ESXi host state repack script\"\r\n!source /esxi_repack\r\n\r\necho \"Copy in state.tgz if present\"\r\n-upload state.tgz /state.tgz \r\necho \"Copy in onetime.tgz if present\"\r\n-upload onetime.tgz /onetime.tgz\r\n\r\necho \"Remove Image Streamer temp directory\"\r\nrm-rf /tmp/ImageStreamer"
}, {
    "type": "PlanScript",
    "description": "",
    "name": "HPE - ESXi 5 - umount",
    "hpProvided": "true",
    "planType": "general",
    "content": "echo \"########################################\"\r\necho \"Cleanup and unmount file systems \"\r\necho \"########################################\"\r\n\r\necho \"Remove ImageStreamer temp directory\"\r\nrm-rf /ImageStreamer\r\n\r\necho \"Unmount file systems\"\r\numount /\r\necho"
},{
    "type": "PlanScript",
    "type": "PlanScript",
    "description": "",
    "name": "HPE - ESXi 5 - generalize host configuration",
    "hpProvided": "true",
    "planType": "capture",
    "state": "active",
    "content": "echo \"########################################\"\r\necho \"Generalize host configuration\"\r\necho \"########################################\"\r\n\r\necho \"Empty jumpstrt.tgz archive to remove any configuration left over from install\"\r\nrm /jumpstrt.gz\r\ntouch /jumpstrt\r\ncompress-out gzip /jumpstrt /jumpstrt.gz\r\nrm /jumpstrt\r\nupload /jumpstrt.gz /jumpstrt.gz\r\n!rm /jumpstrt.gz\r\necho\r\n\r\necho \"Empty useropts.gz archive to remove special user configuration\"\r\nrm /useropts.gz\r\ntouch /useropts\r\ncompress-out gzip /useropts /useropts.gz\r\nrm /useropts\r\nupload /useropts.gz /useropts.gz\r\n!rm /useropts.gz\r\necho \r\n\r\necho \"Remove state.tgz archive which holds host configuration\"\r\nrm-f /state.tgz\r\necho \r\n\r\necho \"Download boot.cfg\"\r\ndownload /boot.cfg /boot.cfg\r\necho\r\n\r\necho \"Construct boot.cfg configuration script\"\r\nupload -<<END /boot_cfg_configure\r\n#!/bin/bash\r\n\r\necho\r\necho \"Original boot.cfg:\"\r\ncat boot.cfg\r\necho\r\n\r\ncp boot.cfg boot.cfg.bak\r\n\r\nsed '/^kernelopt=.*installerDiskDumpSlotSize=/ {\r\n         s/\\(kernelopt=\\).*\\(installerDiskDumpSlotSize=[0-9]*\\).*/\\1 \\2/; n }\r\n     /^kernelopt=/ {\r\n         s/.*/kernelopt=/ }\r\n     /^modules=/ {\r\n         s/--- state.tgz/--- onetime.tgz/ }\r\n    ' < boot.cfg.bak > boot.cfg\r\n\r\nrm boot.cfg.bak\r\n\r\necho \"New boot.cfg:\"\r\ncat boot.cfg\r\necho\r\n\r\necho \"Construct ImageStreamerCapture details file\"\r\necho \"HPE Image Streamer Capture for ESXi 5\" > /ImageStreamerCapture\r\necho \"Complete generalization by host state removal\" >> /ImageStreamerCapture\r\ndate >> /ImageStreamerCapture\r\n\r\nexit 0\r\nEND\r\necho \r\n\r\necho \"Run boot.cfg configuration script\"\r\ndownload /boot_cfg_configure /boot_cfg_configure\r\n!source /boot_cfg_configure\r\nrm-f /boot_cfg_configure\r\necho\r\n\r\necho \"Replace boot.cfg\"\r\nupload /boot.cfg /boot.cfg\r\necho\r\n\r\necho \"Save capture details in Golden Image\"\r\nupload  /ImageStreamerCapture  /ImageStreamerCapture\r\necho"
}, {
    "type": "PlanScript",
    "description": "",
    "name": "planscript general with ca",
    "hpProvided": "true",
    "planType": "general",
    "content": "echo \"########################################\"\necho \"Configure ssh\"\necho \"########################################\"\n\nupload -<<END /ImageStreamer/esxi_ssh\n#!/bin/bash\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\ncat <<\"EOF\" >>local.sh\nvim-cmd hostsvc/enable_esx_shell\nvim-cmd hostsvc/start_esx_shell\nvim-cmd hostsvc/enable_ssh\nvim-cmd hostsvc/start_ssh\nservices.sh restart\n\nEOF\nfi\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_ssh esxi_ssh\necho \"Run esxi_ssh\"\n!source ./esxi_ssh"
}, {
    "type": "PlanScript",
    "description": "",
    "name": "planscript capture with ca",
    "hpProvided": "true",
    "planType": "capture",
    "content": "echo \"########################################\"\necho \"Configure ssh\"\necho \"########################################\"\n\nupload -<<END /ImageStreamer/esxi_ssh\n#!/bin/bash\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\ncat <<\"EOF\" >>local.sh\nvim-cmd hostsvc/enable_esx_shell\nvim-cmd hostsvc/start_esx_shell\nvim-cmd hostsvc/enable_ssh\nvim-cmd hostsvc/start_ssh\nservices.sh restart\n\nEOF\nfi\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_ssh esxi_ssh\necho \"Run esxi_ssh\"\n!source ./esxi_ssh"
}, {
    "type": "PlanScript",
    "description": "",
    "name": "ps-for-update-of-ca-name",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "echo \"########################################\"\necho \"Configure ESXi host management network\"\necho \"########################################\"\n\necho \"Check Image Streamer capture details\"\n-download /ImageStreamerCapture ./ImageStreamerCapture\n\nupload -<<END /ImageStreamer/check_capture\n#!/bin/bash\nif [ -f ./ImageStreamerCapture ]; then\n    echo \"Capture details:\"\n    cat ./ImageStreamerCapture\nelse\n    echo\n    echo \"WARNING: ESXi Golden Image was not captured by Image Streamer.\"\n    echo \"Golden Image may not be prepared for correct personalization.\"\n    echo \"Recommend deploying Golden Image as is and capturing a new\"\n    echo \"Golden Image using Image Streamer via correct capture Build Plan\"\n    echo\nfi\necho\nEND\ndownload /ImageStreamer/check_capture ./check_capture\n!source ./check_capture\n\n-rm-f /ImageStreamerCapture\n\nupload -<<END /ImageStreamer/esxi_mgmt_net\n#! /bin/bash\n\ncat <<\"EOF\" >>local.sh\n# HPE Image Streamer ESXi host configuration\nesxcli system syslog mark --message \"HPE Image Streamer ESXi host configuration for @Hostname@\"\n\n# Image Streamer management network configuration\nesxcli system hostname set --host \"@Hostname:houston@\"\n\n\nVMK1=vmk2\nUPLINK1=`esxcli network nic list | grep -i \"@MgmtNIC.mac@\" | awk '{ print $1 }'`\n\nesxcli network vswitch standard add --vswitch-name=vSwitch1\n\nesxcli network vswitch standard portgroup add --portgroup-name=ManangementNetwork1 --vswitch-name=vSwitch1\n\nesxcli network vswitch standard uplink add --uplink-name=$UPLINK1 --vswitch-name=vSwitch1\n\nesxcli network ip interface add --interface-name=$VMK1 --portgroup-name=ManangementNetwork1\n\nEOF\n\nif [[ \"@MgmtNIC.ipaddress@\" =~ [0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]* ]]; then\n\necho \"Configure ESXi host management network for static IP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip interface ipv4 set --interface-name=$VMK1 --ipv4=@MgmtNIC.ipaddress@ --netmask=@MgmtNIC.netmask@ --type=static\n\nesxcli network ip route ipv4 add --gateway \"@MgmtNIC.gateway@\" --network default\nesxcli network ip dns server add --server=@MgmtNIC.dns1@\nesxcli network ip dns server add --server=@MgmtNIC.dns2@\n\nEOF\n\nelse\n\necho \"Configure ESXi host management network for DHCP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip  interface ipv4 set --interface-name=$VMK1 --type=dhcp   \n\nEOF\nfi\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_mgmt_net ./esxi_mgmt_net\necho \"Run esxi_mgmt_net\"\n!source ./esxi_mgmt_net\necho \"Configure host management complete\""
}, {
    "type": "PlanScript",
    "description": "ps-for-in-useby-bp",
    "name": "ps-for-in-useby-bp",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "echo \"########################################\"\necho \"Configure ESXi host management network\"\necho \"########################################\"\n\necho \"Check Image Streamer capture details\"\n-download /ImageStreamerCapture ./ImageStreamerCapture\n\nupload -<<END /ImageStreamer/check_capture\n#!/bin/bash\nif [ -f ./ImageStreamerCapture ]; then\n    echo \"Capture details:\"\n    cat ./ImageStreamerCapture\nelse\n    echo\n    echo \"WARNING: ESXi Golden Image was not captured by Image Streamer.\"\n    echo \"Golden Image may not be prepared for correct personalization.\"\n    echo \"Recommend deploying Golden Image as is and capturing a new\"\n    echo \"Golden Image using Image Streamer via correct capture Build Plan\"\n    echo\nfi\necho\nEND\ndownload /ImageStreamer/check_capture ./check_capture\n!source ./check_capture\n\n-rm-f /ImageStreamerCapture\n\nupload -<<END /ImageStreamer/esxi_mgmt_net\n#! /bin/bash\n\ncat <<\"EOF\" >>local.sh\n# HPE Image Streamer ESXi host configuration\nesxcli system syslog mark --message \"HPE Image Streamer ESXi host configuration for @Hostname@\"\n\n# Image Streamer management network configuration\nesxcli system hostname set --host \"@Hostname:houston@\"\nesxcli system welcomemsg set --message \"@Message:Welcome@\"\n\nVMK1=vmk2\nUPLINK1=`esxcli network nic list | grep -i \"@MgmtNIC.mac@\" | awk '{ print $1 }'`\n\nesxcli network vswitch standard add --vswitch-name=vSwitch1\n\nesxcli network vswitch standard portgroup add --portgroup-name=ManangementNetwork1 --vswitch-name=vSwitch1\n\nesxcli network vswitch standard uplink add --uplink-name=$UPLINK1 --vswitch-name=vSwitch1\n\nesxcli network ip interface add --interface-name=$VMK1 --portgroup-name=ManangementNetwork1\n\nEOF\n\nif [[ \"@MgmtNIC.ipaddress@\" =~ [0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]* ]]; then\n\necho \"Configure ESXi host management network for static IP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip interface ipv4 set --interface-name=$VMK1 --ipv4=@MgmtNIC.ipaddress@ --netmask=@MgmtNIC.netmask@ --type=static\n\nesxcli network ip route ipv4 add --gateway \"@MgmtNIC.gateway@\" --network default\nesxcli network ip dns server add --server=@MgmtNIC.dns1@\nesxcli network ip dns server add --server=@MgmtNIC.dns2@\n\nEOF\n\nelse\n\necho \"Configure ESXi host management network for DHCP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip  interface ipv4 set --interface-name=$VMK1 --type=dhcp   \n\nEOF\nfi\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_mgmt_net ./esxi_mgmt_net\necho \"Run esxi_mgmt_net\"\n!source ./esxi_mgmt_net\necho \"Configure host management complete\""
}, {
    "type": "PlanScript",
    "description": "ps in use by sp",
    "name": "ps-in-use-by-sp-name-change",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "# Mount /bootbank area for ESXi 5.5+ \r\n#\r\n# Typical partition layout is:\r\n# 1 - UEFI ESP\r\n# 5 - /bootbank  <= holds ESXi host state to be configured\r\n# 6 - /altbootbank\r\n\r\necho \"########################################\"\r\necho \"Mount ESXi /bootbank\"\r\necho \"########################################\"\r\n\r\n# List structure storage layout found in ESXi Golden Image / OS Volume\r\necho \"Devices:\"\r\n-list-devices\r\necho\r\necho \"Partitions:\"\r\n-list-partitions\r\necho\r\necho \"File systems:\"\r\n-list-filesystems\r\necho\r\n\r\necho \"Mount file systems:\"\r\necho \"/dev/sda5 is assumed to hold ESXi host state configuration\"\r\necho \"mount /dev/sda5\"\r\nmount /dev/sda5 /\r\necho \"File system details for /dev/sda5:\"\r\n-statvfs /\r\necho\r\necho \"########################################\"\r\necho \"Copy out and unpack ESXi host state\"\r\necho \"########################################\"\r\n\r\necho \"Create ImageStreamer temp directory\"\r\n-mkdir /ImageStreamer\r\necho\r\n\r\necho \"Extract ESXi host configuration from Golden Image\"\r\necho \"Copy out boot.cfg\"\r\ndownload /boot.cfg boot.cfg\r\necho \"Copy out state.tgz if present\"\r\n-download /state.tgz state.tgz\r\necho \"Copy out onetime.tgz if present\"\r\n-download /onetime.tgz onetime.tgz\r\necho\r\n\r\necho \"Build esxi_unpack ESXi host state unpack script\"\r\nupload -<<END /ImageStreamer/esxi_unpack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"Finding ESXi host state configuration archive in Golden Image\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Unpack state.tgz\"\r\n    mkdir $DIR/esxi_state\r\n    cd $DIR/esxi_state\r\n    tar xvpzf $DIR/state.tgz\r\n    echo\r\n    echo \"Unpack local.tgz\"\r\n    mkdir $DIR/esxi_local\r\n    cd $DIR/esxi_local\r\n    tar xvpzf $DIR/esxi_state/local.tgz\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Unpack onetime.tgz\"\r\n    mkdir $DIR/esxi_onetime\r\n    cd $DIR/esxi_onetime\r\n    tar xvpzf $DIR/onetime.tgz\r\n    echo\r\nfi\r\n\r\nif [ -e etc/rc.local.d/local.sh ]; then\r\n    cp etc/rc.local.d/local.sh $DIR/local.sh\r\nfi\r\n\r\necho \"Unpacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_unpack ./esxi_unpack\r\necho\r\n\r\necho \"Build esxi_repack ESXi host state repack script\"\r\nupload -<<END /ImageStreamer/esxi_repack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"---------------------------------------------------------------\"\r\necho \"Final ESXi host local.sh content for configuration at first boot:\"\r\ncat $DIR/local.sh\r\necho \"---------------------------------------------------------------\"\r\necho\r\n\r\necho \"Finding ESXi host state configuration archive\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Repack local.tgz\"\r\n    cd $DIR/esxi_local\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/esxi_state/local.tgz *\r\n    echo\r\n    echo \"Repack state.tgz\"\r\n    cd $DIR/esxi_state\r\n    tar cvpzf $DIR/state.tgz *\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Repack onetime.tgz\"\r\n    cd $DIR/esxi_onetime\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/onetime.tgz *\r\n    touch $DIR/state.tgz\r\n    echo\r\nfi\r\necho \"Repacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_repack ./esxi_repack\r\necho\r\n\r\necho \"Run  esxi_repack ESXi host state unpack script\"\r\n!source ./esxi_unpack\r\necho\r\necho \"########################################\"\r\necho \"Configure ssh\"\r\necho \"########################################\"\r\n\r\nupload -<<END /ImageStreamer/esxi_ssh\r\n#!/bin/bash\r\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\r\ncat <<\"EOF\" >>local.sh\r\nvim-cmd hostsvc/enable_esx_shell\r\nvim-cmd hostsvc/start_esx_shell\r\nvim-cmd hostsvc/enable_ssh\r\nvim-cmd hostsvc/start_ssh\r\nservices.sh restart\r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_ssh esxi_ssh\r\necho \"Run esxi_ssh\"\r\n!source ./esxi_ssh\r\necho \"########################################\"\r\necho \"Pack and replace ESXi host state into ESXi host OS Volume\"\r\necho \"########################################\"\r\n\r\necho \"Run  esxi_repack ESXi host state repack script\"\r\n!source ./esxi_repack\r\n\r\necho \"Copy in state.tgz if present\"\r\n-upload state.tgz /state.tgz \r\necho \"Copy in onetime.tgz if present\"\r\n-upload onetime.tgz /onetime.tgz\r\n\r\necho \"Remove Image Streamer temp directory\"\r\nrm-rf /tmp/ImageStreamer\r\necho \"########################################\"\r\necho \"Cleanup and unmount file systems \"\r\necho \"########################################\"\r\n\r\necho \"Remove ImageStreamer temp directory\"\r\nrm-rf /ImageStreamer\r\n\r\necho \"Unmount file systems\"\r\numount /\r\necho"
},{
    "type": "PlanScript",
    "description": "plan script to update with name max characters",
    "name": "plan script to update with name max characters",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "reboot command"
}, {
    "type": "PlanScript",
    "description": "plan script to update description max chars",
    "name": "ps to update with max description",
    "hpProvided": "false",
    "planType": "deploy",
    "content": "reboot command"
}, {
    "type": "PlanScript",
    "description": "valid planscript1 for get call",
    "name": "CL RHEL API_GET",
    "hpProvided": "false",
    "planType": "deploy",
    "content":"reboot command"
}, {
    "type": "PlanScript",
    "description": "valid planscript2 for get call",
    "name": "cl artifact_for_GET",
    "hpProvided": "false",
    "planType": "deploy",
    "content":"reboot command"
}, {
    "type": "PlanScript",
    "description": "valid planscript3 for get call",
    "name": "RHEL-7.2-planscript",
    "hpProvided": "false",
    "planType": "deploy",
    "content":"reboot command"
}, {
    "type": "PlanScript",
    "description": "valid planscript4 for get call",
    "name": "123_planscript",
    "hpProvided": "false",
    "planType": "deploy",
    "content":"reboot command"
}, {
    "type": "PlanScript",
    "description": "valid planscript5 for get call",
    "name": "planscript_456",
    "hpProvided": "false",
    "planType": "deploy",
    "content":"reboot command"
}]

planscript_update = [

    {  # Updating planscript content
            "type": "PlanScript",
            "description": "ps for update",
            "name": "ps_for_update",
            "hpProvided": "false",
            "planType": "deploy",
            "content": "updated content"
    }, {  #  Updating planscript hpProvided field
            "type": "PlanScript",
            "description": "Name field valid",
            "name": "EsxiPlanScript",
            "hpProvided": "true",
            "planType": "deploy",
            "content": "# Mount /bootbank area for ESXi 5.5+ \r\n#\r\n# Typical partition layout is:\r\n# 1 - UEFI ESP\r\n# 5 - /bootbank  <= holds ESXi host state to be configured\r\n# 6 - /altbootbank\r\n\r\necho \"########################################\"\r\necho \"Mount ESXi /bootbank\"\r\necho \"########################################\"\r\n\r\n# List structure storage layout found in ESXi Golden Image / OS Volume\r\necho \"Devices:\"\r\n-list-devices\r\necho\r\necho \"Partitions:\"\r\n-list-partitions\r\necho\r\necho \"File systems:\"\r\n-list-filesystems\r\necho\r\n\r\necho \"Mount file systems:\"\r\necho \"/dev/sda5 is assumed to hold ESXi host state configuration\"\r\necho \"mount /dev/sda5\"\r\nmount /dev/sda5 /\r\necho \"File system details for /dev/sda5:\"\r\n-statvfs /\r\necho\r\necho \"########################################\"\r\necho \"Copy out and unpack ESXi host state\"\r\necho \"########################################\"\r\n\r\necho \"Create ImageStreamer temp directory\"\r\n-mkdir /ImageStreamer\r\necho\r\n\r\necho \"Extract ESXi host configuration from Golden Image\"\r\necho \"Copy out boot.cfg\"\r\ndownload /boot.cfg boot.cfg\r\necho \"Copy out state.tgz if present\"\r\n-download /state.tgz state.tgz\r\necho \"Copy out onetime.tgz if present\"\r\n-download /onetime.tgz onetime.tgz\r\necho\r\n\r\necho \"Build esxi_unpack ESXi host state unpack script\"\r\nupload -<<END /ImageStreamer/esxi_unpack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"Finding ESXi host state configuration archive in Golden Image\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Unpack state.tgz\"\r\n    mkdir $DIR/esxi_state\r\n    cd $DIR/esxi_state\r\n    tar xvpzf $DIR/state.tgz\r\n    echo\r\n    echo \"Unpack local.tgz\"\r\n    mkdir $DIR/esxi_local\r\n    cd $DIR/esxi_local\r\n    tar xvpzf $DIR/esxi_state/local.tgz\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Unpack onetime.tgz\"\r\n    mkdir $DIR/esxi_onetime\r\n    cd $DIR/esxi_onetime\r\n    tar xvpzf $DIR/onetime.tgz\r\n    echo\r\nfi\r\n\r\nif [ -e etc/rc.local.d/local.sh ]; then\r\n    cp etc/rc.local.d/local.sh $DIR/local.sh\r\nfi\r\n\r\necho \"Unpacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_unpack ./esxi_unpack\r\necho\r\n\r\necho \"Build esxi_repack ESXi host state repack script\"\r\nupload -<<END /ImageStreamer/esxi_repack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"---------------------------------------------------------------\"\r\necho \"Final ESXi host local.sh content for configuration at first boot:\"\r\ncat $DIR/local.sh\r\necho \"---------------------------------------------------------------\"\r\necho\r\n\r\necho \"Finding ESXi host state configuration archive\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Repack local.tgz\"\r\n    cd $DIR/esxi_local\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/esxi_state/local.tgz *\r\n    echo\r\n    echo \"Repack state.tgz\"\r\n    cd $DIR/esxi_state\r\n    tar cvpzf $DIR/state.tgz *\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Repack onetime.tgz\"\r\n    cd $DIR/esxi_onetime\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/onetime.tgz *\r\n    touch $DIR/state.tgz\r\n    echo\r\nfi\r\necho \"Repacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_repack ./esxi_repack\r\necho\r\n\r\necho \"Run  esxi_repack ESXi host state unpack script\"\r\n!source ./esxi_unpack\r\necho\r\necho \"########################################\"\r\necho \"Configure ssh\"\r\necho \"########################################\"\r\n\r\nupload -<<END /ImageStreamer/esxi_ssh\r\n#!/bin/bash\r\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\r\ncat <<\"EOF\" >>local.sh\r\nvim-cmd hostsvc/enable_esx_shell\r\nvim-cmd hostsvc/start_esx_shell\r\nvim-cmd hostsvc/enable_ssh\r\nvim-cmd hostsvc/start_ssh\r\nservices.sh restart\r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_ssh esxi_ssh\r\necho \"Run esxi_ssh\"\r\n!source ./esxi_ssh\r\necho \"########################################\"\r\necho \"Pack and replace ESXi host state into ESXi host OS Volume\"\r\necho \"########################################\"\r\n\r\necho \"Run  esxi_repack ESXi host state repack script\"\r\n!source ./esxi_repack\r\n\r\necho \"Copy in state.tgz if present\"\r\n-upload state.tgz /state.tgz \r\necho \"Copy in onetime.tgz if present\"\r\n-upload onetime.tgz /onetime.tgz\r\n\r\necho \"Remove Image Streamer temp directory\"\r\nrm-rf /tmp/ImageStreamer\r\necho \"########################################\"\r\necho \"Cleanup and unmount file systems \"\r\necho \"########################################\"\r\n\r\necho \"Remove ImageStreamer temp directory\"\r\nrm-rf /ImageStreamer\r\n\r\necho \"Unmount file systems\"\r\numount /\r\necho"
    }, {  #  Updating planscript planType
            "type": "PlanScript",
            "description": "ps for update",
            "name": "ps_for_update",
            "hpProvided": "false",
            "planType": "capture",
            "content": "updated plantype"
    }, {  #  Updating planscript description
            "type": "PlanScript",
            "description": "updated description",
            "name": "ps_for_update",
            "hpProvided": "false",
            "planType": "capture",
            "content": "updated plantype"
    }, {  #  Updating planscript name
            "type": "PlanScript",
            "description": "Name field valid",
            "name": "EsxiPlanScript_name_updated",
            "hpProvided": "true",
            "planType": "deploy",
            "content": "# Mount /bootbank area for ESXi 5.5+ \r\n#\r\n# Typical partition layout is:\r\n# 1 - UEFI ESP\r\n# 5 - /bootbank  <= holds ESXi host state to be configured\r\n# 6 - /altbootbank\r\n\r\necho \"########################################\"\r\necho \"Mount ESXi /bootbank\"\r\necho \"########################################\"\r\n\r\n# List structure storage layout found in ESXi Golden Image / OS Volume\r\necho \"Devices:\"\r\n-list-devices\r\necho\r\necho \"Partitions:\"\r\n-list-partitions\r\necho\r\necho \"File systems:\"\r\n-list-filesystems\r\necho\r\n\r\necho \"Mount file systems:\"\r\necho \"/dev/sda5 is assumed to hold ESXi host state configuration\"\r\necho \"mount /dev/sda5\"\r\nmount /dev/sda5 /\r\necho \"File system details for /dev/sda5:\"\r\n-statvfs /\r\necho\r\necho \"########################################\"\r\necho \"Copy out and unpack ESXi host state\"\r\necho \"########################################\"\r\n\r\necho \"Create ImageStreamer temp directory\"\r\n-mkdir /ImageStreamer\r\necho\r\n\r\necho \"Extract ESXi host configuration from Golden Image\"\r\necho \"Copy out boot.cfg\"\r\ndownload /boot.cfg boot.cfg\r\necho \"Copy out state.tgz if present\"\r\n-download /state.tgz state.tgz\r\necho \"Copy out onetime.tgz if present\"\r\n-download /onetime.tgz onetime.tgz\r\necho\r\n\r\necho \"Build esxi_unpack ESXi host state unpack script\"\r\nupload -<<END /ImageStreamer/esxi_unpack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"Finding ESXi host state configuration archive in Golden Image\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Unpack state.tgz\"\r\n    mkdir $DIR/esxi_state\r\n    cd $DIR/esxi_state\r\n    tar xvpzf $DIR/state.tgz\r\n    echo\r\n    echo \"Unpack local.tgz\"\r\n    mkdir $DIR/esxi_local\r\n    cd $DIR/esxi_local\r\n    tar xvpzf $DIR/esxi_state/local.tgz\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Unpack onetime.tgz\"\r\n    mkdir $DIR/esxi_onetime\r\n    cd $DIR/esxi_onetime\r\n    tar xvpzf $DIR/onetime.tgz\r\n    echo\r\nfi\r\n\r\nif [ -e etc/rc.local.d/local.sh ]; then\r\n    cp etc/rc.local.d/local.sh $DIR/local.sh\r\nfi\r\n\r\necho \"Unpacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_unpack ./esxi_unpack\r\necho\r\n\r\necho \"Build esxi_repack ESXi host state repack script\"\r\nupload -<<END /ImageStreamer/esxi_repack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"---------------------------------------------------------------\"\r\necho \"Final ESXi host local.sh content for configuration at first boot:\"\r\ncat $DIR/local.sh\r\necho \"---------------------------------------------------------------\"\r\necho\r\n\r\necho \"Finding ESXi host state configuration archive\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Repack local.tgz\"\r\n    cd $DIR/esxi_local\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/esxi_state/local.tgz *\r\n    echo\r\n    echo \"Repack state.tgz\"\r\n    cd $DIR/esxi_state\r\n    tar cvpzf $DIR/state.tgz *\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Repack onetime.tgz\"\r\n    cd $DIR/esxi_onetime\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/onetime.tgz *\r\n    touch $DIR/state.tgz\r\n    echo\r\nfi\r\necho \"Repacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_repack ./esxi_repack\r\necho\r\n\r\necho \"Run  esxi_repack ESXi host state unpack script\"\r\n!source ./esxi_unpack\r\necho\r\necho \"########################################\"\r\necho \"Configure ssh\"\r\necho \"########################################\"\r\n\r\nupload -<<END /ImageStreamer/esxi_ssh\r\n#!/bin/bash\r\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\r\ncat <<\"EOF\" >>local.sh\r\nvim-cmd hostsvc/enable_esx_shell\r\nvim-cmd hostsvc/start_esx_shell\r\nvim-cmd hostsvc/enable_ssh\r\nvim-cmd hostsvc/start_ssh\r\nservices.sh restart\r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_ssh esxi_ssh\r\necho \"Run esxi_ssh\"\r\n!source ./esxi_ssh\r\necho \"########################################\"\r\necho \"Pack and replace ESXi host state into ESXi host OS Volume\"\r\necho \"########################################\"\r\n\r\necho \"Run  esxi_repack ESXi host state repack script\"\r\n!source ./esxi_repack\r\n\r\necho \"Copy in state.tgz if present\"\r\n-upload state.tgz /state.tgz \r\necho \"Copy in onetime.tgz if present\"\r\n-upload onetime.tgz /onetime.tgz\r\n\r\necho \"Remove Image Streamer temp directory\"\r\nrm-rf /tmp/ImageStreamer\r\necho \"########################################\"\r\necho \"Cleanup and unmount file systems \"\r\necho \"########################################\"\r\n\r\necho \"Remove ImageStreamer temp directory\"\r\nrm-rf /ImageStreamer\r\n\r\necho \"Unmount file systems\"\r\numount /\r\necho"
    },  {  #  Updating planscript ca value
            "type": "PlanScript",
            "description": "",
            "name": "ps-for-update-of-ca-name",
            "hpProvided": "false",
            "planType": "deploy",
            "content": "echo \"########################################\"\necho \"Configure ESXi host management network\"\necho \"########################################\"\n\necho \"Check Image Streamer capture details\"\n-download /ImageStreamerCapture ./ImageStreamerCapture\n\nupload -<<END /ImageStreamer/check_capture\n#!/bin/bash\nif [ -f ./ImageStreamerCapture ]; then\n    echo \"Capture details:\"\n    cat ./ImageStreamerCapture\nelse\n    echo\n    echo \"WARNING: ESXi Golden Image was not captured by Image Streamer.\"\n    echo \"Golden Image may not be prepared for correct personalization.\"\n    echo \"Recommend deploying Golden Image as is and capturing a new\"\n    echo \"Golden Image using Image Streamer via correct capture Build Plan\"\n    echo\nfi\necho\nEND\ndownload /ImageStreamer/check_capture ./check_capture\n!source ./check_capture\n\n-rm-f /ImageStreamerCapture\n\nupload -<<END /ImageStreamer/esxi_mgmt_net\n#! /bin/bash\n\ncat <<\"EOF\" >>local.sh\n# HPE Image Streamer ESXi host configuration\nesxcli system syslog mark --message \"HPE Image Streamer ESXi host configuration for @Hostname@\"\n\n# Image Streamer management network configuration\nesxcli system hostname set --host \"@Hostname:houston@\"\n\n\nVMK1=vmk2\nUPLINK1=`esxcli network nic list | grep -i \"@MgmtNIC.mac@\" | awk '{ print $1 }'`\n\nesxcli network vswitch standard add --vswitch-name=vSwitch1\n\nesxcli network vswitch standard portgroup add --portgroup-name=ManangementNetwork1 --vswitch-name=vSwitch1\n\nesxcli network vswitch standard uplink add --uplink-name=$UPLINK1 --vswitch-name=vSwitch1\n\nesxcli network ip interface add --interface-name=$VMK1 --portgroup-name=ManangementNetwork1\n\nEOF\n\nif [[ \"@MgmtNIC.ipaddress@\" =~ [0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]* ]]; then\n\necho \"Configure ESXi host management network for static IP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip interface ipv4 set --interface-name=$VMK1 --ipv4=@MgmtNIC.ipaddress@ --netmask=@MgmtNIC.netmask@ --type=static\n\nesxcli network ip route ipv4 add --gateway \"@MgmtNIC.gateway@\" --network default\nesxcli network ip dns server add --server=@MgmtNIC.dns1@\nesxcli network ip dns server add --server=@MgmtNIC.dns2@\n\nEOF\n\nelse\n\necho \"Configure ESXi host management network for DHCP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip  interface ipv4 set --interface-name=$VMK1 --type=dhcp   \n\nEOF\nfi\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_mgmt_net ./esxi_mgmt_net\necho \"Run esxi_mgmt_net\"\n!source ./esxi_mgmt_net\necho \"Configure host management complete\""
},      {   #  Updating planscript ca name, value
            "type": "PlanScript",
            "description": "",
            "name": "ps-for-update-of-ca-name",
            "hpProvided": "false",
            "planType": "deploy",
            "content": "echo \"########################################\"\necho \"Configure ESXi host management network\"\necho \"########################################\"\n\necho \"Check Image Streamer capture details\"\n-download /ImageStreamerCapture ./ImageStreamerCapture\n\nupload -<<END /ImageStreamer/check_capture\n#!/bin/bash\nif [ -f ./ImageStreamerCapture ]; then\n    echo \"Capture details:\"\n    cat ./ImageStreamerCapture\nelse\n    echo\n    echo \"WARNING: ESXi Golden Image was not captured by Image Streamer.\"\n    echo \"Golden Image may not be prepared for correct personalization.\"\n    echo \"Recommend deploying Golden Image as is and capturing a new\"\n    echo \"Golden Image using Image Streamer via correct capture Build Plan\"\n    echo\nfi\necho\nEND\ndownload /ImageStreamer/check_capture ./check_capture\n!source ./check_capture\n\n-rm-f /ImageStreamerCapture\n\nupload -<<END /ImageStreamer/esxi_mgmt_net\n#! /bin/bash\n\ncat <<\"EOF\" >>local.sh\n# HPE Image Streamer ESXi host configuration\nesxcli system syslog mark --message \"HPE Image Streamer ESXi host configuration for @Hostname@\"\n\n# Image Streamer management network configuration\nesxcli system hostname set --host \"@Hostname:houston@\"\nesxcli system welcomemsg set --message \"@Message:Welcome@\"\n\nVMK1=vmk2\nUPLINK1=`esxcli network nic list | grep -i \"@MgmtNIC.mac@\" | awk '{ print $1 }'`\n\nesxcli network vswitch standard add --vswitch-name=vSwitch1\n\nesxcli network vswitch standard portgroup add --portgroup-name=ManangementNetwork1 --vswitch-name=vSwitch1\n\nesxcli network vswitch standard uplink add --uplink-name=$UPLINK1 --vswitch-name=vSwitch1\n\nesxcli network ip interface add --interface-name=$VMK1 --portgroup-name=ManangementNetwork1\n\nEOF\n\nif [[ \"@MgmtNIC.ipaddress@\" =~ [0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]* ]]; then\n\necho \"Configure ESXi host management network for static IP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip interface ipv4 set --interface-name=$VMK1 --ipv4=@MgmtNIC.ipaddress@ --netmask=@MgmtNIC.netmask@ --type=static\n\nesxcli network ip route ipv4 add --gateway \"@MgmtNIC.gateway@\" --network default\nesxcli network ip dns server add --server=@MgmtNIC.dns1@\nesxcli network ip dns server add --server=@MgmtNIC.dns2@\n\nEOF\n\nelse\n\necho \"Configure ESXi host management network for DHCP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip  interface ipv4 set --interface-name=$VMK1 --type=dhcp   \n\nEOF\nfi\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_mgmt_net ./esxi_mgmt_net\necho \"Run esxi_mgmt_net\"\n!source ./esxi_mgmt_net\necho \"Configure host management complete\""
},      {   #  Updating read-only planscript name
            "type": "PlanScript",
            "description": "",
            "name": "HPE - ESXi 5 - mount",
            "hpProvided": "true",
            "planType": "general",
            "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\r\n# Script to mount disk in libguesfs virtual appliance for personalizaiton or generalization\r\nmount /dev/sda5 /\r\n\r\n\r\n# creating tmp dir at local filesystem\r\n!mkdir -p ./onetime\r\n!mkdir -p ./state/local\r\n\r\n# copying required files for personalization/generalization to local filesysystem\r\n-copy-out /onetime.tgz .\r\n-copy-out /state.tgz .\r\n-copy-out /boot.cfg .\r\n\r\n# trying to findout whether onetime.tgz will be picked up during booting or state.tgz will be picked\r\n# based on that we can process either onetime.tgz or state.tgz for personalization/generalization\r\n\r\n-!grep \"onetime.tgz\"  ./boot.cfg >./onetime_found\r\n-!grep \"state.tgz\" ./boot.cfg > ./state_found"
},     {  #  Updating planscript ca value in-use by serverprofile
            "type": "PlanScript",
            "description": "ps in use by sp",
            "name": "ps-in-use-by-sp",
            "hpProvided": "false",
            "planType": "deploy",
            "content": "# Mount /bootbank area for ESXi 5.5+ \r\n#\r\n# Typical partition layout is:\r\n# 1 - UEFI ESP\r\n# 5 - /bootbank  <= holds ESXi host state to be configured\r\n# 6 - /altbootbank\r\n\r\necho \"########################################\"\r\necho \"Mount ESXi /bootbank\"\r\necho \"########################################\"\r\n\r\n# List structure storage layout found in ESXi Golden Image / OS Volume\r\necho \"Devices:\"\r\n-list-devices\r\necho\r\necho \"Partitions:\"\r\n-list-partitions\r\necho\r\necho \"File systems:\"\r\n-list-filesystems\r\necho\r\n\r\necho \"Mount file systems:\"\r\necho \"/dev/sda5 is assumed to hold ESXi host state configuration\"\r\necho \"mount /dev/sda5\"\r\nmount /dev/sda5 /\r\necho \"File system details for /dev/sda5:\"\r\n-statvfs /\r\necho\r\necho \"########################################\"\r\necho \"Copy out and unpack ESXi host state\"\r\necho \"########################################\"\r\n\r\necho \"Create ImageStreamer temp directory\"\r\n-mkdir /ImageStreamer\r\necho\r\n\r\necho \"Extract ESXi host configuration from Golden Image\"\r\necho \"Copy out boot.cfg\"\r\ndownload /boot.cfg boot.cfg\r\necho \"Copy out state.tgz if present\"\r\n-download /state.tgz state.tgz\r\necho \"Copy out onetime.tgz if present\"\r\n-download /onetime.tgz onetime.tgz\r\necho\r\n\r\necho \"Build esxi_unpack ESXi host state unpack script\"\r\nupload -<<END /ImageStreamer/esxi_unpack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"Finding ESXi host state configuration archive in Golden Image\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Unpack state.tgz\"\r\n    mkdir $DIR/esxi_state\r\n    cd $DIR/esxi_state\r\n    tar xvpzf $DIR/state.tgz\r\n    echo\r\n    echo \"Unpack local.tgz\"\r\n    mkdir $DIR/esxi_local\r\n    cd $DIR/esxi_local\r\n    tar xvpzf $DIR/esxi_state/local.tgz\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Unpack onetime.tgz\"\r\n    mkdir $DIR/esxi_onetime\r\n    cd $DIR/esxi_onetime\r\n    tar xvpzf $DIR/onetime.tgz\r\n    echo\r\nfi\r\n\r\nif [ -e etc/rc.local.d/local.sh ]; then\r\n    cp etc/rc.local.d/local.sh $DIR/local.sh\r\nfi\r\n\r\necho \"Unpacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_unpack ./esxi_unpack\r\necho\r\n\r\necho \"Build esxi_repack ESXi host state repack script\"\r\nupload -<<END /ImageStreamer/esxi_repack\r\n#! /bin/bash\r\nDIR=`pwd`\r\n\r\necho \"---------------------------------------------------------------\"\r\necho \"Final ESXi host local.sh content for configuration at first boot:\"\r\ncat $DIR/local.sh\r\necho \"---------------------------------------------------------------\"\r\necho\r\n\r\necho \"Finding ESXi host state configuration archive\"\r\nSTATE=`grep -c onetime.tgz $DIR/boot.cfg`\r\nif [ \"$STATE\" -eq \"0\" ]; then\r\n    echo\r\n    echo \"Repack local.tgz\"\r\n    cd $DIR/esxi_local\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/esxi_state/local.tgz *\r\n    echo\r\n    echo \"Repack state.tgz\"\r\n    cd $DIR/esxi_state\r\n    tar cvpzf $DIR/state.tgz *\r\n    echo\r\nelse\r\n    echo\r\n    echo \"Repack onetime.tgz\"\r\n    cd $DIR/esxi_onetime\r\n    mkdir -p etc/rc.local.d\r\n    cp $DIR/local.sh etc/rc.local.d/local.sh\r\n    chmod 777 etc/rc.local.d/local.sh\r\n    tar cvpzf $DIR/onetime.tgz *\r\n    touch $DIR/state.tgz\r\n    echo\r\nfi\r\necho \"Repacking ESXi host state complete.\"\r\nexit 0\r\nEND\r\ndownload /ImageStreamer/esxi_repack ./esxi_repack\r\necho\r\n\r\necho \"Run  esxi_repack ESXi host state unpack script\"\r\n!source ./esxi_unpack\r\necho\r\necho \"########################################\"\r\necho \"Configure ssh\"\r\necho \"########################################\"\r\n\r\nupload -<<END /ImageStreamer/esxi_ssh\r\n#!/bin/bash\r\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\r\ncat <<\"EOF\" >>local.sh\r\nvim-cmd hostsvc/enable_esx_shell\r\nvim-cmd hostsvc/start_esx_shell\r\nvim-cmd hostsvc/enable_ssh\r\nvim-cmd hostsvc/start_ssh\r\nservices.sh restart\r\n\r\nEOF\r\nfi\r\n\r\nexit 0\r\nEND\r\n\r\ndownload /ImageStreamer/esxi_ssh esxi_ssh\r\necho \"Run esxi_ssh\"\r\n!source ./esxi_ssh\r\necho \"########################################\"\r\necho \"Pack and replace ESXi host state into ESXi host OS Volume\"\r\necho \"########################################\"\r\n\r\necho \"Run  esxi_repack ESXi host state repack script\"\r\n!source ./esxi_repack\r\n\r\necho \"Copy in state.tgz if present\"\r\n-upload state.tgz /state.tgz \r\necho \"Copy in onetime.tgz if present\"\r\n-upload onetime.tgz /onetime.tgz\r\n\r\necho \"Remove Image Streamer temp directory\"\r\nrm-rf /tmp/ImageStreamer\r\necho \"########################################\"\r\necho \"Cleanup and unmount file systems \"\r\necho \"########################################\"\r\n\r\necho \"Remove ImageStreamer temp directory\"\r\nrm-rf /ImageStreamer\r\n\r\necho \"Unmount file systems\"\r\numount /\r\necho"
}, {      #  Updating planscript ca value in-use by build plan
            "type": "PlanScript",
            "description": "ps-for-in-useby-bp",
            "name": "ps-for-in-useby-BP",
            "hpProvided": "false",
            "planType": "deploy",
            "content": "echo \"########################################\"\necho \"Configure ESXi host management network\"\necho \"########################################\"\n\necho \"Check Image Streamer capture details\"\n-download /ImageStreamerCapture ./ImageStreamerCapture\n\nupload -<<END /ImageStreamer/check_capture\n#!/bin/bash\nif [ -f ./ImageStreamerCapture ]; then\n    echo \"Capture details:\"\n    cat ./ImageStreamerCapture\nelse\n    echo\n    echo \"WARNING: ESXi Golden Image was not captured by Image Streamer.\"\n    echo \"Golden Image may not be prepared for correct personalization.\"\n    echo \"Recommend deploying Golden Image as is and capturing a new\"\n    echo \"Golden Image using Image Streamer via correct capture Build Plan\"\n    echo\nfi\necho\nEND\ndownload /ImageStreamer/check_capture ./check_capture\n!source ./check_capture\n\n-rm-f /ImageStreamerCapture\n\nupload -<<END /ImageStreamer/esxi_mgmt_net\n#! /bin/bash\n\ncat <<\"EOF\" >>local.sh\n# HPE Image Streamer ESXi host configuration\nesxcli system syslog mark --message \"HPE Image Streamer ESXi host configuration for @Hostname@\"\n\n# Image Streamer management network configuration\nesxcli system hostname set --host \"@Hostname:houston123@\"\nesxcli system welcomemsg set --message \"@Message:Welcome@\"\n\nVMK1=vmk2\nUPLINK1=`esxcli network nic list | grep -i \"@MgmtNIC.mac@\" | awk '{ print $1 }'`\n\nesxcli network vswitch standard add --vswitch-name=vSwitch1\n\nesxcli network vswitch standard portgroup add --portgroup-name=ManangementNetwork1 --vswitch-name=vSwitch1\n\nesxcli network vswitch standard uplink add --uplink-name=$UPLINK1 --vswitch-name=vSwitch1\n\nesxcli network ip interface add --interface-name=$VMK1 --portgroup-name=ManangementNetwork1\n\nEOF\n\nif [[ \"@MgmtNIC.ipaddress@\" =~ [0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]* ]]; then\n\necho \"Configure ESXi host management network for static IP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip interface ipv4 set --interface-name=$VMK1 --ipv4=@MgmtNIC.ipaddress@ --netmask=@MgmtNIC.netmask@ --type=static\n\nesxcli network ip route ipv4 add --gateway \"@MgmtNIC.gateway@\" --network default\nesxcli network ip dns server add --server=@MgmtNIC.dns1@\nesxcli network ip dns server add --server=@MgmtNIC.dns2@\n\nEOF\n\nelse\n\necho \"Configure ESXi host management network for DHCP\"\ncat <<\"EOF\" >>local.sh\nesxcli network ip  interface ipv4 set --interface-name=$VMK1 --type=dhcp   \n\nEOF\nfi\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_mgmt_net ./esxi_mgmt_net\necho \"Run esxi_mgmt_net\"\n!source ./esxi_mgmt_net\necho \"Configure host management complete\""
}, {      #  Updating planscript with name max chars
           "type": "PlanScript",
           "description": "plan script to update with name max characters",
           "name": "planscriptupanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanu",
           "hpProvided": "false",
           "planType": "deploy",
           "content": "reboot command"
}, {      #  Updating planscript with name greater than max chars
           "type": "PlanScript",
           "description": "plan script name greater than 255 chars",
           "name": "planscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanuss",
           "hpProvided": "false",
           "planType": "deploy",
           "content": "reboot command"
}, {   #  Updating with duplicate planscript name
            "type": "PlanScript",
            "description": "",
            "name": "HPE - ESXi 5 - generalize host configuration",
            "hpProvided": "true",
            "planType": "general",
            "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\r\n# Script to mount disk in libguesfs virtual appliance for personalizaiton or generalization\r\nmount /dev/sda5 /\r\n\r\n\r\n# creating tmp dir at local filesystem\r\n!mkdir -p ./onetime\r\n!mkdir -p ./state/local\r\n\r\n# copying required files for personalization/generalization to local filesysystem\r\n-copy-out /onetime.tgz .\r\n-copy-out /state.tgz .\r\n-copy-out /boot.cfg .\r\n\r\n# trying to findout whether onetime.tgz will be picked up during booting or state.tgz will be picked\r\n# based on that we can process either onetime.tgz or state.tgz for personalization/generalization\r\n\r\n-!grep \"onetime.tgz\"  ./boot.cfg >./onetime_found\r\n-!grep \"state.tgz\" ./boot.cfg > ./state_found"
},  {   #  Updating with invalid planscript name
            "type": "PlanScript",
            "description": "",
            "name": "$%^&",
            "hpProvided": "true",
            "planType": "general",
            "content": "# (C) Copyright 2015-2015 Hewlett-Packard Development Company, L.P.\r\n# Script to mount disk in libguesfs virtual appliance for personalizaiton or generalization\r\nmount /dev/sda5 /\r\n\r\n\r\n# creating tmp dir at local filesystem\r\n!mkdir -p ./onetime\r\n!mkdir -p ./state/local\r\n\r\n# copying required files for personalization/generalization to local filesysystem\r\n-copy-out /onetime.tgz .\r\n-copy-out /state.tgz .\r\n-copy-out /boot.cfg .\r\n\r\n# trying to findout whether onetime.tgz will be picked up during booting or state.tgz will be picked\r\n# based on that we can process either onetime.tgz or state.tgz for personalization/generalization\r\n\r\n-!grep \"onetime.tgz\"  ./boot.cfg >./onetime_found\r\n-!grep \"state.tgz\" ./boot.cfg > ./state_found"
},  {    # Updating with max description
           "type": "PlanScript",
           "description": "planscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplansplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplansplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplansplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplansplanscriptplanscript",
           "name": "ps to update with max description",
           "hpProvided": "false",
           "planType": "deploy",
           "content": "reboot command"
},  {    # Updating general planscript with ca
           "type": "PlanScript",
           "description": "",
           "name": "HPE - ESXi 5 - umount",
           "hpProvided": "true",
           "planType": "general",
           "content": "echo \"########################################\"\necho \"Configure ssh\"\necho \"########################################\"\n\nupload -<<END /ImageStreamer/esxi_ssh\n#!/bin/bash\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\ncat <<\"EOF\" >>local.sh\nvim-cmd hostsvc/enable_esx_shell\nvim-cmd hostsvc/start_esx_shell\nvim-cmd hostsvc/enable_ssh\nvim-cmd hostsvc/start_ssh\nservices.sh restart\n\nEOF\nfi\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_ssh esxi_ssh\necho \"Run esxi_ssh\"\n!source ./esxi_ssh"
}, {     # Updating capture planscript with ca
           "type": "PlanScript",
           "description": "ps for capture",
           "name": "ps_type_capture",
           "hpProvided": "false",
           "planType": "capture",
           "content": "echo \"########################################\"\necho \"Configure ssh\"\necho \"########################################\"\n\nupload -<<END /ImageStreamer/esxi_ssh\n#!/bin/bash\nif [ \"@SSH:enabled@\" = \"enabled\" ]; then\ncat <<\"EOF\" >>local.sh\nvim-cmd hostsvc/enable_esx_shell\nvim-cmd hostsvc/start_esx_shell\nvim-cmd hostsvc/enable_ssh\nvim-cmd hostsvc/start_ssh\nservices.sh restart\n\nEOF\nfi\n\nexit 0\nEND\n\ndownload /ImageStreamer/esxi_ssh esxi_ssh\necho \"Run esxi_ssh\"\n!source ./esxi_ssh"
},  {     # Updating planscript with all blank fields
           "type": "PlanScript",
           "description": "",
           "name": "",
           "hpProvided": "false",
           "planType": "capture",
           "content": ""
}

]


planscript_get = [{
    "name": "Planscript_valid_deploy"
}, {
    "content": "reboot command"
}, {
    "description": "Name field valid"
}, {
    "planType": "deploy"
}, {
    "name": "ps_non_existing"
},
   {
    "count": "25"
},
   {
    "name": "ps_type_capture"
}, {
    "name": "invalid_ps"}
]



planscript_delete = [{
    "name": "EsxiPlanScript_name_updated"
}, {
    "name": "planscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplans"
}, {
    "name": "descmaxcharas"
}, {
    "name": "ps_for_delete"
}, {
    "name": "ps_for_get"
}, {
    "name": "Planscript_valid_deploy"
}, {
    "name": "ps_type_capture"
}, {
    "name": "ps_for_update"
}, {
    "name": "HPE - ESXi 5 - generalize host configuration"
}, {
    "name": "HPE - ESXi 5 - umount"
}, {
    "name": "HPE - ESXi 5 - repack state"
}, {
    "name": "HPE - ESXi 5 - configure ssh"
}, {
    "name": "HPE - ESXi 5 - set password"
}, {
    "name": "HPE - ESXi 5 - simple double managment NIC"
}, {
    "name": "HPE - ESXi 5 - configure management 1st NIC"
}, {
    "name": "HPE - ESXi 5 - unpack state"
}, {
    "name": "HPE - ESXi 5 - mount"
}, {
    "name": "ps-for-update-of-ca-name"
}, {
    "name": "ps to update with max description"
}, {
    "name": "planscriptupanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanscriptplanu",
}, {
    "name": 'CL RHEL API_GET'
}, {
    "name": 'cl artifact_for_GET'
}, {
    "name": 'RHEL-7.2-planscript'
}, {
    "name": '123_planscript'
}, {
    "name": 'planscript_456'
}]
