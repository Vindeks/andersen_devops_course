#!/bin/bash

if [[ $EUID > 0 ]]
then
  echo "Please run as root or use sudo"
  exit
fi

if [[ -z "$1" || -z "$2" ]]
then
  echo "Please enter PID or process name as a first parameter and lines limit as a second parameter"
  exit
fi

sudo netstat -tunapl | awk -v nameOrPID=$1 '$0~nameOrPID {print $5}' | cut -d: -f1 | sort | uniq -c | sort | tail -n$2 | grep -oP '(\d+\.){3}\d+' | while read IP ; do whois $IP | awk -F: '/^Organization/ {print $2}' ; done
