import discord, os, json
from discord import app_commands
from discord.ext import commands
from core import db, audit
from config import ADMIN_USER_IDS

def is_admin(user): return str(user) in ADMIN_USER_IDS
class AdminCog(commands.Cog):
    def __init__(self, bot): self.bot=bot
    async def admin_check(self, interaction):
        if not is_admin(interaction.user.id): await interaction.response.send_message('No permission', ephemeral=True); return False
        return True
    @app_commands.command(name='admin_ban_guild', description='Admin ban guild')
    async def admin_ban_guild(self, interaction: discord.Interaction, guild_id: str):
        if not await self.admin_check(interaction): return
        db.put(f'banned_guilds/{guild_id}', {'banned_by': str(interaction.user.id)}); await interaction.response.send_message('OK')
async def setup(bot): await bot.add_cog(AdminCog(bot))
