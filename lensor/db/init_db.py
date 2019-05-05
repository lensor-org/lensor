from os import environ

from sqlalchemy import create_engine

DB_USER = 'POSTGRES_USER'
DB_PASSWORD = 'POSTGRES_PASSWORD'
DB_NAME = 'POSTGRES_DB'
DB_URL = 'POSTGRES_URL'


class InitDB:

    def __init__(self):
        (self.db_user, self.db_passwd, self.db_name,
         self.db_url) = self._read_db_env_vars()

    def _read_db_env_vars(self):
        if not all(x in environ for x in [DB_USER,
                                          DB_PASSWORD, DB_NAME, DB_URL]):
            raise EnvironmentError('Data base variables are missing')

        return (environ[DB_USER],
                environ[DB_PASSWORD],
                environ[DB_NAME],
                environ[DB_URL])

    def get_engine(self):
        url = 'postgresql://{}:{}@{}/{}'.format(
             self.db_user, self.db_passwd, self.db_url, self.db_name
            )
        return create_engine(url)
