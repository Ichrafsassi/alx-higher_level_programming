#!/bin/bash
# sends a JSON POST request to a URL
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
