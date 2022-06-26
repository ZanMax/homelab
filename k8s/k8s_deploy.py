#!/usr/bin/python3

import os
import sys
import random
import string
import subprocess
import requests
import re
from pathlib import Path

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def download_file(url, path):
	r = requests.get(url)
	with open(path, 'w') as f:
		f.write(r.text)


def show_help():
    os.system('clear')
    print('')
    print(f'{bcolors.WARNING}- deploy{bcolors.ENDC} - create new k8s configs for delpoyment')
    print(f'{bcolors.WARNING}- redeploy{bcolors.ENDC} - redeploy existing app')
    print(f'{bcolors.WARNING}- secret{bcolors.ENDC} - config secret to connect docker hub')
    print('')

if len(sys.argv) > 1:
	command = sys.argv[1]
	if command == 'deploy':
		app_name = input("APP name: ")
		app_version = input("APP version: ")
		hub_url = input("Hub url: ")

		os.mkdir(app_name)
		os.chdir(app_name)

		download_file("https://raw.githubusercontent.com/ZanMax/homelab/main/README.md", "test.txt")

	if command == 'redeploy':
		print('redeploy')
	if command == 'secret':
		print('secret')
else:
	show_help()