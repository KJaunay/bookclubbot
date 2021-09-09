import os
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.DEBUG)
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

valid_subcommands=('info','summary','meeting')

@app.command("/bookclubbot")
#entry point for /bookclubbot commands
def process(ack, body, say, respond):
    ack() #Can include a response to send personally back to the sender e.g. ack("Please wait while we process your request")
    subcommand=body['text'].split(" ",1)
    if subcommand[0] in valid_subcommands:
        response={
    "response_type": "in_channel",
    "text": "The subcommand you ran was {0} and the content was".format(subcommand[0]),
    "attachments":[
                {
                    "text": subcommand[1]
                }
            ]
        }
        
        say(response) #responds back to channel
    else: 
        respond("The subcommand you have attempted to use is invalid. Please one of the following {0}".format(valid_subcommands))

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()