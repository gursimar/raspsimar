# API documentation - https://api.slack.com/methods
# pip install slacker slackweb flask-slack
from slacker import Slacker
import slackweb
from flask_slack import Slack
from webapp import app
from settings import *

class slackWebAPIAccess:
    def __init__(self, apiToken):
        self.client = Slacker(apiToken)

    def postMessage(self, channel, message):
        slack.chat.post_message('#general', 'Hello fellow slackers!')

    def getUserList(self):
        response = slack.chat.post_message('#general', 'Hello fellow slackers!')

class slackWebHooksAccess:
    def __init__(self, url):
        self.client = slackweb.Slack(url=url)

    #def post(self, message):
    #    self.client.notify(text=message)

    def post(self, message, channel=None, username=None):
        if channel is None and username is None:
            self.client.notify(text=message)
        if channel is None:
            self.client.notify(text=message, username=username)
        elif username is None:
            self.client.notify(text=message, channel=channel)
        else:
            self.client.notify(text=message, channel=channel, username=username)

# configure slash commands in slack
slack = Slack(app)
app.add_url_rule('/', view_func=slack.dispatch)

@app.command('your_command', token='your_token', team_id='your_team_id', methods=['POST'])
def your_method(**kwargs):
    text = kwargs.get('text')
    return slack.response(text)

if __name__ == '__main__':
    print 'Entering: slackAccess class'
    #slackWebAPI = slackWebAPIAccess()
    slackWH = slackWebHooksAccess(webHookURL)
    slackWH.post('test success')
    slackWH.post('test success',username='simar')
    slackWH.post('test success',username='simar', channel='#am')
    #slackSlashCommands = slackSlashCommandsAccess()

