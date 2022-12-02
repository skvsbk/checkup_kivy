from typing import NoReturn
from View.AdminScreens.BottonsScreen.bottons_screen import BottonsScreenView

class BootonsScreenController:
    def __init__(self, model):
        self.model = model
        self.view = BottonsScreenView(controller=self, model=self.model)

    def get_view(self) -> BottonsScreenView:
        return self.view

    def on_tap_button_users(self) -> NoReturn:
        """Called when the `USERS` button is pressed."""

    def on_tap_button_checkpoints(self) -> NoReturn:
        """Called when the `USERS` button is pressed."""

    def on_tap_button_routes(self) -> NoReturn:
        """Called when the `USERS` button is pressed."""

