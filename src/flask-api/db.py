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