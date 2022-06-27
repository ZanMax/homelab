#!/usr/bin/python3

import base64
import json
import os
import re
import sys

import requests


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


def replace_configs(path):
    with open(path, "rt") as file:
        deployment = file.read()

    with open(path, "wt") as file:
        deployment = deployment.replace("<app_name>", app_name)
        deployment = deployment.replace("<hub_url>", hub_url)
        deployment = deployment.replace("<app_version>", app_version)
        deployment = deployment.replace("<app_port>", app_port)
        deployment = deployment.replace("<app_healthcheck>", app_healthcheck)
        deployment = deployment.replace("<app_domain>", app_domain)
        file.write(deployment)


def update_version(path, new_version):
    deployment_file = os.path.join(path, "deployment.yaml")
    with open(deployment_file, "rt") as file:
        deployment = file.read()

    with open(deployment_file, "wt") as file:
        deployment = re.sub("(\d+.\d+.\d+)", new_version, deployment)
        file.write(deployment)


def update_secret_hash(secret_file, credentials_hash):
    with open(secret_file, "rt") as file:
        secret = file.read()

    with open(secret_file, "wt") as file:
        secret = secret.replace("<base64_hash>", credentials_hash)
        file.write(secret)


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
        app_name = input("APP Name: ")
        app_version = input("APP Version: ")

        app_domain = input("APP Domain: ")
        app_port = input("APP Port: ")
        app_healthcheck = input("APP Healthcheck (default / ): ")

        hub_url = input("HUB Url: ")
        env_variables = input("ENV variables --> dict {key:value}: ")

        if env_variables:
            env_dict = json.loads(env_variables)

        os.mkdir(app_name)
        os.chdir(app_name)

        download_file("https://raw.githubusercontent.com/ZanMax/homelab/main/k8s/templates/deployment.yaml",
                      "deployment.yaml")
        download_file("https://raw.githubusercontent.com/ZanMax/homelab/main/k8s/templates/ingress.yaml",
                      "ingress.yaml")
        download_file("https://raw.githubusercontent.com/ZanMax/homelab/main/k8s/templates/service.yaml",
                      "service.yaml")

        replace_configs("deployment.yaml")
        replace_configs("ingress.yaml")
        replace_configs("service.yaml")

    if command == 'redeploy':
        app_path = input("APP path: ")
        mew_app_version = input("New APP Version: ")
        update_version(app_path, mew_app_version)

    if command == 'secret':
        user = input("User: ")
        password = input("Password: ")
        hub = input("Hub url: ")
        registry = input("Registry url: ")
        auth_hash = base64.b64encode('{}:{}'.format(user, password).encode('utf-8'))
        credentials = {
            "auths": {
                hub: {
                    "auth": auth_hash.decode('utf-8')
                },
                registry: {
                    "auth": auth_hash.decode('utf-8')
                }
            }
        }

        credentials_json = json.dumps(credentials, indent=4)
        credentials_hash = base64.b64encode(credentials_json.encode('utf-8'))
        download_file("https://raw.githubusercontent.com/ZanMax/homelab/main/k8s/templates/secret.yaml", "secret.yaml")
        update_secret_hash("secret.yaml", credentials_hash.decode('utf-8'))
else:
    show_help()
