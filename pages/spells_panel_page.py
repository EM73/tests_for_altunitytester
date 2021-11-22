from pages.base_page import BasePage
from altunityrunner import By
from altunityrunner import AltUnityDriver
from altunityrunner import altUnityExceptions


class SpellsPanelPage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)
        #self.altdriver = AltUnityDriver()


    # WINDOW
    @property
    def spells_panel(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells')
    @property
    def spells_panel_exit(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/SpellsTopBar/CloseButton')


    # BUSINESS FEVER
    @property
    def business_fever_upgrade_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel/Opacity/UpgradeButton/ButtonColor')

    def business_fever_upgrade_cost(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel/Opacity/UpgradeButton/Text (TMP) (1)').get_text()

    def business_fever_level(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel/Opacity/LevelBG/LevelText').get_text()

    # AUTO TAP
    @property
    def auto_tap_upgrade_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (1)/Opacity/UpgradeButton/ButtonColor')

    def auto_tap_upgrade_cost(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (1)/Opacity/UpgradeButton/Text (TMP) (1)').get_text()

    def auto_tap_level(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (1)/Opacity/LevelBG/LevelText').get_text()

    def auto_tap_locked(self):
        try:
            return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (1)/LockedPanel')
        except altUnityExceptions.NotFoundException:
            return False

    # CRITICAL TAP CHANCE
    @property
    def critical_tap_chance_upgrade_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (2)/Opacity/UpgradeButton/ButtonColor')

    def critical_tap_chance_upgrade_cost(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (2)/Opacity/UpgradeButton/Text (TMP) (1)').get_text()

    def critical_tap_chance_level(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (2)/Opacity/LevelBG/LevelText').get_text()

    def critical_tap_chance_locked(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (2)/LockedPanel')

    # CRITICAL TAP MULTIPLIER
    @property
    def critical_tap_multiplier_upgrade_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (3)/Opacity/UpgradeButton/ButtonColor')

    def critical_tap_multiplier_upgrade_cost(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (3)/Opacity/UpgradeButton/Text (TMP) (1)').get_text()

    def critical_tap_multiplier_level(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (3)/Opacity/LevelBG/LevelText').get_text()

    def critical_tap_multiplier_locked(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (3)/LockedPanel')

    # TAP BOOST
    @property
    def tap_boost_upgrade_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (4)/Opacity/UpgradeButton/ButtonColor')

    def tap_boost_upgrade_cost(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (4)/Opacity/UpgradeButton/Text (TMP) (1)').get_text()

    def tap_boost_level(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (4)/Opacity/LevelBG/LevelText').get_text()

    def tap_boost_locked(self):
        return self.altdriver.find_object(By.PATH, '/CanvasSpells/bg/Spells/SpellPanel (4)/LockedPanel')
