from msilib.schema import File
import tweepy
import time
import os
import sys

auth = tweepy.AppAuthHandler("sTZnxzh7GJ3fiS1xz1DNhgFWX", "j5909H4UPIa6zTtSCgfz5U90eJPS6aW6wk5dTunMdtZwkXGaM1")
api = tweepy.API(auth)

handle = 'Gotchiverse'

user = api.get_user(screen_name='aavegotchi')
num_followers = user.followers_count
c=str(num_followers)


while(True):
    #clear_output(wait=True)
    #os.system("cls")
    #os.system("clear")
    sys.stdout = open('Twitter.md','wt')
    fileName=open('Twitter.md','a')
    print(handle + " has " + c + " twitter followers",file=fileName)
    os.system("cls")
    fileName=open('Twitter.md','a')
    print("[[Gotchiverse/Gotchiverse Ecosystem/Ecocystem]]",file=fileName)
    #print(end="\r")
    #print('\033[H\033[J', end='')
    time.sleep(1)
