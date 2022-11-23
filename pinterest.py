import datetime
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import json
import pickle
import time
import random
from code_req import selenium_path,driver_configurations


class Pinterest:

    images = []

    chr_options = driver_configurations()

    def set_cred(self, email, password, target_user=None):
        self.email = email
        self.password = password
        self.target_user = target_user
        self.COOKIE_PATH = f"Cookies/{email}_PINTEREST_COOKIE.pkl"
        self.chr_driver = webdriver.Chrome(selenium_path, options=self.chr_options)
        self.hover = ActionChains (self.chr_driver)

    def login(self):

        start_time = time.time()
        print("Getting Pinterest")
        try:
            self.chr_driver.get("https://www.pinterest.com/login/")
        except:
            return "No Internet. Please retry with stable internet"
        end_time = time.time()

        self.wait_time = end_time - start_time
        print("Time to get Site: " + str(self.wait_time))

        try:
            print("Looking For Cookie")
            cookies = pickle.load(open(self.COOKIE_PATH, "rb"))
            for cookie in cookies:
                self.chr_driver.add_cookie(cookie)
            self.chr_driver.refresh()
            time.sleep(self.wait_time / 2)
        except:
            print("Login in Manually")
            try:
                email = WebDriverWait(self.chr_driver, self.wait_time / 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='id']")))
            except TimeoutException as err:
                return err
            try:
                password = WebDriverWait(self.chr_driver, self.wait_time / 2).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
            except TimeoutException as err:
                return err

            print('Filling Username and Password')
            email.clear()
            for i in self.email:
                time.sleep(random.uniform(0.02, 0.1))
                try:
                    email.send_keys(i)
                except:
                    return "Unable to write email. Try Again"

            password.clear()
            for i in self.password:
                time.sleep(random.uniform(0.02, 0.1))
                try:
                    password.send_keys(i)
                except:
                    return "Unable to write Password. Try Again"

            time.sleep(0.2)
            try:
                WebDriverWait(self.chr_driver, self.wait_time / 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
            except TimeoutException as err:
                return err

            try:
                WebDriverWait(self.chr_driver, self.wait_time).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@data-test-id='header-profile']")))
                print("Login Successfully")
            except:
                print("Failed to Login")
                return "Unable to Login"

            pickle.dump(self.chr_driver.get_cookies(), open(self.COOKIE_PATH, 'wb'))

        return "Success"

    def upload_pin(self, information):
        try:
            self.chr_driver.get('https://www.pinterest.com/pin-builder/')
        except:
            return "page not found"

        total_pins = 1
        while True:
            if total_pins == len(information['media']):
                break
            total_pins += 1
            WebDriverWait(self.chr_driver,10).until(EC.visibility_of_element_located((By.XPATH,'//div[@data-test-id="pin-builder-add-draft"]/parent::button')))
            self.chr_driver.find_element(By.XPATH, '//div[@data-test-id="pin-builder-add-draft"]/parent::button').click()
            time.sleep(random.uniform(0.8, 0.2))

        WebDriverWait(self.chr_driver,10).until(EC.visibility_of_any_elements_located((By.XPATH,'//div[@data-test-id="pin-builder-draft"]')))
        pinUploaders = self.chr_driver.find_elements(By.XPATH, '//div[@data-test-id="pin-builder-draft"]')
        for count, pinUploader in enumerate(pinUploaders):
            print("count: ",count)
            # WebDriverWait(self.chr_driver,10).until(EC.visibility_of_element_located((By.XPATH,'.//input[@type="file"]')))
            if information['media'][count] != None:
                media = pinUploader.find_element(By.XPATH, './/input[@type="file"]')
                media.send_keys(information['media'][count])
                print("image uploaded")
            else:
                return "Unable to Post, No Media Path is given."
            if information['title']:
                WebDriverWait(self.chr_driver,10).until(EC.visibility_of_element_located((By.XPATH,'.//textarea[contains(@id, "pin-draft-title")]')))
                title = pinUploader.find_element(By.XPATH, './/textarea[contains(@id, "pin-draft-title")]')
                title.send_keys(information['title'])
                print("title added")

            if information['desc'] != None:
                path = "//div[@aria-label='Tell everyone what your Pin is about']"
                WebDriverWait(self.chr_driver,10).until(EC.visibility_of_element_located((By.XPATH,path)))
                desc = pinUploader.find_element(By.XPATH, path)
                desc.send_keys(information['desc'])
                print("description added")

            if information['destination_link'] != None:
                WebDriverWait(self.chr_driver,10).until(EC.visibility_of_element_located((By.XPATH,'.//textarea[contains(@id, "pin-draft-link")]')))
                destination_link = pinUploader.find_element(By.XPATH, './/textarea[contains(@id, "pin-draft-link")]')
                destination_link.send_keys(information['destination_link'])
                print("link added")
            


        if total_pins == 1:
            btn = "//button[@data-test-id='board-dropdown-save-button']"
            WebDriverWait(self.chr_driver,10).until(EC.visibility_of_element_located((By.XPATH,btn)))
            save = self.chr_driver.find_element(By.XPATH, btn)
            time.sleep(2)
            save.click()
            print("single pin saved")
        else:
            select_pins = self.chr_driver.find_elements(By.XPATH, '//button[@aria-label="Select Pin"]')
            for select in select_pins:
                time.sleep(random.uniform(0.2, 0.6))
                select.click()

            time.sleep(random.uniform(0.2, 0.5))
            self.chr_driver.find_element(By.XPATH, '//button[@name="publish"]').click()

        # WebDriverWait(self.chr_driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@aria-label="Saving Pin..."]')))
        # WebDriverWait(self.chr_driver, 10).until(EC.invisibility_of_element_located((By.XPATH, '//*[@aria-label="Saving Pin..."]')))

        return "Success"


    def get_target(self):
        print("Redirecting to Targeted User")
        try:
            link = f"https://www.pinterest.com/{self.target_user}/_created/"
        except:
            return False

        while True:
            try:
                self.chr_driver.get(link)
                break
            except:
                pass

        try:
            WebDriverWait(self.chr_driver, self.wait_time / 2).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@data-test-id="profile-header"]')))
        except:
            print("Cannot Redirect to User")
            return False

        return True

    def get_board(self):
        try:
            self.chr_driver.get(self.target_user)
        except:
            return False
        return True

    def search(self):
        print("Searching")
        self.chr_driver.get(f'https://www.pinterest.com/search/pins/?q={self.target_user}')

        try:
            WebDriverWait(self.chr_driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@role='list']")))
        except:
            print("No Result Found")
            return False

        return True

    def get_followers(self):
        print("Getting Followers")
        try:
            follower = WebDriverWait(self.chr_driver, self.wait_time / 3).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test-id="profile-followers-count"]'))).text
            follower = follower.split(" ")[0]
        except:
            follower = "0"
        
        return follower

    def get_board_follower(self):
        print("Getting Board Followers")
        follower = WebDriverWait(self.chr_driver, self.wait_time // 2).until(
            EC.visibility_of_element_located((By.XPATH, "//body/div[@id='__PWS_ROOT__']/div/div[@role='main']/div/div/div/div[@data-test-id='board-header']/div/div/div[@data-test-id='LegoBoardHeader__main']/div/div/div[@role='button']/div[1]"))).text
        follower = follower.split(" ")[0]
        print("Followers")
        return follower

    def get_following(self):
        print("Getting Following")
        following = WebDriverWait(self.chr_driver, self.wait_time / 3).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test-id="profile-following-count"]'))).text
        following = following.split(" ")[0]
        return following

    def get_bio(self):
        print("Getting Bio")
        try:
            bio = self.chr_driver.find_element(By.XPATH, '//div[@data-test-id="profile-header"]//div[3]//span[3]').text
        except:
            bio = "None"
        return bio

    def get_views(self):
        print("Getting Views")
        try:
            views = WebDriverWait(self.chr_driver, self.wait_time / 3).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@data-test-id="profile-header"]//div[5]'))).text
        except:
            views = "0"
        return views

    def get_images(self, no_of_posts):

        pin_count = 1

        # Testing Links
        list_pins = []

        pins = list()

        pin_tracer = 0
        retry = 0
        scrol = 1
        profiles = 0
        print("TOTAL PIN REQUIRED: " + str(no_of_posts))
        while pin_count <= no_of_posts + 1:
            pin_tracer += 1
      
            if pin_count < 2 or (pin_count > 2 and scrol == 12):
                self.chr_driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
                scrol = 1
            else:
                scrol += 1
            print("scrol: ",scrol)
           
            try:
                # CHECKING IF IT SHOWING SOME PROFILE
                WebDriverWait(self.chr_driver,10).until(EC.visibility_of_element_located((By.XPATH,f'//*[@role="listitem"][{pin_tracer}]//div[@data-test-id="user-follow-button"]')))
                self.chr_driver.find_element (By.XPATH,
                                              f'//*[@role="listitem"][{pin_tracer}]//div[@data-test-id="user-follow-button"]')
                print("This is profile")
                profiles += 1
                if scrol != 12:
                    scrol += 1
                continue
            except:
                pass

            try:
                list_itm = f'//*[@role="listitem"][{pin_tracer}]//div[@data-test-id="pinWrapper"]//a[1]'
                WebDriverWait(self.chr_driver, 20).until(EC.presence_of_all_elements_located(
                    (By.XPATH, list_itm)))
                pin = self.chr_driver.find_elements(By.XPATH, f"(//div[@role='listitem'])[{pin_tracer}]")
                retry = 0
            except TimeoutException as err:
      
                # print("Retry: ",retry)
                # if retry == 2:
                #     break
                # retry += 1
                # pin_tracer -= 1
                pin_count += 1
                continue

                
            if len(pin) == 0:
                print("No Links Found for this Pin")
            for p in pin:
                try:
                    WebDriverWait(self.chr_driver,10).until(EC.visibility_of_element_located((By.XPATH,'.//div[@data-test-id="pinWrapper"]//a[1]')))
                    link = p.find_element(By.XPATH, './/div[@data-test-id="pinWrapper"]//a[1]')
                    pins.append(link.get_attribute('href'))
                   
                except TimeoutException as err:
                    print(f"Unable to get pin [{err}]")
            pin_count += 1
            print("TOTAL PINS GOT: " + str(len(pins)))

            if pin_count > no_of_posts:
                break

            time.sleep(random.uniform(0.5, 1.4))

        for counter, p in enumerate(pins):

            print("GETTING PIN: " + str(counter+1))
            print(p)
            try:
                self.chr_driver.get(p)
            except:
                print(f"Unable to get this pin: {p}")
                continue
                
            try:
                full_data = self.chr_driver.find_element(By.XPATH, "//script[@id='__PWS_DATA__']")
                full_data_dict = (full_data.get_attribute('innerHTML'))
            except TimeoutException as err:
                continue
            
            data = json.loads(full_data_dict)
            
            
           
            id = str(p.split('/')[-2])
           
            data = data['props']['initialReduxState']['pins'][id]
            

            title = None
            desc = None

            if data['closeup_unified_title']:
                try:
                    title = data['closeup_unified_title']
                except:
                    title = None

            if data['closeup_description']:
                try:
                    desc = data['closeup_description']
                except:
                    desc = None

            try:
                date_created = data['created_at']
            except:
                date_created = None
            try:
                pin_saved = data['aggregated_pin_data']['aggregated_stats']['saves']
            except:
                pin_saved = None
            try:
                repin = data['repin_count']
            except:
                repin = None
            try:
                WebDriverWait(self.chr_driver,10).until(EC.visibility_of_element_located((By.XPATH,'//div[@id="canonical-card"]/div[1]')))
                comment = self.chr_driver.find_element(By.XPATH, '//div[@id="canonical-card"]/div[1]').text
                comment = comment.replace(" ", "").replace("comments", "")
            except:
                comment = ""
            

            list_video = []
            list_image = []

            if data['videos']:
                list_video.append(data['videos']['video_list']['V_720P']['url'])
            elif data['story_pin_data']:
                for i in data['story_pin_data']['pages']:
                    try:
                        list_video.append(i['blocks'][0]['video']['video_list']['V_EXP3']['url'])
                    except:
                        list_image.append(i['blocks'][0]['image']['images']['originals']['url'])
            elif data['images']:
                    list_image.append(data['images']['orig']['url'])

            list_pins.append(
                {
                    'title': title,
                    'desc': desc,
                    'comment': comment,
                    'repin': repin,
                    'pin_saved': pin_saved,
                    'date_created': date_created,
                    'image': list_image,
                    'video': list_video
                }
            )
            time.sleep(random.uniform(0.5, 1.4))

        return list_pins

    def get_images_board(self, no_of_posts):

        count = 1
        scroll = round(no_of_posts / 17) + 1
        for _ in range(0, scroll + 1):
            self.chr_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(2)

        # Testing Links
        list_pins = []

        pins = self.chr_driver.find_elements(By.XPATH, "//div[@data-test-id='pinWrapper']//div//a[contains(@href, '/pin/')]")
        pins = [a.get_attribute('href') for a in pins]
        pins = list(set(pins))

        for p in pins:

            if count > no_of_posts:
                break

            print("GETTING PIN: " + str(count))
            count += 1
            self.chr_driver.get(p)
            full_data = self.chr_driver.find_element(By.XPATH, "//script[@id='__PWS_DATA__']")
            full_data_dict = (full_data.get_attribute('innerHTML'))
            data = json.loads(full_data_dict)


            id = p.split('/')[-2]

            data = data['props']['initialReduxState']['pins'][id]

            title = None
            desc = None

            if data['closeup_unified_title']:
                title = data['closeup_unified_title']

            if data['closeup_description']:
                desc = data['closeup_description']

            date_created = data['created_at']
            pin_saved = data['aggregated_pin_data']['aggregated_stats']['saves']
            repin = data['repin_count']

            comment = self.chr_driver.find_element(By.XPATH, '//div[@id="canonical-card"]/div[1]').text
            comment = comment.replace(" ", "").replace("comments", "")

            list_video = []
            list_image = []

            if data['videos']:
                list_video.append(data['videos']['video_list']['V_720P']['url'])
            elif data['story_pin_data']:
                for i in data['story_pin_data']['pages']:
                    list_video.append(i['blocks'][0]['video']['video_list']['V_EXP3']['url'])
            elif data['images']:
                    list_image.append(data['images']['orig']['url'])

            list_pins.append(
                {
                    'title': title,
                    'desc': desc,
                    'comment': comment,
                    'repin': repin,
                    'pin_saved': pin_saved,
                    'date_created': date_created,
                    'image': list_image,
                    'video': list_video
                }
            )

        return list_pins


    """# TODO: Change Images/Videos Name
    def save_image(self):
        def save():
            counter = 0
            # print(images)
            for image in self.images:
                if not image['image']:
                    continue

                save_as = os.path.join(self.path, self.target_user + " " + str(counter) + '.jpg')
                wget.download(image['image'], save_as)

                counter += 1

        print("Checking for Directory")
        if not os.path.exists("Pinterest"):
            os.mkdir("Pinterest")
            os.mkdir(f"Pinterest/{self.target_user}")
            os.mkdir(f"Pinterest/{self.target_user}/{str(datetime.date.today())}")
            save()
        elif not os.path.exists(f"Pinterest/{self.target_user}"):
            os.mkdir(f"Pinterest/{self.target_user}")
            os.mkdir(f"Pinterest/{self.target_user}/{str(datetime.date.today())}")
            save()
        elif not os.path.exists(f"Pinterest/{self.target_user}/{str(datetime.date.today())}"):
            os.mkdir(f"Pinterest/{self.target_user}/{str(datetime.date.today())}")
            save()
        else:
            save()"""
# pin = Pinterest()
# username = "okanything767@gmail.com"
# password = "12345678q@"

# def put():


    

#         pin.set_cred(username, password)

#         if not pin.login():
#             print("Login Failed")

#         # Add For Loop For List of Posts
#         data = {
#             "title": "Azeem Enterprises",
#             "desc": "I am Selenium!",
#             "destination_link": "azeementerprises.org",
#             "media": ["/Users/macbookpro/Desktop/Projects/Web-Scrapping/Social Media Automation/azeem_logo.png","/Users/macbookpro/Desktop/Projects/Web-Scrapping/Social Media Automation/azeem_logo.png"]
#         }
      
#         status = pin.upload_pin(data)
#         print(status)
        
# put()
