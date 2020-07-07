#!/usr/bin/env python3
__author__ = 'Wim R.M. Cardoen'

import requests
import sys
import zipfile
from . import aux

class Transfer:

    @staticmethod
    def upload(auth,filename):
        """
        Uploads a file (ZIP FILE) and returns a fileid
        :param auth: Auth instance
        :param filename: filename
        :return: zipfile_id
        """
        try:
            if zipfile.is_zipfile(filename):
                r = requests.post(
                        'https://platform.rescale.com/api/v2/files/contents/',
                        data=None,
                        files={'file': open(filename, 'rb')},
                        headers={'Authorization': 'Token ' + auth.TOKEN}
                )
                d = aux.byte2dict(r.content)
                zipfile_id = d["id"]
                return zipfile_id
            else:
                raise Exception(f"  ERROR  Transfer::upload {filename} is NOT a zip file")
        except Exception as err:
            print(f"{err}")
            sys.exit()
