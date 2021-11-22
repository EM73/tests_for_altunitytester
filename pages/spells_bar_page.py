from pages.base_page import BasePage
from altunityrunner import By
from altunityrunner import AltUnityDriver
from altunityrunner import altUnityExceptions


class SpellsBarPage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)
        #self.altdriver = AltUnityDriver()


## SPELLS SLIDER ##
    @property
    def spells_slider_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/SpellsBar/SpellsPanel/ShowButton')

    @property
    def business_fever_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/SpellsBar/SpellsPanel/Spell/SpellButton')

    @property
    def auto_tap_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/SpellsBar/SpellsPanel/Spell (1)/SpellButton')

    @property
    def critical_tap_chance_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/SpellsBar/SpellsPanel/Spell (2)/SpellButton')

    @property
    def critical_tap_chance_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/SpellsBar/SpellsPanel/Spell (3)/SpellButton')

    @property
    def tap_boost_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/SpellsBar/SpellsPanel/Spell (4)/SpellButton')


    # ZABLOKOWANY
    def is_spell_locked(self, spell_number):
        try:
            spell_number = spell_number - 1
            if spell_number == 0:
                return self.altdriver.find_object(By.PATH, '/CanvasMain/SpellsBar/SpellsPanel/Spell/LockImage')
            else:
                return self.altdriver.find_object(By.PATH, f'/CanvasMain/SpellsBar/SpellsPanel/Spell ({spell_number})/LockImage')
        except altUnityExceptions.NotFoundException:
            return False

    # ODBLOKOWANY
    def is_spell_unlocked(self, spell_number):
        return not self.is_spell_locked(spell_number)

    # AKTYWNY
    def is_spell_active(self, spell_number):
        try:
            if (spell_number-1) == 0:
                if self.altdriver.find_object(By.PATH, '/CanvasMain/SpellsBar/SpellsPanel/Spell/ActiveSpellIndicator') and self.is_spell_cooldown(spell_number):
                    return True
            else:
                if self.altdriver.find_object(By.PATH, f'/CanvasMain/SpellsBar/SpellsPanel/Spell ({spell_number-1})/ActiveSpellIndicator') and self.is_spell_cooldown(spell_number):
                    return True
        except altUnityExceptions.NotFoundException:
            return False

    # COOLDOWN
    def is_spell_cooldown(self, spell_number):
        try:
            if (spell_number - 1) == 0:
                if self.altdriver.find_object(By.PATH, '/CanvasMain/SpellsBar/SpellsPanel/Spell/SpellButton/SpellProgress') and self.altdriver.find_object(By.PATH, '/CanvasMain/SpellsBar/SpellsPanel/Spell/SpellButton/Image'):
                    return True
            else:
                if self.altdriver.find_object(By.PATH, f'/CanvasMain/SpellsBar/SpellsPanel/Spell ({spell_number - 1})/SpellButton/SpellProgress') and self.altdriver.find_object(By.PATH, f'/CanvasMain/SpellsBar/SpellsPanel/Spell ({spell_number})/SpellButton/Image'):
                    return True
        except altUnityExceptions.NotFoundException:
            return False

    # cooldown orzechodzi gdy active dlatego przerobić
    # TODO kazdy element /spellLock /spellprogress jako osobna metoda
    # przez co mzna zrobic dokladniejsze warunki





