from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config

from View.screens import main_screen, user_screen, admin_screen


Config.set("graphics", "height", "760")
Config.set("graphics", "width", "320")

class CheckupApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = ScreenManager()

    def build(self):
        """
        Initializes the application; it will be called only once.
        If this method returns a widget (tree), it will be used as the root
        widget and added to the window.

        :return:
            None or a root :class:`~kivy.uix.widget.Widget` instance
            if no self.root exists.
        """

        self.theme_cls.primary_palette = 'Blue' # "DeepOrange"
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self):

        for i, name_screen in enumerate(main_screen.keys()):
            model = main_screen[name_screen]["model"]()
            controller = main_screen[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self.manager_screens
            view.name = name_screen
            self.manager_screens.add_widget(view)


CheckupApp().run()
