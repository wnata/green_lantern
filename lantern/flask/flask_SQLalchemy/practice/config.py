class Config:
    PG_USER = "test_cursor"
    PG_PASSWORD = "test"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "test_cursor_SQLAlchemy"  # Can be empty but should be present
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
