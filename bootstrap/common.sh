#!/usr/bin/env bash
echo "Update system"
apt-get -y -q update
apt-get -y -q upgrade
file="/home/vagrant/project"
if [ -f "$file" ]
    then
	    echo "File $file exist."
    else
	    echo "File $file not found."
	    ln -s /vagrant $file
    fi
