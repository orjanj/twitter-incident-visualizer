#!/usr/bin/python3
import psycopg2, sys
#from Config import Config # TODO: Make it prettier

class DB:
  """ DB initializes and manipulates PostgreSQL databases."""

  def __init__(self, config):
    """ Instance constructor for connecting to an existing database.
    :return: none
    """
    self.connected = False

    # Initialize configuration parameters for the database
#    config = Config()
    self.config_param = config.getConfigParameter('postgresql')

    # Connect to database
    self.connect()

  def connect(self):
    """ Connect to the PostgreSQL database. """
    try:
      self.connection = psycopg2.connect(user = self.config_param['user'],password = self.config_param['passwd'],host = self.config_param['host'],port = self.config_param['port'],database = self.config_param['dbname'])

    except psycopg2.OperationalError as error_message:
      print('Failed: Connecting to database.')

    else:
      self.cursor = self.connection.cursor()
      self.connected = True

  def close(self):
    """ Close the PostgreSQL database connection. """
    self.cursor.close()
    self.connection.close()
    self.connected = False

  def validateConnection(self): # TODO: REMOVE!!!
    """
    Connection validation to PostgreSQL DB.
    :return: version + DSN parameters (string)
    """
    # Connect to database
    self.connect()

    # Check Postgres version and print it
    self.cursor.execute("SELECT version();")
    record = self.cursor.fetchone()
    print('You are connected to:', record[0])

    # Extract the dictionary and print Data Source Name parameters
    dsn_parameters = self.connection.get_dsn_parameters()
    for key, value in dsn_parameters.items():
      print("{}: {}".format(key, value))

    self.close()

  def execute(self, statement, values=None):
    """ Execute database query. """
    if self.connected:
      try:
        self.cursor.execute(statement, (values))
      except psycopg2.Error as error_msg:
        print(error_msg)

      if statement.upper().startswith('SELECT'):
        data = self.cursor.fetchall()
        return data
      else:
        self.connection.commit()
        return(self.cursor.rowcount)




# PoC
#if __name__ == '__main__':
#  db = DB()
#  query = "INSERT INTO account(account_name, account_url, account_text, account_reg_date, account_webpage, account_pic_url, account_verified) VALUES(%s, %s, %s, %s, %s, %s, %s)"
#  values = ('testtest', 'https://lol.com', 'this is a test msg', int(0), 'https://lol.cn', 'http://lol.no', 'false')
#  if db.execute(query, values):
#    print("Row inserted in DB")