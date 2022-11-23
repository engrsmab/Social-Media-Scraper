import datetime

import selenium.common.exceptions
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import pickle
import time
import random
from code_req import selenium_path,driver_configurations

class Twitter:
    options = driver_configurations()

    def set_cred(self, email, password,username, target_user=None):
        self.email = email
        self.username = username
        self.password = password
        self.target_user = target_user
        self.COOKIE_PATH = f"Cookies/ok_anything_767_TWITTER_COOKIE.pkl"

        self.path = os.path.join(f"Twitter/{self.target_user}", str(datetime.date.today()))
        self.driver = webdriver.Chrome(selenium_path, options=self.options)
        self.hover = ActionChains(self.driver)

    def login(self):

        start_time = time.time()
        print("Getting Twitter")
        try:
            self.driver.get ("https://twitter.com/i/flow/login")
        except:
            return "Internet Issue. Unable to get url"
        end_time = time.time()

        self.wait_time = end_time - start_time
        print("Time to get Site: " + str(self.wait_time))

        try:
          
            print('Looking For Cookies')
            cookies = pickle.load(open(self.COOKIE_PATH, 'rb'))
            for c in cookies:
                self.driver.add_cookie(c)
            time.sleep(self.wait_time/2)
            try:
                self.driver.get("https://twitter.com/home")
            except:
                return "Unable to open targeted url. Internet Issue, Please try with stable internet"
        except:

            print("Login in Manually")
            try:
                username = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//input[@autocomplete="username"]')))
            except:
                return "Username Entry Could Not be located"
            username.clear()
            for i in self.email:
                time.sleep(random.uniform(0.02, 0.1))
                username.send_keys(i)

            time.sleep(0.3)
            try:
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//span[text()="Next"]')))
                self.driver.find_element(By.XPATH, '//span[text()="Next"]').click()
            except:
                print("")
                return "Next Button Could not be located"
            try:
                user = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//input[@name="text"]')))
                user.clear()
                for i in self.username:
                    time.sleep(random.uniform(0.02, 0.1))
                    user.send_keys(i)
                self.driver.find_element(By.XPATH,"//div[@class='css-1dbjc4n r-pw2am6']").click()
            except:
                pass
            
            try:    
                password = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
                password.clear()
                for i in self.password:
                    time.sleep(random.uniform(0.02, 0.1))
                    password.send_keys(i)
            
            except:

                return "Password Entry Could not be located"
            

            time.sleep(random.uniform(0.2, 0.5))
            try:
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//span[text()="Log in"]')))
                self.driver.find_element(By.XPATH, '//span[text()="Log in"]').click()
            except:

                return "Login Button Could not be located"
            try:
                    WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//body/div[@id='react-root']/div/div/div[@id='layers']/div/div/div/div[@role='dialog']/div/div/div[@role='group']/div[@role='dialog']/div/div/div[@role='group']/div/div/div/div[2]")))
                    return "Email Varification is required. Unable to login"
            except:
                    pass
            pickle.dump(self.driver.get_cookies(), open(self.COOKIE_PATH, "wb"))

        try:
            WebDriverWait(self.driver, self.wait_time + 3).until(EC.presence_of_element_located((By.XPATH, '//nav[@role="navigation"]')))
        except:
      
            return "Failed to Login"

        return "Login Successfuly"

    #########################################################################
    #################### METHODS TO POST DATA FOR USER ######################
    #########################################################################

    def upload(self, information):

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='textbox']")))

        if information['desc']:
            print("Typing Description")
            desc = self.driver.find_element(By.XPATH, "//div[@role='textbox']")
            desc.send_keys(information['desc'])
            time.sleep(1)

        if information['media']:
            media_source = str()
            for media_index in range(0, len(information['media'])):
                if media_index == len(information['media']) - 1:
                    media_source += f"{information['media'][media_index]}"
                else:
                    media_source += f"{information['media'][media_index]}\n"

            media = self.driver.find_element(By.XPATH, '//input[@data-testid="fileInput"]')
            media.send_keys(media_source)
            time.sleep(3)

        if information['media'] or information['desc']:
            self.driver.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]').click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Your Tweet was sent.")]')))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, '//span[contains(text(), "Your Tweet was sent.")]')))

        return information

    #########################################################################
    ############# METHODS TO FETCH DATA FROM USER OR SEARCH ITEMS ###########
    #########################################################################

    def get_target(self):
        print("Redirecting to Targeted User")
        try:
            self.driver.get('https://twitter.com/' + str(self.target_user )+ "/media")
        except:
            return "Unable to get to url. Internet Issue or server down"
        try:
            WebDriverWait(self.driver, self.wait_time + 3).until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//div[@data-testid="UserName"]')))
        except:
           
            return "Cannot Redirect to User"

        return "Done"

    def search(self):
        print("Searching for Data")
        try:
            self.driver.get(f'https://twitter.com/search?q={self.target_user}&src=typed_query')
        except:
            return False
        try:
            self.driver.find_element (By.TAG_NAME, 'body').send_keys (Keys.PAGE_DOWN)
            WebDriverWait(self.driver, self.wait_time + 3).until(
                EC.visibility_of_element_located((By.XPATH, '//article[@role="article"]')))
        except:
            print("Cannot Find Results")
            return False

        return True

    def get_following(self):
        print("Getting Following")
        following = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, '//div[@data-testid="UserName"]/following-sibling::div[3]/div[1]//span[1]')))
        return following.text

    def get_follower(self):
        print("Getting Follower")
        following = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//div[@data-testid="UserName"]/following-sibling::div[3]/div[2]//span[1]')))
        return following.text

    def get_bio(self):
        print("Getting Bio")
        bio = WebDriverWait (self.driver, 20).until (
            EC.visibility_of_element_located((By.XPATH, '//div[@data-testid="UserDescription"]')))
        return bio.text

    def get_name(self):
        print("Getting Name")
        try:
            name = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@data-testid="UserName"]//div//span'))).text
        except:
            name = "Not Found"
        return name

    def get_location(self):
        print("Getting Location")
        try:
            location = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, '//span[@data-testid="UserLocation"]//span'))).text
        except:
            location = "Not Found"
        return location

    def get_join_date(self):
        print("Getting Join Date")
        try:
            join_date = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//span[@data-testid="UserJoinDate"]//span'))).text
        except:
            join_date = "Not Found"
        print(join_date)
        return join_date

    def get_images(self, no_of_posts):

            tweet = []
            list_tweet = []
            count = 1

        # SCROLLING THROUGH PAGE
        # try:
            while True:
                time.sleep(random.uniform(0.01, 0.1))
                try:
                    WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//div[@data-testid="cellInnerDiv"]//a[contains(@href, "status")]')))
                    tl = self.driver.find_elements(By.XPATH, '//div[@data-testid="cellInnerDiv"]//a[contains(@href, "status")]')
                except TimeoutException as err:
                    return err
                for link in tl:
                    try:
                        tweet.append(link.get_attribute('href').split("/")[5])
                    except:
                        pass

                tweet = list(set(tweet))
                if len(tweet) > no_of_posts:
                    break
                try:
                    self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
                except: 
                    continue
                time.sleep(random.uniform(0.1, 0.5))

            for t in tweet:
                if count > no_of_posts:
                    break
                
                post_url = f"https://twitter.com/{self.target_user}/status/{t}"
                print(post_url)
                try:
                    self.driver.get(post_url)
                except:
                    return "Internet Error Unable to open post URL. Please try again with stable internet"

                print("Getting Tweet : " + str(count))
                count += 1

                print("Waiting to Load")
                try:
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//article[@data-testid="tweet"][1]')))
                except:
                    continue

                try:
                    print("Getting Desc")
                    desc = self.driver.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text
                except:
                    desc = None

                print("Getting Likes")
                like_xpath = "//span[contains(text(),'Likes')]"
                role = "//body/div[@id='react-root']/div/div/div[1]"
                
                # self.driver.execute_script("window.scrollTo(1,document.body.scrollHeight)")
                # time.sleep(2)
                # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,role)))
                # fine = self.driver.find_elements(By.XPATH, role)
        
                # for f in fine:
                #     print(f.text)
                
                
                try:
                    
                    WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,like_xpath)))
                    like = self.driver.find_element(By.XPATH, like_xpath).text
                except:
                    like = "0"
            

                print("Getting Retweets")
                retweets_xpath = "//span[contains(text(),'Retweets')]"
                try:
                    WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,retweets_xpath)))
                    retweet = self.driver.find_element(By.XPATH, retweets_xpath).text
                except:
                    retweet = "0"
                # reply = self.driver.find_element(By.XPATH, './/div[@data-testid="reply"]//span').text

                list_image = []
                try:
                    print("Looking For Image")
                    img = self.driver.find_elements(By.XPATH, '//div[@data-testid="cellInnerDiv"][1]//div[@data-testid="tweetPhoto"]//img')
                    for a in img:
                        list_image.append(a.get_attribute('src'))
                except:
                    list_image = []

                list_video = []
                try:
                    print("Looking For Video")
                    video = self.driver.find_elements(By.XPATH, '//div[@data-testid="cellInnerDiv"][1]//video')
                    for a in video:
                        list_video.append(a.get_attribute('src'))
                except:
                    video = None

                list_tweet.append(
                    {
                        'desc': desc,
                        'like': like,
                        'retweet': retweet,
                        'image': list_image,
                        'video': list_video
                    }
                )
                time.sleep(random.uniform(0.5, 1))
        # except selenium.common.exceptions.TimeoutException:
        #     print("Unstable Internet Connection")

            return list_tweet
"""
images=[]
n_scrolls = 3

caption=[]
result = []

def get_tweet_data(card):
    images = []
    #Extract data from tweet data
    time.sleep(3)
    # username = card.find_element_by_xpath('.//span').text
    # handle = card.find_element_by_xpath('.//span[contains(text(), "@")]').text
    try:
        postdate = card.find_element_by_xpath('//time').get_attribute('datetime')
    except:
        return
    text = card.find_element_by_xpath('.//div[@class="css-1dbjc4n"]').text

    reply_count = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
    retweet_count = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
    like_count = card.find_element_by_xpath('.//div[@data-testid="like"]').text
    # pic=card.find_elements_by_xpath('.//div[@data-testid="tweetPhoto"]')
    pic = card.find_elements(By.TAG_NAME, "img")
    for k in pic:
        images.append(k.get_attribute("src"))
    del images[0]

    str1 = ' , '.join(str(e) for e in images)

    path = os.getcwd()

    path = os.path.join(path, str(datetime.date.today()))

    if (os.path.exists(str(datetime.date.today()))):
        counter = 0
        for image in images:
            save_as = os.path.join(path, user+" "+str(counter) + '.jpg')
            wget.download(image, save_as)
            counter += 1
    else:
        os.mkdir(path)
        counter = 0
        for image in images:
            save_as = os.path.join(path, user+" "+str(counter) + '.jpg')
            wget.download(image, save_as)
            counter += 1

    print(path)

    tweet = (postdate, text, reply_count, retweet_count, like_count, str1 )
    # print(tweet)
    return tweet


def start_scraping():
    data = []
    tweet_ids = set()
    last_position = driver.execute_script("return window.pageYOffset;")
    scrolling = True

    while scrolling:
        page_cards = driver.find_elements_by_xpath('//article[@data-testid="tweet"]')
        for card in page_cards[-15:]:
            tweet = get_tweet_data(card)
            if tweet:
                tweet_id = ''.join(tweet)
                if tweet_id not in tweet_ids:
                    tweet_ids.add(tweet_id)
                    data.append(tweet)

        scroll_attempt = 0
        while True:
            # check scroll position
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(1)
            curr_position = driver.execute_script("return window.pageYOffset;")
            if last_position == curr_position:
                scroll_attempt += 1

                # end of scroll region
                if scroll_attempt >= 3:
                    scrolling = False
                    break
                else:
                    time.sleep(2)  # attempt to scroll again
            else:
                last_position = curr_position
                break
    print(data)

start_scraping()
"""

# email = "okanything767@gmail.com"
# password = "12345678q@"
# user = "ok_anything_767"
# twi = Twitter()
# def put():
    # twi.set_cred(email, password,user)

    # if not twi.login():
    #     return 'Failed to Login'
    
    # data = {
    #     "email":"",
    #     "password": "",
    #     "username": "",
    #     "title":["Twitter Post"],
    #     "desc": ["First Post"],
    #     "media":[["/Users/macbookpro/Desktop/Projects/Web-Scrapping/Social Media Automation/azeem_logo.png"]],

    # }
    # message = []
    # for i in range(len(data['title'])):
    #     post = {
    #     "title":data['title'][i],
    #     "desc": data['desc'][i],
    #     "media":data['media'][i],

    #     }
    #     status = twi.upload (post)
    #     message.append (
    #             {
    #                 'no': i + 1,
    #                 'status': status
    #             })
    #     return message
# print(put())


      