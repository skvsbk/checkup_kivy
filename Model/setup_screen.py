from Utility.jsonfile import JSONFile

class SetupScreenModel:
    def __init__(self):
        self._observers = []
        self.server_data = {}
        self.json_file = JSONFile("setup.json")
        json_data = self.json_file.get_json()
        if json_data != {}:
            self.server_data.update(json_data)

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def set_server_data(self, key, value):
        """Sets a dictionary of data that the user enters."""

        self.server_data[key] = value

    def save_button(self):
        self.json_file.save_to_json(self.server_data)

        return 'login screen'