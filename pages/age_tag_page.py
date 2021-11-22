from pages.base_page import BasePage
from altunityrunner import By


class AgeTagPage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    @property
    def age_tag_window(self):
        return self.altdriver.find_object(By.PATH, '/PopupCanvas/AgeTagging/bg')

    @property
    def age_tag_submit_button(self):
        return self.altdriver.find_object(By.PATH, '/PopupCanvas/AgeTagging/bg/Buttons/SubmitButton')


    def is_displayed(self):
        if self.age_tag_window and self.age_tag_submit_button:
            return True

    def get_age(self):
        # TODO age getter from controller?
        # return int(self.character.call_component_method("CharacterInputController", "get_currentLife", ""))
        return True

