# -*- coding: utf-8 -*-
import os
import re

import aiohttp
import botpy
from botpy import BotAPI
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import Message, DirectMessage
from botpy.types.message import ArkKv, Ark
from botpy.user import Member

from Function.event_handlers import on_guild_member_add, on_guild_member_update, on_guild_member_remove
from command_register import Commands
from util import get_menu, errorweather, get_weather_data, get_hitokoto_data

#  以上为依赖库

_log = logging.get_logger()  # 用于回复日志

test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))


class MyClient(botpy.Client):

    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_guild_member_add(self, member: Member):
        await on_guild_member_add(self, member)

    async def on_guild_member_update(self, member: Member):
        await on_guild_member_update(self, member)

    async def on_guild_member_remove(self, member: Member):
        await on_guild_member_remove(self, member)

    async def on_at_message_create(self, message: Message):
        _log.info(f"机器人({self.robot.name})收到({message.member.nick})艾特了: {message.content}")

        split_command = message.content.split()  # 按照空格分割字符串
        substring = None
        for item in split_command:
            if "天气查询" in item:
                substring = item
            elif "随机一言" in item:
                substring = item
            elif "菜单" in item:
                substring = item

        print(substring)

        if substring:
            if "/随机一言" in substring:
                ret = await get_hitokoto_data()
                await message.reply(content=ret)
                _log.info("消息返回：\n%s" % ret)

            elif "/天气查询" in substring:
                if message.content == "/天气查询":
                    ret = await errorweather()
                    await message.reply(content=ret)
                    _log.info("消息返回：\n%s" % ret)
                    return True
                else:
                    # 提取被艾特的用户和其他参数
                    command_parts = message.content.split(maxsplit=2)
                    if len(command_parts) != 3:
                        ret = errorweather()
                        await message.reply(content=ret)
                        _log.info("消息返回：\n%s" % ret)
                        return True
                    else:
                        # 提取其他参数
                        location = command_parts[2]
                        ret = await get_weather_data(location)
                        await message.reply(content=ret)
                        _log.info("消息返回：\n%s" % ret)

            elif "/菜单" in substring:
                await message.reply(content=get_menu())
                _log.info("消息返回：\n%s" % get_menu())

        else:
            print("未找到指定字符串")

    async def on_direct_message_create(self, message: DirectMessage):
        _log.info(f"机器人{self.robot.name}收到私信了: {message.content}")
        split_command = message.content.split()  # 按照空格分割字符串
        substring = None
        for item in split_command:
            if "天气查询" in item:
                substring = item
            elif "随机一言" in item:
                substring = item
            elif "菜单" in item:
                substring = item

        print(substring)

        if substring:
            if "/随机一言" in substring:
                ret = await get_hitokoto_data()
                await message.reply(content=ret)
                _log.info("消息返回：\n%s" % ret)

            elif "/天气查询" in substring:
                if message.content == "/天气查询":
                    ret = errorweather()
                    await message.reply(content=ret)
                    _log.info("消息返回：\n%s" % ret)
                    return True
                else:
                    location = extract_location(message.content)
                    if location == '':
                        ret = errorweather()
                        await message.reply(content=ret)
                        _log.info("消息返回：\n%s" % ret)
                        return True
                    else:
                        # 提取其他参数
                        ret = await get_weather_data(location)
                        await message.reply(content=ret)
                        _log.info("消息返回：\n%s" % ret)

            elif "/菜单" in substring:
                await message.reply(content=get_menu())
                _log.info("消息返回：\n%s" % get_menu())

        else:
            print("未找到指定字符串")


def extract_location(query):
    # 找到空格位置
    space_index = query.find(' ')

    # 如果找到了空格
    if space_index != -1:
        # 返回空格后面的部分作为地点
        return query[space_index + 1:]
    else:
        # 如果没有空格，则返回整个字符串
        return query


if __name__ == "__main__":
    intents = botpy.Intents(direct_message=True, public_guild_messages=True, guild_members=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], token=test_config["token"])
