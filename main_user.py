#import the user module and the User Class
from user import User

#import the post module with the Post Class
from post import Post

#Create an Object from the class
app_user_one = User("APOLLOS-GANDE", "Apollos", "info@stapollos.com.ng", "DevOps Engineer")

#Call Method to Display Message
#app_user_one.display_message()

#Create an object from the Post Class and replace its parameters
new_post = Post("This Tutorial is the best I have even seen, Hmmm ", app_user_one.name)

#Call the Method to display the Post Message
new_post.message_post_info()