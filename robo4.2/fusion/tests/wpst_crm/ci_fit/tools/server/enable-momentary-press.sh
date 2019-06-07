#!/bin/bash
# Blame: Eric Conrad (eric.conrad@hpe.com)

echo "[org/gnome/settings-daemon/plugins/power]" > /etc/dconf/db/local.d/01-power
echo "button-sleep='nothing'" >> /etc/dconf/db/local.d/01-power
echo "button-suspend='nothing'" >> /etc/dconf/db/local.d/01-power
echo "button-hibernate='nothing'" >> /etc/dconf/db/local.d/01-power
echo "button-power='shutdown'" >> /etc/dconf/db/local.d/01-power

dconf update

echo "restart system to complete changes."
