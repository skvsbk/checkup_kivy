from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard


from Utility.observer import Observer

class CheckupActionScreenView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        self.dialog = MDDialog()

    def on_enter(self):
        self.ids.carousel.clear_widgets()
        for i in range(10):
            card = CheckCard()
            self.ids.carousel.add_widget(card)


    def model_is_changed(self):
        """
        The method that will be called on the observer when the model changes.
        """

class CheckCard(MDCard):
    """Slide card"""

