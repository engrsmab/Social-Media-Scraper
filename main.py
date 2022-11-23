
import os.path

from flask import Flask, request
from flask_restful import Resource, Api
from reddit import Reddit
from pinterest import Pinterest
from instagram import Instagram
from twitter import Twitter
from facebook import Facebook
import json

app = Flask(__name__)
api = Api(app)

red = Reddit()


class RedditUserAPI(Resource):

    def put(self):
        data = {
            'email': request.json['email'],
            'password': request.json['password'],
            'target_user': request.json['target_user'],
            'no_of_posts': int(request.json['no_of_posts'])
        }

        red.set_cred(data['email'], data['password'], data['target_user'])

        resp =  red.login()
        if resp != "Login Successfuly":
            message = {'message': resp}
            return json.dumps(message, indent=4)

        resp = red.get_target()
        if resp != "Done":
            message = {'message': resp}
            return json.dumps(message, indent=4)

        response = {
            'username': data['target_user'],
            'posts': red.get_images_and_related_data(data['no_of_posts'])
        }

        return json.dumps(response, indent=4), 200


class RedditSubAPI(Resource):

    def put(self):
        data = {
            'email': request.json['email'],
            'password': request.json['password'],
            'target_user': request.json['subreddit'],
            'no_of_posts': int(request.json['no_of_posts'])
        }

        red.set_cred(data['email'], data['password'], data['target_user'])

        resp =  red.login()
        if resp != "Login Successfuly":
            message = {'message': resp}
            return json.dumps(message, indent=4)

        if not red.get_subreddit():
            message = {'message': 'Failed to Get Targeted User'}
            return json.dumps(message, indent=4)

        response = {
            'username': data['target_user'],
            'posts': red.get_images_and_related_data(data['no_of_posts'])
        }

        return json.dumps(response, indent=4), 200


class RedditSearchAPI(Resource):

    def put(self):
        data = {
            'email': request.json['email'],
            'password': request.json['password'],
            'target_user': request.json['search'],
            'no_of_posts': int(request.json['no_of_posts'])
        }

        red.set_cred(data['email'], data['password'], data['target_user'])

        resp =  red.login()
        if resp != "Login Successfuly":
            message = {'message': resp}
            return json.dumps(message, indent=4)

        if not red.search():
            message = {'message': 'Failed to Get Targeted User'}
            return json.dumps(message, indent=4)

        response = {
            'username': data['target_user'],
            'posts': red.get_images_and_related_data(data['no_of_posts'])
        }

        return json.dumps(response, indent=4), 200


class RedditPostHomeFeedAPI(Resource):

    def put(self):
        form = request.json
        username = form['email']
        password = form['password']

       

        red.set_cred(username, password)

        resp = red.login()
        if resp != "Login Successfuly":
            message = {'message': resp}
            return json.dumps(message, indent=4)

        # Add For Loop For List of Posts
        message = list ()
  
        for i in range(len(form['title'])):
            post = {
                "title": form['title'][i],
                "desc": form['desc'][i],
                "community": form['community'][i],
                "media":form['media'][i],
                "link":form['link'][i]
                            }
            status = red.upload_on_home_feed(post)
            message.append (
                {
                    'no': i + 1,
                    'status': status
                }
            )

        return json.dumps(message, indent=4), 200

# REDDIT FETCHING APIS
api.add_resource(RedditUserAPI, '/reddit/fetch/user')
api.add_resource(RedditSearchAPI, '/reddit/fetch/search')
api.add_resource(RedditSubAPI, '/reddit/fetch/subreddit')
api.add_resource(RedditPostHomeFeedAPI, '/reddit/post/feed')

insta = Instagram()


class InstagramUserAPI(Resource):

    def put(self):
        data = {
            'email': request.json['email'],
            'password': request.json['password'],
            'target_user': request.json['target_user'],
            'no_of_posts': int(request.json['no_of_posts'])
        }

        insta.set_cred(data['email'], data['password'], data['target_user'])

        resp = insta.login()
        if resp != "Success":
            message = {'message': resp}
            return json.dumps(message, indent=4)

        if not insta.get_target():
            message = {'message': 'Failed to Get Targeted User'}
            return json.dumps(message, indent=4)

        response = {
            'username': data['target_user'],
            'bio': insta.get_bio(),
            'follower': insta.get_follower(),
            'following': insta.get_following(),
            'posts': insta.get_posts(data['no_of_posts'])
        }

        return json.dumps(response, indent=4), 200


class InstagramHashTagAPI(Resource):

    def put(self):
        data = {
            'email': request.json['email'],
            'password': request.json['password'],
            'hashtag': request.json['hashtag'],
            'no_of_posts': int(request.json['no_of_posts'])
        }

        insta.set_cred(data['email'], data['password'], data['hashtag'])

        resp = insta.login()
        if resp != "Success":
            message = {'message': resp}
            return json.dumps(message, indent=4)

        if not insta.get_hashtag():
            message = {'message': 'Failed to Get HashTag'}
            return json.dumps(message, indent=4)

        response = {
            'username': data['hashtag'],
            'posts': insta.get_posts(data['no_of_posts'])
        }

        return json.dumps(response, indent=4), 200


class InstagramFeedPostAPI(Resource):

    def put(self):
        form = request.json
        username = form['email']
        password = form['password']

       

        insta.set_cred(username, password)

        resp = insta.login()
        if resp != "Success":
            message = {'message': resp}
            return json.dumps(message, indent=4)

        # Add For Loop For List of Posts
        message = list ()
  
        for i in range(len(form['title'])):
            post = {
                "title": form['title'][i],
                "desc": form['desc'][i],

                "media":form['media'][i],

                            }
            status = insta.upload_feed(post)
            message.append(
                {
                    'no': i+1,
                    'status': status
                }
            )

        return json.dumps(message, indent=4), 200


# INSTAGRAM POSTING API
api.add_resource(InstagramUserAPI, '/instagram/fetch/user')
api.add_resource(InstagramHashTagAPI, '/instagram/fetch/hashtag')

# INSTAGRAM POSTING API
api.add_resource(InstagramFeedPostAPI, '/instagram/post/feed')

pin = Pinterest()


class PinterestUserAPI(Resource):
    def put(self):

        data = {
            'email': request.json['email'],
            'password': request.json['password'],
            'target_user': request.json['target_user'],
            'no_of_posts': int(request.json['no_of_posts'])
        }

        pin.set_cred(data['email'], data['password'], data['target_user'])

        resp = pin.login()
        if resp != "Success":
            message = {'message': resp}
            return json.dumps(message, indent=4)

        if not pin.get_target():
            message = {'message': 'Failed to Get Targeted User'}
            return json.dumps(message, indent=4)

        response = {
            'username': data['target_user'],
            'follower': pin.get_followers(),
            'following': pin.get_following(),
            'bio': pin.get_bio(),
            'views': pin.get_views(),
            'posts': pin.get_images(data['no_of_posts'])
        }

        return json.dumps(response, indent=4), 200


class PinterestSearchAPI(Resource):
    def put(self):
        data = {
            'email': request.json['email'],
            'password': request.json['password'],
            'target_user': request.json['search'],
            'no_of_posts': int(request.json['no_of_posts'])
        }

        pin.set_cred(data['email'], data['password'], data['target_user'])

        resp = pin.login()
        if resp != "Success":
            message = {'message': resp}
            return json.dumps(message, indent=4)

        # pin.get_full_data()

        if not pin.search():
            message = {'message': 'No Result Found'}
            return json.dumps(message, indent=4)

        response = {
            'username': data['target_user'],
            'posts': pin.get_images(data['no_of_posts'])
        }

        return json.dumps(response, indent=4), 200


class PinterestBoardAPI(Resource):
    def put(self):
        data = {
            'email': request.json['email'],
            'password': request.json['password'],
            'target_user': request.json['board'],
            'no_of_posts': int(request.json['no_of_posts'])
        }

        pin.set_cred(data['email'], data['password'], data['target_user'])

        resp = pin.login()
        if resp != "Success":
            message = {'message': resp}
            return json.dumps(message, indent=4)

        if not pin.get_board():
            message = {'message': 'No Result Found or Invalid Board Link'}
            return json.dumps(message, indent=4)

        response = {
            'username': data['target_user'],
            'follower': pin.get_board_follower(),
            'posts': pin.get_images_board(data['no_of_posts'])
        }

        return json.dumps(response, indent=4), 200


class PinterestPostAPI(Resource):

    def put(self):
        form = request.json
        username = form['email']
        password = form['password']

       

        pin.set_cred(username, password)

        resp = pin.login()
        if resp != "Success":
            message = {'message': resp}
            return json.dumps(message, indent=4)

        # Add For Loop For List of Posts
        message = list ()
  
        for i in range(len(form['title'])):
            post = {
                "title": form['title'][i],
                "desc": form['desc'][i],
                "destination_link":form['destination_link'][i],
                "media":form['media'][i],

                            }
            status = pin.upload_pin(post)
            message.append(
                {
                    'no': i+1,
                    'status': status
                }
            )

        return json.dumps(message, indent=4), 200

api.add_resource(PinterestUserAPI, '/pinterest/fetch/user')
api.add_resource(PinterestSearchAPI, '/pinterest/fetch/search')
api.add_resource(PinterestBoardAPI, '/pinterest/fetch/board')

api.add_resource(PinterestPostAPI, '/pinterest/post/pin')

twi = Twitter()


class TwitterUserAPI(Resource):
    def put(self):
        data = {
            'email': request.json['email'],
            'password': request.json['password'],
            'username': request.json['username'],
            'target_user': request.json['target_user'],
            'no_of_posts': int(request.json['no_of_posts'])
        }

        twi.set_cred(data['email'], data['password'],data['username'], data['target_user'])


        resp =  twi.login()
        if resp != "Login Successfuly":
            message = {'message': resp}
            return json.dumps(message, indent=4)


        resp = twi.get_target()
        if resp != "Done":
            message = {'message': resp}
            return json.dumps(message, indent=4)

        response = {
            'username': data['target_user'],
            'name': twi.get_name(),
            'bio': twi.get_bio(),
            'follower': twi.get_follower(),
            'following': twi.get_following(),
            'location': twi.get_location(),
            'join_date': twi.get_join_date(),
            'tweet': twi.get_images(data['no_of_posts'])
        }

        return json.dumps(response, indent=4), 200


class TwitterSearchAPI(Resource):
    def put(self):
        data = {
            'email': request.json['email'],
            'username':request.json['username'],
            'password': request.json['password'],
            'target_user': request.json['search'],
            'no_of_posts': int(request.json['no_of_posts'])
        }

        twi.set_cred(data['email'], data['password'], data['username'],data['target_user'])


        resp =  twi.login()
        if resp != "Login Successfuly":
            message = {'message': resp}
            return json.dumps(message, indent=4)


        if not twi.search():
            message = {'message': 'Failed to Search Results'}
            return json.dumps(message, indent=4)

        response = {
            'username': data['target_user'],
            'result': twi.get_images(data['no_of_posts'])
        }

        return json.dumps(response, indent=4), 200


class TwitterPostApi(Resource):
    def put(self):
        data = request.json
        twi.set_cred(data['email'], data['password'],data['username'])

        resp =  twi.login()
        if resp != "Login Successfuly":
            message = {'message': resp}
            return json.dumps(message, indent=4)
      
        message = []
        for i in range(len(data['title'])):
            post = {
            "title":data['title'][i],
            "desc": data['desc'][i],
            "media":data['media'][i],
            }
            status = twi.upload (post)
            message.append (
                    {
                        'no': i + 1,
                        'status': status
                    })
            
        return json.dumps({"message":message},indent=4)

"""
TWITTER FETCHING API
"""
api.add_resource(TwitterUserAPI, '/twitter/fetch/user')
api.add_resource(TwitterSearchAPI, '/twitter/fetch/search')

"""
TWITTER UPLOADING API
"""
api.add_resource(TwitterPostApi, '/twitter/post/feed')

fb = Facebook()


class FacebookUserAPI(Resource):

    def put(self):
        data = {
            'email': request.json['email'],
            'password': request.json['password'],
            'target_user': request.json['target_user'],
            'no_of_posts': int(request.json['no_of_posts'])
        }

        fb.set_cred(data['email'], data['password'], target_user=data['target_user'])

        resp =  fb.login()
        if resp != "Success":
            message = {'message': str(resp)}
            return json.dumps(message, indent=4)

        if not fb.get_target():
            message = {'message': 'Failed to Get Targeted User'}
            return json.dumps(message, indent=4)


        response = {
            'username': data['target_user'],
            'posts': fb.get_posts(data['no_of_posts'])
        }

        return json.dumps(response, indent=4), 200


class FacebookGroupAPI(Resource):

    def put(self):
        data = {
            'email': request.json['email'],
            'password': request.json['password'],
            'group_url': request.json['group_url'],
            'no_of_posts': int(request.json['no_of_posts'])
        }

        fb.set_cred(data['email'], data['password'], group_url=data['group_url'])

        resp =  fb.login()
        if resp != "Success":
            message = {'message': str(resp)}
            return json.dumps(message, indent=4)

        if not fb.get_group():
            message = {'message': 'Failed to Get Targeted User'}
            return json.dumps(message, indent=4)


        response = {
            'username': data['group_url'],
            'posts': fb.get_posts(data['no_of_posts'])
        }

        return json.dumps(response, indent=4), 200

class FacebookPublishPostAPI(Resource):
    def put(self):
        print("Hi Data")
        form = request.json
        data = {
            'email': form['email'],
            'password': form['password'],
            'desc': form['desc'],
            'image': form['image'],
            "feeling":form['feeling'],
            "tag":form['tag']
        }
        print("data validated")
        fb.set_cred(data['email'], data['password'])

        resp =  fb.login()
        if resp != "Success":
            message = {'message': str(resp)}
            return json.dumps(message, indent=4)
        message = fb.post(data)
        message = {'message':message}
            
        return json.dumps(message,indent=4)
       

class FacebookPublishPagePostAPI(Resource):
    def put(self):
        form = request.json
        data = {
            'email': form['email'],
            'password': form['password'],
            'desc': form['desc'],
            'image': form['image'],
            "feeling":form['feeling'],
        }

        fb.set_cred(data['email'], data['password'])

        resp =  fb.login()
        if resp != "Success":
            message = {'message': str(resp)}
            return json.dumps(message, indent=4)
        message = fb.page_post(data,page = True)
 
           
        return json.dumps(message,indent=4)

api.add_resource(FacebookUserAPI, '/facebook/fetch/user')
api.add_resource(FacebookGroupAPI, '/facebook/fetch/group')
api.add_resource(FacebookPublishPostAPI,'/facebook/publish/user')
api.add_resource(FacebookPublishPagePostAPI,'/facebook/publish/page')

if __name__ == "__main__":
    print("API IS NOW RUNNING")
    # MAKING COOKIES DIRECTORY
    if not os.path.exists('Cookies'):
        os.mkdir("Cookies")

    app.run(host='0.0.0.0', port=5000)
