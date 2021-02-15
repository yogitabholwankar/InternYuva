
from twilio.rest import Client 
import random

otp = random.randint(11111,99999)


account_sid = 'ACffe0282cbc8dcdd87fea5c58b8292f9c' 
auth_token = '12ff3b8f0492dd1ff55f6643de4e768a'
# customer_number = '+917011101001'
def send_otp(account_sid , auth_token , customer_number):
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create( 
                                from_= +15108265123,
                                body = str(otp) +' is your MySchool OTP. \nDo not share it with anyone.',
                                to = customer_number 
                            ) 
    print(message.sid)
