from webexteamssdk import WebexTeamsAPI

#
# MODULE 2
#
# Your task: register a webhook which should trigger when your bot receives a
# message. In order to test whether your script works properly, you can use
# the predefined "webhooks.py" application in your current folder which allows
# you to list all webhooks registered to your bot and remove them.
# ATTENTION: Do not forget to update the access token in the "webhooks.py" file!
#
# Once your script works properly, try to start ngrok (download it from
# https://ngrok.com/download), register a webhook which points to your local
# host and monitor the activity by visiting http://127.0.0.1:4040.
#
# You should use the official WebexTeamsAPI - the documentation is available
# on https://webexteamssdk.readthedocs.io/en/latest/.
# The documentation about Webex Teams webhooks is available on
# https://developer.webex.com/docs/api/guides/webhooks
#
# If you want to see a sample implementation, check out the "solution.py" file
# in the current folder.
#

# update token to point to your Webex Teams bot
teams_token = ''

api = WebexTeamsAPI(access_token=teams_token)

# creating a simple event listener for new messages
api.webhooks.create(name='message-created-listener', targetUrl='http://www.example.com/messageCreated', resource='messages', event='created')

# creating a simple event listener for deleted messages
api.webhooks.create(name='message-deleted-listener', targetUrl='http://www.example.com/messageDeleted', resource='messages', event='deleted')

# creating a simple event listener for attachment actions (required for
# adaptive cards)
api.webhooks.create(name='attachment-listener', targetUrl='http://www.example.com/attachments', resource='attachmentActions', event='created')
