from os import environ

from sqlalchemy import create_engine


class InitDB:

    def __init__(self):
        (self.db_user, self.db_passwd, self.db_name,
         self.db_url) = self._read_db_env_vars()

    def _read_db_env_vars(self):
        return (environ['POSTGRES_USER'],
                environ['POSTGRES_PASSWORD'],
                environ['POSTGRES_DB'],
                environ['POSTGRES_URL'])

    def get_engine(self):
        return create_engine('postgresql://' + self.db_user + ':' +
                             self.db_passwd + '@' + self.db_url + '/' +
                             self.db_name)
