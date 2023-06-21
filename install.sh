#!/bin/bash

if [ -d "venv/" ]
then
    echo "A venv already exist.. Installation of required packages.."
    source venv/bin/activate
    pip install -r requirements.txt
else
    sudo apt-get install python3
    sudo apt-get install python3-pip
    sudo apt install python3.11-venv
    sudo python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
fi
