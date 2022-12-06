from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label.label import MDLabel
from kivymd.uix.list.list import MDList

from Utility.dbase import DBase
from Utility.observer import Observer

class ChooseRouteScreenView(MDScreen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)
        # self.dialog = MDDialog()

        # icons = list(md_icons.keys())
        for route in DBase().get_all_routes():
            self.ids.container.add_widget(
                ListItemWithCheckbox(text=f"{route['description']}", icon='cellphone-wireless', id=route['number'])
                # ListItemWithCheckbox1(text=f"{route['description']}")
            )

    def model_is_changed(self):
        """
        The method that will be called on the observer when the model changes.
        """

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''
    controller = ObjectProperty()
    model = ObjectProperty()
    manager_screens = ObjectProperty()

    icon = StringProperty("android")

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''

    def on_active(self, rcb, value):
        print(rcb.listItem.text, 'is', value)
