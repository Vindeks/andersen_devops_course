#!/bin/bash

sudo netstat -tunapl | awk -v nameOrPID=$1 '$0~nameOrPID {print $5}' | cut -d: -f1 | sort | uniq -c | sort | tail -n$2 | grep -oP '(\d+\.){3}\d+' | while read IP ; do whois $IP | awk -F: '/^Organization/ {print $2}' ; done
