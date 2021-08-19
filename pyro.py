"""
MIT License

Copyright (c) 2021 UltronRoBo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os 

os.system('pip install --upgrade pip')
os.system('pip install pyrogram==1.2.9')

from pyrogram import Client

a = """
 
"""

print(a)
print("""UʟᴛʀᴏɴMᴜsɪᴄ Sᴛʀɪɴɢ Sᴇssɪᴏɴ\n\n:~ 𝘽𝙮 𝙏𝙚𝙖𝙢 𝙐𝙡𝙩𝙧𝙤𝙣𝙍𝙤𝘽𝙤.
Please go to https://my.telegram.org and get your details.""")
print("Enter The Your Values Below :~")

print(
    "Never Share Your String Session To Anyone, Your Account Can be Hacked And can be Misused !!"
)

API_ID = API_HASH = None
try:
    from decouple import config

    API_ID = config("API_ID")
    API_HASH = config("API_HASH")
except:
    API_ID = int(input("Enter your API ID: "))
    API_HASH = input("Enter your API HASH: ")

# generate a session
print("Enter phone number when asked.\n\n")
if not API_ID and API_HASH:
    print("Missing api id and hash!")
    exit(0)
with Client(":memory", api_id=API_ID, api_hash=API_HASH) as pyro:
    ss = pyro.export_session_string()
    pyro.send_message(
        "me",
        f"`{ss}`\n\nAbove is your Pyrogram Session String for UltronMusic. **DO NOT SHARE IT.**",
    )
    print("Session has been successfully sent to your Telegram Account's Saved Messages!")
    exit(0)
