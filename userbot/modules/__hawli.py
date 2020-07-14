""" UserBot yardım komutu """

from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.hawli(?: |$)(.*)")
async def hawli(event):
    """ .hawli komutu için """
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Lütfen bir Hawli modülü adı belirtin.")
    else:
        await event.edit("Lütfen hangi Hawli modülü için yardım istediğinizi belirtin !!\
            \nKullanım: .hawli <modül adı>")
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\n"
        await event.reply(string)
