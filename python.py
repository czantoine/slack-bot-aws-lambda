import os
from six.moves import urllib
import json

def send_text_response(event, response_text):
    # use postMessage if we want visible for everybody
    # use postEphemeral if we want just the user to see
    SLACK_URL = "https://slack.com/api/chat.postMessage"
    channel_id = event["event"]["channel"]
    user = event["event"]["user"]
    bot_token = os.environ["BOT_TOKEN"]
    data = urllib.parse.urlencode({
        "token": bot_token,
        "channel": channel_id,
        "text": response_text,
        "user": user,
        "link_names": True
    })
    data = data.encode("ascii")
    request = urllib.request.Request(SLACK_URL, data=data, method="POST")
    request.add_header("Content-Type", "application/x-www-form-urlencoded")
    res = urllib.request.urlopen(request).read()
    print('res:', res)

def check_message(text):
    if 'Hello' in text:
        return 'Hello from AWS Lambda'
    if 'who' in text:
        return 'https://github.com/Yris-ops | Join my slack https://join.slack.com/t/yrisgroupe/shared_invite/zt-1q51z8dmv-GC0XzUSclzBnUQ0tpKhznw'
    return None

def is_bot(event):
    return 'bot_profile' in event['event']

def lambda_handler(event, context):
    event = json.loads(event["body"])
    print('event', event)
    if not is_bot(event):
        message = check_message(event["event"]["text"])
        if message:
            send_text_response(event, message)

    return {
        'statusCode': 200,
        'body': 'OK'
    }
