import json
import discord
from discord.ext.commands import Command



with open(".") as bot_json:
    bot_data = json.load(bot_json)

commands_json = bot_data['commands']
for command_name, command_actions in commands_json:
    command = convert_actions_to_command(command_name, command_actions)
    # add to bot

listeners_json = bot_data['listeners']
for command_name, command_actions in commands_json:
    command = convert_actions_to_command(command_name, command_actions)