import random
import smtplib

server= smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("sarthaksahoo32@gmail.com","otcgcrrsidgkwlwk")

otp=''.join([str(random.randint(0,9)) for i in range (4)])

server.sendmail('sarthaksahoo32@gmail.com',
                "sanjuktaranisahoo6@gmail.com",
    "Hi there your otp is:" +str(otp))
