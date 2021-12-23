from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message


invite_logger = 
esanaChat = 
esanaChannel = 
session=

api_id = 
api_hash = 

app = Client(session,api_id,api_hash)

@app.on_message(filters.command('invite'))
def my_handler(client, message):
    r=app.search_messages(invite_logger, query='('+str(message.from_user.id), limit=5)
    if len(r)==0:
        link = app.create_chat_invite_link(esanaChannel)
        m=message.reply("User: {0} ( {2} )\nYour invite link : {1}\n\nShare as you can to get free netflix.".format(message.from_user.mention(message.from_user.first_name) ,link.invite_link ,message.from_user.id) , disable_web_page_preview = True)
        m.forward(invite_logger)
    else:
        message.reply(r[-1]['text'],  disable_web_page_preview = True)

app.run()