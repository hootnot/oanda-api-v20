"""simple auth method for examples."""


def exampleAuth():
    accountID, token = None, None
    with open("account.txt") as I:
        accountID = I.read().strip()
    with open("token.txt") as I:
        token = I.read().strip()
    return accountID, token
