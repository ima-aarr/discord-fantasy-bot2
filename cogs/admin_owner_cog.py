import discord, json, os, traceback
from discord import app_commands
from discord.ext import commands
from core import db, audit
from config import BOT_OWNER_ID

def _is_owner(user):
    return BOT_OWNER_ID and str(user)==str(BOT_OWNER_ID)

class AdminOwnerCog(commands.Cog):
    def __init__(self, bot): self.bot=bot
    async def owner_check(self, interaction):
        if not _is_owner(interaction.user.id):
            await interaction.response.send_message('No permission (owner only)', ephemeral=True); return False
        return True
    @app_commands.command(name='admin_get_data', description='Owner: get db path')
    async def admin_get_data(self, interaction: discord.Interaction, path: str):
        if not await self.owner_check(interaction): return
        await interaction.response.defer(); data = db.get(path)
        await interaction.followup.send('``\n'+json.dumps(data, ensure_ascii=False, indent=2)+'\n``')
    @app_commands.command(name='admin_set_value', description='Owner set db value')
    async def admin_set_value(self, interaction: discord.Interaction, path: str, value: str):
        if not await self.owner_check(interaction): return
        await interaction.response.defer()
        try: v=json.loads(value)
        except: v=value
        db.put(path, v); await interaction.followup.send('OK')
    @app_commands.command(name='admin_wipe_all_data', description='Owner wipe all')
    async def admin_wipe_all_data(self, interaction: discord.Interaction):
        if not await self.owner_check(interaction): return
        await interaction.response.defer(); db.delete(''); await interaction.followup.send('All wiped')
    @app_commands.command(name='admin_shutdown_bot', description='Owner shutdown')
    async def admin_shutdown_bot(self, interaction: discord.Interaction):
        if not await self.owner_check(interaction): return
        await interaction.response.defer(); await interaction.followup.send('Shutting down'); await self.bot.close()
    @app_commands.command(name='admin_exec', description='Owner exec')
    async def admin_exec(self, interaction: discord.Interaction, code: str):
        if not await self.owner_check(interaction): return
        await interaction.response.defer()
        try: res=eval(code, {'db':db,'audit':audit}); await interaction.followup.send('``\n'+str(res)+'\n``')
        except Exception as e: await interaction.followup.send('Error:\n'+traceback.format_exc())

async def setup(bot): await bot.add_cog(AdminOwnerCog(bot))
