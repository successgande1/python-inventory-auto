#Create Post Class
class Post:
    def __init__(self, message, author):
        self.post_message = message
        self.post_author = author

    #Method to Display Post and Author
    def message_post_info(self):
        print(f"{self.post_message} {self.post_author}")
