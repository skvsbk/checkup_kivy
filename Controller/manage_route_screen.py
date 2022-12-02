from typing import NoReturn
from View.AdminScreens.ManageRouteScreen.manage_route_screen import ManageRouteScreenView

class ManageRouteScreenController:
    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = ManageRouteScreenView(controller=self, model=self.model)

    def get_view(self) -> ManageRouteScreenView:
        return self.view

