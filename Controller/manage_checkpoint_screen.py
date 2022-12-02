from typing import NoReturn
from View.AdminScreens.ManageCheckpointScreen.manage_checkpoint_screen import ManageCheckpointScreenView

class ManageCheckpointScreenController:
    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = ManageCheckpointScreenView(controller=self, model=self.model)

    def get_view(self) -> ManageCheckpointScreenView:
        return self.view

