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