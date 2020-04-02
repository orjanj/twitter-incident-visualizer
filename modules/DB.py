#!/usr/bin/python3
import psycopg2, sys
from Config import Config # TODO: Make it prettier

class DB:
  """ DB initializes and manipulates PostgreSQL databases."""

  def __init__(self):
    """ Instance constructor for connecting to an existing database.
    :return: none
    """
    self.connected = False

    # Initialize configuration parameters for the database
    config = Config()
    self.config_param = config.getConfigParameter('postgresql') # TODO: Lag et config objekt kun i mining fila og fjern denne linja fra alle objektfiler

    # Connect to database
    self.connect()

  def printError(self, error_message): # TODO: Remove this function if it's not going to be used
    # Get details about the exception
    error_type, error_object, traceback = sys.exc_info()

    # Get line number when exception occured
    line_number = traceback.tb_lineno

    # Print connect() error
    print("\npsycopg2 ERROR:", error_message, "on line number:", line_number)
    print("psycopg2 traceback:", traceback,"-- type:", error_type)

    #psycopg2 extensions.Diagonstics object attribute
    print("\nextensions.Diagnostics:", error_message.diag) # TODO: Check this shiet

    print("pgerror:", error_message.pgerror)      # TODO: Consider if there should be a 'None' check
    print("pgcode:", error_message.pgcode, "\n")  # TODO: Consider if there should be a 'None' check

    # Exit the program due to an error
    sys.exit(1)


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

  def validateConnection(self): # TODO: Consider removing this, probably not going to be used
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


  def execute(self, statement, values):
#  def execute(self, statement):
    """ Execute database query. """
    if self.connected:
      self.cursor.execute(statement, (values))
#      self.cursor.execute(statement)
      if statement.upper().startswith('SELECT'):
        data = self.cursor.fetchall()
        return data
#        print(data) # debugging
      else:
        self.connection.commit()
#        print(self.cursor.rowcount) # debugging
        return self.cursor.rowcount


# PoC
if __name__ == '__main__':
  db = DB()
  query = "INSERT INTO account(account_name, account_url, account_text, account_reg_date, account_webpage, account_pic_url, account_verified) VALUES(%s, %s, %s, %s, %s, %s, %s)"
  values = ('testtest', 'https://lol.com', 'this is a test msg', int(0), 'https://lol.cn', 'http://lol.no', 'false')
  if db.execute(query, values):
    print("Row inserted in DB")

# Can also run the following query, to validate the insertion, from the `tiv` user on the server in psql: SELECT * FROM account;

  # Validate connection
  #db.validateConnection()




# References:
# https://www.psycopg.org/docs/module.html
# https://kb.objectrocket.com/postgresql/python-error-handling-with-the-psycopg2-postgresql-adapter-645
# https://stackoverflow.com/questions/24661754/necessity-of-explicit-cursor-close
# https://www.psycopg.org/docs/cursor.html
# https://www.postgresqltutorial.com/postgresql-python/connect/
# https://codereview.stackexchange.com/questions/134535/a-class-to-create-and-modify-sqlite3-databases-with-a-terminal