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




    def test_tutorial_flow(self):
        # TODO clear all prefs
        self.altdriver.load_scene('LoaderScene')
        self.altdriver.wait_for_current_scene_to_be('MainScene')
