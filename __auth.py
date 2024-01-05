from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


def auth_setup():
    # Authentication setup
    SCOPES = "https://www.googleapis.com/auth/gmail.send"
    store = file.Storage("token.json")  # Store credentials in a file
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
        creds = tools.run_flow(flow, store)
    service = build("gmail", "v1", http=creds.authorize(Http()))

    return service
