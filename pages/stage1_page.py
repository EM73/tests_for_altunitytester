from pages.base_page import BasePage
from altunityrunner import By

class Stage1Page(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)

    @property
    def upgrade_button1(self):
        return self.altdriver.find_object(By.PATH, '/BusinessBuildingController/Zone1/zone_1_building_2/EarnBuildingCanvas/ButtonLevelUp')
    @property
    def tap_building(self):
        return self.altdriver.find_object(By.PATH, '/BusinessBuildingController/Zone1/zone_1_building_1/TapBuildingCanvas/TapButton')

    @property
    def building_3_upgrade_button(self):
        return self.altdriver.find_object(By.PATH, '/BusinessBuildingController/Zone1/zone_1_building_3/EarnBuildingCanvas/ButtonLevelUp')
    @property
    def building_3_stage_1(self):
        return self.altdriver.find_object(By.PATH, '/BusinessBuildingController/Zone1/zone_1_building_3/BuildingModels/prefab_zone_1_building_3_stage_1/model_zone_1_building_3_stage_1')
    @property
    def building_3_stage_2(self):
        return self.altdriver.find_object(By.PATH, '/BusinessBuildingController/Zone1/zone_1_building_3/BuildingModels/prefab_zone_1_building_3_stage_1/model_zone_1_building_3_stage_2')

    @property
    def building_4_upgrade_button(self):
        return self.altdriver.find_object(By.PATH, '/BusinessBuildingController/Zone1/zone_1_building_4/EarnBuildingCanvas/ButtonLevelUp')

    @property
    def building_4_stage_2(self):
        return self.altdriver.find_object(By.PATH, '/BusinessBuildingController/Zone1/zone_1_building_4/BuildingModels/prefab_zone_1_building_4_stage_1/model_zone_1_building_4_stage_2')

