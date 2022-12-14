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
        self.ids.setup_server_db.text = 'pn-srv01.acticomp.local'

    def model_is_changed(self):
        """
        The method that will be called on the observer when the model changes.
        """