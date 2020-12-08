class InvalidTopic(Exception):
    """
    There are no photos about the topic.
    """
    def __init__(self):
        super().__init__("There are no photos about the topic.")
