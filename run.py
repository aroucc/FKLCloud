#!/usr/bin/python

import requests
import sys


with requests.get(sys.argv[1]) as result:
    print('状态码:{}'.format(result.status_code))
    print('内容：\n{}'.format(result.text))
