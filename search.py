#coding by tegar sxc
#team: securityxploitcrew and tkj blackhats
# -*- coding: UTF-8 -*-

w = '\033[37;1m'
g = '\033[32;1m'

logo = """\033[33;1m
  ╔═╗╔═╗╔═╗╦═╗╔═╗╦ ╦
  ╚═╗║╣ ╠═╣╠╦╝║  ╠═╣
  ╚═╝╚═╝╩ ╩╩╚═╚═╝╩ ╩
"""
print logo
from googlesearch import search
query = raw_input( g + 'Search: ' + w )
for URL in search(query=query):
    print(URL)



