#!/bin/bash
sudo iptables -t nat -A DOCKER ! -i  docker0 -p tcp --dport 3305 -j DNAT --to-destination 192.168.0.2:3306
sudo iptables -t nat -D DOCKER ! -i  docker0 -p tcp --dport 3306 -j DNAT --to-destination 192.168.0.2:3306
sudo iptables-save