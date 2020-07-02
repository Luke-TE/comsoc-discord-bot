import unittest.mock
from unittest.mock import MagicMock

import pytest
import discord
from main.bot import Regime
from asynctest import CoroutineMock


def get_mock_message():
    mock_message = CoroutineMock(spec=discord.Message)
    mock_message.channel = CoroutineMock(spec_set=discord.TextChannel)
    mock_message.author = CoroutineMock(spec=discord.Member)
    mock_message.guild = CoroutineMock(spec=discord.Guild)
    return mock_message


@pytest.mark.asyncio
async def test_bot_makes_new_members_capitalists():
    bot = Regime({"capitalist scum": 0})
    mock_role = MagicMock(spec_set=discord.Role)
    mock_member = CoroutineMock(spec_set=discord.Member)
    mock_member.guild.get_role = MagicMock(return_value=mock_role)
    await bot.on_member_join(mock_member)
    mock_member.add_roles.assert_called_once_with(mock_role, reason=unittest.mock.ANY)


@pytest.mark.asyncio
async def test_bot_removes_capitalists():
    bot = Regime({})
    mock_message = get_mock_message()
    await bot.on_message(mock_message)
    mock_message.guild.kick.assert_called_once_with(mock_message.author, reason=unittest.mock.ANY)
