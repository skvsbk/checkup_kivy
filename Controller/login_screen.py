from typing import NoReturn
from View.LoginScreen.login_screen import LoginScreenView

class LoginScreenController:
    def __init__(self, model):
        self.model = model  # Model.slider_menu_screen.SliderMenuScreenModel
        self.view = LoginScreenView(controller=self, model=self.model)

    def get_view(self) -> LoginScreenView:
        return self.view

    def on_tap_button_login(self) -> NoReturn:
        """Called when the `LOGIN` button is pressed."""

        # self.view.show_dialog_wait()
        screen_name = self.model.chek_data()
        self.view.manager_screens.current = screen_name

    def set_user_data(self, key, value) -> NoReturn:
        """Called every time the user enters text into the text fields."""

        self.model.set_user_data(key, value)

    def reset_data_validation_status(self, *args) -> NoReturn:
        self.model.reset_data_validation_status()

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')
