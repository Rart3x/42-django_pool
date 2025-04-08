#!/bin/bash

RED='\033[0;31m'
RESET='\033[0m'

if [ -z "$1" ]; then
    echo -e "${RED}Usage: $0 <URL>${RESET}"
    exit 1
fi

url=$(curl -I "$1" 2>/dev/null | grep Location: | cut -d " " -f2- | tr -d '\r')

if [ -z "$url" ]; then
    echo -e "${RED}No URL found${RESET}"
else
    echo "$1 -> $url"
fi
