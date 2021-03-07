import discord
from discord.ext import commands
TOKEN = ''
PREFIX = '/'
INTENTS = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=INTENTS)


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def reload(ctx,md):
    try:
        bot.reload_extension(md)
    except Exception as e:
        await ctx.send(f'```\n{e}\n```')
    else:
        await ctx.send('completed')


@bot.command()
async def load(ctx,md):
    try:
        bot.load_extension(md)
    except Exception as e:
        await ctx.send(f'```\n{e}\n```')
    else:
        await ctx.send('completed')

@bot.command()
async def unload(ctx,md):
    try:
        bot.unload_extension(md)
    except Exception as e:
        await ctx.send(f'```\n{e}\n```')
    else:
        await ctx.send('completed')

bot.load_extension('msgcheck')

bot.run(TOKEN)