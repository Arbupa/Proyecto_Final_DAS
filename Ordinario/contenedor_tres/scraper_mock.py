from scraper import *
from unittest import TestCase
from unittest.mock import patch, Mock

class ScraperTestMock(TestCase):

    @patch("scraper.Scraper.animedetailsname", autospec=True)
    def test_animedetailsname(self, mock_search):
        mock_search.return_value = ["lalala"]
        esperado = ["lalala"]
        scrap = Scraper()
        real = scrap.animedetailsname()
        return self.assertEqual(esperado, real)

    @patch("scraper.Scraper.animedetailsname", autospec=True)
    def test_animedetailsname_request(self, mock_search):
        mock_search.return_value = "Error: request failed"
        esperado = "Error: request failed"
        scrap = Scraper()
        real = scrap.animedetailsname()
        return self.assertEqual(esperado, real)

    @patch("scraper.Scraper.animedetailsname", autospec=True)
    def test_animedetailsname_request2(self, mock_search):
        mock_search.return_value = "Error: request time exceeded"
        esperado = "Error: request time exceeded"
        scrap = Scraper()
        real = scrap.animedetailsname()
        return self.assertEqual(esperado, real)

    @patch("scraper.Scraper.animedetailsid", autospec=True)
    def test_animedetailsid(self, mock_id):
        mock_id.return_value = [{"name": "Spongebob", "id": 1,
                               "name": "Sandy", "id": 2,
                               "name": "Patrick", "id": 3,
                               "name": "Squidward", "id": 4,
                               "name": "Gary", "id": 5
                                }]
        esperado =  [{"name": "Spongebob", "id": 1,
                               "name": "Sandy", "id": 2,
                               "name": "Patrick", "id": 3,
                               "name": "Squidward", "id": 4,
                               "name": "Gary", "id": 5
                    }]
        scrap = Scraper()
        real = scrap.animedetailsid()
        return self.assertEqual(esperado, real)

    @patch("scraper.Scraper.animedetailsid", autospec=True)
    def test_animedetailsid_request2(self, mock_id):
        mock_id.return_value = "request status 200 OK"
        esperado = "request status 200 OK"
        scrap = Scraper()
        real = scrap.animedetailsid()
        return self.assertEqual(esperado, real)

    @patch("scraper.Scraper.animedetailsid", autospec=True)
    def test_animedetailsid_request3(self, mock_id):
        mock_id.return_value = [{"a"},
                                {"b"},
                                {"c"},
                                {"d"},
                                {"e"},
                                {"f"},
                                {"g"},
                                {"h"},
                                {"i"},
                                {"j"},
                                {"k"},
                                {"l"},
                                {"m"},
                                {"n"},
                                {"o"},
                                {"p"},
                                {"q"},
                                {"r"}
                               ]
        esperado =             [{"a"},
                                {"b"},
                                {"c"},
                                {"d"},
                                {"e"},
                                {"f"},
                                {"g"},
                                {"h"},
                                {"i"},
                                {"j"},
                                {"k"},
                                {"l"},
                                {"m"},
                                {"n"},
                                {"o"},
                                {"p"},
                                {"q"},
                                {"r"}
                               ]
        scrap = Scraper()
        real = scrap.animedetailsid()
        return self.assertEqual(esperado, real)

    @patch("scraper.Scraper.animedetailsid", autospec=True)
    def test_animedetailsid_request4(self, mock_id):
        mock_id.return_value = "request status 400: Bad Request"
        esperado = "request status 400: Bad Request"
        scrap = Scraper()
        real = scrap.animedetailsid()
        return self.assertEqual(esperado, real)

    @patch("scraper.Scraper.animeforgenreid", autospec=True)
    def test_animeforgenreid(self, mock_genre):
        mock_genre.return_value = """request status 403 Forbidden:
                                  The client does not have the necessary permissions 
                                  for certain content, so the server is refusing to 
                                  grant an appropriate response."""

        esperado =                """request status 403 Forbidden:
                                  The client does not have the necessary permissions 
                                  for certain content, so the server is refusing to 
                                  grant an appropriate response."""
        scrap = Scraper()
        real = scrap.animeforgenreid()
        return self.assertEqual(esperado, real)

    @patch("scraper.Scraper.animeforgenreid", autospec=True)
    def test_animeforgenreid_request2(self, mock_genre):
        mock_genre.return_value = True
        esperado = True
        scrap = Scraper()
        real = scrap.animeforgenreid()
        return self.assertEqual(esperado, real)

    @patch("scraper.Scraper.animeforgenreid", autospec=True)
    def test_animeforgenreid_request3(self, mock_genre):
        mock_genre.return_value = (1,2,3,4,5,6,7,8,9)
        esperado = (1,2,3,4,5,6,7,8,9)
        scrap = Scraper()
        real = scrap.animeforgenreid()
        return self.assertEqual(esperado, real)

    @patch("scraper.Scraper.mangaforname", autospec=True)
    def test_mangaforname(self, mock_manga):
        mock_manga.return_value = {"""404 Not Found: The server 
                                   could not find the requested content. """
                                  }

        esperado =                {"""404 Not Found: The server 
                                   could not find the requested content. """
                                  }
        scrap = Scraper()
        real = scrap.mangaforname()
        return self.assertEqual(esperado, real)

    @patch("scraper.Scraper.mangaforname", autospec=True)
    def test_mangaforname_request2(self, mock_manga):
        mock_manga.return_value = """Error 414 URI Too Long: 
                                  The URI requested by the client is longer 
                                  than the server is willing to interpret."""

        esperado =                """Error 414 URI Too Long: 
                                  The URI requested by the client is longer 
                                  than the server is willing to interpret."""
        scrap = Scraper()
        real = scrap.mangaforname()
        return self.assertEqual(esperado, real)
    
    @patch("scraper.Scraper.mangaforname", autospec=True)
    def test_mangaforname_request3(self, mock_manga):
        mock_manga.return_value = """Error 418 I'm a teapot: 
                                  The server refuses to try to make coffee with a kettle."""
                                  
        esperado =                """Error 418 I'm a teapot: 
                                  The server refuses to try to make coffee with a kettle."""
        scrap = Scraper()
        real = scrap.mangaforname()
        return self.assertEqual(esperado, real)