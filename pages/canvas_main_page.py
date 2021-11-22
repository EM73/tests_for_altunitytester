from pages.base_page import BasePage
from altunityrunner import By
from altunityrunner import AltUnityDriver


class CanvasMainPage(BasePage):

    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)
        #self.altdriver = AltUnityDriver()

    ## DOWN BAR ##
    @property
    def shop_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/BottomBar/ButtonsPanel/ShopButton')

    @property
    def cards_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/BottomBar/ButtonsPanel/CardsButton')

    @property
    def spells_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/BottomBar/ButtonsPanel/SpellsButton')

    @property
    def advisors_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/BottomBar/ButtonsPanel/AdvisorButton')

    @property
    def king_portrait(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/BottomBar/KingAnchor/KingScreenButton')




    ## MINI BUTTONS ##

    @property
    def settings_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/SettingsButton')

    @property
    def daily_reward_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/DailyRewards')

    @property
    def tournament_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/TournamentsButton')

    @property
    def marketing_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/MarketingButton')

    @property
    def quest_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/DailyQuestsButton')

    @property
    def special_offer1_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/SpecialOfferButton')

    @property
    def special_offer2_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/SpecialOfferButton (1)')

    @property
    def building_stats_button(self):
        return self.altdriver.find_object(By.PATH, '/CanvasMain/BuildingStatsButton')
