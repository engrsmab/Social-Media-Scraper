import datetime
import random
import time

from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from code_req import selenium_path,driver_configurations
import os
import pickle


class Facebook:
    options = driver_configurations()

    images = []

    def set_cred(self, email, password, target_user=None, group_url=None):
        self.username = email
        self.password = password
        self.target_user = target_user
        self.group_url = group_url
        self.COOKIE_PATH = f"Cookies/{email}_FACEBOOK_COOKIE.pkl"

        self.path = os.path.join(f"Facebook/{self.target_user}", str(datetime.date.today()))
        self.driver = webdriver.Chrome(selenium_path, options=self.options)
        self.hover = ActionChains(self.driver)

    def login(self):

        # Getting Instagram
        print('Getting Facebook')
        self.driver.get("http://www.facebook.com/login")

        try:
            print("Looking For Cookies")
            cookies = pickle.load(open(self.COOKIE_PATH, "rb"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        except:

            print("Logging in Manually")
            email = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@name="email"]')))
              
            password = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//input[@name="pass"]')))

            # Filling Username and Password
            print('Filling Username and Password')
            email.clear()
            for i in self.username:
                time.sleep(random.uniform(0.02, 0.1))
                email.send_keys(i)

            password.clear()
            for i in self.password:
                time.sleep(random.uniform(0.02, 0.1))
                password.send_keys(i)

            time.sleep(0.2)

            WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@id="loginbutton"]'))).click()

            time.sleep(3)

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//form[contains(@action, "/logout.php")]')))
                print("Login Successfully")
            except:
                print("Failed to Login")
                return False

            pickle.dump(self.driver.get_cookies(), open(self.COOKIE_PATH, "wb"))
        finally:
            self.driver.refresh()
            time.sleep(2)

        return True

    def get_target(self):
        print("Redirecting to Targeted User")
        self.driver.get(f'https://www.facebook.com/{self.target_user}')
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//div[@role="banner"]/following-sibling::div//span[@dir="auto"]')))
        except:
            print("Cannot Redirect to User")
            return False

        return True

    def get_group(self):
        print("Redirecting to Group")
        self.driver.get(self.group_url)
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "facebook.com/groups/") and @role="link"]')))
        except:
            print("Cannot Redirect to Group")
            return False

        return True

    def get_posts(self, no_of_posts):

        list_post = list()
        post_counter = 1
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        # LOCATING POSTS HERE
        
        time.sleep(random.uniform(0.01, 0.2))
        
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[3]")))
            

        while post_counter <= no_of_posts:
            timeline1 = f"//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[3]/div[{str(post_counter)}]"  
            
            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, timeline1)))
                post = self.driver.find_element(By.XPATH,timeline1)
            except:
                self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
                try:
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, timeline1)))
                    post = self.driver.find_element(By.XPATH,timeline1)
                except:
                    return list_post
            
            print(post)
            text_path = f"//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[3]/div[{str(post_counter)}]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]"

            try:
                print(post.find_element(By.XPATH,text_path).text)
            except:
                pass
            
            # post_link = self.driver.find_element(By.XPATH, f'//div[@aria-posinset={post_counter}]//span/span/a[@role="link"][1]')
            # self.hover.move_to_element(post_link).perform()
            # time.sleep(1)
            # post_link = self.driver.find_element (By.XPATH,f'//div[@aria-posinset={post_counter}]//span/span/a[@role="link"][1]')

            # self.driver.execute_script ("arguments[0].scrollIntoView();", post)
            # time.sleep (2)
            # print('getting Images')
            # try:
            #     img = self.driver.find_elements (By.XPATH, f'//div[@aria-posinset={post_counter}]//div[8]/div/div[3]//a//img')
            #     img = [a.get_attribute ('src') for a in img]
            # except:
            #     img = None

            # print ('getting Video')
            # try:
            #     video = self.driver.find_elements (By.XPATH,
            #                                        f'//div[@aria-posinset={post_counter}]//div[8]/div/div[3]//video[@playsinline]')
            #     video = [a.get_attribute ('src') for a in video]
            # except:
            #     video = None

            # if (not img) and (not video):
            #     print("NO MEDIA FOUND SKIPPING")
            #     continue

            # try:
            #     print ('getting Likes')
            #     likes = self.driver.find_element (By.XPATH,
            #                                       f'//div[@aria-posinset={post_counter}]//span[@role="toolbar"]/parent::div/parent::div/div[1]/div//div//span').text

            #     likes = likes.split ('\n')[0]
            #     print ("LIKES: " + likes)
            # except:
            #     likes = None

            # try:
            #     print ('getting Comments')
            #     comment = self.driver.find_element (By.XPATH,
            #                                         f'//div[@aria-posinset={post_counter}]//span[@role="toolbar"]/parent::div/parent::div/div[2]/div[2]//div//span').text
            #     comment = comment.split (" ")[0]
            # except:
            #     comment = None

            # try:
            #     print ('getting Share')
            #     share = self.driver.find_element (By.XPATH,
            #                                       f'//div[@aria-posinset={post_counter}]//span[@role="toolbar"]/parent::div/parent::div/div[2]/div[3]').text
            #     share = share.split (" ")[0]
            # except:
            #     share = None

            post_counter += 1
            # list_post.append (
            #     {
            #         'post_url': post_link.get_attribute('href').split("?")[0],
            #         'img': img,
            #         'like': likes,
            #         'share': share,
            #         'coment': comment,
            #         'video': video
            #     }
            # )

        return post
    def publish_post(self,data,page):
        if page == None:
            try: 
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='Menu']//*[name()='svg']//*[name()='circle']")))
                create_btn = self.driver.find_element(By.XPATH,"//div[@aria-label='Menu']//*[name()='svg']//*[name()='circle']")
            except:
                try:
                    WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='q8kr2fb9']//span[@class='f7rl1if4 adechonz f6oz4yja dahkl6ri axrg9lpx rufpak1n qtovjlwq qbmienfq rfyhaz4c rdmi1yqr ohrdq8us nswx41af fawcizw8 l1aqi3e3 sdu1flz4']")))
                    create_btn = self.driver.find_element(By.XPATH, "//div[@class='q8kr2fb9']//span[@class='f7rl1if4 adechonz f6oz4yja dahkl6ri axrg9lpx rufpak1n qtovjlwq qbmienfq rfyhaz4c rdmi1yqr ohrdq8us nswx41af fawcizw8 l1aqi3e3 sdu1flz4']")
                except:
                    return "Time Out Due to Slow Internet"
            create_btn.click()
            time.sleep(1)
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Post']")))
                post_btn = self.driver.find_element(By.XPATH,"//span[normalize-space()='Post']")
                post_btn.click()
            except:
                return "Unable To locate Post Button"

            
            write_path = "//p[@class='cr00lzj9 kmwttqpk kjdc1dyq l7ghb35v m8h3af8h']"
        else:
            write_path = f"//div[@aria-label='Write something to {page}...']"
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Public']")))
            self.driver.find_element(By.XPATH,"//span[normalize-space()='Public']").click()
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='Done']")))
            self.driver.find_element(By.XPATH,"//div[@aria-label='Done']").click()
            print("Done Pressed")
        except:
            pass
        WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,write_path)))
        write_post = self.driver.find_element(By.XPATH,write_path)
        write_post.clear()

        for i in range(len(data["desc"])):
            time.sleep(random.uniform(0.02, 0.1))
            write_post.send_keys(data["desc"][i])
        time.sleep(0.5)

        if data["image"] != None:
            file_xpath = "div[class='bdao358l om3e55n1 g4tp4svg alzwoclg cqf1kptm jez8cy9q gvxzyvdx b0eko5f3 fwlpnqze i0rxk2l3 laatuukc gjezrb0y abh4ulrg'] input[type='file']"
            for img_path in data['image']:
                try:
                    # (//div[@role='button'])[57]
                    WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,file_xpath)))
                    img = self.driver.find_element(By.CSS_SELECTOR,file_xpath)
                    print("uploading image")
                except:
                    print("click on image icon")
                    img_icon = self.driver.find_element(By.XPATH,"//div[@aria-label='Photo/Video']//div//div//i[@class='gneimcpu p9wrh9lq']")
                    img_icon.click()
                    WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "(//div[@role='button'])[56]")))
                    print("uploading image")
                    img = self.driver.find_element(By.CSS_SELECTOR,file_xpath)
                img.send_keys(img_path)
                time.sleep(2)
                print("Image Uploaded")
        
        if data["feeling"] != None:
            feeling_list = ["happy","sad","angry","loved","thankful","blessed","lovely","excited","in love","crazy","grateful","blissful","fantastic","silly","festive","wonderful","cool","amused","relaxed","positive","chill","hopeful","joyful","tired","motivated","proud","alone","thoughtful","ok","nostalgic","sick","delighted","drained","emotional","confident","awesome","fresh","determined","exhausted","annoyed","glad","lucky","heartbroken","bored","sleepy","energyzed","hungry","professional","pained","peaceful","disappointed","optimistic","cold","cute","fabulous","great","sorry","super","worried","funny","bad","down","inspired","satisfied","pumped","calm","confused","goofy",'missing',"good","sarcastic","lonely","strong","concerned","special","depressed","jolly","curious","low","welcome"]
            if str(data["feeling"]).lower() not in feeling_list:
                return "incorrect feeling value"
            if page != None:
                more_ico = "//div[@aria-label='More']//div//div//div[@class='i85zmo3j alzwoclg jcxyg2ei om3e55n1 pytsy3co mfclru0v']"
                self.driver.find_element(By.XPATH,more_ico).click()
                WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf tb6i94ri gupuyl1y i2onq4tn b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas f5mw3jnl hxfwr5lz hpj0pwwo sggt6rq5 innypi6y pbevjfx6 ztn2w49o'][normalize-space()='Feeling/activity']")))
                self.driver.find_element(By.XPATH,"//span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf tb6i94ri gupuyl1y i2onq4tn b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas f5mw3jnl hxfwr5lz hpj0pwwo sggt6rq5 innypi6y pbevjfx6 ztn2w49o'][normalize-space()='Feeling/activity']").click()
            else:
                feeling_ico = self.driver.find_element(By.XPATH,"//div[@aria-label='Feeling/activity']//div//div//i[@class='gneimcpu p9wrh9lq']")
                feeling_ico.click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
            feeling_search = self.driver.find_element(By.XPATH,"//input[@placeholder='Search']")
            feeling_search.clear()
            for i in range(len(data["feeling"])):
                time.sleep(random.uniform(0.02, 0.1))
                feeling_search.send_keys(data["feeling"][i])
            if data["feeling"] != "sad":
                path = "//div[@class='i85zmo3j h8391g91 m0cukt09 kpwa50dg ta68dy8c fsf7x5fv alzwoclg q46jt4gp b0eko5f3 r5g9zsuq fwlpnqze dtlcmhqt']"
              
            else:
                path = "//div[@class='i85zmo3j h8391g91 m0cukt09 kpwa50dg ta68dy8c fsf7x5fv alzwoclg q46jt4gp b0eko5f3 r5g9zsuq fwlpnqze dtlcmhqt ednat9xy']"
            
            WebDriverWait(self.driver,10).until(
                    EC.visibility_of_element_located((By.XPATH,path)))
            self.driver.find_element(By.XPATH,path).click()
        if page == None:
            if data["tag"] != None:
                WebDriverWait(self.driver,10).until(
                        EC.visibility_of_element_located((By.XPATH,"//div[@aria-label='Tag people']//div//div//i[@class='gneimcpu p9wrh9lq']")))
                self.driver.find_element(By.XPATH,"//div[@aria-label='Tag people']//div//div//i[@class='gneimcpu p9wrh9lq']").click()
                WebDriverWait(self.driver,10).until(
                        EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Search for friends']")))
                search_people = self.driver.find_element(By.XPATH,"//input[@placeholder='Search for friends']")
                for tags in data["tag"]:
                    search_people.clear()
                    for i in range(len(tags)):
                        time.sleep(random.uniform(0.02, 0.1))
                        search_people.send_keys(tags[i])
                    try:
                        # //span[normalize-space()='{tags}']
                        path = "//ul[@role='listbox']"
                        WebDriverWait(self.driver,10).until(
                            EC.visibility_of_any_elements_located((By.XPATH,path))
                        )
                        self.driver.find_element(By.XPATH,path).click()
                    except:
                        pass
                time.sleep(0.5)
                self.driver.find_element(By.XPATH,"//span[contains(text(),'Done')]").click()
        post_xpath = "//div[@aria-label='Post']//div[@class='om3e55n1 g4tp4svg alzwoclg jez8cy9q jcxyg2ei i85zmo3j sr926ui1 jl2a5g8c k7n6ui8p b41d885q hmqrhxox got7tec9 frfouenu bonavkto djs4p424 r7bn319e bdao358l aesu6q9g e4ay1f3w n75z76so ed17d2qt']"
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,post_xpath)))
        self.driver.find_element(By.XPATH,post_xpath).click()
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(By.XPATH,"//span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf tb6i94ri gupuyl1y i2onq4tn k1z55t6l oog5qr5w tes86rjd elsxfac6']"))
            self.driver.find_element(By.XPATH,"//div[@class='facqkgn9 s8sjc6am h28iztb5']//div[@aria-label='Close']").click()
            return "post exists"
        except:
            return "posted successfully"
    
    def page_post(self,data,page=None):
        if page == None:
            page = f"groups/{data['group']}"
            title = "group"
        else:
            page = data["page"]
            title = "page"
        try:
            self.driver.get(f"https://www.facebook.com/profile.php?id={page}")
        except:
            return f"{title} not found"

        try:
            WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.XPATH,"//span[contains(text(),'Photo/video')]")))
            self.driver.find_element(By.XPATH,"//span[contains(text(),'Photo/video')]").click()
        except:
            return f"Unable to Past Button"
        
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"(//span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf tb6i94ri gupuyl1y i2onq4tn b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas f5mw3jnl hxfwr5lz k1z55t6l oog5qr5w innypi6y pbevjfx6'][normalize-space()='Automation-dummy'])[1]")))
            pg_nm = self.driver.find_element(By.XPATH,"(//span[@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf tb6i94ri gupuyl1y i2onq4tn b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas f5mw3jnl hxfwr5lz k1z55t6l oog5qr5w innypi6y pbevjfx6'][normalize-space()='Automation-dummy'])[1]").text
        except:
            pg_nm = "None"
        return self.post(data,pg_nm)


    def post(self,data,page=None):
        message = []
        for no in range(len(data["desc"])):
            if page == None:
                post_data = {
                      "desc":data["desc"][no],
                      "image":data["image"][no],
                      "feeling":data["feeling"][no],
                      "tag":data["tag"][no]}
            else:
                post_data = {
                      "desc":data["desc"][no],
                      "image":data["image"][no],
                      "feeling":data["feeling"][no]}
            resp = self.publish_post(post_data,page)
            message.append(
                {
                    'n': no+1,
                    'message': resp
                }
            )
            time.sleep(random.uniform(0.5,1.5))
  
        return message

     








import random
user = "03248546559"
password = "thisisid123"
# fb = Facebook()
# def put():
#         num = random.randint(1,1000)
#         data = {"email":user,
#         "password":password,
#         "desc":[f"Random Number {str(num)}",f"Random Number {str(num)}"],
#         "image":["/Users/macbookpro/Desktop/Projects/Web-Scrapping/Social Media Automation/azeem_logo.png",None],
#         "feeling":["happy","sad"],
#         "tag":[["syed mubashir azeem bukhari"],["maavia khalid"]]
#         }

#         fb.set_cred(data['email'], data['password'])

#         if not fb.login():
#             print("not logged in")
#         if not fb.post(data):
#             print("post faild")
#         print("done")
# put()
# group = "264777498549905"

# def post_group():
#     num = random.randint(1,1000)
#     data = {"email":user,
#     "password":password,
#     "desc":[f"I'm a robot. Test {str(num)}"],
#     "image":[["/Users/macbookpro/Desktop/Projects/Web-Scrapping/Social Media Automation/azeem_logo.png"]],
#     "feeling":["happy"],
#     "group":[group]}

#     fb.set_cred(data['email'], data['password'])

#     if not fb.login():
#         print("not logged in")

    
#     status = fb.page_post(data)

#     return status
# print(post_group())

# def fetch_user():
#     fb.set_cred(user, password, "mubashir.azeem.142")
#     if not fb.login():
#         print("Login Failed")

#     if not fb.get_target():
#         print("Failed to get target user")


#     response = {
#         'username': "mubashir.azeem.142",
#         'posts': fb.get_posts(9)
#     }

#     return response
# print(fetch_user())

 
