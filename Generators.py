from bs4 import BeautifulSoup
from urllib.request import urlopen

class TopicGenerator:
    def __init__(self, min_photos = 10):
        """
        Generator of great topic
        """
        self.main_url = "https://unsplash.com/s/photos/"
        self.min_photos = min_photos
        self.read_topics()


    def numbers_of_photos(self, topic):
        """
        Return how many photos about the topic is on the unsplash.com
        """
        url = self.main_url+topic
        try:
            request = urlopen(url)
            soup = BeautifulSoup(request.read(), "html.parser")
            response = soup.findAll("span", {"class": "_3ruL8"})
            count = int(response[0].get_text())
        except ValueError: # count is for example: "1.1k"
            return self.min_photos*2
        except:
            return -1
        return count


    def new_word(self, word):
        return word in self.topics


    def random_topic(self):
        """
        Get random word from herokuapp.com
        """
        new_word = True
        while new_word:
            request = urlopen("https://random-word-api.herokuapp.com/word?number=1")
            word = request.read().decode("utf-8")[2:-2]
            new_word = self.new_word(word)
        return word


    def read_topics(self):
        self.topics = []
        try:
            with open("topics_base.txt") as file:
                for line in file:
                    self.topics.append(line.strip())
        except FileNotFoundError:
            file = open("topics_base.txt", "w")
            file.close
            self.topics = []
        
    

    def add_topic(self, topic):
        file = open("topics_base.txt", "a+")
        print(topic, file = file)
        file.close()
        self.topics.append(topic)
        

    def find_new_topic(self):
        """
        Function created for being a thread which looking for good topic.
        The topic have more than self.min_limit photos on unsplash.com
        """
        random_topic = self.random_topic()
        numbers_of_photos = self.numbers_of_photos(random_topic)
        if numbers_of_photos >= self.min_photos:
            self.add_topic(random_topic)
            print(f"[+] {random_topic} - {numbers_of_photos}")
        else:
            print(f"[-] {random_topic} - {numbers_of_photos}")


    def good_topics(self):
        """
        Searching for topics until there is one.
        """
        while len(self.topics) != 1000:
            try:
                self.find_new_topic()
            except:
                print("[!] some error")
            


if __name__ == "__main__":
    gen = TopicGenerator(200)
    gen.good_topics()
