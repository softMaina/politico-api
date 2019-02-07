import json

from flask import current_app

from app.tests import base_test

class TestParties(base_test.TestBaseClass):
    # class contains tests for party endpoints

    def test_add_new_party(self):

        response = self.app_test_client.post('/api/v1/party/add',json=self.PARTY)

        self.assertEqual(response.status_code, 201)
        