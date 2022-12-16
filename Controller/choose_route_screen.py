from typing import NoReturn
from View.UserScreens.ChooseRouteScreen.choose_route_screen import ChooseRouteScreenView


class ChooseRouteScreenController:
    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = ChooseRouteScreenView(controller=self, model=self.model)
        self.route_id = None

    def get_view(self) -> ChooseRouteScreenView:
        return self.view

    def on_tap_button_start(self) -> NoReturn:
        if self.route_id:
            screen_name = self.model.get_checkpionts_for_make_screen(self.route_id)
            self.view.manager_screens.current = screen_name

    def on_tap_button_cancel(self) -> NoReturn:
        self.view.manager_screens.current = 'login screen'

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.route_id = checkbox.listItem.id
