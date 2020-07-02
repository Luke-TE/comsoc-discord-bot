from abc import ABC, abstractmethod
from discord.ext.commands import Command, Context


class CommandAction(ABC):
    @abstractmethod
    async def execute(self, ctx, **args):
        pass

    @abstractmethod
    async def _execute_with_params(self, ctx, params):
        pass

class LogAction(CommandAction):
    def __init__(self, params, action_json):
        self.params = params
        self.text = action_json['text']

    async def execute(self, ctx, *args):
        params = zip(self.params, args)
        return self._execute_with_params(ctx, params)

    async def _execute_with_params(self, ctx, params):
        log_text = self.text
        for name, val in params:
            log_text = log_text.replace(f"${name}", val)
        print(log_text)


class MessageAction(CommandAction):
    def __init__(self, params, action_json):
        self.params = params
        self.text = action_json['text']

    async def execute(self, ctx, *args):
        params = zip(self.params, args)
        return self._execute_with_params(ctx, params)

    async def _execute_with_params(self, ctx, params):
        msg_text = self.text
        for name, val in params:
            msg_text = msg_text.replace(f"${name}", val)
        await ctx.channel.send(msg_text)


class RoleAction(CommandAction):
    def __init__(self, params, action_json):
        self.params = params
        self.reason = action_json['text']
        self.role = action_json['role']

    async def execute(self, ctx, *args):
        params = zip(self.params, args)
        return self._execute_with_params(ctx, params)

    async def _execute_with_params(self, ctx, params):
        reason = self.reason
        for name, val in params:
            reason = reason.replace(f"${name}", val)

        scum_id = self.get_role("capitalist scum")
        role =  member.guild.get_role(scum_id)
        for member in ctx.bot.get_all_members():
            if member.nick == params['user']:
                await ctx.message.add_roles(role, reason=reason)


create_action_fn = {
    "log": LogAction,
    "message": MessageAction,
    "role": RoleAction
}

def convert_action_to_function(actionJson):
    action = mapping[actionJson['action']](actionJson['text'], actionJson['user'])

    return lambda ctx, args: ctx

def convert_actions_to_function(actions):
    action_functions = [convert_action_to_function(action) for action in actions]
    ( for action in )
    return lambda ctx, args: (action_function(ctx, **args) for action_function in action_functions)

def convert_actions_to_command(name, actions):
    command_function = convert_actions_to_function(actions)
    return Command(command_function, name=name)