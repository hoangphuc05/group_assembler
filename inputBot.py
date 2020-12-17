import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

picker = {}
receiver = {}


@client.event
async def on_message(message):
    content = message.content.strip().split()
    if len(content) < 1:
        return
    if message.author == client.user:
        return
    if content[0] == "~help":
        await message.channel.send("""
Welcome to project group Generator!
Set reference: `~addReference <Group index (0-1)> <name of picker> <name of person>`
Edit reference: `~editReference <Group index (0-1)> <name of picker> <index of reference> <name of person>`
Import reference: `~importReference <Group index (0-1)> <name of picker> <list of people, seperated by space>`
        """)
    if content[0] == "~addReference":
        if content[1] == "0":
            if content[2] in picker:
                #content[1] is name of picker
                picker[content[2]].append(content[3])
            else:
                picker[content[2]] = [content[3]]
        else:
            if content[2] in receiver:
                #content[1] is name of picker
                receiver[content[2]].append(content[3])
            else:
                receiver[content[2]] = [content[3]]


    #edit reference
    elif content[0] == "~editReference":
        if content[1] == "0":
            if content[2] not in picker:
                message.channel.send(f"{content[2]} doesn't have any reference!")
            else:
                if len(picker[content[2]]) <= (int(content[3]) + 1):
                    #replace reference
                    picker[content[2]][content[3]] = content[4]

                else:
                    message.channel.send(f"{content[1]} doesn't have that many referenecs!")
        else:
            if content[2] not in receiver:
                message.channel.send(f"{content[2]} doesn't have any reference!")
            else:
                if len(receiver[content[2]]) <= (int(content[3]) + 1):
                    #replace reference
                    receiver[content[2]][content[3]] = content[4]
                else:
                    message.channel.send(f"{content[1]} doesn't have that many referenecs!")
    
    elif content[0] == "~importReference":
        if content[1] == "0":
            if content[2] in picker:
                for i, name in enumerate(content):
                    if i > 2:
                        picker[content[2]].append(name)

            else:
                picker[content[2]] = []
                for i, name in enumerate(content):
                    if i > 1:
                        picker[content[2]].append(name)
        
        else:
            if content[2] in receiver:
                for i, name in enumerate(content):
                    if i > 2:
                        receiver[content[2]].append(name)

            else:
                receiver[content[2]] = []
                for i, name in enumerate(content):
                    if i > 1:
                        receiver[content[2]].append(name)

        print(picker[content[1]])
    

    print(picker)
    print(receiver)

client.run(TOKEN)