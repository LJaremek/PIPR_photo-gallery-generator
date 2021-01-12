class InvalidTopic(Exception):
    """
    There are no photos about the topic.
    """
    def __init__(self):
        super().__init__("There are no photos about the topic.")


class UnsplashConnectError(Exception):
    """
    There are a problem with connection to unsplash.com
    """
    def __init__(self):
        super().__init__("There are not connection to unsplash.com")
