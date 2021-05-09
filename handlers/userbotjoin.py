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




from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Önce beni grubunun yöneticisi olarak ekle</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "WylineMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"İstediğiniz gibi buraya katıldım")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Sohbetinizde zaten yardımcı</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Taşan Bekleme Hatası 🛑 \n kullanıcı {user.first_name} userbot için yoğun katılım istekleri nedeniyle grubunuza katılamadı! Asistanın grupta yasaklı olmadığından emin olun."
            "\n\nOr ekleme yerinden @WylineMusic i grubunuza ekleyin</b>",
        )
        return
    await message.reply_text(
            "<b>yardımcı userbot sohbetinize katıldı</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Kullanıcı grubunuzdan ayrılamadı! Floodwaits olabilir."
            "\n\nOr beni grubunuza manuel olarak ekle</b>",
        )
        return
