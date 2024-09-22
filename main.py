import discord
from discord.ext import commands
import asyncio
import aiohttp
import random

token = "MTI4MzQyODE3MjM5MzYxMTM0NQ.... (user)"

headers = {
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,haw;q=0.7",
    "authorization": token,
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "pl",
    "x-discord-timezone": "Europe/Budapest",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6ImNhbmFyeSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNzY0MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==",
    "cookie": "__dcfduid=756025a02a8f11ef9dd5912419f2cc0b; __sdcfduid=756025a12a8f11ef9dd5912419f2cc0b35c0dd899d1fee1ba86b644e53b857db4cfc5ae469f8fb6454c777481d85c7f2; __stripe_mid=14b4f822-28bc-45d0-96ba-b41d6c1b8688330471; cf_clearance=NPDJvy3Hbc6xvwn.UrCO1xsVS2IrTjEBZ_6kCQ2dSBY-1719905098-1.0.1.1-uFDKAIngsyH1WVSRK7JQCl7g_7PabxBuIfsv3oUPv_5hpaVaGeJhR5bNYWEXTcpODXhfhGLnnRxVKc0trePYMA; __cfruid=7158c03c918d7a7f88774a5365f2784d6eff3ef2-1720088042; OptanonConsent=isIABGlobal=false&datestamp=Thu+Jul+04+2024+13%3A43%3A03+GMT%2B0200+(Central+European+Summer+Time)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0&AwaitingReconsent=false; locale=pl; dbind=81d19aa3-9bbc-40a9-a540-0962e3d0657e; _cfuvid=l0LcPDjwUsXgelgu1dFG62b9s8Soarv5e7nYCoOGybA-1720095334746-0.0.1.1-604800000",
    "Referer": "https://canary.discord.com/channels/738914241595310160/1187293709180604425",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
  }

invite_link = 'https://discord.gg/invitehere'

channel_messages = [
    'j4j dm',
    'j4j dm me',
    'j4j fast',
    'j4j dm',
    'dm j4j rn',
    'dm j4j',
    'Dm me j4j',
    'J4J dm',
    'J4j',
    'j4j dm asap',
    'j4j anyone',
    'j4j no bot',
    'j4j dm me fast',
    'j4j insta reply',
    'j4j instant',
    'j4j dm me now'
]

dmessages = [
    'j4j fast and verify' + invite_link,
    invite_link + ' j4j fast bro and verify',
    invite_link + ' fast join and verify or',
    'join and verify fast ' + invite_link
]

remessages = [
    'bro verify',
    'bruh verify',
    'bro u have to verify',
    'and verify pls',
    'pls verify',
    'verify?'
]

antibotmessages = [
    'bro im not bot a4a',
    'not bot',
    'bro im not bot a4a fast or im reporting',
    'im not bot wtf',
    'bro not bot pls a4a',
    'bro wdym bot join now pls'
]

already_messaged = []
already_remessaged = []
already_botmessaged = []

channels = {
    
}

bot = commands.Bot(command_prefix=None)

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        channels[message.channel.id] = True 
        return

    channels[message.channel.id] = False
    
    if message.channel.type == discord.ChannelType.private:
        if 'bot' in message.content:
            if message.author.id not in already_botmessaged:
                await message.channel.send(random.choice(antibotmessages))
                already_botmessaged.append(message.author.id)
        await asyncio.sleep(random.randint(3, 6))
        if message.author.id in already_messaged:
            if message.author.id in already_remessaged:
                return
            else:
                await message.channel.send(random.choice(remessages))
                already_remessaged.append(message.author.id)
        else:
            await message.channel.send(random.choice(dmessages))
            already_messaged.append(message.author.id)

@bot.event
async def on_ready():
    print(bot.user.name)
    while True:
        try:
            for guild in bot.guilds:
                for channel in guild.text_channels:
                    if 'j4j' in channel.name:
                        if channels.get(channel.id, False):
                            continue  

                        print(f"Sending to {channel.name}")
                        async with aiohttp.ClientSession() as session:
                            await session.post(f'https://canary.discord.com/api/channels/{channel.id}/messages', json={
                                "mobile_network_type": "unknown",
                                "content": random.choice(channel_messages),
                                "tts": False,
                                "flags": 0,
                                "nonce": 1283435039668830208 + random.randint(1000, 100000)}, headers=headers)
                            await session.close()

                        channels[channel.id] = True

        except Exception as e:
            print(f"Error: {e}")
        await asyncio.sleep(random.randint(45, 75))

bot.run(token)