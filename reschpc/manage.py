#!/usr/bin/env python3
__author__ = 'Wim R.M. Cardoen'

import requests
import sys
from . import aux

MAX_LENGTH=1000

class Manage:

    @staticmethod
    def submit(auth, jobid, isVerbose=False):
        """
        Method to submit Job
        :param auth: Instance of the Auth Class
        :param jobid:
        :param isVerbose:
        :return: r object
        """
        print(f"Submission of Job {jobid}.")
        try:
            r = requests.post(
                  'https://platform.rescale.com/api/v2/jobs/' + jobid + '/submit/',
                  headers={'Authorization': 'Token ' + auth.TOKEN}
            )
            if isVerbose:
                print(f"  Status : {r.status_code}")
                print(f"  Content:{r.content}")
            return r
        except Exception as err:
            print(f"  ERROR  Manage::submit -> {err}")
            sys.exit()


    @staticmethod
    def listJobs(auth):
        """
        List all Jobs
        :param auth: authentication
        :return: r object
        """
        try:
            r = requests.get('https://platform.rescale.com/api/v2/jobs/?page_size=' + str(MAX_LENGTH) ,
                             headers={'Authorization': 'Token ' + auth.TOKEN})
            d = aux.byte2dict(r.content) 
            numJobs = d['count']
            lstJobs = d['results']
            if len(lstJobs) != numJobs:
                print(f"  numjobs:{numjobs}")
                print(f"  lstJobs:{len(lstJobs)}")
                raise Exception("  Length of the list Jobs != count")
            for i, job in enumerate(lstJobs):
                print(f"  Job:")
                print(f"    Id    :'{job['id']}'")
                print(f"    Name  :'{job['name']}'")
                print(f"    Owner :'{job['owner']}'")
                print(f"    Status:'{job['jobStatus']['content']}'") 
            return r
        except Exception as err:
            print(f"  ERROR  Manage::listJobs -> {err}")
            sys.exit()     


    @staticmethod
    def checkJob(auth, jobid):
        """
        Check Status of a job
        :param auth:
        :param jobid:
        :return: r object
        """
        try:
            r = requests.get(
                  'https://platform.rescale.com/api/v2/jobs/' + jobid + '/',
                  headers={'Authorization': 'Token ' + auth.TOKEN}
            )
            d = aux.byte2dict(r.content)
            print(f"  Job:")
            print(f"    Id        :'{d['id']}'")
            print(f"    Name      :'{d['name']}'")
            print(f"    Owner     :'{d['owner']}'")
            print(f"    Project ID:'{d['projectId']}'")
            return r 
        except Exception as err:
            print(f"  ERROR  Manage::checkJob -> {err}")
            sys.exit()

