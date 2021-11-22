from tests.base_test import TestBase

from pages.tutorial_page import TutorialPage
from pages.stage1_page import Stage1Page
from pages.age_tag_page import AgeTagPage


import os
import unittest
import pytest
import sys
import json
import time

class TestTutorial(TestBase):

    def setUp(self):
        self.tutorial_page = TutorialPage(self.altdriver)
        self.stage1_page = Stage1Page(self.altdriver)
        self.age_tag_page = AgeTagPage(self.altdriver)

    def test_tutorial_popup_displayed_corectly(self):
        assert (self.tutorial_page.tutorial_popup)
        # TODO  for multiple elements


    def test_tutorial_flow(self):
        #self.age_tag_page.age_tag_submit_button.click()
        self.tutorial_page.tutorial_ok.tap()
        #self.stage1_page.upgrade_button1.tap()

    def test_tutorial_flow1(self):
        self.tutorial_page.tutorial_ok.tap()
        self.stage1_page.upgrade_button1.tap()
        #first tap x5
        # assert for tut text
        self.stage1_page.tap_building.tap()
        self.stage1_page.tap_building.tap()
        self.stage1_page.tap_building.tap()
        self.stage1_page.tap_building.tap()
        self.stage1_page.tap_building.tap()

        #reach x2.5 combo
        # assert for tut text
        self.stage1_page.tap_building.tap()
        self.stage1_page.tap_building.tap()
        self.stage1_page.tap_building.tap()
        self.stage1_page.tap_building.tap()
        self.stage1_page.tap_building.tap()
        self.stage1_page.tap_building.tap()
        self.stage1_page.tap_building.tap()
        self.stage1_page.tap_building.tap()
        self.stage1_page.tap_building.tap()
        self.stage1_page.tap_building.tap()

        #upgrading1 building1
        # assert for tut text
        self.stage1_page.upgrade_button1.tap()

        #upgrading2 building1
        # assert for tut text
        self.stage1_page.upgrade_button1.tap()
        self.stage1_page.upgrade_button1.tap()
        self.stage1_page.upgrade_button1.tap()
        self.stage1_page.upgrade_button1.tap()
        self.stage1_page.upgrade_button1.tap()
        self.stage1_page.upgrade_button1.tap()
        self.stage1_page.upgrade_button1.tap()

        #milestone building1
        # assert for tut text
        self.stage1_page.upgrade_button1.tap()









if __name__ == '__tutorial_test__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTutorial)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())