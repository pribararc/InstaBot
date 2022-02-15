from instabot import Bot

my_bot = Bot()

my_bot.login(username="", password="")

# follow multiple users
my_bot.follow("nft.money")

#Unfollowed the non followers
my_bot.unfollow_non_followers()

#Upload an image
my_bot.upload_photo(" ", caption=" ")

# Send message to user
my_bot.send_message(" ", "username")

# like a post
my_bot.like_user("nft.collectors", amount=5, filtration=False)


# Comment on a post
user_id = my_bot.get_user_id_from_username("nft.collectors")
user_id = my_bot.get_last_user_medias(user_id)
my_bot.comment(comment_text= "This is very nice!!")



# Get list of followers of anyone
followers_list = my_bot.get_user_followers("nft.collectors")
following_list = my_bot.get_user_following("nft.collectors")

for each_follower in enumerate(followers_list):
    print(my_bot.get_username_from_user_id(each_follower))

for each_follow in following_list:
    print(my_bot.get_username_from_user_id(each_follow))

my_bot.logout()
