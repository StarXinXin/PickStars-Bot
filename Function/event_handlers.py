# event_handlers.py
from botpy import logging
from botpy.user import Member


# async def on_guild_member_add(member: Member, api):
#     dms_payload = await api.create_dms(member.guild_id, member.user.id)
#     _log.info("%s 加入频道，已向 %s 发送宣传私信" % (member.nick, member.nick))
#     await api.post_dms(dms_payload["guild_id"],
#                        content="我是摘星辰，欢迎加入我们的频道。 \n如果你想体验我们的APP，可以进入官网进行下载。\nhttps://www.xinstudio.top",
#                        msg_id=member.event_id)
#
# async def on_guild_member_update(member: Member):
#     _log.info("%s 更新了资料" % member.nick)
#
# async def on_guild_member_remove(member: Member, api):
#     dms_payload = await api.create_dms(member.guild_id, member.user.id)
#     _log.info("%s 加入频道，已向 %s 发送宣传私信" % (member.nick, member.nick))
#     await api.post_dms(dms_payload["guild_id"],
#                        content="摘星辰，感谢有你的陪伴。如果想我们了，可以进入官网找回记忆。\nhttps://www.xinstudio.top",
#                        msg_id=member.event_id)
_log = logging.get_logger()  # 用于回复日志

async def on_guild_member_add(self, member: Member):
    _log.info(f"{member.user.id}({member.nick}) 加入频道!")
    dms_payload = await self.api.create_dms(member.guild_id, member.user.id)
    await self.api.post_dms(dms_payload["guild_id"], content="我是摘星辰，欢迎加入我们的频道。 \n如果你想体验我们的APP，可以进入官网（发送信息：/官网）进行下载。", msg_id=member.event_id)

async def on_guild_member_update(self, member: Member):
    _log.info("%s 更新了资料" % member.nick)


async def on_guild_member_remove(self, member: Member):
    dms_payload = await self.api.create_dms(member.guild_id, user_id="1402832033")
    await self.api.post_dms(dms_payload["guild_id"], content="摘星辰，感谢有你的陪伴。", msg_id=member.event_id)

    _log.info(f"{member.user.id}({member.nick}) 退出频道!")