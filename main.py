import os
import logging
import json
from slack_bolt import App, logger
from slack_bolt.adapter.socket_mode import SocketModeHandler

def get_book():
    with open ('book.json', 'r') as book:
        data=book.read()
    obj=json.loads(data)
    return obj

logging.basicConfig(level=logging.DEBUG)
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

valid_subcommands=('info','summary','meeting','chapter')

@app.command("/bookclubbot")
#entry point for /bookclubbot commands
def process(ack, body, say, respond):
    ack() #Can include a response to send personally back to the sender e.g. ack("Please wait while we process your request")
    txt=body['text'].split(" ",1)
    subcommand=txt[0]
    if subcommand in valid_subcommands:
        book=get_book()
        if subcommand == 'info':
            msg="Title: {0}, Author: {1}".format(book['title'],book['author'])
            response={
                "response_type": "in_channel",
                "text": msg
            }

        say(response) #responds back to channel 
    else: 
        respond("The subcommand you have attempted to use is invalid. Please one of the following {0}".format(valid_subcommands))

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()