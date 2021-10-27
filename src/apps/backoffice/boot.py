from src.apps.backoffice.BackofficeServer import BackofficeServer


def boot():
    server = BackofficeServer()
    server.run()
