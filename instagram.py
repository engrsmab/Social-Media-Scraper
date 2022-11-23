import datetime
import random
import time

from selenium import webdriver
import selenium.common.exceptions

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import wget
import pickle
from code_req import selenium_path,driver_configurations


class Instagram:
    options = driver_configurations()

    images = []

    def set_cred(self, username, password, target_user=None):
        self.username = username
        self.password = password
        self.target_user = target_user
        self.COOKIE_PATH = f"Cookies/{username}_INSTAGRAM_COOKIE.pkl"

        self.path = os.path.join(f"Instagram/{self.target_user}", str(datetime.date.today()))
        self.driver = webdriver.Chrome(selenium_path,options=self.options)
        self.hover = ActionChains(self.driver)

    def login(self):

        # Getting Instagram

        start_time = time.time()
        print('Getting Instagram')
        try:
            self.driver.get("http://www.instagram.com")
        except:
            return "Internet Issue. Please Try again"
        end_time = time.time()

        self.wait_time = end_time - start_time

        print("Time to Load Site: " + str(self.wait_time))

        try:
            print("Looking For Cookies")
            cookies = pickle.load(open(self.COOKIE_PATH, "rb"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            time.sleep(self.wait_time/2)
        except:

            print("Logging in Manually")
            try:
                username = WebDriverWait(self.driver, self.wait_time).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
            except TimeoutException as err:
                return err
            try:
                password = WebDriverWait(self.driver, self.wait_time).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
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
                WebDriverWait(self.driver, self.wait_time/2).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
            except TimeoutException as err:
                return err

            time.sleep(3)
            try:
                WebDriverWait(self.driver,self.wait_time*2).until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Save Info']")))
                self.driver.find_element(By.XPATH,"//button[normalize-space()='Save Info']").click()
            except:
                pass
            try:
                WebDriverWait(self.driver, self.wait_time * 2).until(
                    EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Log Out")]')))
                print("Login Successfully")
            except:
                try:
                    WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Search']")))
                    print("Login Successful")
                except:
                    
                    return "Login Failed"


            pickle.dump(self.driver.get_cookies(), open(self.COOKIE_PATH, "wb"))
        finally:
            try:
                self.driver.get('https://www.instagram.com/')
            except:
                return "Internet Issue"
            try:
                WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Not Now"]'))).click()
            except:
                pass

        return "Success"

    def get_target(self):
        print("Redirecting to Targeted User")
        try:
            self.driver.get("https://www.instagram.com/" + self.target_user + "/")
        except:
            return False
        time.sleep(self.wait_time)
        try:
            WebDriverWait(self.driver, self.wait_time * 2).until(
                EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Go back to Instagram.']")))
            print("Cannot Redirect to User")
            return False
        except:
            pass

        return True

    # change to search result
    def get_hashtag(self):
        print("Looking For HASHTAG")
        try:
            self.driver.get(f"https://www.instagram.com/explore/tags/{self.target_user}/")
        except:
            return False
        time.sleep(2)
        try:
            WebDriverWait(self.driver, self.wait_time * 2).until(
                EC.presence_of_element_located((By.XPATH, '//header//button')))
        except:
            print("No Hashtag Found!")
            return False

        return True

    #########################################################################
    #################### METHODS TO POST DATA FOR USER ######################
    #########################################################################
    def upload_feed(self, information):

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="New post"]/../parent::button'))).click()

        time.sleep(random.uniform(0.1, 1.0))

        if not information['media']:
            return "Media Not Available"

        media_source = str()
        for media_index in range(0, len(information['media'])):
            if media_index == len(information['media']) - 1:
                media_source += f"{information['media'][media_index]}"
            else:
                media_source += f"{information['media'][media_index]}\n"

        media = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="dialog"]//input')))
        media.send_keys(media_source)

        time.sleep(random.uniform(0.1, 0.5))
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Next']")))
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()
        time.sleep(random.uniform(0.1, 0.5))
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Next']")))
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Next']").click()

        if information['desc']:
            print("Typing Description")
            desc = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//textarea[@aria-label="Write a caption..."]')))
            for desc_char in information['desc']:
                time.sleep(random.uniform(0.08, 0.1))
                desc.send_keys(desc_char)

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//div[@role="dialog"]//button[text()="Share"]')))
        post_btn = self.driver.find_element (By.XPATH, '//div[@role="dialog"]//button[text()="Share"]')
        post_btn.click()

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Your post has been shared.']")))
        self.driver.find_element(By.XPATH, "//div[contains(@class,'qi72231t n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq i85zmo3j alzwoclg nu7423ey pkdwr69g sc980dfb kq3l28k4 rc95jfaf fsf7x5fv jcxyg2ei q46jt4gp b0eko5f3 r5g9zsuq fwlpnqze')]").click()

        return "Success"

    #########################################################################
    ############# METHODS TO FETCH DATA FROM USER OR SEARCH ITEMS ###########
    #########################################################################

    def get_follower(self):
        print("Getting User Followers")
        try:
            follower = WebDriverWait(self.driver, self.wait_time / 2).until(
            EC.visibility_of_element_located((By.XPATH, '//header//ul//li[2]//span'))).text
        except:
            follower = None
        return follower

    def get_following(self):
        print("Getting User Following")
        try:
            following = WebDriverWait(self.driver, self.wait_time / 2).until(
            EC.visibility_of_element_located((By.XPATH, '//header//ul//li[3]//span'))).text
        except:
            following = None
        return following

    def get_bio(self):
        print("Getting User Bio")
        try:
            bio = WebDriverWait(self.driver, self.wait_time / 2).until(
                (EC.visibility_of_element_located((By.XPATH, '//header/section/div[last()]/div')))).text
        except:
            bio = None

        return bio

    # add choice to download images and videos
    def get_posts(self, no_of_posts):

        count_posts = 1
        list_posts = []

        try:
            try:
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//article//a[@role="link"]')))
                posts = self.driver.find_elements (By.XPATH, '//article//a[@role="link"]')
            except:
                return "No Posts Found"
            for p in posts:

                if count_posts > no_of_posts:
                    break

                print("GETTING POST: " + str(count_posts))

                try:
                    self.driver.execute_script ("arguments[0].scrollIntoView();", p)
                    self.hover.move_to_element(p).perform()
                except:
                    pass

                print("GETTING POST LIKES")
                try:
                    likes = p.find_element(By.XPATH, './div[last()]//li[1]//span').text
                    print("Likes: ",likes)
                except:
                    likes = None

                print("GETTING POST COMMENTS")
                try:
                    comment = p.find_element(By.XPATH, './div[last()]//li[2]/div/span').text
                    print("Comments: ",comment)
                except:
                    comment = likes
                    likes = 0
               
                
                print("OPENING POST")

                # ERROR FOR THE HASHTAG AND USERS ARE SAME
                # THIS METHOD CLICKS FOR MAX USERS BUT NOT FOR SOME USERS
                try:
                    p.click()
                except:
                    continue

                try:
                    WebDriverWait(self.driver, self.wait_time * 2).until(EC.visibility_of_element_located((By.XPATH, '//article//section[1]')))
                    time.sleep(1)
                except TimeoutException as err:
                    return err

                try:
                    btn = self.driver.find_element(By.XPATH, '//article[@role="presentation"]//button[@aria-label="Next"]')
                except:
                    btn = None

                list_image = []
                list_video = []

                if btn:
                    print("MULTI POST DETECTED")
                    while True:
                        # GETTING IMAGES
                        try:
                            image = self.driver.find_elements(By.XPATH, '//article[@role="presentation"]/div/div[1]//img')
                        except:
                            pass

                        try:
                            video = self.driver.find_elements(By.XPATH, '//article[@role="presentation"]/div/div[1]//video')
                        except:
                            pass

                        # GETTING THERE LINKS
                        # TODO: ALSO SCRAPPING THE IMAGE OF THE VIDEO
                        for a in image:
                            try:
                                list_image.append(a.get_attribute('src'))
                            except:
                                pass

                        for b in video:
                            try:
                                list_video.append(b.get_attribute('src'))
                            except:
                                pass

                        # CHECKING IF THE IMAGES ARE COMPLETED
                        list_image = list(set(list_image))
                        list_video = list(set(list_video))

                        time.sleep(random.uniform(0.3,0.9))
                        try:
                            btn.click()
                        except:
                            # NO MORE POSTS AVAILABLE
                            break
                        time.sleep(random.uniform(0.5,1.4))

                if not btn:
                    image = None
                    video = None
                    try:
                        print("SINGLE IMAGE POST")
                
                        img_path2 = '//article[@role="presentation"]/div/div[1]//img'
                        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,img_path2)))
                        image = self.driver.find_element(By.XPATH, img_path2).get_attribute('src')
                        list_image.append(image)
                    except:
                        print("SINGLE VIDEO POST")
                        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//article[@role="presentation"]/div/div[1]//video')))
                        video = self.driver.find_element(By.XPATH, '//article[@role="presentation"]/div/div[1]//video').get_attribute('src')
                        list_video.append(video)
                    finally:
                        pass
                print("Getting Description")
                try:
                    desc = self.driver.find_element(By.XPATH,"//body/div/div/div/div/div/div/div/div/div/div/div/div/div[@role='dialog']/div/div[@role='dialog']/div/article[@role='presentation']/div/div/div/div[@role='presentation']/div/div/ul/div[@role='button']/li[@role='menuitem']/div/div/div[1]/div[1]").text
                    print("Desc: ",desc)
                except:
                    desc = ""

                try:
                    WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//article[@role="presentation"]//section[1]/following-sibling::div[2]//time')))
                    date_posted = self.driver.find_element(By.XPATH, '//article[@role="presentation"]//section[1]/following-sibling::div[2]//time').get_attribute('title')
                except:
                    date_posted = None

                try:
                    self.driver.find_element(By.XPATH, '//*[@aria-label="Close"]').click()
                except TimeoutException as err:
                    return err
                time.sleep(random.uniform(0.5,1.5))

                list_posts.append(
                    {
                        'description': desc,
                        'like': likes,
                        'comment': comment,
                        'image': list_image,
                        'video': list_video,
                        'date_posted': date_posted
                    }
                )
                count_posts += 1
        except selenium.common.exceptions.TimeoutException:
            print("Unstable Internet Connection Got This Result")


        return list_posts

# user = "okanything767@gmail.com"
# password = "12345678q@"
# target = "natgeo"
# insta = Instagram()

# def put():
#     insta.set_cred(user, password,target)

#     if not insta.login():
#         print("Failed to Login")
#     if not insta.get_target():
#         print("User Not Exist")

#     response = {
#         'username': target,
#         'bio': insta.get_bio(),
#         'follower': insta.get_follower(),
#         'following': insta.get_following(),
#         'posts': insta.get_posts(9)
#     }
#     return response

    
    
# print(put())

