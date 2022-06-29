import os
import discord
import datetime
from time import sleep
channel = ''
my_secret = '' # Your token here
client = discord.Client()
send = True

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return 
  if '//channel' in message.content:
    await message.channel.send('Set channel to ' + str(message.channel))
    channel = message.channel
    used_channel = True
    
    while True:
      time = datetime.datetime
      
      if time.weekday == 3 and time.hour - 4 == 1 and time.minute == 0 and time.second == 0:
        
        await message.channel.send('https://www.youtube.com/watch?v=CMjdxUZeXj4')
        print('it worked')
      sleep(1)

client.run(my_secret)