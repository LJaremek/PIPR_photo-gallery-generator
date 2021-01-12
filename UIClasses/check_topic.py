from urllib.request import urlopen
from bs4 import BeautifulSoup


def check_topic(topic: str):
        """
        Checking if the topic is correctly.
        If it is:
            return True
        else:
            return False
        """
        url = f"https://unsplash.com/s/photos/{topic}"
        try:
            request = urlopen(url)
        except URLError:
            assert ConnectionError
            return False, -1
        soup = BeautifulSoup(request.read(), "html.parser")
        response = soup.findAll("span", {"class": "_3ruL8"})
        try:
            count = response[0].get_text()
            count = int(count) # count is a int number (<1000)
            return (count > 10, count)
        except ValueError: # count is bigger than 1000 (1.0k)
            return True, 300
