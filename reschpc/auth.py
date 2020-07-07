#!/usr/bin/env python3
__author__ = 'Wim R.M. Cardoen'

class Auth:

    def __init__(self, TOKEN, PROJECTID=None):
        """
        Constructor of the Authorization class
        :param TOKEN: TOKEN generated on the Rescale Website
        :param PROJECTID: PROJECTID
        """
        self.TOKEN = TOKEN
        self.PROJECTID = PROJECTID

    def changeProjectId(self, PROJECTID):
        """
        Change PROJECTID
        :param PROJECTID: 
        :return: None
        """
        self.PROJECTID = PROJECTID
        return

    def __str__(self):
        """
        Magic Method
        :return: string
        """
        out =  f"  Token: '{self.TOKEN}'\n"
        if self.PROJECTID is not None:
            out += f"    Project ID:'{self.PROJECTID}'"
        else:
            out += "    Project ID: ---- "
        return out
