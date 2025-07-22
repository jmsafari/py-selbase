from seleniumbase import BaseCase

# We used the website https://www.saucedemo.com/ Used by Sauce Labs for demo purposes
# created by Sauce Labs, a trusted company in the automated testing industry

class TestWebsite(BaseCase):

    def test_verify_homepage_url_title(self):  #Test method name needs to start with test_

        self.open("https://www.google.com/")
        self.assert_url_contains("google.com")
        self.assert_title_contains("Google")

    def test_type_click_assert_page_using_selector(self):
        # We used the website https://www.saucedemo.com/ Used by Sauce Labs for demo purposes
        # created by Sauce Labs, a trusted company in the automated testing industry
        # SELECTOR: In this test we will fill both username and password then click on login button

        self.open("https://www.saucedemo.com/")
        self.type("[name='user-name']","standard_user")
        self.type("[name='password']", "secret_sauce")
        self.click("[name='login-button']")
        self.assert_text_visible("Swag Labs")

    def test_type_click_assert_page_using_xpath(self):
        # We used the website https://www.saucedemo.com/ Used by Sauce Labs for demo purposes
        # created by Sauce Labs, a trusted company in the automated testing industry
        # XPATH: In this test we will fill both username and password then click on login button

        self.open("https://www.saucedemo.com/")
        self.type("//input[@name='user-name']","standard_user")
        self.type("//input[@name='password']", "secret_sauce")
        self.click("//input[@name='login-button']")
        self.assert_text_visible("Swag Labs")

    def test_multiple_elements(self):

        #loop through the main menu to see if the labels are the ones needed.

        self.open("https://practice-react.sdetunicorns.com/")

        menu_labels = ['Home', 'Products', 'About Us', 'Contact', 'Upload']

        for i, label_text in enumerate(menu_labels, start=1):

            self.wait_for_element_present()

            self.assert_text(label_text,f'.main-menu li:nth-child({i})')

    def test_progessbar(self):

        #Test websites controllers - https://seleniumbase.io/demo_page
        self.open("https://seleniumbase.io/demo_page")

        #verify if the slider load at 50%

        self.assert_attribute('#mySlider', 'value','50')

        self.set_value('#mySlider',80)

        progressbar_value = self.get_value('#progressBar')
        self.assert_true(progressbar_value == 80)

        # OR

        self.assert_attribute('#progressBar','value','80')

        self.sleep(3)

    def test_dropdown(self):

        #Test websites controllers - https://seleniumbase.io/demo_page
        # NOTE: Seleniumbase access dropdown by index, text and value

        self.open("https://seleniumbase.io/demo_page")

        #verify if the dropdown/select load at 0.25, as well as the progressbar at 0.25

        self.assert_element("meter[value='0.25'")  # verify if the default value of the progressbar is set to 25
        self.assert_element("select#mySelect option[value='25%']")   #verify if the default value of the dropdown/select is set to 25%

        self.sleep(3)

        # select new value by text and check the progressbar

        self.select_option_by_text('select#mySelect','Set to 75%')
        self.assert_element("meter[value='0.75'")

        self.sleep(3)

        # select new value by value and check the progressbar

        self.select_option_by_value('select#mySelect','50%')
        self.assert_element("meter[value='0.5'")

        self.sleep(3)

        # select new value by index and check the progressbar

        self.select_option_by_index('select#mySelect','3')
        self.assert_element("meter[value='1'")

        self.sleep(3)

    def test_checkbox(self):

        #Test websites controllers - https://seleniumbase.io/demo_page

        self.open("https://seleniumbase.io/demo_page")

        #check the initial state (checkbox not selected and the below row containing img not visible)

        self.assert_false(self.is_selected('#checkbox1'))
        self.assert_element_not_visible('img#logo')

        # after #checkbox1 is selected

        self.click('#checkbox1')
        self.assert_true(self.is_selected('#checkbox1'))
        self.assert_element_visible('img#logo')

    def test_iframe(self):

        #Test websites controllers - https://seleniumbase.io/demo_page
        # NOTE: Here we need to keep in mind that Main DOM and the one of the iFrame are different

        self.open("https://seleniumbase.io/demo_page")

        # Inside the root DOM

        self.assert_element_not_visible('h4')

        #Now inside iFrame '#myFrame2' where h4 belong

        self.switch_to_frame('#myFrame2')
        self.assert_element_visible('h4')

        #THEN return to the root DOM

        self.switch_to_default_content()
        self.assert_element_not_visible('h4')

    def test_hover_dropdown(self):
        # Test websites controllers - https://seleniumbase.io/demo_page
        # NOTE: Dropdown based on a div NOT a select

        self.open("https://seleniumbase.io/demo_page")

        #self.hover('#myDropdown')
        #self.click('#dropOption2')

        # OR the two functions above can be combined into:

        self.hover_and_click('#myDropdown','#dropOption2')

        self.assert_text('Link Two Selected','h3')

    def test_new_tab(self):

        #switch between the new tab and the 1st tab.

        self.open("https://practice-react.sdetunicorns.com/")

        # Click on a link that opens a new tab
        self.click('.copyright p a')
        self.switch_to_tab(1)
        self.assert_title_contains('Master Software')

        # Click on a link that opens a new tab
        self.switch_to_default_tab()
        self.assert_title_contains('Practice with React')




