from typing import NoReturn
from View.UserScreens.CheckupActionScreen.checkup_act_screen import CheckupActionScreenView

class CheckupActionScreenController:
    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = CheckupActionScreenView(controller=self, model=self.model)

    def get_view(self) -> CheckupActionScreenView:
        return self.view

