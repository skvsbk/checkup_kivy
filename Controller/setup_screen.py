from typing import NoReturn
from View.SetupScreen.setup_screen import SetupScreenView

class SetupScreenController:
    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = SetupScreenView(controller=self, model=self.model)

    def get_view(self) -> SetupScreenView:
        return self.view

    def on_tap_button_save(self):
        #Todo: save to json in Model side

        self.view.manager_screens.current = 'login screen'
