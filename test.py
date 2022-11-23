


host = "http://192.168.100.250:5000"    # UPDATE THIS ON EACH SERVER RUN
user = "03248546559"
password = "thisisid123"
from requests import put,get
# ===================================================================
#                   FACEBOOK PUBLISHING                             =
#====================================================================
# Facebook User Posting:

data = {"email":user,
        "password":password,
        "desc":["First Post","Second Post"],
        "image":[None,None],
        "feeling":["happy","sad"],
        "tag":[["syed mubashir azeem bukhari"],["maavia khalid"]]
        }

fb_publish_usr = put(f"{host}/facebook/publish/user",json=data)
print(fb_publish_usr.content)

# Facebook Page Posting
data = {"email":user,
        "password":password,
        "desc":["First Post","Second Post"],
        "image":[None,None],
        "feeling":["happy","sad"],
        "tag":[["syed mubashir azeem bukhari"],["maavia khalid"]],
        "page": "/Automation-dummy-110033485155418"
        }
fb_publish_page = put(f"{host}/facebook/publish/page",json=data)

# ===================================================================
#                   PINTEREST PUBLISHING                            =
#====================================================================
# Pinterest Posting
username = "okanything767@gmail.com"
password = "12345678q@"
data = {    
           "email":user,
        "password":password,
            "title": ["Azeem Enterprises","2nd Title"],
            "desc": ["I am Selenium!","I am Selenium!"],
            "destination_link": ["azeementerprises.org","azeementerprises.org"],
            "media": [None,None]
        }

pin_publish_post = put(f"{host}/pinterest/post/pin",json=data)

# ===================================================================
#                   REDDIT PUBLISHING                               =
#====================================================================
user = "mubbashir_ahmed_"
password = "12345678q@"
post = {
        "email":user,
        "password":password,
        "title": ["Azeem Enterprises","2nd Title"],
        "desc": ["I am Selenium!","I am Selenium!"],
        "community": ["u/mubbashir_ahmed_","u/mubbashir_ahmed_"],
        "media":[["Image Link Here","Image Link Here"],["Image for 2nd Post","Image for 2nd Post"]],
        "link":["azeementerprises.org",None]
    }

reddist_publish_post = put(f"{host}/reddit/post/feed",json=post)

# ===================================================================
#                   INSTAGRAM PUBLISHING                            =
#====================================================================
user = "okanything767@gmail.com"
password = "12345678q@"
post = {
        "email":user,
        "password":password,
        "title": ["Azeem Enterprises"],
        "desc": ["My First Post Now"],
        "media":[["Image 1 for post 1","Image 2 for post 2"]],
 
    }
insta_publish_post = put(f"{host}/instagram/post/feed",json=post)


# ===================================================================
#                   TWITTER PUBLISHING                            =
#====================================================================

data = {
        "email":"okanything767@gmail.com",
        "password": "12345678q@",
        "username": "ok_anything_767",
        "title":["Twitter Post"],
        "desc": ["First Post"],
        "media":[["/Users/macbookpro/Desktop/Projects/Web-Scrapping/Social Media Automation/azeem_logo.png"]],
    }
    
twitter_publish_post = put(f"{host}/twitter/post/feed",json=data)
print(twitter_publish_post.json)

# reddit_user = put(f"{host}/reddit/fetch/user",data={"email":"engr.smab","password":"mr03056842507","target_user":"engr.smab","no_of_posts":9})
# reddit_search = put(f"{host}/reddit/fetch/search",data={"email":"engr.smab","password":"mr03056842507","search":"engr.smab","no_of_posts":9})
# reddit_sub = put(f"{host}/reddit/fetch/subreddit",data={"email":"engr.smab","password":"mr03056842507","subreddit":"engr.smab","no_of_posts":9})
# reddit_post = put(f"{host}/reddit/post/feed",json={"email":user,"password":password,"post_data":"Hi"})

# print(reddit_search.text)
# print(reddit_search)

# fb_user = put(f"{host}/facebook/fetch/user",data={"email":user,"password":password,"target_user":"mubashir.azeem.142","no_of_posts":9})


#=========== Index XPath

# comment
"(//div[@id='jsc_c_te'])[1]"
# Post
"(//div)[1036]"

# Image
"(//div[@id='jsc_c_tf'])[1]"

# Do Share
"(//div[@aria-label='Send this to friends or post it on your timeline.'])[4]"

# Do Comment
"(//div[@aria-label='Leave a comment'])[4]"

# Get Likes
"(//span[@class='f7rl1if4 adechonz f6oz4yja dahkl6ri axrg9lpx rufpak1n qtovjlwq qbmienfq rfyhaz4c rdmi1yqr ohrdq8us nswx41af fawcizw8 l1aqi3e3 sdu1flz4'])[52]"

# Get Comment Count
"(//span)[432]"

# ================= Rel XPath ==================

# Get Comments:
"//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/span[1]"
