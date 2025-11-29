import discord
from discord import app_commands
from discord.ext import commands
from systems.characters import create_adventurer
from systems.exploration import explore
class AdventureCog(commands.Cog):
    def __init__(self, bot): self.bot=bot
    @app_commands.command(name='create_adventurer', description='Create adventurer')
    async def create_adv(self, interaction: discord.Interaction, name: str, job: str, *, desc: str=''):
        await interaction.response.defer()
        server=str(interaction.guild.id)
        adv=create_adventurer(server, str(interaction.user.id), name, job, desc)
        await interaction.followup.send(f'Adventurer created: {adv["id"]}')
    @app_commands.command(name='explore', description='Explore')
    async def explore_cmd(self, interaction: discord.Interaction, adv_id: str):
        await interaction.response.defer(); server=str(interaction.guild.id)
        res = await explore(server, adv_id)
        await interaction.followup.send(str(res))
async def setup(bot): await bot.add_cog(AdventureCog(bot))
