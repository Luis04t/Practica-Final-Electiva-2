import unittest
from app import app

class TestHelloWorld(unittest.TestCase):
    def test_home_route(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'¡Hola, Mundo!', response.data)

if __name__ == '__main__':
    unittest.main()
