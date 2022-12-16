from Utility.dbase import DBase


class ChooseRouteScreenModel:
    def __init__(self):
        self._observers = []

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def get_checkpionts_for_make_screen(self, route_id):
        checkpionts = DBase().get_checkpoints_for_routes(route_id)
        return 'checkup action screen'
