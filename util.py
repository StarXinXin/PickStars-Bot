#!/usr/bin/env python3
import logging

import aiohttp


def get_menu():
    return "摘星辰 智能QQ频道机器人为你服务~\n已有功能：————————\n/天气查询   正常\n/随机一言   正常"


def errorweather():
    return "查询指令错误：\n标准格式：/天气查询 地点"


async def get_weather_data(location: str) -> str:
    url = f"https://www.mxnzp.com/api/weather/current/{location}?app_id=gk9sxmmmlefnmloh&app_secret=bUxFcVh4MVhoQjZEMmgreGNTRWJWZz09"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # _log.info(response)
            data = await response.json()

    if data["code"] == 1:
        address = data["data"]["address"]
        temp = data["data"]["temp"]
        weather = data["data"]["weather"]
        wind_direction = data["data"]["windDirection"]
        wind_power = data["data"]["windPower"]
        humidity = data["data"]["humidity"]
        report_time = data["data"]["reportTime"]

        return f"查询地点：{address}\n温度：{temp}\n天气情况：{weather}\n风向：{wind_direction}\n风力：{wind_power}\n湿度：{humidity}\n更新时间：{report_time}"
    else:
        return "查询天气失败，请联系Bot管理员~"


async def get_hitokoto_data():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://v1.hitokoto.cn/") as response:
            if response.content_type == "application/json":

                # print(response)
                data = await response.json()
                hitokoto = data["hitokoto"]
                from_where = data["from"]
                from_who = data["from_who"]
                return f"{hitokoto}\n来自：{from_where} - {from_who}"
            else:
                return "错误-响应数据未知"
