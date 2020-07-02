from discord.ext import commands


class JsonCog(commands.Cog):
    def __init__(self):
        pass

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass

    @commands.Cog.listener()
    async def on_message(self, message):
        pass