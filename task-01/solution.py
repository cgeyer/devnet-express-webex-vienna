from webexteamssdk import WebexTeamsAPI

#
# TASK 1
#
# Your task: send a message to your Webex Teams account, preferrably a question.
# You should use the official WebexTeamsAPI - the documentation is available
# on https://webexteamssdk.readthedocs.io/en/latest/.
#
# If you want to see a sample implementation, check out the "solution.py" file
# in the current folder.
#
# Optional tasks:
#  * Send the same message to multiple users using a for loop and an array
#  * Try to format a message using markdown
#

# update token to point to your Webex Teams bot
teams_token = ''

api = WebexTeamsAPI(access_token=teams_token)

# update the email address to point to your personal account
api.messages.create(toPersonEmail='email@mail.com', text='Hello world!')


# Optional task 1: send message to multiple users
recipients = ['email1@mail.com', 'email2@mail.com']

for recipient in recipients:
  api.messages.create(toPersonEmail=recipient, text='Hello world!')


# Optional task 2: send message with formatting
api.messages.create(toPersonEmail='email@mail.com', markdown='# Sample title \n\n1. Sample item one\n\n2. Sample item two')
