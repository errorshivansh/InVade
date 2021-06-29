from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

import time
from datetime import datetime

from . import *

#--------------------------------------------------------------------------------
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

uptime = get_readable_time((time.time() - StartTime))
#-------------------------------------------------------------------------------

hell_pic = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
alive_c = f"__**🔥🔥ɦɛʟʟɮօt ɨs օռʟɨռɛ🔥🔥**__\n\n"
alive_c += f"__↼ Øwñêr ⇀__ : 『 {hell_mention} 』\n\n"
alive_c += f"•• Telethon     :  `{tel_ver}` \n"
alive_c += f"•• Hêllẞø†       :  __**{hell_ver}**__\n"
alive_c += f"•• Sudo            :  `{is_sudo}`\n"
alive_c += f"•• Channel      :  {hell_channel}\n"

#-------------------------------------------------------------------------------

@bot.on(hell_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(hell):
    if hell.fwd_from:
        return
    await hell.get_chat()
    await hell.delete()
    await bot.send_file(hell.chat_id, hell_pic, caption=alive_c)
    await hell.delete()

msg = f"""
**⚡ нєℓℓвσт ιѕ σиℓιиє ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**Telethon :**  `{tel_ver}`
**Hêllẞø†  :**  **{hell_ver}**
**Uptime   :**  `{uptime}`
**Abuse    :**  **{abuse_m}**
**Sudo      :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME

@bot.on(hell_cmd(pattern="hell$"))
@bot.on(sudo_cmd(pattern="hell$", allow_sudo=True))
async def hell_a(event):
    try:
        hell = await bot.inline_query(botname, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "hell", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
