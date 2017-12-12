#!/usr/bin/env bash
cd
echo "Install selenium"
wget -O selenium-server-standalone-3.8.0.jar https://goo.gl/SVuU9X
mkdir selenium
cp selenium-server-standalone-3.8.0.jar ./selenium

echo "Install firefox + geckodriver on VM"
add-apt-repository ppa:mozillateam/firefox-next
apt-get -y install firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
tar -xvzf geckodriver*
mv geckodriver /usr/local/sbin