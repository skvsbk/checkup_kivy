from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog

from Utility.observer import Observer


class LoginScreenView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        # self.dialog = MDDialog()
        # self.dialog.bind(on_dismiss=self.controller.reset_data_validation_status)

        # load from json
        if self.model.user_data != {}:
            self.ids.login_username.text = self.model.user_data['user']
            self.ids.login_passwd.text = self.model.user_data['password']
            if self.model.user_data['save'] == 0:
                self.ids.login_checkbox.active = False
            else:
                self.ids.login_checkbox.active = True
        else:
            self.model.user_data['save'] = 0
            self.ids.login_checkbox.active = False

    def model_is_changed(self):
        """
        The method that will be called on the observer when the model changes.
        """
    # def show_dialog_wait(self):
    #     """Displays a wait dialog while the model is processing data."""
    #
    #     self.dialog.auto_dismiss = False
    #     self.dialog.text = "Data validation..."
    #     self.dialog.open()
