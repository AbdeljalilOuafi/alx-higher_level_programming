#!/bin/bash
#this script displays length of a response

curl -sI $@ | grep 'Content-Length:' | cut -d ' ' -f2
