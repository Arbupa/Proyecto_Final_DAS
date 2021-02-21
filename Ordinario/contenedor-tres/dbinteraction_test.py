from unittest import TestCase
from unittest.mock import patch, Mock
from dbinteraction import *

class DbTest(TestCase):

    @patch("dbinteraction.DbInteraction.__init__", autospec=True)
    def test_create_tab_animebysearch(self, MockTable):
        MockTable.return_value = "the table was created succesfully"
        db = DbInteraction()
        real = db.create_tab_animebysearch()
        expected = "the table was created succesfully"
        return self.assertEqual(real, expected)

    # solucionar el error de la conexión de la db dentro
    # del constructor 