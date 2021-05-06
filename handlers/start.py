# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Merhaba 👋! Telegram Gruplarının sesli sohbetlerinde müzik çalabiliyorum. Sizi şaşırtacak pek çok harika özelliğim var! \ n \ n 🔴 Telegram gruplarınızın sesli sohbetlerinizde müzik çalmamı ister misiniz? ? Beni nasıl kullanabileceğinizi öğrenmek için lütfen aşağıdaki \ ' 📜 Kullanım Kılavuzu 📜 \' düğmesini tıklayın. \ N \ n 🔴 Grubunuzun sesli sohbetinde müzik çalabilmek için Asistanın grubunuzda olması gerekir. \ N \ n 🔴 [Kullanıcı Kılavuzu] (https://telegra.ph/WylineDev-05-06-2) bahsedilen daha fazla bilgi ve komutlar \ n \ n @zeus0901 tarafından hazırlanan bir proje "" " ,
      """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Manual Komutlar👤", url="https://telegra.ph/Daisy-X-04-19")
                  ],[
                    InlineKeyboardButton(
                        "👨‍💻Güncelleme👨‍💻", url="https://t.me/WylineDevUpdate"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Support Grup 🗣️", url="https://t.me/WylineDevSupport"
                    )
              ],[ 
                    InlineKeyboardButton(
                        "Sohbet Grup 🇹🇷", url="https://t.me/OlympusCh4t"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Müzik çalar yayında**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎧 Support Grup 🎧", url="https://t.me/WylineDevSupport")
                ]
            ]
        )
   )

