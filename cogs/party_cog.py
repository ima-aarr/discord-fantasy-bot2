import discord
from discord import app_commands
from discord.ext import commands
from systems.parties import create_party
class PartyCog(commands.Cog):
    def __init__(self, bot): self.bot=bot
    @app_commands.command(name='create_party', description='Create party')
    async def create_party_cmd(self, interaction: discord.Interaction, leader_adv: str):
        await interaction.response.defer(); server=str(interaction.guild.id)
        p = create_party(server, leader_adv); await interaction.followup.send(f'Party {p["id"]}')
async def setup(bot): await bot.add_cog(PartyCog(bot))
