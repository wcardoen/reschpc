#!/usr/bin/env python3
__author__ = 'Wim R.M. Cardoen'

import requests
import sys
from . import aux

class Lammps:

    @staticmethod
    def create(auth, jobName, zippedFileId,
               lmpInputFile, lmpVersion="7Aug19",
               numOfNodes=2, coresPerSlot=88 , coreType="carbon",
               walltime=24, isVerbose=False):
        """
        Method to create the job in the Rescale Cloud
        :param auth:
        :param jobName:
        :param zippedFileId:
        :param lmpInputFile:
        :param lmpVersion:
        :param numOfNodes:
        :param coresPerSlot:
        :param coreType:
        :param inputfile:
        :param walltime:
        :param isVerbose:
        :return jobid
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
                                   "code": "lammps",
                                   "version": lmpVersion ,
                                },
                               "command": "mpirun lmp_rescale -in " + lmpInputFile,
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
            print(f"  ERROR Lammps::create -> {err}")
            sys.exit()
        return jobid
