import boto3

message1 = 'We have noticed that you have not been in quarentine for the past 3 days. Please return to your home address. \nTraveling around will only make matters worse for everyon else. \nThank you'

message = 'hi'

client = boto3.client('sns', 'eu-west-1')

client.publish(PhoneNumber = '+447939139857', Message=message)
#client.publish(PhoneNumber = '+447306042191', Message=message)
client.publish(PhoneNumber = '+447853834066', Message=message)
