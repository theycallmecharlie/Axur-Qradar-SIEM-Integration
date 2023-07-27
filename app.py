from src.Auth import Authentication
from src.Search import Search
from src.BuildPayload import Ticket

from dotenv import dotenv_values
import os

global URL
URL = "https://api.axur.com/gateway/1.0/api"
CONFIG = dict(dotenv_values())
MAIL = CONFIG['MAIL']
PASSWORD = CONFIG['PW']
TENANT = CONFIG['TENANT']

if __name__ == "__main__":
    try:
        TENANT = TENANT.split(",")
        for tenant in TENANT:
            auth = Authentication(MAIL, PASSWORD, tenant)
            bearer = auth.authenticate()

            newsearch = Search(bearer)
            tickets = newsearch.createFilter()

            event = Ticket(tickets, bearer)
            event.retrieveTicket()

    except Exception as err:
        print(err)
