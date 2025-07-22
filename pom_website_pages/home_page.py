from seleniumbase import BaseCase
from config.default import BASE_URL


class HomePage:

    def __init__(self, sb:BaseCase):

        self.sb = sb
        self.main_menu = '.main-menu li'


    def open_page(self):

        self.sb.open(BASE_URL)

    def test_multiple_elements(self, menu_labels):

        # This interaction will loop through the main menu to see if the labels are the ones needed.
        self.open_page()

        for i, label_text in enumerate(menu_labels, start=1):

            self.sb.assert_text(label_text,f'{self.main_menu}:nth-child({i})')