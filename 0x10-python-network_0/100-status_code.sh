#!/bin/bash
# sends and display the dipicof  a request to a URL passed as an argument, and displaly.
curl -s -o /dev/null -w "%{http_code}" "$1"
