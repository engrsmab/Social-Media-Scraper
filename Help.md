# Apis for Fetching the Data
Here are the data that you will send while requesting each API
### Note ###
```
The Server only accept PUT requests so make sure to send send PUT requests only
127.0.0.1 is the Local host and can be changed 
```
### For Instagram ###
```
To Get User Posts
http://127.0.0.1:5000/instagram/fetch/user

To Get Hashtag Posts
http://127.0.0.1:5000/instagram/fetch/hashtag

Also send the Dictinoary with the request with the following keys 
and there relative data

insta = {
    'email' = <youemail@email.com>,
    'password' = youpassword_123,
    'target_user' = <username_of_user>, # IF GETTING USER POSTS
    'hashtag' = <Hashtag>, # IF GETTING HASHTAG POSTS
    'no_of_posts' = <Number_of_Posts_required>
}
```
### For Reddit ###
```
To Get User Posts
http://127.0.0.1:5000/reddit/fetch/user

To Get Search Posts
http://127.0.0.1:5000/reddit/fetch/search

To Get SubReddit Posts
http://127.0.0.1:5000/reddit/fetch/subreddit

Also send the Dictinoary with the request with the following keys 
and there relative data

red = {
    'email' = <youemail@email.com>,
    'password' = youpassword_123,
    'target_user' = <username_of_user>, # IF GETTING USER POSTS
    'search' = <search>, # IF GETTING SEARCH POSTS
    'subreddit' = <Page_name>, # IF GETTING SUBREDDIT POSTS
    'no_of_posts' = <Number_of_posts_required>
}
```
### For Pinterest ###
```
To Get User Posts
http://127.0.0.1:5000/pinterest/fetch/user

To Get Search Posts
http://127.0.0.1:5000/pinterest/fetch/search

To Get Board Posts
http://127.0.0.1:5000/pinterest/fetch/board

Also send the Dictinoary with the request with the following keys 
and there relative data

pin = {
    'email' = <youemail@email.com>,
    'password' = youpassword_123,
    'target_user' = <username_of_user>, # IF GETTING USER POSTS
    'search' = <search>, # IF GETTING SEARCH POSTS
    'board' = <board_link>, # IF GETTING BOARD POSTS
    'no_of_posts' = <Number_of_Posts_required>
}
```
### For Twitter ###
```
To Get User Posts
http://127.0.0.1:5000/twitter/fetch/user

To Get Search Posts
http://127.0.0.1:5000/twitter/fetch/search

Also send the Dictinoary with the request with the following keys 
and there relative data

twi = {
    'email' = <youemail@email.com>,
    'password' = youpassword_123,
    'target_user' = <username_of_user>, # IF GETTING USER POSTS
    'search' = <search>, # IF GETTING SEARCH POSTS
    'no_of_posts' = <Number_of_Posts_required>
}
```
### For Facebook ###
```
To Get User Posts
http://127.0.0.1:5000/facebook/fetch/user

To Get Search Posts
http://127.0.0.1:5000/facebook/fetch/group

Also send the Dictinoary with the request with the following keys 
and there relative data

fb = {
    'email' = <youemail@email.com>,
    'password' = youpassword_123,
    'target_user' = <username_of_user>, # IF GETTING USER POSTS OR PAGE POSTS
    'group_url' = <group_url>, # IF GETTING GROUP POSTS
    'no_of_posts' = <Number_of_Posts_Required>
}
```

# Apis for Posting the Post
Here are the data that you will send while requesting each API, Make sure to send the data as required by the API

### How the Json should be ###
```
{
    'desc': <Description/Caption> data_type: String,
    'media': <paths for images and videos> data_type: List/Array
}
```

### For Twitter ###
```
To post data on Feed
http://127.0.0.1:5000/twitter/post/user

Also send the Dictinoary with the request with the following keys 
and there relative data

twi = {
    'email' = <youemail@email.com>,
    'password' = youpassword_123,
    'post_data' = <details_of_post> # MUST BE JSON
}
```