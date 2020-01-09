from flask import Flask, request
from webexteamssdk import WebexTeamsAPI
import json
import requests

#
# MODULE 4
#
# Your task: Create an chatbot which sends out a multiple choice question using
# adaptive cards.
#
# Before you start make sure you prepare your environment properly:
#   - update the access token in the "webhooks.py" file
#   - execute "ngrok http 5000" in a command line (see Moduole 2)
#   - copy & paste the public URL and execute "python webhooks.py <URL>" so that
#     the webhook will trigger a "post" event to your local host
#   - set the "FLASK_APP" environment variable to point to your "task.py" file:
#     * on Windows: "set FLASK_APP=task.py"
#     * on Mac/Linux: "export FLASK_APP=task.py"
#   - set the "FLASK_ENV" environment variable so it enables debug mode:
#     * on Windows: "set FLASK_ENV=development"
#     * on Mac/Linux: "export FLASK_ENV=development"
#   - start the web server by running "python -m flask run" in your command line
#   - don't forget to update the "teams_token" and "bot_mail" variables in this
#     file.
#
# You only need to extend the "sendQuestion()" function so the web server sends
# a question to the person you specify. You can trigger the function by visiting
# http://127.0.0.1:5000/sendquestion
#
# The processing of webhooks has already been done for you in the "root()"
# function and will simply display the transmitted answers in the command line
# as well as remove the old message in the conversation.
#
# Useful references:
#   - http://flask.palletsprojects.com/en/1.1.x/quickstart/#
#   - https://developer.webex.com/docs/api/guides/cards
#   - https://adaptivecards.io/explorer/
#   - https://adaptivecards.io/designer/
#
# If you want to see a sample implementation, check out the "solution.py" file
# in the current folder. You can run it by changing the FLASK_APP environment
# variable to "solution.py" (see above for details).
#

app = Flask(__name__)

# update token to point to your Webex Teams bot
teams_token = ''

# handler for sending out a single adaptive card
@app.route('/sendquestion')
def sendQuestion():

  wxtApi = WebexTeamsAPI(access_token=teams_token)

  # enter the mail address of your Webex Teams user here
  emailId = ''

  #
  # START PROGRAMMING HERE
  #
  # Replace the code below so it uses adaptive cards instead of markdown.
  #
  # Hint: Debugging adaptive cards is quite cumbersome - try to start with a
  # small card and only add one more item before testing it again.
  #

  messageToSend = '# Which of the following Collaboration tools do you like?\n\n'
  messageToSend += '1. Jabber\n\n'
  messageToSend += '2. Webex Teams\n\n'
  messageToSend += '3. Webex Meetings\n\n'
  messageToSend += '4. Skype\n\n'
  messageToSend += '5. Slack\n\n'
  messageToSend += '6. WhatsApp\n\n'
  messageToSend += '7. Facebook Messenger\n\n'
  messageToSend += '8. Microsoft Teams'

  wxtApi.messages.create(toPersonEmail=emailId, markdown=messageToSend)

  return 'Question sent'

def getAttachmentAction(attachmentId):
  """Returns the details of a Webex Teams attachment action as JSON object."""
  headers = {
    'content-type': 'application/json; charset=utf-8',
    'authorization': 'Bearer ' + teams_token
  }

  url = 'https://api.ciscospark.com/v1/attachment/actions/' + attachmentId
  response = requests.get(url, headers=headers)
  return response.json()

# main handler for webhook and web GUI
@app.route('/', methods=['POST', 'GET'])
def root():
  # handling reply via webhook (i.e., a post request from Webex Teams)
  if request.method == 'POST':

    # save JSON reply from Webex Teams in the data variable
    data = json.loads(request.data)

    # the attachment ID is saved in the "data" section of the JSON object
    attachmentId = data['data']['id']

    wxtApi = WebexTeamsAPI(access_token=teams_token)

    # get the details of the submitted data
    response = getAttachmentAction(attachmentId)

    # delete original adaptive card
    wxtApi.messages.delete(response['messageId'])

    # print response in console for debugging purposes
    print(response)

    return ''

  # handling a request through the browser --> show HTML landing page
  elif request.method == 'GET':
    return 'Please check your commandline...'
