import os

db_user = os.environ.get('DB_USER') #'my_db_user'
db_password = os.environ.get('DB_PASS') #'my_db_pass_123!'

print(db_user)
print(db_password)

#os.getenv("SECRET_KEY")