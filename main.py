import discord
import random
from discord.ext import commands
from discord import app_commands
from asyncio import sleep
from discord.utils import *

intents = discord.Intents.default()
intents.message_content = True



Bot = commands.Bot(command_prefix="YOUR PREFIX", intents=intents)



@Bot.event
async def on_ready():
    print("Ready!")
@Bot.command()
@commands.has_guild_permissions(administrator=True)
async def kick(ctx, member:discord.Member, *, reason=None):
    if reason == None:
        reason="no reason provided"
    await ctx.guild.kick(member)
    await ctx.send(f"User {member.mention} has been kicked for {reason}")
@kick.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        embed = discord.Embed(title='У вас нету прав на пользования данной командой', description='Administrator+', color=0x00ff00)
        await ctx.send(embed=embed)
@Bot.command()
@commands.has_guild_permision(administrator=True)
async def ban(ctx, member:discord.Member, *, reason=None):
    if reason == None:
        reason="no reason provided"
    await ctx.guild.ban(member)
    await ctx.send(f"User {member.mention} has been ban for {reason}")
@ban.error
async def test_error(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        embed = discord.Embed(title='У вас нету прав на пользования данной командой', description='Administrator+', color=0x00ff00)
        await ctx.send(embed=embed)

Bot.run('YOUR TOKEN')