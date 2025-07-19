# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class BrowserManager:

    def __init__(self, browser_name, is_open=False):
        self.browser_name = browser_name
        self.is_open = is_open

    def browser_status(self):
        if self.is_open:
            print("Browser is open")
        else:
            print("Browser is closed")

    def open_browser(self):
        if self.is_open== False:
            self.is_open = True
            print(f"Open {self.browser_name}")
        else:
            print("Browser already open")

    def close_browser(self):
        if self.is_open == True:
            self.is_open = False
            print(f"Closing {self.browser_name}")
        else:
            print("Browser already closed")


    def change_browser(self, new_browser_name):

        if self.browser_name != new_browser_name and self.is_open == True:
            print("Close the browser before changing".)
            self.close_browser()

        self.browser_name = new_browser_name
        print(f"Browser changed to {new_browser_name}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    manager = BrowserManager('Chrome')
    manager.open_browser()
    manager.change_browser('Firefox')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
