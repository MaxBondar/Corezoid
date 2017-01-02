#!/usr/bin/env python3.5

__version__ = '0.1.1'

from json import dumps
from time import time
import requests
import hashlib

"""
Corezoid SDK for creating and modifying task in Corezoid processes
Find out more info about Corezoid API: https://doc.corezoid.com/en/api/upload_data/
Requirements: pip install requests
"""


class Corezoid():

    # Initialize Corezoid SDK
    def __init__(self, api_key, api_secret, process_id):
        if not api_key:
            raise ValueError('Parameter api_key is empty.')
        if not api_secret:
            raise ValueError('Parameter api_secret is empty.')
        if not process_id:
            raise ValueError('Parameter process_id is empty.')
        # Corezoid Host
        self._host = 'https://api.corezoid.com'
        # Corezoid API Version
        self._api_version = '1'
        # Corezoid Data Format.
        # Available formats: json, xml, nvp
        self._format = 'json'
        # Corezoid Process API_LOGIN
        self._api_key = api_key
        # Corezoid Process API_SECRET
        self._api_secret = api_secret
        # Corezoid Process ID that will be used to receive data
        self._process_id = process_id
        # Task object that will be sent to Corezoid process
        self.task = []

    # Create a new task
    def create_task(self, ref, data):
        if not ref:
            raise ValueError('Parameter ref is empty.')
        if not data:
            raise ValueError('Parameter data is empty.')
        self.task.append({
            'ref': ref,
            'type': 'create',
            'obj': 'task',
            'conv_id': self._process_id,
            'data': data
        })
        return self.send_task()

    # Modify an existing task
    def modify_task(self, ref, data):
        if not ref:
            raise ValueError('Parameter ref is empty.')
        if not data:
            raise ValueError('Parameter data is empty.')
        self.task.append({
            'ref': ref,
            'type': 'modify',
            'obj': 'task',
            'conv_id': self._process_id,
            'data': data
        })
        return self.send_task()

    # Send task to the Corezoid process
    def send_task(self):
        # Content obj that will be sent to a Corezoid process
        content = dumps({'ops': self.task})
        timestamp = time()
        url = self.make_url(timestamp, content)
        try:
            r = requests.post(url, content)
            if r.status_code == 200:
                self.task = [] # Clear task object
            return dumps({'status_code': r.status_code, 'response': r.text})
        except requests.RequestException as e:
            return e

    # Make a signature to sign the request
    # Signature: hex( sha1({GMT_UNIXTIME} + {API_SECRET} + {CONTENT} + {API_SECRET}) )
    def make_sign(self, timestamp, content):
        s = (str(timestamp) + self._api_secret + content + self._api_secret).encode('utf-8')
        return hashlib.sha1(s).hexdigest()

    # Check a signature validity
    def check_sign(self, sign, timestamp, content):
        tmp_sign = self.make_sign(timestamp, content)
        if sign == tmp_sign:
            return True
        else:
            return False

    # Make a request URL
    def make_url(self, timestamp, content):
        sign = self.make_sign(timestamp, content)
        url = self._host + '/api/' \
              + self._api_version + '/' \
              + self._format + '/' \
              + self._api_key + '/' \
              + str(timestamp) + '/' \
              + sign
        return url