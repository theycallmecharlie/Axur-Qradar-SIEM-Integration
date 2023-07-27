import time
import sys

import requests


class Search:
    def __init__(self, TENANT_TOKEN):
        self.tenant_token = TENANT_TOKEN

    def createFilter(self):
        header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.tenant_token}'
        }
        payload = {
            "queries": [
                {
                    "fieldName": "current.type",
                    "values": [
                        "code-secret-leak",
                        "corporate-credential-leak",
                        "database-exposure",
                        "other-sensitive-data",
                        "dw-activity",
                        "data-exposure-website",
                        "data-sale-website",
                        "fraud-tool-scheme-website",
                        "suspicious-activity-website",
                        "data-exposure-message",
                        "data-sale-message",
                        "fraud-tool-scheme-message",
                        "suspicious-activity-message",
                        "infrastructure-exposure",
                        "fake-mobile-app",
                        "fake-social-media-profile",
                        "fraudulent-brand-use",
                        "malware",
                        "paid-search",
                        "phishing",
                        "similar-domain-name",
                        "unauthorized-distribution",
                        "unauthorized-sale",
                        "executive-card-leak",
                        "executive-credential-leak",
                        "executive-fake-social-media-profile",
                        "executive-personalinfo-leak"
                    ],
                    "operation": "OR"
                },
                {
                    "fieldName": "current.open.date",
                    "values": [
                        f"{int(time.time() - int(60)) * 1000}"
                    ],
                    "operation": "GREATER_THAN_OR_EQUAL"
                }
            ],
            "operation": "AND"
        }
        queryId = requests.post(
            f"https://api.axur.com/gateway/1.0/api/tickets-filters/filters/tickets", headers=header, json=payload)
        print(f"Query ID: {queryId.json()['queryId']}")
        return self.retrieveFilterResults(queryId.json()['queryId'], self.tenant_token)

    def retrieveFilterResults(self, queryId, TENANT_TOKEN):
        header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {TENANT_TOKEN}'
        }
        tickets = requests.get(
            f"https://api.axur.com/gateway/1.0/api/tickets-filters/filters/tickets?q={queryId}", headers=header)
        tickets = tickets.json()['tickets']
        if len(tickets) >= 1:
            print(f"{len(tickets)} found, retrieving information")
            return tickets
        else:
            print("No tickets to retrieve, passing")
            sys.exit(1)
