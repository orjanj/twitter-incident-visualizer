#!/usr/bin/python3
import psycopg2

class DB:
  """ DB initializes and manipulates PostgreSQL databases."""

  def __init__(self, config):
    """ Instance constructor for connecting to an existing database.
    :return: none
    """
    self.connected = False

    # Initialize configuration parameters for the database
    self.config_param = config.getConfigParameter('postgresql')

    # Connect to database
    self.connect()


  def connect(self):
    """ Connect to the PostgreSQL database. """
    try:
      self.connection = psycopg2.connect(user = self.config_param['user'],password = self.config_param['passwd'],host = self.config_param['host'],port = self.config_param['port'],database = self.config_param['dbname'])

    # Catch connection error and print error message
    except psycopg2.OperationalError as error_message:
      print('Failed: Connecting to database.')

    # Set up an connection cursor
    else:
      self.cursor = self.connection.cursor()
      self.connected = True


  def close(self):
    """ Close the PostgreSQL database connection. """

    # Close connection cursor
    self.cursor.close()

    # Close connection
    self.connection.close()

    # Set connected to `false`
    self.connected = False


  def validateConnection(self):
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

    # Close database connection
    self.close()

  def execute(self, statement, values=None):
    """ Execute database query. """
    
    # Check if connection exists
    if self.connected:

      # Try to execute the statement
      try:
        self.cursor.execute(statement, (values))

      # Catch error message and print it
      except psycopg2.Error as error_msg:
        print(error_msg)

      # Check if the statement is a `SELECT` statement or not, if yes; return selected data
      if statement.upper().startswith('SELECT'):
        data = self.cursor.fetchall()
        return data

      # If not, commit changes (such as UPDATE, DELETE, INSERT)
      else:
        self.connection.commit()
        return(self.cursor.rowcount)