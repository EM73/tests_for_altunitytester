from pages.base_page import BasePage
from altunityrunner import By


class TutorialPage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    @property
    def tutorial_popup(self):
        return self.altdriver.wait_for_object(By.PATH, '/PopupCanvas/TutorialSimple')
    @property
    def tutorial_ok(self):
        return self.altdriver.wait_for_object(By.PATH, '/PopupCanvas/TutorialSimple/Bg/OkButton')
    @property
    def tutorial_text(self):
        return self.altdriver.wait_for_object(By.PATH, '/PopupCanvas/TutorialSimple/Bg/Desc')

    def get_tutorial_text(self):
        self.tutorial_text.get_text()
