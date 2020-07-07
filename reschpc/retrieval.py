#!/usr/bin/env python3
__author__ = 'Wim R.M. Cardoen'
__modified__ = '06/26/2020'
# Change on 06/26/2020:
#   Replaced:
#     r = requests.get(
#           'https://platform.rescale.com/api/v2/jobs/' + jobid + '/files/',
#            headers={'Authorization': 'Token ' + auth.TOKEN} )
#   with:
#     r = requests.get(
#           'https://platform.rescale.com/api/v2/jobs/' + jobid + '/files/?page_size=1000',
#            headers={'Authorization': 'Token ' + auth.TOKEN} ) 
#   and added (Additional check!):
#       numFiles = d['count'] 
#       if numFiles != len(arrFileUrl):
#          raise Exception(f"  Numfiles:{numFiles} != Retrieved files:{len(arrFileUrl)}")

import requests
import os
import pathlib
import sys
from . import aux

class Retrieval:

    @staticmethod
    def findFilesInJob(auth, jobid, isVerbose=False):
        """
        Find the files attached to a job
        :param auth: Instance of the Auth Class
        :param jobid:
        :param isVerbose:
        :return:
        """
        arrFileUrl = []
        arrFileId = []
        arrFileName = []
        arrFileTypeId = []
        arrFileIsDeleted = []
        arrFileCheckSum = []   # sha512sum for each file
        try:
            r = requests.get(
                   'https://platform.rescale.com/api/v2/jobs/' + jobid + '/files/?page_size=1000',
                   headers={'Authorization': 'Token ' + auth.TOKEN}
            )
            d = aux.byte2dict(r.content)
            numFiles = d['count']
            res = d['results']
            for i, item in enumerate(res):
                if isVerbose:
                    print(f"  Item:{i+1}")
                    for k in item.keys():
                        print(f"  '{k}' -> '{item[k]}'")
                arrFileUrl.append(item['downloadUrl'])
                arrFileId.append(item['id'])
                arrFileName.append(item['name'])
                arrFileTypeId.append(item['typeId'])
                arrFileIsDeleted.append(item['isDeleted'])
                arrFileCheckSum.append(item['fileChecksums'][0]['fileHash'])
            if numFiles != len(arrFileUrl):
                raise Exception(f"  Numfiles:{numFiles} != Retrieved files:{len(arrFileUrl)}")
        except Exception as err:
            print(f"  ERROR  Retrieval::findFilesInJob -> {err}")
            sys.exit()

        if isVerbose:
            print(f"  Array w. File URLs:{arrFileUrl}")
            print(f"  Array w. File IDs:{arrFileId}")
            print(f"  Array w. File Names:{arrFileName}")
            print(f"  Array w. File Types:{arrFileTypeId}")
            print(f"  Array w. isDeleted:{arrFileIsDeleted}")
            print(f"  Array w. Sha512 Sums:{arrFileCheckSum}")

        return (arrFileUrl, arrFileId, arrFileName,
                arrFileTypeId, arrFileIsDeleted, arrFileCheckSum)


    @staticmethod
    def downloadFiles(auth, arrFileUrl, arrFileName, path="./", isVerbose=False):
        """
        Download an Array of Files (based on URLS)
        and to be stored in path/arrFileName
        :param auth: Instance of the Auth Class
        :param arrFileUrl: Array of URLs to be downloaded
        :param arrFileName: Array of Filenames
        :param path: Name of the directory where output will be stored
        :param isVerbose:
        :return: # Downloaded files
        """
        try:
            if len(arrFileUrl) != len(arrFileName):
                raise Exception("arrFileUrl MUST have same length as arrFileName")

            # Check whether directory exists, if not create it
            if not os.path.isdir(path):
                pathlib.Path(path).mkdir(parents=True, exist_ok=True)

            for i, fileUrl in enumerate(arrFileUrl):

                filename = path + "/" + arrFileName[i]
                if isVerbose:
                    print(f"  Downloading URL:{fileUrl}")
                    print(f"    into: {filename}")

                r = requests.get(
                        fileUrl, allow_redirects=True,
                        headers={'Authorization': 'Token ' + auth.TOKEN}
                )
                if isVerbose:
                    print(f" Status:{r.status_code}")

                with open(filename, 'wb') as f:
                    f.write(r.content)
        except Exception as err:
            print(f"  ERROR  Retrieval::downloadFiles -> {err}")
            sys.exit()
        return len(arrFileUrl)


    @staticmethod
    def deleteFiles(auth, arrFileId, isVerbose=False):
        """
        Delete Files a given List
        :param auth: Instance of the Auth Class
        :param arrFileId: Array of Files Id.
        :param isVerbose:
        :return:
        """
        try:
            for fileid in arrFileId:
                print(f"  Delete '{fileid}'")
                r = requests.delete(
                        'https://platform.rescale.com/api/v2/files/' + fileid + '/',
                        headers={'Authorization': 'Token ' + auth.TOKEN}
                )
                if isVerbose:
                    print(f"  Status:{r.status_code}")
        except Exception as err:
            print(f"  ERROR  Retrieval::deleteFiles -> {err}")
            sys.exit()


    @staticmethod
    def deleteJob(auth, jobid, isVerbose=False):
        try:
            r = requests.delete(
                    'https://platform.rescale.com/api/v2/jobs/' + jobid + '/',
                    headers={'Authorization': 'Token ' + auth.TOKEN}
            )
            if isVerbose:
                print(f"  Status:{r.status_code}")
        except Exception as err:
            print(f"  ERROR  Retrieval::deleteJob -> {err}")
            sys.exit()
