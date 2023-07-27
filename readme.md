Create a ".env" file containing the following attributes:

*Tenant separated by "," if u have more than one on your console

```
MAIL=
PW=
TENANT=
```

Set the "fieldname" on "/src/Search.py" to "current.incident.date" 
if you want to send only incident events to SIEM

Config the IP Destination on "/src/BuildPayload.py"

```
handler = logging.handlers.SocketHandler('<destination_ip>', 514)
```

Set your recurrence to run the script in "/src/Search.py"

Create a crontab

Example: runs the script every minute

```
 * * * * * /bin/python3 /root/axur/app.py
```

Event Sample

```
LEEF:2.0|Axur One|Digital Protection|1.0|eventid|key=	customer=	reference=	ticket.last-update.date=	ticket.creation.date=	ticket.tags=	current.status=	current.credential.username=	current.incident.date=	current.close.date=	current.resolution.reason=	current.credential.password.type=	current.type=	current.credential.first-seen=	current.credential.password.value=	current.open.date=	current.resolution=	current.assets=	current.leak.sources=	detection.status=	detection.credential.username=	detection.incident.date=	detection.close.date=	detection.resolution.reason=	detection.credential.password.type=	detection.type=	detection.credential.first-seen=	detection.credential.password.value=	detection.open.date=	detection.resolution=	detection.assets=	detection.leak.sources=
```