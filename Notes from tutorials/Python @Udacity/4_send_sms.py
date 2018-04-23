from twilio.rest import TwilioRestClient 
# We are telling the computer: 
# There is a folder named rest inside twilio, 
# and inside the folder there is a *class* called TwilioRestClient

# Your account sid and auth token from twilio.com/user/account 
account_sid = "AC549aa63960668d37c9a2ddb9f0da4c6b"
auth_token = "da5f33794ca71650402d007ea832c2f8"

# The instance is called "client"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
	body = "Steve please?! I love you <3", 
	to = "+16126154486",
	from_="+16122604617")

print message.sid


## Or 
# from twilio import rest 

# account_sid = "AC549aa63960668d37c9a2ddb9f0da4c6b"
# auth_token = "da5f33794ca71650402d007ea832c2f8"
# client = rest.TwilioRestClient(account_sid, auth_token)

# message = client.sms.messages.create(
# 	body = "Steve please?! I love you <3", 
# 	to = "+16126154486",
# 	from_="+16122604617")

# print message.sid