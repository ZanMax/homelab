#!/bin/bash

uram=$(free -m | awk '$1 == "Mem:" {print $3}')
udisk=$(df -Bm | grep '^/dev/' | grep -v '/boot$' | awk '{ut += $3} END {print ut}')
cpul=$(top -bn1 | grep '^%Cpu' | cut -c 9- | xargs | awk '{printf("%.1f%%"), $1 + $3}')
lb=$(who -b | awk '$1 == "system" {print $3 " " $4}')
pram=$(free | awk '$1 == "Mem:" {printf("%.2f"), $3/$2*100}')
pdisk=$(df -Bm | grep '^/dev/' | grep -v '/boot$' | awk '{ut += $3} {ft+= $2} END {printf("%d"), ut/ft*100}')
fram=$(free -m | awk '$1 == "Mem:" {print $2}')
fdisk=$(df -Bg | grep '^/dev/' | grep -v '/boot$' | awk '{ft += $2} END {print ft}')
up=$(uptime -p)

echo "Server statisctics:"
echo "-------------------"
echo "CPU load: $cpul"
echo "Memory Usage: $uram/${fram}MB ($pram%)"
echo "Disk Usage: $udisk/${fdisk}Gb ($pdisk%)"
echo "Uptime: $up"
echo "Last boot: $lb"
echo "-------------------"