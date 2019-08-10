import discord


class Regime(discord.Client):
    def __init__(self, roles):
        super(Regime, self).__init__()
        self.roles = roles

    def get_role(self, role_name: str):
        return self.roles[role_name]

    async def on_ready(self):
        print("History repeats itself, first as a tragedy, second as farce.")
    
    async def on_message(self, message):
        print("{0.author} said \"{0.content}\"".format(message))

        if message.content.startswith('communism'):
            await message.channel.send('https://www.youtube.com/watch?v=U06jlgpMtQs')

        if message.content.startswith("capitalism"):
            await message.guild.kick(message.author, reason="Capitalist scum aren't welcome here >:(")
            await message.channel.send("{0} has been removed for treason.".format(message.author.nick))

        if message.content.startswith('ping'):
            await message.channel.send('pong')

    async def on_member_join(self, member):
        scum_reason = "You've been given the role \"Capitalist Scum\" for invading the motherland!"
        scum_id = self.get_role("capitalist scum")
        scum_role = member.guild.get_role(scum_id)
        await member.add_roles(scum_role, reason=scum_reason)

