from flask import Flask, request
from webexteamssdk import WebexTeamsAPI
import json

#
# MODULE 3
#
# Your task: Create an "interactive" chatbot which simply replies to the person
# who sent a message to your bot.
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
# You only need to extend the "root()" function so the web server replies to any
# messages your bot receives. The content of the webhook triggered when a
# message is sent is already saved in the "data" variable.
#
# Useful references:
#   - http://flask.palletsprojects.com/en/1.1.x/quickstart/#
#   - https://webexteamssdk.readthedocs.io/en/latest/user/api.html#messages
#   - https://developer.webex.com/docs/api/guides/webhooks/handling-requests-from-webex-teams
#
# If you want to see a sample implementation, check out the "solution.py" file
# in the current folder. You can run it by changing the FLASK_APP environment
# variable to "solution.py" (see above for details).
#

app = Flask(__name__)

# update token to point to your Webex Teams bot
teams_token = ''
# update bot mailer so it points to your own Webex Teams bot mail address
bot_mail = ''

# main handler for webhook and web GUI
@app.route('/', methods=['POST', 'GET'])
def root():
  # handling reply via webhook (i.e., a post request from Webex Teams)
  if request.method == 'POST':

    # save JSON reply from Webex Teams in the data variable
    data = json.loads(request.data)

    # this is for debugging only, feel free to remove if not needed
    print(data)

    #
    # START PROGRAMMING HERE
    #
    # Hint: do not forget to check the sender mail address - otherwise, your
    # bot might reply to its own messages in an infinite loop ;-)
    #

    return ''

  # handling a request through the browser --> show HTML landing page
  elif request.method == 'GET':
    return 'Please check your commandline...'
