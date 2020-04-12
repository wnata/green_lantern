import inject

from store_app import app
from fake_storage import FakeStorage


def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)

        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client


class TestUsers(Initializer):
    def test_create_new(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        assert resp.status_code == 201
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/users',
            json={'name': 'Andrew Derkach'}
        )
        assert resp.json == {'user_id': 2}

    def test_successful_get_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.get(f'/users/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'John Doe'}

    def test_get_unexistent_user(self):
        resp = self.client.get(f'/users/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}

    def test_succesful_update_user(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        user_id = resp.json['user_id']
        resp = self.client.put(
            f'/users/{user_id}',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_unexistent_update_user(self):
        resp = self.client.put(
            f'/users/1',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}


class TestGoods(Initializer):
    def test_create_new_good(self):
        resp = self.client.post(
            '/goods',
            json=[{'good': 'Chocolate_bar',
                   'price': 10},
                  {'good': 'Milk',
                   'price': 5}
                  ]
        )

        assert resp.status_code == 201
        assert resp.json == {'numbers of items created': 2}

    def test_get_goods(self):
        resp = self.client.post(
            '/goods',
            json=[{'good': 'Chocolate_bar', 'price': 10},
                  {'good': 'Milk', 'price': 5}]
        )
        resp = self.client.get('/goods')
        assert resp.status_code == 200
        assert resp.json == [{'good': 'Chocolate_bar', 'price': 10, 'id': 1},
                             {'good': 'Milk', 'price': 5, 'id': 2}]

    def test_update_goods(self):
        resp = self.client.post(
            '/goods',
            json=[{'good': 'Chocolate_bar', 'price': 10},
                  {'good': 'Milk', 'price': 5}]
        )
        resp = self.client.put(
            '/goods',
            json=[{'good': 'Chocolate_bar', 'price': 25, 'id': 1},
                  {'good': 'Milk', 'price': 15, 'id': 2},
                  {'good': 'crisps', 'price': 5, 'id': 3}]
        )
        assert resp.status_code == 200
        assert resp.json == {'successfully_updated': 2, 'errors': {'no such id in goods': [3]}}


class TestStore(Initializer):
    def test_succes_post_store(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        assert resp.status_code == 201
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow',
                  'location': 'Lviv',
                  'manager_id': 1}
        )
        assert resp.status_code == 201
        assert resp.json == {'store_id': 1}

    def test_fail_post_store(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        resp = self.client.get(f'/users/2')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 2'}

        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow',
                  'location': 'Lviv',
                  'manager_id': 2}
        )
        assert resp.status_code == 201
        assert resp.json == {'store_id': 1}

    def test_succes_get_store(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 1}
        )
        store_id = resp.json['store_id']
        resp = self.client.get(f'/store/{store_id}')

        assert resp.status_code == 200
        assert resp.json == {'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 1}

    def test_get_unexistent_store(self):
        resp = self.client.get(f'/store/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such store_id 1'}

    def test_succesful_update_store(self):
        resp_user = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )

        user_id = resp_user.json['user_id']

        resp_user = self.client.put(
            f'/users/{user_id}',
            json={'name': 'Johanna Doe'}
        )

        assert resp_user.status_code == 200
        assert resp_user.json == {'status': 'success'}

        resp_store = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': 1}
        )

        store_id = resp_store.json['store_id']

        resp_store = self.client.put(
            f'/store/{store_id}',
            json={'name': 'Mad Deer', 'location': 'Kiev', 'manager_id': 1}
        )

        assert resp_store.status_code == 200
        assert resp_store.json == {'status': 'success'}

    def test_unexistent_update_user(self):
        resp = self.client.put(
            '/users/1',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}

        resp_store = self.client.put(
            '/store/1',
            json={'name': 'Mad Deer', 'location': 'Kiev', 'manager_id': 1}
        )

        assert resp_store.status_code == 404
        assert resp_store.json == {'error': 'No such store_id 1'}
