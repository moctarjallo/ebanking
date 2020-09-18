import unittest

from ebank.domain.agents import Agent

from ebank.domain import CreateAccount

class TestCreateAccount(unittest.TestCase):
    def setUp(self):
        agent = Agent()
        self.create_account = CreateAccount(agent)

    def test_normal(self):
        client_request = {
            'firstname': 'moctar',
            'lastname': 'diallo',
            'address': 'medina',
            'balance': 400
        }

        response = self.create_account.execute(client_request)

        self.assertEqual(response['firstname'], 'moctar')
        self.assertEqual(response['lastname'], 'diallo')
        self.assertEqual(response['address'], 'medina')
        self.assertEqual(response['balance'], 400)

if __name__ == '__main__':
    unittest.main()