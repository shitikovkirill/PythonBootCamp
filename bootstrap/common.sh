#!/usr/bin/env bash
echo "Update system"
apt-get -y -q update
apt-get -y -q upgrade
ln -s /vagrant /home/vagrant/project