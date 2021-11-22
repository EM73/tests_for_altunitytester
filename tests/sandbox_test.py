from tests.base_test import TestBase

from pages.age_tag_page import AgeTagPage
from pages.tutorial_page import TutorialPage
from pages.stage1_page import Stage1Page
from pages.canvas_main_page import CanvasMainPage
from pages.spells_bar_page import SpellsBarPage




import os
import unittest
import pytest
import sys
import json
import time

class SandboxTest(TestBase):

    def setUp(self):
        self.tutorial_page = TutorialPage(self.altdriver)
        self.stage1_page = Stage1Page(self.altdriver)
        self.age_tag_page = AgeTagPage(self.altdriver)
        self.canvas_main_page = CanvasMainPage(self.altdriver)
        self.spells_bar_page = SpellsBarPage(self.altdriver)

    def test_main_canvas_the_first(self):
        assert (self.stage1_page.building_3_stage_2)

    def test_main_canvas_the_second(self):
        self.stage1_page.building_3_upgrade_button.tap()
        assert (self.stage1_page.building_3_stage_2)

    def test_spell1_locked(self):
        self.canvas_main_page.spells_slider_button.tap()
        assert (self.canvas_main_page.is_spell_locekd(3))
        self.canvas_main_page.spells_slider_button.tap()

    def test_spell1_tap(self):
        assert (self.spells_bar_page.is_spell_cooldown(2))




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SandboxTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())