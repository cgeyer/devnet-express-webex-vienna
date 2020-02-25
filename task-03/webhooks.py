from webexteamssdk import WebexTeamsAPI
import sys

# update token to point to your Webex Teams bot
teams_token = ''


def clearWebhooks():
  """Will clear all webhooks associated with the current token."""

  api = WebexTeamsAPI(access_token=teams_token)
  webhooks = api.webhooks.list()

  # no need to iterate through all the webhooks if the list is empty
  if len(list(webhooks)) == 0:
    print('no webhooks registered')
    return

  print('clearing webhooks...')

  # iterate through all webhooks and delete them
  for webhook in webhooks:
    print('deleting webhook "%(webhookName)s"...' % {'webhookName' : webhook.name})
    api.webhooks.delete(webhook.id)

  print('done')


def listWebhooks():
  """Will list all webhooks associated with the current token."""

  api = WebexTeamsAPI(access_token=teams_token)
  webhooks = api.webhooks.list()

  # no need to iterate through all the webhooks if the list is empty
  if len(list(webhooks)) == 0:
    print('no webhooks registered')
    return

  print('listing webhooks...')

  # iterate through all webhooks and list the details
  for webhook in webhooks:
    print('webhook "%(webhookName)s" - target URL: %(url)s - resource: %(resource)s - event type: %(event)s' % {'webhookName' : webhook.name, 'url' : webhook.targetUrl, 'resource' : webhook.resource, 'event' : webhook.event})

  print('done')


def registerWebhook(url):
  """Registers an event listener for new messages to the specified URL."""

  print('registering new webhook to URL %(url)s' % {'url' : url})

  api = WebexTeamsAPI(access_token=teams_token)
  api.webhooks.create(name='message-created-listener', targetUrl=url, resource='messages', event='created')

  print('done')


def main():
  # the script only supports 3 arguments - "clear", "list" or a URL
  if (len(sys.argv) == 2):
    if (sys.argv[1] == 'clear'):
      clearWebhooks()
    elif (sys.argv[1] == 'list'):
      listWebhooks()
    else:
      registerWebhook(sys.argv[1])
  else:
    print('Usage: [python] ' + sys.argv[0] + ' clear|list|url')


if __name__ == "__main__":
  main()
