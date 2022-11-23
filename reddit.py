import datetime
import time
import pickle
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException
import os
import wget
import random
from code_req import selenium_path,driver_configurations


class Reddit:

    data = []
    options = driver_configurations()

    def set_cred(self, username, password, target_user=None):
        self.username = username
        self.password = password
        self.target_user = target_user
        self.COOKIE_PATH = f"Cookies/{username}_REDDIT_COOKIE.pkl"

        self.path = os.path.join(f"Reddit/{self.target_user}", str(datetime.date.today()))
        self.driver = webdriver.Chrome(selenium_path, options=self.options)

    def login(self):

        start_time = time.time()
        print('Getting Reddit')
        try:
            self.driver.get("https://www.reddit.com/login/")
        except:
            return "It seems you have internet issue"
        
        end_time = time.time()

        self.wait_time = end_time - start_time
        print("Time to get Site: " + str(self.wait_time))

        try:
            print("Looking For Cookies")
            cookies = pickle.load(open(self.COOKIE_PATH, "rb"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            time.sleep(self.wait_time / 2)
        except:

            print("Logging in Manually")

            try:
                username = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="loginUsername"]')))
                password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="loginPassword"]')))
            except TimeoutException as err:
                return err

            # Filling Username and Password
            print('Filling Username and Password')
            username.clear()
            for i in self.username:
                time.sleep(random.uniform(0.02, 0.1))
                username.send_keys(i)

            password.clear()
            for i in self.password:
                time.sleep(random.uniform(0.02, 0.1))
                password.send_keys(i)

            time.sleep(0.2)

            try:
                WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, '//form[@action="/login"]//*[@type="submit"]'))).click()
            except TimeoutException as err:
                return err

            time.sleep(3)

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//button[@id="USER_DROPDOWN_ID"]')))

            except:
                print("Failed to Login")
                return "Failed to Login"

            pickle.dump(self.driver.get_cookies(), open(self.COOKIE_PATH, "wb"))

        return "Login Successfuly"

    #################################################################
    ############## REDDIT POSTING DATA FROM ACCOUNT ################
    #################################################################
    def upload_image(self,images):
        c = 0
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//p[@class='_23Ktfv_B7IB6GfAwZ1n5KM']")))
        except:
            return c
        for image in images:
            if c == 0:
                p = "//input[@class='sU2P34us34ODfjtvAFHEh']"
            else:
                p =  "//input[@class='_8GGSjoMJRi3bIAaFgk5VT']"
            try:
                self.driver.find_element(By.XPATH,p).send_keys(image)
                time.sleep(2)
            except:
                return c
            c += 1
        return c
        
    def upload_on_home_feed(self, information):
        try:
            self.driver.get(f'https://www.reddit.com/{information["community"]}/submit')
        except:
            return f"{information['community']} community doesn't exist."

        title_path = '//textarea[@placeholder="Title"]'
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,title_path)))
            title = self.driver.find_element(By.XPATH, title_path)
            for title_char in information['title']:
                time.sleep(random.uniform(0.1, 0.3))
                title.send_keys(title_char)
        except:
            return "unable to locate Title field please retry"

        if information["desc"] != None:
            desc_path = '//div[@role="textbox"]'
            try:
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,desc_path)))
                desc = self.driver.find_element(By.XPATH, desc_path)
                for desc_char in information['desc']:
                    time.sleep(random.uniform(0.1, 0.2))
                    desc.send_keys(desc_char)
            except:
                print("Posts is disabled")

        if information['media'] != None:
            

            if self.upload_image(information['media']) == 0:
            
                try:
                    self.driver.find_element(By.XPATH,"//button[normalize-space()='Images & Video']").click()
                except TimeoutException as err:
                    print(err)
           
                if self.upload_image(information['media']) == 0:
                    print(f"Media is disabled for the community {information['community']}")
                    
          
                   

            

        if information['link'] != None:
            link_path = "//textarea[@placeholder='Url']"
            
            try:
                self.driver.find_element(By.XPATH,"//button[normalize-space()='Link']").click()
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,link_path)))
                self.driver.find_element(By.XPATH,link_path).send_keys(information['link'])

            except:
                print(f"Link is disabled for the community {information['community']}")


        # if not information['get_post_notification']:
        #     # CODE TO CHANGE NOTIFICATION
        #     pass

        

        try:
            self.driver.find_element(By.XPATH,"//button[@role='button'][normalize-space()='Post']").click()
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='_3h_9YwxjuOr77VhScPrjCI']")))
            time.sleep(2)
            return self.driver.find_element(By.XPATH,"//span[@class='_3h_9YwxjuOr77VhScPrjCI']").text
        except:
            pass
        
        return "Success"

    #################################################################
    ############## REDDIT FETCHING DATA FROM ACCOUNT ################
    #################################################################

    def get_target(self):
        print("Redirecting to Target User")
        try:
            self.driver.get(f"https://www.reddit.com/user/{self.target_user}")
        except:
            return "Unable to get this user"
        time.sleep(self.wait_time / 2)

        return "Done"

    def get_subreddit(self):
        print("Redirecting to Target User")
        try:
            self.driver.get(f"https://www.reddit.com/r/{self.target_user}")
        except:
            return False
        time.sleep(self.wait_time / 2)

        return True

    def search(self):
        print("Searching")
        try:
            self.driver.get(f'https://www.reddit.com/search/?q={self.target_user}')
        except:
            return False
        time.sleep(self.wait_time / 2)

        return True

    def get_images_and_related_data(self, no_of_posts):

        count_posts = 0
        list_posts = []

        # SCROLLING THROUGH PAGE
        scroll = round(no_of_posts / 6) + 1
        for _ in range(0, scroll + 1):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//div[ @data-testid="post-container"]//a[@data-click-id="body"]')))
        except TimeoutException as err:
            clos_btn_xpath = "//div[@role='dialog']//div[contains(text(),'Interests')]"
            try:
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,clos_btn_xpath)))
                self.driver.find_element(By.XPATH,"//div[@role='dialog']//button[@aria-label='Close']").click()
            except:
                pass
            # return "Unwanted pop up apeared. I cannot handle it yet. Add XPATH of pop-up close button"
        posts = self.driver.find_elements(By.XPATH, '//div[ @data-testid="post-container"]//a[@data-click-id="body"]')
        posts = [a.get_attribute('href') for a in posts]

        print(f"Total Posts Found {len(posts)}")
        done = False
        for a in posts:

            if count_posts >= no_of_posts:
                done = True
                break

            # Getting Description
            print("Getting Data For Post: " + str(count_posts+1))
            try:
                self.driver.get(a)
            except:
                 print(f"Unable to get link {a}")

            img = None
            video = None

            try:
                try:
                    video = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//div[@data-test-id="post-content"]/div[5]//video')))
                except:
                    video = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(
                            (By.XPATH, '//div[@data-test-id="post-content"]//video')))
                video = video.get_attribute('src')
            except:
                try:
                    img = self.driver.find_element(By.XPATH,
                                               '//div[@data-test-id="post-content"]/div[5]//img').get_attribute('src')
                except:
                    img = self.driver.find_element(By.XPATH, '//div[@data-test-id="post-content"]/div[4]//img').get_attribute('src')
            finally:
                if (not img) and not (video):
                    print("No Media Found. Skipping this post")
                    continue

            try:
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//button[@data-click-id="upvote"]/following-sibling::div')))
                upsight = self.driver.find_element(By.XPATH, '//button[@data-click-id="upvote"]/following-sibling::div').text
            except TimeoutException as err:
                upsight = "0"
       
            try:
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//div[@data-test-id="post-content"]/div[last()]/div/div[1]//span')))
                comment = self.driver.find_element(By.XPATH, '//div[@data-test-id="post-content"]/div[last()]/div/div[1]//span').text
                comment = comment.replace(" ", "").replace("Comments", "")
            except TimeoutException as err:
                comment = "0"

            
           

            count_posts += 1

            list_posts.append(
                {
                    'img': img,
                    'video': video,
                    'comment': comment,
                    'upsight': upsight,
                    'post_url': a
                }
            )
            time.sleep(random.uniform(0.5,1.4))
        if not done:
            print(f"Only {len(posts)} posts found")
            return [list_posts,f"Only {len(posts)} posts found"]

        return list_posts



    """
    def save_posts(self):
        def save():
            # print(images)
            for image in self.data:
                if not image['image']:
                    continue
                image_name = image['image'].split("?")[0].split("/")[-1]
                save_as = os.path.join (self.path, image_name)
                wget.download(image['image'], save_as)

            for video in self.data:
                if not video['video']:
                    continue
                video_name = video['video'].split('/')[4].split('=')[1]
                self.driver.get(video['video'])

        print("Checking for Directory")
        if not os.path.exists("Reddit"):
            os.mkdir("Reddit")
            os.mkdir(f"Reddit/{self.target_user}")
            os.mkdir(f"Reddit/{self.target_user}/{str(datetime.date.today())}")
            save()
        elif not os.path.exists(f"Reddit/{self.target_user}"):
            os.mkdir(f"Reddit/{self.target_user}")
            os.mkdir(f"Reddit/{self.target_user}/{str(datetime.date.today())}")
            save()
        elif not os.path.exists(f"Reddit/{self.target_user}/{str(datetime.date.today())}"):
            os.mkdir(f"Reddit/{self.target_user}/{str(datetime.date.today())}")
            save()
        else:
            save()
    """
# red = Reddit()
# user = "mubbashir_ahmed_"
# password = "12345678q@"
# def put():
#     red.set_cred(user, password)

#     if not red.login():
#         print("Failed to Login")
#     post = {
#         "title": "Azeem Enterprises",
#         "desc": "This is my 2nd post",
#         "community": "u/mubbashir_ahmed_",
#         "media":["/Users/macbookpro/Desktop/Projects/Web-Scrapping/Social Media Automation/azeem_logo.png","/Users/macbookpro/Desktop/Projects/Web-Scrapping/Social Media Automation/azeem_logo.png"],
#         "poll":None,
#         "link":"azeementerprises.org"
#     }

    
#     status = red.upload_on_home_feed(post)
#     print(status)
# put()
        
