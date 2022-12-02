from kivy.properties import ObjectProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog

from Utility.observer import Observer

class ManageUsersScreenView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.dialog = MDDialog()

    def model_is_changed(self):
        """
        The method that will be called on the observer when the model changes.
        """