from userbot import CMD_HELP, ASYNC_POOL, tgbot, SPOTIFY_DC, G_DRIVE_CLIENT_ID, lastfm, LYDIA_API_KEY, YOUTUBE_API_KEY, OPEN_WEATHER_MAP_APPID, AUTO_PP, REM_BG_API_KEY, OCR_SPACE_API_KEY, PM_AUTO_BAN, BOTLOG_CHATID
from userbot.events import register
from telethon import version
from platform import python_version

def durum(s):
    if s == None:
        return "❌"
    else:
        if s == False:
            return "❌"
        else:
            return "✅"

@register(outgoing=True, pattern="^.durum")
async def durums(event):

    await event.edit(f"""
**Python Sürümü:** `{python_version()}`
**TeleThon Sürümü:** `{version.__version__}` 
**Hawli Sürümü:** `1.9`

**Plugin Sayısı:** `{len(CMD_HELP)}`

**Inline Bot:** `{durum(tgbot)}`
**Spotify:** `{durum(SPOTIFY_DC)}`
**GDrive:** `{durum(G_DRIVE_CLIENT_ID)}`
**LastFm:** `{durum(lastfm)}`
**YouTube ApiKey:** `{durum(YOUTUBE_API_KEY)}`
**Lydia:** `{durum(LYDIA_API_KEY)}`
**OpenWeather:** `{durum(OPEN_WEATHER_MAP_APPID)}`
**AutoPP:** `{durum(AUTO_PP)}`
**RemoveBG:** `{durum(REM_BG_API_KEY)}`
**OcrSpace:** `{durum(OCR_SPACE_API_KEY)}`
**Pm AutoBan:** `{durum(PM_AUTO_BAN)}`
**BotLog:** `{durum(BOTLOG_CHATID)}`
**Pluginler:** `Kalıcı`

**Her Şey Normal ✅**
    """)

CMD_HELP["durum"] = ".durum\nKullanım: Eklenen Apiler ve sürümleri gösterir."
