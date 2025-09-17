#!/usr/bin/python3
#
#  py-rundeckapi.py
#
#  Copyright 2025 Xavier Humbert <xavier@amdh.fr>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


'''
module Rundeck REST API query
'''

import requests

class Rundeck:
    '''
    class Rundeck object
    '''
    def __init__(
        self,
        rundeck_url,
        token,
        api_version=41,
        timeout = 10,
        verify=True,
        proxy = None
    ):
        self.rundeck_url = rundeck_url
        self.token = token
        self.api_version = api_version
        self.timeout = timeout
        self.verify = verify
        self.auth_cookie = None
        self.proxy = proxy

    def __request(
        self,
        method,
        rdurl,
        params=None,
        upload_file=None,
        content_type="json"
    ):
        cookies = {}
        h = {
            f"Accept": "application/{content_type}",
            f"Content-Type": "application/{content_type}",
            "X-Rundeck-Auth-Token": self.token,
        }
        options = {
            "cookies": cookies,
            "headers": h,
            "verify": self.verify,
            "proxies" : { "https" : self.proxy,
                          "http" : self.proxy
                        }
        }
        if method == "GET":
            options["params"] = params
        elif upload_file is not None:
            options["data"] = upload_file
            options["headers"]["Content-Type"] = "octet/stream"
        else:
            options["json"] = params
        r = requests.request(method, rdurl, **options, timeout=self.timeout)
        r.raise_for_status()
        if content_type == "json":
            try:
                return r.json()
            except ValueError:
                return r.text
        else:
            return r.text

    def get (self, endpoint):
        '''
        Implements the GET method
        '''
        rdurl = f"{self.rundeck_url}/api/{self.api_version}/{endpoint}"
        return self.__request("GET", rdurl)

    def post (self, endpoint, rd_data, mime_type="application/json"):
        '''
        Implements the POST method
        '''
        rdurl = f"{self.rundeck_url}/api/{self.api_version}/{endpoint}"
        h = {
            "Accept": "application/json",
            "Content-Type": mime_type,
            "X-Rundeck-Auth-Token": self.token,
        }
        r = requests.post(rdurl, data=rd_data , headers=h, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def put (self, endpoint, rd_data, mime_type="application/json"):
        '''
        Implements the PUT method
        '''
        rdurl = f"{self.rundeck_url}/api/{self.api_version}/{endpoint}"
        h = {
            "Accept": "application/json",
            "Content-Type": mime_type,
            "X-Rundeck-Auth-Token": self.token,
        }
        r = requests.put(rdurl, data=rd_data, headers=h, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def delete (self, endpoint):
        '''
        Implements the DELETE method
        '''
        rdurl = f"{self.rundeck_url}/api/{self.api_version}/{endpoint}"
        h = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Rundeck-Auth-Token": self.token,
        }
        r = requests.delete(rdurl, headers=h, timeout=self.timeout)
        r.raise_for_status()
