from telethon import events
import asyncio
from userbot.events import register
import random
import os

@register(outgoing=True, pattern="^.gosmeyn")
async def gosmeyn(event):
    # Daha karma olması için Albümleri Ekliyoruz #
    ALBUMLER = ["Hexada", "Plagues", "Rituals", "Blackmage", "Opium", "Fear Network", "For the Aspiring Occultist", "N/O/I/S/E", "D(R)Ead", "Nails", "Ballgag", "Rake"]
    await event.edit(f"`Rastgele bir` **Ghostemane** `şarkısı seçiliyor...`")

    try:
        sonuclar = await event.client.inline_query('deezermusicbot', 'Ghostemane ' + random.choice(ALBUMLER))
    except:
        await event.edit("`Üzgünüm, bottan yanıt alamadım!`")
        return

    sonuc = False
    while sonuc is False:
        rast = random.choice(sonuclar)
        if rast.description == "Ghostemane":
            await event.edit("`Şarkı indiriliyor! Lütfen bekleyiniz...`")
            indir = await rast.download_media()
            await event.edit("`İndirme tamamlandı! Dosya yükleniyor...`")
            await event.client.send_file(event.chat_id, indir, caption=f"@HawliUserBot sizin için `{rast.description} - {rast.title}` seçti :)")
            await event.delete()
            os.remove(indir)
            sonuc = True
            
            
CMD_HELP.update({
    "gosmeyn":
    ".gosmeyn\
\nKullanımı: Rastgele bir Ghostemane şarkısı indirir\
\n\nEdited by HawliJojuk."
})            

