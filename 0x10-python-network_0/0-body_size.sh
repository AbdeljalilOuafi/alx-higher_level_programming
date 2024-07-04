#!/usr/bin/env bash
#this script takes in a URL, sends a request to that URL,
#and displays the size of the body of the response

#-s: run curl in silent mode
#-I: bring the header only, not the whole content
#$@: all arguments, in this case its going to be the url to be fetched

curl -sI $@ | grep 'Content-Length:' | cut -d ' ' -f2

