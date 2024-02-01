import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None)

GUILD_ID = 1052930063810699294
CHANNEL_ID = 1075414521918783579

@client.event
async def on_ready():
    os.system('clear')
    print(f'Logged in as {client.user} ({client.user.id})')
    vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id = CHANNEL_ID)
    await vc.guild.change_voice_state(channel=vc, self_mute=False, self_deaf=True)
    print(f"Successfully joined {vc.name} ({vc.id})")

    guild = client.get_guild(1052930063810699294)  # Replace GUILD_ID with your server's ID
    member_count = guild.member_count
    guild_name = guild.name
    await client.change_presence(activity=discord.Streaming(name=f'{member_count} คน', url='https://www.youtube.com/watch?v=YcbPB2Zu9T0'))
    print("Bot is connected to all of the available servers in the bots mainframe.")

keep_alive()
client.run(os.getenv("TOKEN"), bot=True)

