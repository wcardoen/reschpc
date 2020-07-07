#!/usr/bin/env python3
__author__ = 'Wim R.M. Cardoen'

import requests
import sys
from . import aux

class Vasp:

    @staticmethod
    def create(auth, 
               jobName, zippedFileId, vaspVersion="5.4.4-impi2018",
               numOfNodes=2, coresPerSlot=88 , coreType="carbon",
               walltime=24, isVerbose=False):
        """
        Method to create a VASP job in the Rescale Cloud
        :param jobName:
        :param zippedFileId:
        :param vaspVersion:
        :param numOfNodes:
        :param coresPerSlot:
        :param coreType:
        :param walltime:
        :param isVerbose:
        :return: jobid
        """
        try:
            r = requests.post(
                   'https://platform.rescale.com/api/v2/jobs/',
                    json={
                          "name": jobName,
                          "projectId": auth.PROJECTID,
                          "jobanalyses": [
                             {
                               "analysis":{
                                   "code": "vasp",
                                   "version": vaspVersion ,
                                },
                               "command": "mpirun vasp_std",
                               "hardware": {
                                   "numOfNodes": numOfNodes,
                                   "coresPerSlot": coresPerSlot,
                                   "coreType": coreType,
                                   "walltime": walltime,
                               },
                               "inputFiles": [
                                   {
                                    "id": zippedFileId
                                   }
                                ],
                                "useMpi": True,
                             }
                          ],
                        },
                    headers={'Authorization': 'Token ' + auth.TOKEN}
            )
            print(f"  Status :{r.status_code}")
            d = aux.byte2dict(r.content)
            if isVerbose:
                for k in d.keys():
                    print(f"    Key:'{k}'  ->  Value:'{d[k]}'")
            jobid = d["id"]
        except Exception as err:
            print(f"  ERROR Vasp::create -> {err}")
            sys.exit()
        return jobid
