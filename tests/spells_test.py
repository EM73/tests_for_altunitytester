import os
import unittest
import pytest
import sys
import json
import time

from tests.base_test import TestBase
from pages.canvas_main_page import CanvasMainPage
from pages.spells_panel_page import SpellsPanelPage
from pages.spells_bar_page import SpellsBarPage

class SpellsTest(TestBase):

    def setUp(self):
        self.canvas_main_page = CanvasMainPage(self.altdriver)
        self.spells_panel_page = SpellsPanelPage(self.altdriver)
        self.spells_bar_page = SpellsBarPage(self.altdriver)

    def test_is_all_spells_locked_after_ascend(self):
        self.spells_bar_page.spells_slider_button.tap()
        for i in range(1, 6):
            assert (self.spells_bar_page.is_spell_locked(i))
        self.spells_bar_page.spells_slider_button.tap()
        self.canvas_main_page.spells_button.tap()
        assert (self.spells_panel_page.auto_tap_locked() and self.spells_panel_page.critical_tap_chance_locked() and self.spells_panel_page.critical_tap_multiplier_locked() and self.spells_panel_page.tap_boost_locked())
        self.spells_panel_page.spells_panel_exit.tap()

    def test_unlock_auto_tap(self):
        self.spells_bar_page.spells_slider_button.tap()
        assert (self.spells_bar_page.is_spell_locked(1))
        self.spells_bar_page.spells_slider_button.tap()
        self.canvas_main_page.spells_button.tap()
        assert (self.spells_panel_page.business_fever_level() == "0")
        self.spells_panel_page.business_fever_upgrade_button.tap()
        assert (self.spells_panel_page.business_fever_level() == "1")
        assert not (self.spells_panel_page.auto_tap_locked())
        self.spells_panel_page.spells_panel_exit.tap()
        self.spells_bar_page.spells_slider_button.tap()
        assert (self.spells_bar_page.is_spell_unlocked(1))
        self.spells_bar_page.spells_slider_button.tap()
        time.sleep(10)

    def test_auto_tap_states(self):
        self.spells_bar_page.spells_slider_button.tap()
        assert (self.spells_bar_page.is_spell_unlocked(3))
        time.sleep(1)
        self.spells_bar_page.critical_tap_chance_button.tap()
        time.sleep(1)
        assert (self.spells_bar_page.is_spell_active(3))
        time.sleep(30)
        assert (self.spells_bar_page.is_spell_cooldown(3))
        self.spells_bar_page.spells_slider_button.tap()

    def test_is_spell_active(self):
        assert (self.spells_bar_page.is_spell_cooldown(3))






