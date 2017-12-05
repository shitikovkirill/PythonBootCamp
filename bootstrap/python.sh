#!/usr/bin/env bash
echo -e "\e[34mInstall pip, virtualenv and virtualenvwrapper"
apt-get install -y python-pip python-dev build-essential
pip install --upgrade pip
pip install -q --upgrade virtualenv virtualenvwrapper