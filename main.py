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
        if subcommand == 'summary':
            msg="*Title:* {0},\n*Author*: {1},\n *Synopsis*: {2}".format(book['title'],book['author'],book['synopsis'])
            response={
                "response_type": "in_channel",
                "text": msg
            }
            say(response) #responds back to channel 
        elif subcommand == 'info':
            msg="The company book club is an opportunity to read a book with your colleagues and then have a discussion to learn and gather insights into their perspective. Please contact {0} for more info.".format(book['coordinator'])
            response={
                "response_type": "in_channel",
                "text": msg
            }
            say(response) #responds back to channel 
        elif subcommand == 'chapter': 
            chapter_number=int(txt[1].split(" ",1)[0])
            if chapter_number <= len(book['chapters']):
                chapter=book['chapters'][str(chapter_number)]
                msg="*Chapter {0}*: {1},\n*Summary*: {2},\n*Questions*: {3}".format(chapter_number,chapter['title'],chapter['summary'],chapter['questions'])
                response={
                    "response_type": "in_channel",
                    "text": msg
                }
                say(response) #responds back to channel 
            else: 
                msg="The chapter number you have specified ({0}), does not yet have any information available on it.".format(chapter_number)
                respond(msg)

        else: 
            msg="Thank you for choosing Bookclubbot, the subcommand \"{0}\", is still under construction!".format(subcommand)
            response={
                "response_type": "in_channel",
                "text": msg
            }
            respond(msg)
        
    else: 
        respond("The subcommand you have attempted to use is invalid. Please one of the following {0}".format(valid_subcommands))

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()