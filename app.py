from twilio.rest import Client

my_phone_num = 1234567890 #Enter your own phone number to receive msg and register with same phone number
account_sid = 'Enter account sid'
auth_token = 'Enter auth_token'

client = Client(account_sid, auth_token)

sms = client.messages.create(
    from_="Enter trial number here",
    body="Hello, Sending SMS through Twilio",
    to=my_phone_num

)
print(sms.sid)
