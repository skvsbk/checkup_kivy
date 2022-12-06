from typing import NoReturn
from View.UserScreens.ChooseRouteScreen.choose_route_screen import ChooseRouteScreenView

class ChooseRouteScreenController:
    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = ChooseRouteScreenView(controller=self, model=self.model)

    def get_view(self) -> ChooseRouteScreenView:
        return self.view

    def on_tap_button_start(self):
        print('start button')

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')
