#test_app.py
import unitest
from app Import hello_world
class TestApp(unitest.TestCase):
      self.assertEqual(hello_world(), "Hello,World!")

if _name_ -- ' _main_':
      unitest.main()
    