#!/usr/bin/env bash
file="/usr/bin/virtualenvwrapper.sh"
if [ -f "$file" ]
then
    echo "File $file found."
	source "$file"
else
    echo "File $file not found."
	file="/usr/local/bin/virtualenvwrapper.sh"
    if [ -f "$file" ]
    then
	    echo "File $file found."
	    source "$file"
    else
	    echo "File $file not found."
	    exit
    fi
fi

workon $WIRTUALENV_NAME

echo "JAVA version"
java -version

echo "Python version"
python -V

cd /vagrant

pytest

find -name '*.pyc' -delete
