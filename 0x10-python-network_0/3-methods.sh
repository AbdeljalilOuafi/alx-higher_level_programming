#!/bin/bash
#displays all HTTP methods the server will accept.
curl -I -X OPTIONS $@
