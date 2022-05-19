from keep_alive import keep_alive
import os
import discord
import random

client = discord.Client()
print("Client")
print(client)
@client.event

async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event

async def on_message(message):
  # if message.author == client.user:
  #   return
  
  msg = message.content.lower()
  chan_id = message.channel.id
  channel = client.get_channel(chan_id)

  if msg.startswith('!traits'):
    num = random.randint(0,5)
    await select_category(num, chan_id)
    num2 = random.randint(0,5)
    if num2 == num:
      num2 += 1
    await select_category(num2, chan_id)
  
  if msg.startswith('!pick'):
    category = msg.split()[1].lower()
    await select_from(category, chan_id)



async def select_from(word, chan_id):
  print(word)
  channel = client.get_channel(chan_id)
  num = random.randint(1,100)
  print(num)
  if word == "background":
      if num < 10:
        await channel.send("Bar")
      elif 10 < num < 41:
        await channel.send("Bathroom")
      elif 40 < num < 61:
        await channel.send("Dance Floor")
      else:
        await channel.send("VIP")
        
  if word == "species":
      if num < 2:
          await channel.send("aquatic blue")
      elif 1 < num < 3:
          await channel.send("aquatic green")
      elif 2 < num < 4:
          await channel.send("aquatic indigo")
      elif 3 < num < 5:
          await channel.send("aquatic orange")
      elif 4 < num < 6:
          await channel.send("aquatic pink")
      elif 5 < num < 11:
          await channel.send("aquatic red")
      elif 10 < num < 12:
          await channel.send("aquatic violet")
      elif 11 < num < 16:
          await channel.send("aquatic zombie")
      elif 15 < num < 17:
          await channel.send("devil blue")
      elif 16 < num < 18:
          await channel.send("devil green")
      elif 17 < num < 19:
          await channel.send("devil indigo")
      elif 18 < num < 20:
          await channel.send("devil orange")
      elif 19 < num < 24:
          await channel.send("devil pink")
      elif 23 < num < 25:
          await channel.send("devil red")
      elif 24 < num < 29:
          await channel.send("devil violet")
      elif 28 < num < 35:
          await channel.send("devil zombie")
      elif 34 < num < 36:
          await channel.send("humanoid blue")
      elif 35 < num < 37:
          await channel.send("humanoid green")
      elif 36 < num < 38:
          await channel.send("humanoid indigo")
      elif 37 < num < 39:
          await channel.send("humanoid orange")
      elif 38 < num < 43:
          await channel.send("humanoid pink")
      elif 42 < num < 44:
          await channel.send("humanoid red")
      elif 43 < num < 48:
          await channel.send("humanoid violet")
      elif 47 < num < 54:
          await channel.send("humanoid zombie")
      elif 53 < num < 55:
          await channel.send("imp blue")
      elif 54 < num < 56:
          await channel.send("imp green")
      elif 55 < num < 57:
          await channel.send("imp indigo")
      elif 56 < num < 58:
          await channel.send("imp orange")
      elif 57 < num < 62:
          await channel.send("imp pink")
      elif 61 < num < 63:
          await channel.send("imp red")
      elif 62 < num < 69:
          await channel.send("imp zombie")
      elif 68 < num < 75:
          await channel.send("mr melon")
      elif 74 < num < 76:
          await channel.send("ogre blue")
      elif 75 < num < 77:
          await channel.send("ogre green")
      elif 76 < num < 81:
          await channel.send("ogre indigo")
      elif 80 < num < 82:
          await channel.send("ogre orange")
      elif 83 < num < 88:
          await channel.send("ogre pink")
      elif 87 < num < 89:
          await channel.send("ogre red")
      elif 88 < num < 93:
          await channel.send("ogre violet")
      elif 92 < num < 101:
          await channel.send("ogre zombie")
        
  if word == "clothes":
    if num < 5:
        await channel.send("angel wings")
    elif 4 < num < 6:
        await channel.send("basketball jersey blue")
    elif 5 < num < 7:
        await channel.send("basketball jersey green")
    elif 6 < num < 8:
        await channel.send("basketball jersey red")
    elif 7 < num < 9:
        await channel.send("basketball jersey yellow")
    elif 8 < num < 11:
        await channel.send("collared black")
    elif 10 < num < 13:
        await channel.send("collared white")
    elif 12 < num < 15:
        await channel.send("fancy dress black")
    elif 14 < num < 17:
        await channel.send("fancy dress red")
    elif 16 < num < 18:
        await channel.send("football jersey blue")
    elif 17 < num < 19:
        await channel.send("football jersey green")
    elif 18 < num < 20:
        await channel.send("football jersey red")
    elif 19 < num < 21:
        await channel.send("football jersey yellow")
    elif 22 < num < 25:
        await channel.send("hawaiian blue")
    elif 24 < num < 27:
        await channel.send("hawaiian red")
    elif 25 < num < 28:
        await channel.send("hoodie black")
    elif 27 < num < 32:
        await channel.send("king robe")
    elif 31 < num < 36:
        await channel.send("labcoat")
    elif 35 < num < 40:
        await channel.send("mcw classic")
    elif 39 < num < 44:
        await channel.send("mcw orlando")
    elif 43 < num < 46:
        await channel.send("mesh shirt")
    elif 45 < num < 50:
        await channel.send("mrmelon suit")
    elif 49 < num < 53:
        await channel.send("necromancer shawl")
    elif 52 < num < 55:
        await channel.send("polkadot dress black")
    elif 54 < num < 57:
        await channel.send("polkadot dress red")
    elif 56 < num < 61:
        await channel.send("space suit")
    elif 60 < num < 65:
        await channel.send("steam punk")
    elif 64 < num < 67:
        await channel.send("suit black tie")
    elif 66 < num < 69:
        await channel.send("suspenders black")
    elif 68 < num < 71:
        await channel.send("suspenders red")
    elif 70 < num < 72:
        await channel.send("track suit black")
    elif 71 < num < 73:
        await channel.send("track suit blue")
    elif 72 < num < 74:
        await channel.send("track suit green")
    elif 73 < num < 75:
        await channel.send("track suit red")
    elif 74 < num < 76:
        await channel.send("track suit yellow")
    elif 75 < num < 77:
        await channel.send("t shirt black")
    elif 76 < num < 78:
        await channel.send("t shirt blue")
    elif 77 < num < 79:
        await channel.send("t shirt green")
    elif 78 < num < 83:
        await channel.send("t shirt melon")
    elif 82 < num < 84:
        await channel.send("t shirt red")
    elif 83 < num < 85:
        await channel.send("t shirt yellow")
    elif 84 < num < 89:
        await channel.send("tuxedo")
    elif 88 < num < 90:
        await channel.send("vest black")
    elif 89 < num < 91:
        await channel.send("v neck black")
    elif 90 < num < 92:
        await channel.send("v neck blue")
    elif 91 < num < 93:
        await channel.send("v neck green")
    elif 92 < num < 94:
        await channel.send("v neck red")
    elif 93 < num < 95:
        await channel.send("v neck yellow")
    elif 94 < num < 96:
        await channel.send("wizard robe")
    elif 95 < num < 101:
        await channel.send("wsb suit")

  if word == "head":
    if num < 3:
      await channel.send("antlers")
    elif 2 < num < 6:
        await channel.send("baseball cap")
    elif 5 < num < 8:
        await channel.send("black horns")
    elif 7 < num < 11:
        await channel.send("bucket hat")
    elif 10 < num < 14:
        await channel.send("bull horns")
    elif 13 < num < 17:
        await channel.send("cat ears")
    elif 16 < num < 19:
        await channel.send("demon horns")
    elif 18 < num < 22:
        await channel.send("fedora")
    elif 21 < num < 24:
        await channel.send("fire blue")
    elif 23 < num < 26:
        await channel.send("fire red")
    elif 25 < num < 29:
        await channel.send("flower")
    elif 28 < num < 32:
        await channel.send("halo")
    elif 31 < num < 39:
        await channel.send("king crown")
    elif 38 < num < 41:
        await channel.send("long horns")
    elif 40 < num < 43:
        await channel.send("mad scientist")
    elif 42 < num < 51:
        await channel.send("melon helmet")
    elif 50 < num < 53:
        await channel.send("mohawk")
    elif 52 < num < 60:
        await channel.send("mr melon")
    elif 59 < num < 65:
        await channel.send("necromancer hood")
    elif 64 < num < 68:
        await channel.send("pirate hat")
    elif 67 < num < 70:
        await channel.send("single horn")
    elif 69 < num < 72:
        await channel.send("single horn white")
    elif 71 < num < 74:
        await channel.send("skull")
    elif 73 < num < 76:
        await channel.send("small horns")
    elif 75 < num < 83:
        await channel.send("space helmet")
    elif 82 < num < 85:
        await channel.send("spines")
    elif 84 < num < 88:
        await channel.send("steam punk hat")
    elif 87 < num < 92:
        await channel.send("top hat")
    elif 91 < num < 95:
        await channel.send("wizard hat")
    elif 94 < num < 101:
        await channel.send("wsb hair")

  if word == "eyes":
    if num < 6:
        await channel.send("bead")
    elif 5 < num < 11:
        await channel.send("bead angry")
    elif 10 < num < 16:
        await channel.send("big")
    elif 15 < num < 21:
        await channel.send("big angry")
    elif 21 < num < 26:
        await channel.send("cyclops")
    elif 25 < num < 31:
        await channel.send("cyclops laser")
    elif 30 < num < 41:
        await channel.send("eyepatch")
    elif 40 < num < 46:
        await channel.send("glasses")
    elif 45 < num < 51:
        await channel.send("high")
    elif 50 < num < 56:
        await channel.send("laser")
    elif 55 < num < 61:
        await channel.send("none")
    elif 60 < num < 71:
        await channel.send("round sunglasses")
    elif 70 < num < 76:
        await channel.send("sad")
    elif 75 < num < 81:
        await channel.send("simple")
    elif 80 < num < 86:
        await channel.send("simple angry")
    elif 85 < num < 91:
        await channel.send("sleeping")
    elif 90 < num < 101:
        await channel.send("wsb sunglasses")

  if word == "mouth":
      if num < 7:    
        await channel.send("angry")
      elif 6 < num < 17:
        await channel.send("burp")
      elif 16 < num < 27:    
          await channel.send("cat")
      elif 26 < num < 40:    
          await channel.send("cool")
      elif 39 < num < 50:    
          await channel.send("dumb")
      elif 49 < num < 56:    
          await channel.send("mischievous")
      elif 55 < num < 69:    
          await channel.send("none")
      elif 68 < num < 75:    
          await channel.send("open")
      elif 74 < num < 81:    
          await channel.send("sad")
      elif 80 < num < 91:    
          await channel.send("sharp")
      elif 90 < num < 101:    
          await channel.send("tongue")  

async def select_category(number, chan_id):
  categories = {
      0: "background",
      1: "species",
      2: "clothes",
      3: "head",
      4: "eyes",
      5: "mouth",
      6: "background"
    }
  channel = client.get_channel(chan_id)
  category = categories[number]
  await channel.send("!pick " + category)

def start():
  keep_alive()
  client.run(process.env.CLIENT_SECRET)
