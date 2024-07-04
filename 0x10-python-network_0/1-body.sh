#!/bin/bash
#displays the body of the response
echo "$(curl -s "$@")"
