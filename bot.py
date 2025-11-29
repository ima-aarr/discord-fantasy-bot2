import threading, logging, asyncio
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import discord
from discord.ext import commands
from config import DISCORD_TOKEN, PORT
if not DISCORD_TOKEN:
    raise RuntimeError('DISCORD_TOKEN not set')

def start_health():
    handler=SimpleHTTPRequestHandler
    with TCPServer(('', PORT), handler) as httpd:
        print(f'Health server on {PORT}'); httpd.serve_forever()
threading.Thread(target=start_health, daemon=True).start()
intents = discord.Intents.default(); intents.message_content=True; intents.members=True; intents.guilds=True
bot = commands.Bot(command_prefix='/', intents=intents)
COGS = ['cogs.adventure_cog','cogs.country_cog','cogs.party_cog','cogs.battle_cog','cogs.rewards_cog','cogs.admin_cog','cogs.admin_owner_cog']
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} ({bot.user.id})')
    for c in COGS:
        try:
            await bot.load_extension(c); print('Loaded', c)
        except Exception as e:
            print('Failed to load', c, e)
    try: await bot.tree.sync(); print('Slash commands synced')
    except Exception as e: print('Slash sync failed', e)
if __name__=='__main__': logging.basicConfig(level=logging.INFO); asyncio.run(bot.start(DISCORD_TOKEN))
