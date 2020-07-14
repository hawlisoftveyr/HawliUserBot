from userbot import CMD_HELP
from userbot.events import register
from PIL import Image
import io
import os
import asyncio

@register(outgoing=True, pattern="^.çevir ?(foto|ses|gif)? ?(.*)")
async def cevir(event):
    islem = event.pattern_match.group(1)
    try:
        if len(islem) < 1:
            await event.edit("**Bilinmeyen komut!** `Kullanım: .çevir foto/ses/gif`")
            return
    except:
        await event.edit("**Bilinmeyen komut!** `Kullanım: .çevir foto/ses/gif`")
        return

    if islem == "foto":
        rep_msg = await event.get_reply_message()

        if not event.is_reply or not rep_msg.sticker:
            await event.edit("`Lütfen bir Sticker'a yanıt verin.`")
            return
        await event.edit("`Fotoğraf'a çeviriliyor...`")
        foto = io.BytesIO()
        foto = await event.client.download_media(rep_msg.sticker, foto)

        im = Image.open(foto).convert("RGB")
        im.save("sticker.png", "png")
        await event.client.send_file(event.chat_id, "sticker.png", reply_to=rep_msg, caption="@AsenaUserBot `ile fotoğrafa çevirildi.`")

        await event.delete()
        os.remove("sticker.png")
    elif islem == "ses":
        EFEKTLER = ["çocuk", "robot", "earrape", "hızlı", "parazit", "yankı"]
        # https://www.vacing.com/ffmpeg_audio_filters/index.html #
        KOMUT = {"çocuk": '-filter_complex "rubberband=pitch=1.5"', "robot": '-filter_complex "afftfilt=real=\'hypot(re,im)*sin(0)\':imag=\'hypot(re,im)*cos(0)\':win_size=512:overlap=0.75"', "earrape": '-filter_complex "acrusher=level_in=8:level_out=18:bits=8:mode=log:aa=1"', "hızlı": "-filter_complex \"rubberband=tempo=1.5\"", "parazit": '-filter_complex "afftfilt=real=\'hypot(re,im)*cos((random(0)*2-1)*2*3.14)\':imag=\'hypot(re,im)*sin((random(1)*2-1)*2*3.14)\':win_size=128:overlap=0.8"', "yankı": "-filter_complex \"aecho=0.8:0.9:500|1000:0.2|0.1\""}
        efekt = event.pattern_match.group(2)

        if len(efekt) < 1:
            await event.edit("`Lütfen bir efekt belirtin. Kullanbilecek efektler: ``çocuk/robot/earrape/hızlı/parazit/yankı`")
            return

        rep_msg = await event.get_reply_message()

        if not event.is_reply or not (rep_msg.voice or rep_msg.audio):
            await event.edit("`Lütfen bir Ses'e yanıt verin.`")
            return

        await event.edit("`Efekt uygulanıyor...`")
        if efekt in EFEKTLER:
            indir = await rep_msg.download_media()
            ses = await asyncio.create_subprocess_shell(f"ffmpeg -i '{indir}' {KOMUT[efekt]} output.mp3")
            await ses.communicate()
            await event.client.send_file(event.chat_id, "output.mp3", reply_to=rep_msg, caption="@HawliUserBot `ile efekt uygulandı.`")
            
            await event.delete()
            os.remove(indir)
            os.remove("output.mp3")
        else:
            await event.edit("**Belirttiğiniz efekt bulunamadı! **`Kullanılabileceğiniz efektler: ``çocuk/robot/earrape/hızlı/parazit/yankı`")
    elif islem == "gif":
        rep_msg = await event.get_reply_message()

        if not event.is_reply or not rep_msg.video:
            await event.edit("`Lütfen bir Video'ya yanıt verin.`")
            return

        await event.edit("`Gif'e çeviriliyor...`")
        video = io.BytesIO()
        video = await event.client.download_media(rep_msg.video)
        gif = await asyncio.create_subprocess_shell(f"ffmpeg -i '{video}' -filter_complex 'fps=20,scale=320:-1:flags=lanczos,split [o1] [o2];[o1] palettegen [p]; [o2] fifo [o3];[o3] [p] paletteuse' out.gif")
        await gif.communicate()
        await event.edit("`Gif yükleniyor...`")

        try:
            await event.client.send_file(event.chat_id, "out.gif",reply_to=rep_msg, caption="@AsenaUserBot `ile Gif'e çevirildi.`")
        except:
            await event.edit("`Gif'e çeviremedim :/`")
            await event.delete()
            os.remove("out.gif")
            os.remove(video)
        finally:
            await event.delete()
            os.remove("out.gif")
            os.remove(video)

    else:
        await event.edit("**Bilinmeyen komut!** `Kullanım: .çevir ses/foto`")
        return

CMD_HELP["cevir"] = ".çevir foto/gif/ses <çocuk/robot/earrape/hızlı/parazit/yankı>\n**Foto:** Yanıt verdiğiniz Sticker'ı fotoğrafa çevirir.\n**Gif:** Yanıt verdiğiniz videoyu Gif'e çevirir.\n**Ses:** Yanıt verdiğiniz Ses'e efektler uygular. Efektler: çocuk/robot/earrape/hızlı/parazit/yankı."
