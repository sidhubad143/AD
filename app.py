from pyrogram import Client
from pyrogram.types import ChatPrivileges

API_ID = 25742938
API_HASH = "b35b715fe8dc0a58e8048988286fc5b6"
BOT_TOKEN = "8386112420:AAFTrWCXckzj-YnHxaErcTnhB6u32Gvj0os"

TARGET_CHAT = -1003158056993
TARGET_USER = 7616808278

app = Client("promoter_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

PRIVS = ChatPrivileges(
    can_delete_messages=True,
    can_restrict_members=True,
    can_promote_members=True,
    can_change_info=True,
    can_invite_users=True,
    can_pin_messages=True,
    is_anonymous=False
)

@app.on_message()
async def handler(client, message):
    try:
        me = await client.get_me()
        bot_member = await client.get_chat_member(TARGET_CHAT, me.id)
        if not getattr(bot_member.privileges, "can_promote_members", False):
            print("❌ Bot kol 'Promote Members/Add Admins' rights nahi ne. Owner ton enable karvao.")
            return
        await client.promote_chat_member(TARGET_CHAT, TARGET_USER, PRIVS)
        print("✅ User promoted successfully!")
    except Exception as e:
        print("⚠️ Error:", e)

app.run()
