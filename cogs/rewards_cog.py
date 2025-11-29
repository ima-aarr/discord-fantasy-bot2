import discord
from discord import app_commands
from discord.ext import commands
from systems.rewards import distribute_rewards
class RewardsCog(commands.Cog):
    def __init__(self, bot): self.bot=bot
    @app_commands.command(name='split_rewards', description='Split rewards')
    async def split_rewards(self, interaction: discord.Interaction, party_id: str, gold: int):
        await interaction.response.defer(); server=str(interaction.guild.id)
        ok,res = distribute_rewards(server, party_id, {'gold': gold}); await interaction.followup.send(str(res))
async def setup(bot): await bot.add_cog(RewardsCog(bot))
