#!/bin/bash
#this script takes in a URL, sends a request to that URL,
#and displays the size of the body of the response

curl -sI $@ | grep 'Content-Length:' | cut -d ' ' -f2
