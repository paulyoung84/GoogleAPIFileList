#!/usr/bin/python3

"""

  In order to run this script you need python3 and pip3 installed.

  You also need some additional python modules. Please run

    sudo pip3 install httplib2

    sudo pip3 install --upgrade google-api-python-client



  To authenticate in Google follow the instructions at

  https://developers.google.com/drive/v3/web/quickstart/python

  A client_secret.json file needs to placed in the same directory

  with this script. The link above contains the instruction on

  how to obtain this file. Once you complete these steps run

    python3 this_script.py --noauth_local_webserver

  and follow the instructions

"""

import httplib2

import os

from apiclient import discovery

from oauth2client import client

from oauth2client import tools

from oauth2client.file import Storage

try:

    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()

except ImportError:

    flags = None

import pandas as pd

# If modifying these scopes, delete your previously saved credentials

# at ~/.credentials/drive-python-quickstart.json

SCOPES = 'https://www.googleapis.com/auth/drive.metadata.readonly'

CLIENT_SECRET_FILE = 'client_secret.json'

APPLICATION_NAME = 'Drive API Python Quickstart'

folder_id = '1bpFgrL2PnnkeinEa5u3voOU147PjDo-Y' #Set to id of the parent folder you want to list
folder_list = []
all_folders = []
file_list = []



def get_credentials():
    """Gets valid user credentials from storage.



    If nothing has been stored, or if the stored credentials are invalid,

    the OAuth2 flow is completed to obtain the new credentials.



    Returns:
