import discord
from discord.ext import commands
import datetime
import asyncio
import apikey

TOKEN = apikey.token()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = ">", intents=intents)

@client.event
async def on_ready():
    print(f"CONNECTED\nBot name: {client.user.name}")

    asyncio.create_task(daily())

async def daily():
    while True:
        now = datetime.datetime.now()
        then = now.replace(hour=6, minute=0, second=0, microsecond=0)
        if now > then:
            then += datetime.timedelta(days=1)

        wait_time = (then - now).total_seconds()
        await asyncio.sleep(wait_time)

        channel = client.get_channel(CHANNEL_ID)
        embed = discord.Embed(
            title = 'YOUR_TITLE',
            description = 'YOUR_DESCRIPTION',
            colour = 11875610 #decimal color
        )
        await channel.send(embed = embed)

client.run(TOKEN)
