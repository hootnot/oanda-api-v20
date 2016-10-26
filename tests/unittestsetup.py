""" initialization of unittests and data for unittests """

import time
environment = "practice"

# calculate expiryDate as an offset from today
# now + 5 days
days = 5
expiryDate = time.strftime("%Y-%m-%dT%H:%M:%S",
                           time.localtime(int(time.time() + 86400*days)))


def fetchTestData(responses, k):
    resp = responses[k]['response']
    params, data = None, None
    try:
        data = responses[k]['body']
    except:
        pass

    try:
        params = responses[k]['params']
    except:
        pass

    return (resp, data, params)


def auth():
    access_token = None
    account = None
    currency = None
    with open("tests/account.txt") as A:
        account, currency = A.read().strip().split("|")
    with open("tests/token.txt") as T:
        access_token = T.read().strip()

    if account == "99999999|EUR":
        raise Exception(
              "\n"
              "**************************************************\n"
              "*** PLEASE PROVIDE YOUR account in account.txt ***\n"
              "*** AND token IN token.txt TO RUN THE TESTS    ***\n"
              "**************************************************\n")

    return account, currency, access_token
