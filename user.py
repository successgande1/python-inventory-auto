#Create a Class
class User:
    def __init__(self, user_name, user_pass, user_email, user_job_title):
        self.name = user_name
        self.password = user_pass
        self.email = user_email
        self.position = user_job_title

    #Method to Change Password in the class
    def change_password(self, new_password):
        self.password = new_password

    #Method to change email address
    def change_email(self, change_email):
        self.email = change_email

    #Method to Change Job Title
    def change_job_title(self, new_position):
        self.position = new_position

    #Method to Output Message to User
    def display_message(self):
        print(f"Hey {self.name}, Your email address is {self.email} and your Job role is {self.position}")



    