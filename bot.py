# -*- coding: utf-8 -*-
import os

import aiohttp
import botpy
from botpy import BotAPI
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import Message

from command_register import Commands
from util import get_menu, errorweather, get_weather_data, get_hitokoto_data

#  以上为依赖库

_log = logging.get_logger()  # 用于回复日志

test_config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))


@Commands("/菜单")
async def ask_menu(api: BotAPI, message: Message, params=None):
    await message.reply(content=get_menu())
    return True




@Commands("/天气查询")
async def ask_weather(api: BotAPI, message: Message, params=None):
    params = "" if params is None else params
    if params == '':
        await message.reply(content=errorweather())
        return True
    else:
        ret = await get_weather_data(params)
        await message.reply(content=ret)
    return True

@Commands("/随机一言")
async def ask_hitokoto(api: BotAPI, message: Message, params=None):
    ret = await get_hitokoto_data()
    await message.reply(content=ret)
    return True

class MyClient(botpy.Client):

    async def on_at_message_create(self, message: Message):
        _log.info("接收消息：%s" % message.content)
        # 注册指令handler
        tasks = [
            ask_menu,  # /菜单
            ask_weather,  # /天气
            ask_hitokoto,  # /一言
        ]
        for handler in tasks:
            if await handler(api=self.api, message=message):
                return

    # 私信部分
    # async def on_ready(self):
    #     _log.info(f"robot 「{self.robot.name}」 on_ready!")
    #
    #
    #
    # async def on_direct_message_create(self, message: DirectMessage):
    #     _log.info("接收消息：%s" % message.content)
    #     if message.content == "/菜单":
    #         await self.api.post_dms(
    #             guild_id=message.guild_id,
    #             # content=f"机器人{self.robot.name}收到你的私信了: {message.content}",
    #             content = get_menu(),
    #             msg_id=message.id,
    #         )


if __name__ == "__main__":
    intents = botpy.Intents(public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], token=test_config["token"])
