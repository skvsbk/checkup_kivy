class DBase:
    def __init__(self):
        connection = None

    def get_user(self):
        # make request to DB with username and password and return dict or None
        # return {'username': 'user', 'role': 'user', 'fio': 'Иванов Петр Сергеевич'}
        return {'user': 'admin', 'role': 'admin', 'fio': 'Administrator'}
        # return None

    def get_routes(self):
        return [{'number': '1', 'description': 'Обход технологического этажа'},
                {'number': '2', 'description': 'Обход 1, 2, 3 участков'},
                {'number': '3', 'description': 'Обход водоподготовки'},
                {'number': '4', 'description': 'Обход всех участков, ВП, тех.этажа'},
                ]

    def get_checkpoints(self):
        return [{'name': '1.004', 'nfc': '04ac78'},
                {'name': '1.038', 'nfc': '02ac67'},
                {'name': '1.101', 'nfc': '03ac56'},
                {'name': '1.086', 'nfc': '01ac45'},
                {'name': '2.017', 'nfc': '07ac34'},
                ]

    def get_checkpoints_for_routes(self):
        return [{'step': '1', 'name': '1.004', 'nfc': '04ac78'},
                {'step': '2', 'name': '1.038', 'nfc': '02ac67'},
                {'step': '3', 'name': '1.101', 'nfc': '03ac56'},
                {'step': '4', 'name': '1.086', 'nfc': '01ac45'},
                {'step': '5', 'name': '2.017', 'nfc': '07ac34'},
                ]
