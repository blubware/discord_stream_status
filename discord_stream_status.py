import discord
from discord.ext import commands
from clear_screen import clear

def discord_stream_status():

    clear()
    token = input('Token > ')
    text = input('Text > ')
    url = input('URL > ')

    client = discord.Client()

    @client.event
    async def on_connect():
        stream = discord.Streaming(name = text, url = f'https://twitch.tv/{url}')
        await client.change_presence(activity=stream)
        
    client.run(token)

if __name__ == '__main__':
    discord_stream_status()