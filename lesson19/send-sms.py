from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb62b2f83497e236b361bb7c2867f166d"
# Your Auth Token from twilio.com/console
auth_token = "507096b93d4e316eae35380d332f0d13"

client = Client(account_sid, auth_token)
user = 'sdfdf'
passwrd = '54654'
mobile = '798671767'
message = client.messages.create(
    to="+962"+mobile,
    from_="+12569063699",
    body="your account is : " + user + "\n and your password is: " + passwrd + "")

print(message.sid)
