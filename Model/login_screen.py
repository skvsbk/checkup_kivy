from Utility.dbase import DBase
# from View.screens import user_screen
import View.screens

from Utility.jsonfile import JSONFile


class LoginScreenModel:
    def __init__(self):
        self._observers = []
        self.user_data = {}
        self.json_file = JSONFile("login.json")
        json_data = self.json_file.get_json()
        if json_data != {}:
            self.user_data.update(json_data)

    def notify_observers(self):
        """
        The method that will be called on the observer when the model changes.
        """

        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    # def reset_data_validation_status(self):
    #     self.data_validation_status = None

    def set_user_data(self, key, value):
        """Sets a dictionary of data that the user enters."""

        self.user_data[key] = value

    def login_button(self):
        """
        Get data from the database and compares this data with the data entered
        by the user.
        """
        data = None
        # data = {'user': 'skv', 'password': 'Qwerty123'}
        # self.user_data['user'], self.user_data['password']
        data = DBase().get_user('user', 'pass')

        if data != {}:
            if self.user_data['save'] == 1:
                self.json_file.save_to_json(self.user_data)
            else:
                self.json_file.save_to_json({'user': self.user_data['user'],
                                             'password': '',
                                             'save': 0})

        if data['role'] == 'user':
            self.generate_new_screens(View.screens.user_screen)
            return 'choose route screen'

        if data['role'] == 'admin':
            self.generate_new_screens(View.screens.admin_screen)
            return 'buttons screen'

    def generate_new_screens(self, screens):
        for name_screen in screens:
            if name_screen not in self._observers[0].manager_screens.screen_names:
                model = screens[name_screen]["model"]()
                controller = screens[name_screen]["controller"](model)
                view = controller.get_view()
                view.manager_screens = self._observers[0].manager_screens
                view.name = name_screen
                self._observers[0].manager_screens.add_widget(view)
