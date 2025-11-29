import discord
from discord import app_commands
from discord.ext import commands
from systems.countries import create_country
class CountryCog(commands.Cog):
    def __init__(self, bot): self.bot=bot
    @app_commands.command(name='create_country', description='Create country')
    async def create_country_cmd(self, interaction: discord.Interaction, name: str):
        await interaction.response.defer(); ok,res=create_country(str(interaction.user.id), name)
        await interaction.followup.send('Created' if ok else f'Failed: {res}')
async def setup(bot): await bot.add_cog(CountryCog(bot))
