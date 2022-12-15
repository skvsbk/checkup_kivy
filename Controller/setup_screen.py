from typing import NoReturn
from View.SetupScreen.setup_screen import SetupScreenView

class SetupScreenController:
    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = SetupScreenView(controller=self, model=self.model)

    def get_view(self) -> SetupScreenView:
        return self.view

    def on_tap_button_save(self) -> NoReturn:

        screen_name = self.model.save_button()
        self.view.manager_screens.current = screen_name

    def set_server_data(self, key, value) -> NoReturn:
        self.model.set_server_data(key, value)
