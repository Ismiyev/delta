from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Məni Qrupna At", url=f"http://t.me/SozTapBot?startgroup=new")
    ],
    [
        InlineKeyboardButton("🇦🇿 Sahibim", url="https://t.me/RiyaddBlog"),
        InlineKeyboardButton("🌐 Chat", url="https://t.me/karabakhteamm"),
    ]
])


START = game"""
**🔮 Salam, Sözləri tapma oyununa xoş gəldin..**

➤ Məlumat üçün 👉 /help Basın. Ayarlar asand və sadədir. 
"""
)
HELP = help"""
**✌️ Ayarlar Menyusuna Xoşgeldiniz.**
/oyun - Oyunu başlamaq üçün..
/kec - Üç ədəd keçmə haqqınız var , oyunu keçmək üçün.. 
/qreytinq - Oyuncular arasındaki rəqabət məlumatı..
/cancel - Oyundan çıxmaq üçün lazımlı olan ayardır.. 
"""
)
# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://images.app.goo.gl/45Mm2Tc3y86eoeMf6",caption=START,reply_markup=keyboard)
)
@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://images.app.goo.gl/45Mm2Tc3y86eoeMf6",caption=HELP) 
)
# Oyunu başlat. 
@Client.on_message(filters.command("oyun")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False
)
    if aktif:
        await m.reply("**❗ Oyun Onsuzda Qrubunuzda Davam Edir ✍🏻 \n Oyunu dayandırmaq üçün yazın /cancel dayandırbilərsiz")
    else:
        await m.reply(f"**{m.from_user.mention}** Taərəfindən! \nSözü Tapma Oyunu Başladı .\n\nHamınıza Uğurlar ❣️!", reply_markup=RiyaddBlog )
        )
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        )
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        )
        for harf in kelime:
            kelime_list+= harf + " "
        )
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/20 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandığınız Say: 1
🔎 Kömək: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq həriflərdən düzgün sözü tapma
        """
        await c.send_message(m.chat.id, text)
        
