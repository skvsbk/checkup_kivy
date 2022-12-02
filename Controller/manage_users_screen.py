from typing import NoReturn
from View.AdminScreens.ManageUsersScreen.manage_users_screen import ManageUsersScreenView

class ManageUsersScreenController:
    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = ManageUsersScreenView(controller=self, model=self.model)

    def get_view(self) -> ManageUsersScreenView:
        return self.view

