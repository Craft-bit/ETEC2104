from asyncio.windows_events import NULL

accounts = {}

class AccountError(Exception):
    def __init__(self, reason):
        super().__init__(reason)

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def addAccount(username, password):
    if username in accounts:
        raise AccountError("Username already in use: enter a different username.")
    elif username is None or password is None:
        raise AccountError("Must input something for username and/or password.")
    elif username == "" or password == "":
        raise AccountError("Must input something for username and/or password.")
    u = Account(username, password)
    accounts[username] = u

def clear():
    global accounts
    accounts = {}