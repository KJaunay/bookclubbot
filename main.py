#curl -X POST      -H "Authorization: Bearer $TOKEN"      -H 'Content-type: application/json;charset=utf-8'     --data '{"channel":"#general","text":"Hello, Slack!"}' https://slack.com/api/chat.postMessage

import os
import logging
from slack_sdk.web.client import WebClient
from slack_sdk.errors import SlackApiError


logging.basicConfig(level=logging.DEBUG)

def sendMessage(slack_client, msg):
    try:   
        logging.debug("inside call")
        slack_client.chat_postMessage(
            channel='#general',
            text=msg
        )

    except SlackApiError as e:
        logging.error('Request to Slack API Failed: {}.'.format(e.response.status_code))
        logging.error(e.response)

if __name__ == "__main__":
    SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
    slack_client = WebClient(SLACK_BOT_TOKEN)
    logging.debug("authorized slack client")
    msg = "Good Morning!"
    sendMessage(slack_client, msg)