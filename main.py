#curl -X POST      -H "Authorization: Bearer $TOKEN"      -H 'Content-type: application/json;charset=utf-8'     --data '{"channel":"#general","text":"Hello, Slack!"}' https://slack.com/api/chat.postMessage

from os import environ

if __name__ == "__main__":
    #do stuff
    print("hello, world!")
