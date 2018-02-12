
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb6#######################"
# Your Auth Token from twilio.com/console
auth_token  = "50$$$$$$$$$$$$$$$$$$$$$$$$$"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+966666666666666",
    from_="+122222222222222222",
    body="Hello from Python!")

print(message.sid)

