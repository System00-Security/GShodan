#!/usr/bin/env python3
__author__      = "Joy Ghosh"
__Ver__         = "V 1.0"
__copyright__   = "Copyright 2021, SYSTEM00 SECURITY"
from colorama import Fore, Back, Style
import requests
import argparse
from json2html import *
##########################
api_key="YOUR_API_KEY"
##########################
api_url='https://api.shodan.io/shodan/host/search?key='+api_key+'&query='
##########################
def logo():
    print(Fore.RED+"""

█▀▀ █▀ █░█ █▀█ █▀▄ ▄▀█ █▄░█
█▄█ ▄█ █▀█ █▄█ █▄▀ █▀█ █░▀█
---------------------------
    Gui Shodans result
---------------------------

    """+Fore.WHITE)
def shodan_result(query):
    request=requests.get(api_url+query)
    result=request.text
    html=json2html.convert(json = result)
    out=open(query+'.html', "w")
    out.write(html)
    out.close()
    print(Fore.GREEN+"[X] File Saved as : "+query+'.html'+Fore.WHITE)
logo()
try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--query", help="Enter Your Shodan Query ", type=str)
    args = parser.parse_args()
    shodan_result(args.query)
except TypeError:
  print("Type -h to see all the options")
except:
  exit()
