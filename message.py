from discord.message import Message
from secret import nasa_token
from client import client
import random
import requests

@client.event
async def on_message(message: Message):
    
    PREFIX = "%";
    args = message.content.split(" ");
    command = args[0][len(PREFIX)::];

    if message.author == client.user or not message.content.startswith(PREFIX):
        return

    elif command == "help":
        help_msg = """```md
# Welcome to ThanosBot help menu :)
%  - Thanos's default prefix
[!] - Mandatory parameter
[?] - Optional parameter
You can also check Thanos's source code at:
https://www.github.com/gumbarros/thanos-bot
# %thanos 
- Check if Thanos is alive
# %standups
- JJConsulting members exclusive JJ Stand Ups meeting
# %nasa
- Send NASA image of the day
# %dog,[?BREED]
- Send a nice dog from the DogAPI (https://dog.ceo/dog-api)
# %person,[?GENDER]
- Send a I.A generated person.
# %nathan
- Nathan.
        ```"""
        await message.channel.send(help_msg)

    elif command == "thanos":
        await message.channel.send("Hello, " + message.author.nick + "!");
        
    elif command == "standups":

        await message.channel.send("⚠️ =-=  Stand Ups Stand Ups =-= ⚠️");

        members = message.channel.guild.members
        random.shuffle(members)

        names = ""

        for member in members:
            if not member.bot:
                names+=f"➡️ {member.nick}\n\n"

        await message.channel.send(names)
        await message.channel.send("⚠️ =-=-=-=-=-=-=-=-=-=-=-=-= ⚠️")

    elif command == "thanos":
        await message.channel.send("Hello, " + message.author.nick + "!");

    elif command == "nasa":
        response = requests.get(f'https://api.nasa.gov/planetary/apod?hd=true&api_key={nasa_token}')

        json = response.json()
        
        await message.channel.send(json['hdurl'])
        await message.channel.send(json['explanation'])

    elif command == "nathan":
        await message.channel.send("Nathan")

    elif command == "dog":
        if args[1] == "help":
            response = requests.get("https://dog.ceo/api/breeds/list/all")

            json = response.json()

            await message.channel.send("=-= List of Breeds -=-")

            breeds = ''

            for breed in json['message']:
                breeds += f"➡️ {breed}\n\n"
            
            await message.channel.send(breeds)
            await message.channel.send("=-=-=-=-=-=-=-=-=-=")

        else:
            response = requests.get(f"https://dog.ceo/api/breed/{args[1]}/images/random")

            json = response.json()
            
            if response.status_code != 404: await message.channel.send(json['message']);
            else:
               response = requests.get(f"https://dog.ceo/api/breeds/image/random")

               json = response.json()

               await message.channel.send(json['message']);

    elif command == "person":

        gender = ''

        if 'male' in args[1] or 'female' in args[1]:
            gender = args[1]

        response = requests.get(f"https://fakeface.rest/face/json?gender={gender}")
        json = response.json()

        await message.channel.send(json['image_url'])