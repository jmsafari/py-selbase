from seleniumbase import BaseCase
from pom_website_pages.home_page import HomePage

class TestMenu(BaseCase):

    def setUp(self):

        super().setUp()
        self.homepage = HomePage(self)
        self.homepage.open_page()

    def tearDown(self):
        print("FINISHED")
        super().tearDown()


    def test_my_menus(self):

        the_menu_items = ['Home', 'Products', 'About Us', 'Contact', 'Upload']
        self.homepage.test_multiple_elements(the_menu_items)







