import requests
import logging
import logging.handlers


class Ticket:
    def __init__(self, tickets, TENANT_TOKEN):
        self.tickets = tickets
        self.tenant_token = TENANT_TOKEN

    def retrieveTicket(self):
        header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.tenant_token}'
        }
        for ticketKey in self.tickets:
            ticket = requests.get(
                f"https://api.axur.com/gateway/1.0/api/tickets-core/tickets/{ticketKey['key']}", headers=header)
            text = requests.get(
                f"https://api.axur.com/gateway/1.0/api/tickets-texts/texts/tickets/{ticketKey['key']}", headers=header)
            text = text.json()['texts']
            ticket = ticket.json()
            ticket['ticket']['texts'] = str(text)
            BuildPayload.buildPayload(ticket)


class BuildPayload:
    def __init__(self, ticket):
        self.ticket = ticket

    def buildPayload(ticket):
        payload = []
        payload.append(f"key={ticket['ticket']['key']}")
        payload.append(f"customer={ticket['ticket']['customer']}")
        payload.append(f"reference={ticket['ticket']['reference']}")

        for i in ticket['ticket']['fields']:
            if 'value' in i:
                payload.append(f"{i['key']}={i['value']}")
            if 'values' in i:
                payload.append(f"{i['key']}={i['values']}")
        for j in ticket['detection']['fields']:
            if 'value' in j:
                payload.append(f"{j['key']}={j['value']}")
            if 'values' in j:
                payload.append(f"{j['key']}={j['values']}")

        prefix = f"LEEF:2.0|Axur One|Digital Protection|1.0|eventid"
        payload = '\t'.join(payload)
        payload = f"{prefix}|{payload}"
        event_ids = ["code-secret-leak",
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
                     "executive-personalinfo-leak"]

        eventid = next(ticket_type for ticket_type in ticket["detection"]["fields"] if ticket_type["value"] in event_ids)
        payload = payload.replace("eventid", eventid["value"])
        print(payload)
        my_logger = logging.getLogger('MyLogger')
        my_logger.setLevel(logging.INFO)
        handler = logging.handlers.SocketHandler('<destination_ip>', 514)
        my_logger.addHandler(handler)
        my_logger.info(payload)
