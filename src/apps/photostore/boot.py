from src.apps.photostore.PhotoStoreServer import PhotoStoreServer


def boot():
    server = PhotoStoreServer()
    server.run()
