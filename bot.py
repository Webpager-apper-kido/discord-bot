import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=intents)

# command to display a button
@bot.command()
async def button(ctx):
    embed = discord.Embed(title="Button", description="Press the button to trigger an action.")
    embed.add_field(name="Button", value="[Press me](https://www.example.com)", inline=False)
    await ctx.send(embed=embed)
    
# command to repeat a message
@bot.command()
async def repeat(ctx, *, message: str):
    await ctx.send(message)

# command to clear a certain number of messages
@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)
    
# command to say hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

# command to show help
@bot.command()
async def bhelp(ctx):
    embed = discord.Embed(title="Help", description="List of commands:")
    embed.add_field(name="!hello", value="Says hello", inline=False)
    embed.add_field(name="!repeat [message]", value="Repeats the message", inline=False)
    embed.add_field(name="!clear [number]", value="Clears the specified number of messages", inline=False)
    embed.add_field(name="!button", value="Displays a button message", inline=False)
    embed.add_field(name="!kick @user", value="Kick a user from the server", inline=False)
    embed.add_field(name="!Ban @user", value="Ban a user from the server", inline=False)
    await ctx.send(embed=embed)

# command to kick a user
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member}')

# command to ban a user
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member}')

bot.run("MTA2NjkzMjk5MTQ5MTg1MDI0MQ.GrB06x.FJaTiESfnvH-6GQ-q-uUDnXCp4_K_qloTShdcU")