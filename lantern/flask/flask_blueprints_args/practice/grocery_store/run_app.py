from store_app import app
from fake_storage import FakeStorage
import inject
from views.users import users


def configure(binder):
    db = FakeStorage()
    binder.bind('DB', db)


inject.clear_and_configure(configure)


if __name__ == '__main__':
    app.register_blueprint(users)
    app.run(port=8080, debug=True)
