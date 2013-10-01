#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# timeoLED.py
#
# Copyright © 2013 jerome B (jblbl) <jerome@jblb.no-ip.org>
#
#
# Distributed under WTFPL terms
#
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
# Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
# TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
# 0. You just DO WHAT THE FUCK YOU WANT TO.
#
 
"""
  
"""
import requests
import re
import json

# from bs4 import BeautifulSoup as BS


URL="http://timeoapi.haum.org"
session = requests.Session()

session.headers.update({'User-Agent': 'timeoLED', 'Content-type': 'application/x-www-form-urlencoded'})

# session.get(URL)

get_lines = "/v1/lines"

result = session.get(URL+get_lines)

print json.dumps(result.json())
