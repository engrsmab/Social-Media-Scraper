
import requests



xs1 = "34%3Amjq9JsPsHaJXXg%3A2%3A1668509359%3A-1%3A6008%3A%3AAcU1EjD90WHwa8X7qtMUZmnYIN2bE_5Wwq-DeceX2w"
xs2 = ""
fr1 = "026kjfE6e9u9MLbBp.AWW9mnXTJgq9h-F87VsELhm94Es.BjdGU-.og.AAA.0.0.BjdGXo.AWVjnNNaE34"
fr2 = ""
usida1 = "eyJ2ZXIiOjEsImlkIjoiQXJsZjk2MDEyMnM0Z28iLCJ0aW1lIjoxNjY4NTcyNjc4fQ%3D%3D"
usida2 = ""
usid1 = "6-Trlfax23almmr:Prlfax2145jvy5:0-Arlf960122s4go-RV=6:F="

cookies = {
    'sb': 'Lo2JYQUrqCvh2jCUcDg6Xja7',
    'datr': 'Lo2JYXbyV5qZVyDZncpXiZtr',
    'dpr': '2',
    'locale': 'en_US',
    'm_pixel_ratio': '2',
    'c_user': '100005768826578',
    'm_page_voice': '100005768826578',
    'x-referer': 'eyJyIjoiL3Byb2ZpbGUucGhwP2lkPTEwMDA4NzM3MjgwNzYyNiIsImgiOiIvcHJvZmlsZS5waHA%2FaWQ9MTAwMDg3MzcyODA3NjI2IiwicyI6Im0ifQ%3D%3D',
    'xs': '34%3Amjq9JsPsHaJXXg%3A2%3A1668509359%3A-1%3A6008%3A%3AAcU1EjD90WHwa8X7qtMUZmnYIN2bE_5Wwq-DeceX2w',
    'fr': '026kjfE6e9u9MLbBp.AWW9mnXTJgq9h-F87VsELhm94Es.BjdGU-.og.AAA.0.0.BjdGXo.AWVjnNNaE34',
    'i_user': '100087372807626',
    'usida': 'eyJ2ZXIiOjEsImlkIjoiQXJsZjk2MDEyMnM0Z28iLCJ0aW1lIjoxNjY4NTcyNjc4fQ%3D%3D',
    'wd': '609x602',
}



data = {
    'av': '100087372807626',
    '__usid': '6-Trlfax23almmr:Prlfax2145jvy5:0-Arlf960122s4go-RV=6:F=',
    '__user': '100087372807626',
    '__a': '1',
    '__dyn': '7AzHxqU5a5Q1ryaxG4VuC0BVU98nwgU765QdwSwAyUco5S3O2Saxa1NwJwpUe8hw6vwb-q7oc81xoswIK1Rwwwg8a8465o-cwfG12wOKdwGxu782lwv89kbxS2218wc61axe3S1lwlE-UqwsUkxe2GewyDwkUtxGm2SUbElxm3y1lUlDw-wAw8im7-8wywdqUuBwJCwLyES0Io88cA0z8c84qifxe3u362-2B0oobo8o',
    '__csr': 'ghMR92cI44aqliYAN5lAKlqkx1q9lWWbEgRj9iFSKh4nayiWuV4jaO4qmQnHIGLi_HqHmmBGeXmF4y39VHLhHBBBKSWpQ9AjyqyoSmWVGAlczmVqh_yerxIwKJ13G5t4DjGaGu8VUyVaK9QrGmVbh68VkXVoCmh0TzEW9KqifVpuFFEB4yoiAypQUF5AQ8yolDz4immfFzUmypfzk4Q4998Ly9rwgrz9Zeq8z9oWUhUWdgO5opwYwzxui32u2W7oqBKmdglwjFK79UGUtBBG1aBxx0zzpo5q5pEpwxxWUC6Ua8mzElxS3W1Gig4J2U6C4EfUO1ewxw2Y83jg1ko0a2U09a81F82hw0nQo0vsw1D20f2K0bazk0ZE1SU3Nw2Morw51DzUhG8o1hU0jdwaz803Xaewww17St8C0_oWew0JowmVT8rrhEhDkw0SK1twoU0F0Epwby0tO1ow55wpES1Uw862G0yaw8y0QE',
    '__req': 'z',
    '__hs': '19312.HYP:comet_pkg.2.1.0.2.1',
    'dpr': '2',
    '__ccg': 'EXCELLENT',
    '__rev': '1006613421',
    '__s': 'uclb1w:vf44aj:eqqdld',
    '__hsi': '7166465085064830900',
    '__comet_req': '15',
    'fb_dtsg': 'NAcNjDKmOVxpvj5t_43nwfmUVlYIleLIb19v2Dm-sZi-nM0E18UBJAw:34:1668509359',
    'jazoest': '25423',
    'lsd': 'pb--535QkueK2uwzAP-061',
    '__aaid': '220911458111147',
    '__spin_r': '1006613421',
    '__spin_b': 'trunk',
    '__spin_t': '1668572678',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'CometComposerInterceptionPluginUtilsQuery',
    'variables': '{"target_type":"PROFILE_PLUS","target_id":"104386299162215","params":{"logging_data":{"entry_point":"PROFILE_PLUS_FEED","session_id":"4e4c453e-dc56-45d1-940b-6d5995bd3032"},"photo_ids":[],"placement":"COMPOSER_POST_BUTTON","post_text":"Again-Testing"}}',
    'server_timestamps': 'true',
    'doc_id': '5970639646279568',
}

# response = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)


cookies = {
    'sb': 'Lo2JYQUrqCvh2jCUcDg6Xja7',
    'datr': 'Lo2JYXbyV5qZVyDZncpXiZtr',
    'dpr': '2',
    'locale': 'en_US',
    'm_pixel_ratio': '2',
    'c_user': '100005768826578',
    'm_page_voice': '100005768826578',
    'x-referer': 'eyJyIjoiL3Byb2ZpbGUucGhwP2lkPTEwMDA4NzM3MjgwNzYyNiIsImgiOiIvcHJvZmlsZS5waHA%2FaWQ9MTAwMDg3MzcyODA3NjI2IiwicyI6Im0ifQ%3D%3D',
    'i_user': '100087372807626',
    'usida': 'eyJ2ZXIiOjEsImlkIjoiQXJsZjk2MDEyMnM0Z28iLCJ0aW1lIjoxNjY4NTczMDcxfQ%3D%3D',
    'xs': '34%3Amjq9JsPsHaJXXg%3A2%3A1668509359%3A-1%3A6008%3A%3AAcV6GLWXkuu41BtSa9EpoMmhK4W7aIEJhQfwY7uOZg',
    'fr': '01FieGJxrotx71BXA.AWVNotGVdUhbpPvb4D2Cc5BGqEY.BjdGeS.og.AAA.0.0.BjdGeS.AWVa2LoDpIs',
    'wd': '609x602',
}

headers = {
    'authority': 'www.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'sb=Lo2JYQUrqCvh2jCUcDg6Xja7; datr=Lo2JYXbyV5qZVyDZncpXiZtr; dpr=2; locale=en_US; m_pixel_ratio=2; c_user=100005768826578; m_page_voice=100005768826578; x-referer=eyJyIjoiL3Byb2ZpbGUucGhwP2lkPTEwMDA4NzM3MjgwNzYyNiIsImgiOiIvcHJvZmlsZS5waHA%2FaWQ9MTAwMDg3MzcyODA3NjI2IiwicyI6Im0ifQ%3D%3D; i_user=100087372807626; usida=eyJ2ZXIiOjEsImlkIjoiQXJsZjk2MDEyMnM0Z28iLCJ0aW1lIjoxNjY4NTczMDcxfQ%3D%3D; xs=34%3Amjq9JsPsHaJXXg%3A2%3A1668509359%3A-1%3A6008%3A%3AAcV6GLWXkuu41BtSa9EpoMmhK4W7aIEJhQfwY7uOZg; fr=01FieGJxrotx71BXA.AWVNotGVdUhbpPvb4D2Cc5BGqEY.BjdGeS.og.AAA.0.0.BjdGeS.AWVa2LoDpIs; wd=609x602',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/profile.php?id=100087372807626',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'viewport-width': '609',
    'x-fb-friendly-name': 'CometComposerInterceptionPluginUtilsQuery',
    'x-fb-lsd': 'pb--535QkueK2uwzAP-061',
}

data = {
    'av': '100087372807626',
    '__usid': '6-Trlfax23almmr:Prlfax2145jvy5:0-Arlf960122s4go-RV=6:F=',
    '__user': '100087372807626',
    '__a': '1',
    '__dyn': '7AzHxqU5a5Q1ryaxG4VuC0BVU98nwgU765QdwSwAyUco5S3O2Saxa1NwJwpUe8hw6vwb-q7oc81xoswIK1Rwwwg8a8465o-cwfG12wOKdwGxu782lwv89kbxS2218wc61axe3S1lwlE-UqwsUkxe2GewyDwkUtxGm2SUbElxm3y1lUlDw-wAw8im7-8wywdqUuBwJCwLyES0Io88cA0z8c84qifxe3u362-2B0oobo8o',
    '__csr': 'ghMR92cI44aqliYAN5lAKlqkx1q9lWWbEgRj9iFSKh4nayiWuV4jaO4odnofanao232no23mmBGeXmF4y39VHLhHBBBKSWpQ9AjyqyoSmWVGAlczmVqh_yerxIwKJ13G5t4DjGaGu8VUyVaK9QrGmVbh68VkXVoCmh0FzoWeyrCAz-mnGqq9h8C4F8Cteahpd28C5pUN4BBzWo-5ECjUR1d12iibUymU46UOvjCy8OmeK4uezkcxm6of88UnAwMDwKxS6FrBzk5o4WrxOuaK7ppqwiFoog8USm1mxmq6o8ouK9xK2y5EW5otw-wqAA1bgK1Fxa3-cwjE8o0L20QQ0l602wK02iy0qi0Ao05Z607T80pMw3MHw2OER0fq0tK0Yo0I66U1gpU-4qy60ku04Po2EO00-OzE880hZDi9wfSezE0bm85KtO6SQq4pR80dHwno6e0aga6o2Uw7swm81ho6qdwu821wGw8yE28wda',
    '__req': '1z',
    '__hs': '19312.HYP:comet_pkg.2.1.0.2.1',
    'dpr': '2',
    '__ccg': 'EXCELLENT',
    '__rev': '1006613421',
    '__s': 'q1iczf:vf44aj:eqqdld',
    '__hsi': '7166465085064830900',
    '__comet_req': '15',
    'fb_dtsg': 'NAcNjDKmOVxpvj5t_43nwfmUVlYIleLIb19v2Dm-sZi-nM0E18UBJAw:34:1668509359',
    'jazoest': '25423',
    'lsd': 'pb--535QkueK2uwzAP-061',
    '__aaid': '220911458111147',
    '__spin_r': '1006613421',
    '__spin_b': 'trunk',
    '__spin_t': '1668572678',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'CometComposerInterceptionPluginUtilsQuery',
    'variables': '{"target_type":"PROFILE_PLUS","target_id":"104386299162215","params":{"logging_data":{"entry_point":"PROFILE_PLUS_FEED","session_id":"443faf12-b1ec-4cd0-ad5c-3f27f8cda5c1"},"photo_ids":[],"placement":"COMPOSER_POST_BUTTON","post_text":"3rd-Automated-Post"}}',
    'server_timestamps': 'true',
    'doc_id': '5970639646279568',
}

response = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
print(response.json())