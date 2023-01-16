import database as db

user_db = db.UserDatabase()
server_db = db.ServerDatabase()

print(user_db.user_exists(username="qazmoke"))
print(server_db.add_user(username="qazmoke", password="qazmoke"))
print(server_db.add_card(username="qazmoke", card="Void"))
print(user_db.user_exists(username="qazmoke"))
print(server_db.update_password(username="qazmoke", password="zaqqazx"))
