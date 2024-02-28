#!/bin/bash

echo "-------------------------------------"
echo "       CONFIGURING PROJECT ...       "
echo "-------------------------------------"

echo "[INFO] Creating and activating environment ..."
ENV_NAME="venv"
python3 -m venv $ENV_NAME
. $ENV_NAME/bin/activate

which python3


echo "[INFO] Install requirements ..."
pip3 install -r requirements.txt