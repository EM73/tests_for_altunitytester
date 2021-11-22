# -*- coding: UTF-8

import os
import unittest
import sys
import json
import time
from altunityrunner import *


class MyFirstTest(unittest.TestCase):

    altdriver = None

    @classmethod
    def setUpClass(cls):
        cls.altdriver = AltUnityDriver()

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()

    def test_open_close_panel(self):
        self.altdriver.load_scene('MainScene')

        self.altdriver.find_object(By.PATH, "//PopupCanvas/AgeTagging/bg/Buttons/SubmitButton/ButtonColor").tap()
        self.altdriver.find_object(By.PATH, "//PopupCanvas/TutorialSimple/Bg/OkButton/ButtonColor").tap()
        self.altdriver.find_object(By.PATH, "//BusinessBuildingController/Zone1/zone_1_building_2/EarnBuildingCanvas/ButtonLevelUp").tap()
        self.altdriver.find_object(By.PATH, "//BusinessBuildingController/Zone1/zone_1_building_1/TapBuildingCanvas/TapButton").tap()
        self.altdriver.find_object(By.PATH, "//BusinessBuildingController/Zone1/zone_1_building_1/TapBuildingCanvas/TapButton").tap()
        self.altdriver.find_object(By.PATH, "//BusinessBuildingController/Zone1/zone_1_building_1/TapBuildingCanvas/TapButton").tap()
        self.altdriver.find_object(By.PATH, "//BusinessBuildingController/Zone1/zone_1_building_1/TapBuildingCanvas/TapButton").tap()


        panelElement = self.altdriver.wait_for_object(By.NAME, "Bg")
        self.assertTrue(panelElement.enabled)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyFirstTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())