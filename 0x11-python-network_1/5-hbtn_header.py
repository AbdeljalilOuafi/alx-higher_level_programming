#!/usr/bin/python3

    response = requests.get(argv[1])
    print(response.headers.get("X-Request-Id"))
