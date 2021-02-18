
from twilio.rest import Client 
import random


def generate_opt():
    n=random.randrange(1000,9999)
    return n

# otp=1234

# otp = generate_opt()



# customer_number = '+917011101001'

def send_otp(customer_number,current_otp):
    account_sid = 'ACffe0282cbc8dcdd87fea5c58b8292f9c'
    auth_token = '12ff3b8f0492dd1ff55f6643de4e768a'
    client = Client(account_sid, auth_token)
    # current_otp=otp
    customer_number_='+91'+str(customer_number)
    message = client.messages.create(
                                body=str(current_otp) +' is your MySchool OTP.\nDo not share it with anyone.',
                                from_='+15108265123',
                                to=customer_number_
                            )
    return



