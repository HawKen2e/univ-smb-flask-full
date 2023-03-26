import mysql.connector

# Configurer la connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="passwordDbUniv01",
  database="identity"
)

if mydb.is_connected():
  print("Connexion à la base de données réussie.")
else:
  print("Impossible de se connecter à la base de données.")

#ajoute un utilisateur dans la db
def add_user():
  cursor = mydb.cursor()
  users = ("pierry", "pierry", "benoit")
  cursor.execute("""INSERT INTO user (login, first_name, last_name ) VALUES (%s, %s, %s)""", users)
  mydb.commit()
  mydb.close()
  return ("donnees ajouté avec succes")

def add_password():
  cursor = mydb.cursor()
  user_password = ("pierry", "benoit")
  cursor.execute("""INSERT INTO user_pw (login_pw, password ) VALUES (%s, %s)""", user_password)
  mydb.commit()
  mydb.close()
  return ("donnees ajouté avec succes")

add_user()
add_password()