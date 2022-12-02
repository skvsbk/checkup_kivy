from Utility.dbase import DBase
# from View.screens import user_screen
import View.screens


class LoginScreenModel:
    def __init__(self):
        self._observers = []

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

    def reset_data_validation_status(self):
        self.data_validation_status = None

    def chek_data(self):
        """
        Get data from the database and compares this data with the data entered
        by the user.
        This method is completely asynchronous. It does not return any value.
        """

        # data = {'user': 'skv', 'password': 'Qwerty123'}

        data = DBase().get_user()
        if data['role'] == 'user':
            self.generate_new_screens(View.screens.user_screen)
            return 'choose route screen'


        if data['role'] == 'admin':
            self.generate_new_screens(View.screens.admin_screen)
            return 'bottons screen'


    def generate_new_screens(self, screens):
        for name_screen in screens:
            model = screens[name_screen]["model"]()
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.manager_screens = self._observers[0].manager_screens
            view.name = name_screen
            self._observers[0].manager_screens.add_widget(view)
