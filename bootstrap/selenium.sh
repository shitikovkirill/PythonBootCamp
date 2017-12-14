#!/usr/bin/env bash
cd
echo "Install selenium"
wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X
wget -O sg-node.json https://gist.github.com/extsoft/aed4cb6e0b1ae3cd1d38cafffdd79310/raw/

mkdir selenium
cp selenium-server-standalone-3.8.0.jar ./selenium
cp sg-node.json ./selenium

echo "Install firefox + geckodriver on VM"
sudo add-apt-repository ppa:mozillateam/firefox-next
sudo apt-get -y -q update
sudo apt-get -y install firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
tar -xvzf geckodriver*
sudo mv geckodriver /usr/local/sbin