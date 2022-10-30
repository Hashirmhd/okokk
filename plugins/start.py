from pyrogram import Client, filters, StopPropagation
from bot import BotStartTime
from pyrogram.types import  InlineKeyboardButton, InlineKeyboardMarkup
import datetime as dt

@Client.on_message(filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/ytdofficial")]
    ])

    
    currentTime = dt.datetime.now()

    FMT = '%H:%M:%S'
    tdelta = dt.datetime.strptime(currentTime.strftime(FMT), FMT) - dt.datetime.strptime(BotStartTime.strftime(FMT), FMT)

    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info \n <code>Bot Uptime: {tdelta}</code>"
 
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
