from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog

from Utility.observer import Observer


class SetupScreenView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.dialog = MDDialog()
        # load from json:

        if self.model.server_data != {}:
            self.ids.setup_server_db.text = self.model.server_data['db_server']
            self.ids.setup_name_db.text = self.model.server_data['db_name']
            self.ids.setup_username_db.text = self.model.server_data['db_username']
            self.ids.setup_passwd_db.text = self.model.server_data['db_password']

    def model_is_changed(self):
        """
        The method that will be called on the observer when the model changes.
        """