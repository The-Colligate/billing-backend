## Pipenv commands
`pipenv install fastapi uvicorn pydantic[email,dotenv] pandas openpyxl`
`pipenv install sqlalchemy python-multipart "python-jose[cryptography]" "passlib[bcrypt]"`

l1 - create, request, request decommissioning 
l2 - approve decommissioning, recommission clients, create invoices, submit renegotiations of downtime (deals with invoices tab)
l3 - approve/reject renegotiations of downtime, generate reports (deals with messages tab)

onboarding 
enforce tier 3 with subs


silver - prepaid; will be disconnected if they don't pay
gold - ultimatum to pay, credit period
platinum - can't be disconnected, prioritized support

silver customers who still owe will be disconnected

COMMANDS
curl ifconfig.me - to get public IP address


TODO
- validate voice/data file
- validate focalpoint phone number
- validate URL for client website
- do focal points get created immediately a client is created or after? (for now, I set it to after) ✅
- confirm wtf revenue is ✅
- search clients
- pagination
- define parent-child relationships 
- calculate loyalty
- resolve whether invoices come in with a timestamp (to sort for recent_invoices route)
- access management
- token expiration
- pending clients (in the design)
- change to Decimal
