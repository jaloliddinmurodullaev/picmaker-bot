import requests
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import aiohttp
from aiogram import types
from loader import bot
async def photomaker(text: str):
    text.capitalize()
    text = 'Happy New Year ' + text
    img = Image.open('utils/pikachu.jpg')
    image = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('arial.ttf', 45)
    image.text((180, 100), text, font=myFont, fill=(255, 0, 0))
    img.save('utils/tabrik.jpg')
