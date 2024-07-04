#!/bin/bash
#this script displays length of a response
curl -sI $@ | grep 'Content-Length:' | awk '{print $2}'
