from discord.ext import commands


class BannedWords(commands.Cog):
    def __init__(self, bot, banned_words):
        self.bot = bot
        self.banned_words = banned_words

    @commands.Cog.listener()
    async def on_message(self, message):
        for word in self.banned_words:
            if word in message:
                await message.guild.kick(message.author, reason=f"You've spoken a forbidden word: {word}")
                await message.channel.send(f"{message.author.nick} has been removed for saying a bad word: {word}.")
                print(f"{message.author.nick} has been kicked from the server.")