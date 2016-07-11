#!/bin/bash
#
# Generated script to restart steemd to run in a screen under user {{ansible_user}}
#

set -e
set -u
set -x

# Find our app
SCRIPT="{{steemd}}"

# Command line arguments
ARGS="--rpc-endpoint"

# Find app supposed run to run this user
UNAME="{{ansible_user}}"

echo "Running steemd restart script as $USER, $SCRIPT, $UNAME"

sudo logger "Restarting steemd for user $UNAME: $SCRIPT as $USER"

echo "Terminating all screens running on the box"
sudo pkill steemd || true
sudo pkill screen || true

sleep 0.5

echo "Starting new screen"
sudo -iu $UNAME /usr/bin/screen -dmS steemd-screen /bin/bash -c "$SCRIPT $ARGS ; exec bash"

sudo logger "steemd restarted"
sleep 0.5