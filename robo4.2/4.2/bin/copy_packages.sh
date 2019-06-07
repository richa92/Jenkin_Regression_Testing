SHARE=$1
REPO=$2
USERNAME=$3
PASSWORD=$4
MOUNTPOINT=./deploy
mkdir -p ./deploy
echo "Mounting $SHARE\\$REPO to $MOUNTPOINT"
mount -t cifs -o domain=americas,user="$USERNAME",password="$PASSWORD" $SHARE\\$REPO $MOUNTPOINT
cp -v dist/* $MOUNTPOINT
umount $MOUNTPOINT
