from flask import Flask, abort

PARTIES = []
class Party(object):
    def __init__(self):
        self.party = PARTIES
    

    def get_parties(self):
        return self.party

    