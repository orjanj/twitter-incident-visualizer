#!/usr/bin/python3
import psycopg2
from Config import Config as Config # TODO: Make it prettier

class DB():
  """ DB initializes and manipulates PostgreSQL databases."""
# https://codereview.stackexchange.com/questions/134535/a-class-to-create-and-modify-sqlite3-databases-with-a-terminal
  def __init__(self, statements=None):
    """ Initialize a new or connect to an existing database.
    Accept setup statements to be executed.
    :return: none
    """
    config = Config()
    self.config_param = config.getConfigParameter('postgresql')

    if statements is None:
      statements = []
    else:
      self.statements = statements

  def connect(self):
    """ Connect to the PostgreSQL database. """
#    self.connection = psycopg2.connect(user = self.config_param['user'],password = self.config_param['passwd'],host = self.config_param['host'],port = self.config_param['port'],database = self.config_param['dbname'])
#    self.cursor = self.connection.cursor()
#    self.connected = True
#    self.statement = ''

  def close(self):
    """ Close the PostgreSQL database connection. """
#    self.connection.commit()
#    self.connection.close()
#    self.connected = False

  def insertQuery(statement):
    """ Insert data to DB. """

  def updateQuery(statement):
    """ Update data in DB. """

  def deleteQuery(statement):
    """ Delete data from DB. """

  def validateConnection(self):
    """
    Connection validation to PostgreSQL DB.
    :return: credential information (?)
    """

db = DB()
db.connect()