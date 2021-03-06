DEBUG = True
PORT = 8080 
HOST = "0.0.0.0"
SQLALCHEMY_ECHO = False
SECRET_KEY = "SOME SECRET"

"""
# MYSQL
mysql_db_username = 'root'
mysql_db_password = ''
mysql_db_name = 'lakadee'
mysql_db_hostname = 'localhost'

# MySQL
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=mysql_db_username,
                                                                                        DB_PASS=mysql_db_password,
                                                                                        DB_ADDR=mysql_db_hostname,
                                                                                        DB_NAME=mysql_db_name)
"""

SQLALCHEMY_DATABASE_URI = 'sqlite:///lakadee.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Email Server Configuration
MAIL_DEFAULT_SENDER = "leo@localhost"

PASSWORD_RESET_EMAIL ="""
    Hi,
      Please click on the link below to reset your password
      <a href="/forgotpassword/{token}> Click here </a>"""
