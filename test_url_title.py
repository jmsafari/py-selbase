from seleniumbase import BaseCase

class UrlTile(BaseCase):

    def test_url_title(self):  #Test method name needs to start with test_

        self.open("https://afrigen-d.org/")
        self.assert_url_contains("afrigen-d.org")
        self.assert_title_contains("Afrigen-D")