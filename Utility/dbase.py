class DBase:
    def __init__(self):
        self.connection = None

    def get_user(self, username, password):
        # make request to DB with username and password and return dict or None
        query = f'SELECT fio, role FROM users WHERE username={username} AND passwd={password} AND active=1'
        res = self._get_query(query)
        return {'username': 'user', 'role': 'user', 'fio': 'Иванов Петр Сергеевич'}
        # return {'user': 'admin', 'role': 'admin', 'fio': 'Administrator'}
        # return None

    def get_all_routes(self):
        query = f'SELECT route_num, description FROM routes_name WHERE active=1'
        res = self._get_query(query)
        return [{'number': '1', 'description': 'Обход технологического этажа'},
                {'number': '2', 'description': 'Обход 1, 2, 3 участков'},
                {'number': '4', 'description': 'Обход водоподготовки'},
                {'number': '7', 'description': 'Обход всех участков, ВП, тех.этажа'},
                ]

    def get_checkpoints(self, id):
        query = f'SELECT name, nfc FROM checkpoints WHERE active=1 and id=id'
        res = self._get_query(query)
        return [{'name': '1.004', 'nfc': '04ac78'},
                {'name': '1.038', 'nfc': '02ac67'},
                {'name': '1.101', 'nfc': '03ac56'},
                {'name': '1.086', 'nfc': '01ac45'},
                {'name': '2.017', 'nfc': '07ac34'},
                ]

    def get_checkpoints_for_routes(self, id):
        query = f'SELECT step, name, nfc FROM routes WHERE active=1 ORDER BY step'
        res = self._get_query(query)
        return [{'step': '1', 'name': '1.004', 'nfc': '04ac78'},
                {'step': '2', 'name': '1.038', 'nfc': '02ac67'},
                {'step': '3', 'name': '1.101', 'nfc': '03ac56'},
                {'step': '4', 'name': '1.086', 'nfc': '01ac45'},
                {'step': '5', 'name': '2.017', 'nfc': '07ac34'},
                ]

    def _get_query(self, query):
        coursor = None
        res = None
        return res

    def _new_query(self):
        pass

    def _update_query(self):
        pass