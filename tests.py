import os
import sqlite3
import unittest

from app import app


TESTING_DATABASE_NAME = 'test_requests.db'
app.config.update({
    'DATABASE_NAME': TESTING_DATABASE_NAME
})


class RequestsTestCase(unittest.TestCase):
    

    @classmethod
    def setUpClass(cls):
        cls.db = sqlite3.connect(TESTING_DATABASE_NAME)
        cls.db.execute("CREATE TABLE request (url text, method text)")
        cls.db.commit()

    def setUp(self):
        self.app = app.test_client()
        # Reset request table BEFORE every test.
        self.db.execute("DELETE FROM request;")
        self.db.commit()

    @classmethod
    def tearDownClass(cls):
        os.remove(TESTING_DATABASE_NAME)

    def test_dashboard(self):
        """Should return data from performed requests stored in the DB"""
        for i in range(10):
            self.app.get('/home')
        for i in range(8):
            self.app.post('/home')
        for i in range(5):
            self.app.put('/home')
        for i in range(3):
            self.app.patch('/home')
        response = self.app.get('/dashboard')
        self.assertTrue('Total requests: 26' in response.data)
        self.assertTrue('GET requests: 10' in response.data)
        self.assertTrue('POST requests: 8' in response.data)
        self.assertTrue('PUT requests: 5' in response.data)
        self.assertTrue('PATCH requests: 3' in response.data)
        self.assertTrue('DELETE requests: 0' in response.data)

if __name__ == '__main__':
    unittest.main()
