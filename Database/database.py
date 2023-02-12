import sqlite3
import logging
import ast

try:
    logging.basicConfig(filename="Database\\database.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
except FileNotFoundError:
    logging.basicConfig(filename="database.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")


class _Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.con = sqlite3.connect(self.db_file)

    def _get_data(self, table, columns, condition):
        cursor = self.con.cursor()
        cursor.execute(f"SELECT {columns} FROM {table} WHERE {condition}")
        return cursor.fetchall()

    def _insert_data(self, table, columns, values):
        cursor = self.con.cursor()
        cursor.execute(f"INSERT INTO {table} ({columns}) VALUES ({values})")
        self.con.commit()

    def _update_data(self, table, condition, values):
        cursor = self.con.cursor()
        print(f"UPDATE {table} SET {values} WHERE {condition}")
        cursor.execute(f"UPDATE {table} SET {values} WHERE {condition}")
        self.con.commit()

    def _delete_data(self, table, condition):
        cursor = self.con.cursor()
        cursor.execute(f"DELETE FROM {table} WHERE {condition}")
        self.con.commit()


class ServerDatabase(_Database):
    def __init__(self, db_file="Database\\users.db"):
        super().__init__(db_file)

    def add_user(self, username, password):
        try:
            self._insert_data(
                "users",
                "username, password",
                f"'{username}', '{password}'")

            logging.info(f"successfully added user {username}")
            return True
        except sqlite3.Error:
            logging.critical(f"failed to add user {username}", exc_info=True)
            return False

    def add_card(self, username, card):
        try:
            print(", ".join(self._get_data("users", "cards", f"username = '{username}'")[0]))
            cards = ast.literal_eval(", ".join(self._get_data("users", "cards", f"username = '{username}'")[0]))
            cards[str(len(cards) - 1)] = card
            self._update_data(table="users", values="cards="f'"{str(cards)}"', condition=f"username = '{username}'")

            return True
        except sqlite3.Error:
            logging.critical(f"failed to add card {card} to user {username}", exc_info=True)
            return False

    def delete_user(self, username):
        try:
            self._delete_data("users", f"username='{username}'")
            logging.info(f"successfully deleted user {username}")
            return True
        except sqlite3.Error:
            logging.critical(f"failed to delete user {username}", exc_info=True)
            return False

    def update_password(self, username, password):
        try:
            self._update_data(table="users", values=f"password='{password}'", condition=f"username='{username}'")
            logging.info(f"successfully updated password for user {username}")
            return True
        except sqlite3.Error:
            logging.critical(f"failed to update password for user {username}", exc_info=True)
            return False


class UserDatabase(_Database):
    def __init__(self, db_file="Database\\users.db"):
        super().__init__(db_file)

    def user_exists(self, username):
        try:
            return self._get_data("users", f"username", f"username='{username}'") != []
        except sqlite3.Error:
            return None

    def update_deck(self, username, new_deck):
        try:
            self._update_data("users", f"deck='{new_deck}'", f"username='{username}'")
            logging.info(f"successfully updated deck for user {username}")
            return True
        except sqlite3.Error:
            logging.critical(f"failed to update deck for user {username}", exc_info=True)
            return False
