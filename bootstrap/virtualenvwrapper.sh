#!/usr/bin/env bash

echo -e "\e[34mCreate virtualenv"
file="/usr/bin/virtualenvwrapper.sh"
if [ -f "$file" ]
then
    echo "File $file found."
	source "$file"
	echo "source $file" >> ~/.bashrc
else
    echo "File $file not found."
	file="/usr/local/bin/virtualenvwrapper.sh"
    if [ -f "$file" ]
    then
	    echo "File $file found."
	    source "$file"
	    echo "source $file" >> ~/.bashrc
    else
	    echo "File $file not found."
	    exit
    fi
fi

if [[ -z "$PROJECT_DIR" ]]; then
    echo "ERROR: PROJECT_DIR env is empty"
    exit 1
fi

mkvirtualenv --python=python2.7 $WIRTUALENV_NAME
workon $WIRTUALENV_NAME
pip install -r $PROJECT_DIR/requirements.txt