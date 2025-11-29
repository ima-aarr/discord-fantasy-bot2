import discord
from discord import app_commands
from discord.ext import commands
from systems.combat import resolve_party_vs_monster
class BattleCog(commands.Cog):
    def __init__(self, bot): self.bot=bot
    @app_commands.command(name='battle', description='Battle')
    async def battle(self, interaction: discord.Interaction, party_id: str, monster_id: str):
        await interaction.response.defer(); server=str(interaction.guild.id)
        ok,res = resolve_party_vs_monster(server, party_id, {'id':monster_id}); await interaction.followup.send(str(res))
async def setup(bot): await bot.add_cog(BattleCog(bot))
