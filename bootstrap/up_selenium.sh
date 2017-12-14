#!/usr/bin/env bash
cd /home/vagrant/selenium

java -jar selenium-server-standalone-3.8.0.jar -role hub >> log.txt 2>&1 &

java -jar selenium-server-standalone-3.8.0.jar -role node  -nodeConfig sg-node.json >> log.txt 2>&1 &