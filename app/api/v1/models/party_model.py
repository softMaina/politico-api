from flask import Flask, abort

PARTIES = []
class Party(object):
    def __init__(self):
        self.party = PARTIES
    

    def get_parties(self):
        return self.party
    

      
    def add_party(self,name,hqaddress,logoUrl):
        party={
            'id':len(self.party)+1,
            'name':name,
            'hqaddress':hqaddress,
            'logoUrl':logoUrl
        }
        self.party.append(party)