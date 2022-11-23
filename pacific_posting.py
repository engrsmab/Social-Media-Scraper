

# import requests

cookies = {
    'sb': 'Lo2JYQUrqCvh2jCUcDg6Xja7',
    'datr': 'Lo2JYXbyV5qZVyDZncpXiZtr',
    'dpr': '2',
    'locale': 'en_US',
    'm_pixel_ratio': '2',
    'c_user': '100005768826578',
    'xs': '23%3ALzfxvhJldGmpgQ%3A2%3A1668444828%3A-1%3A6008',
    'fr': '0mZVLWMc2PNJ3qvQm.AWXbxEZFKMu7EQqHSU2Q2E3Xlbw.BjcmP4.og.AAA.0.0.BjcnKd.AWVtt6xzcbY',
    'i_user': '100087372807626',
    'usida': 'eyJ2ZXIiOjEsImlkIjoiQXJsY2thZjQ0dmR4OSIsInRpbWUiOjE2Njg0NDU2NTh9', 
    'wd': '451x689',
}

headers = {
    'authority': 'www.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'sb=Lo2JYQUrqCvh2jCUcDg6Xja7; datr=Lo2JYXbyV5qZVyDZncpXiZtr; dpr=2; locale=en_US; m_pixel_ratio=2; c_user=100005768826578; xs=23%3ALzfxvhJldGmpgQ%3A2%3A1668444828%3A-1%3A6008; fr=0mZVLWMc2PNJ3qvQm.AWXbxEZFKMu7EQqHSU2Q2E3Xlbw.BjcmP4.og.AAA.0.0.BjcnKd.AWVtt6xzcbY; i_user=100087372807626; usida=eyJ2ZXIiOjEsImlkIjoiQXJsY2thZjQ0dmR4OSIsInRpbWUiOjE2Njg0NDU2NTh9; wd=451x689',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/profile.php?id=100087372807626',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'viewport-width': '451',
    'x-fb-friendly-name': 'ComposerStoryCreateMutation',
    'x-fb-lsd': 'rG3sXYtcygIXQxe9AqzYYC',
}

data = {
    'av': '100087372807626',
    '__usid': '6-Trlckaf1uktajn:Prlckwo58lkyn:0-Arlckaf44vdx9-RV=6:F=',

    '__user': '100087372807626',
    '__a': '1',
    '__dyn': '7AzHxqU5a5Q1ryaxG4VuC0BVU98nwgU765QdwSwAyUco5S3O2Saxa1NwJwpUe8hw6vwb-q7oc81xoswIK1Rwwwg8a8465o-cwfG12wOKdwGxu782lwv89kbxS2218wc61axe3S1lwlE-UqwsUkxe2GewyDwkUtxGm2SUbElxm3y1lUlDw-waCm7-8wywdqUuBwJCwLyES0Io88cA0z8c84qifxe3u362-2B0oobo8o',
    '__csr': 'giglNsoIrYIjcJhR5iitkLn9WQJPvXRAYLAWq9v8znlq9WvF9KXleZfOOuqlQHLBrpbJrUGvARSFEyAu_BF4zQteA4RBK-gyChEzjyUlLmaCiz8F1j8vGvLiGaA-Ugyu45KqQUKA4JGKQFrBiBDVpZ1rAhoOm6azpo-7bxq48ghAnxCt5zEJAx3gyUydABJ1eu8gcXQ68iUG8yUkGquiifxdABGcyUSquibUuy8mxeq3eeAwAxemqexC2q2S22dwm9o9EK6pECdxK4oN1C58LgswFAxW7XwywTwzxa5UlDxC6FU88aoS0wXG18xG1bwu8aU6-02zG02wvw6zw2BU39g0Ry01Luw0Bkwho0zl04sw3ZU1Vo0HK1Uwgk02bG021W1Oa0dzw1kG0AoAJ09Fw0HewWw2h4Uvg8hpvg2Fw4hwij5wbC0kK3W0qi32E1SE8SbzE88co3IxC0sd0gU2Gw',
    '__req': 'u',
    '__hs': '19310.HYP:comet_pkg.2.1.0.2.1',
    'dpr': '2',
    '__ccg': 'GOOD',
    '__rev': '1006599348',
    '__s': 'r7a2fq:cyvflv:du3uqf',
    '__hsi': '7165919528791339508',
    '__comet_req': '15',
    'fb_dtsg': 'NAcPk90pWqUNkODWs1DjDa4OS3BnMVYmaXsPIf5bCTmOHcrN4DTvH8w:23:1668444828',
            #    'NAcPM3D4nTTRsTvqfu24HPkR6ER-GkUYAOaDW62uW537rjwNBj1M4FQ:23:1668444828'
    'jazoest': '25380',
    'lsd': 'rG3sXYtcygIXQxe9AqzYYC',
    '__aaid': '220911458111147',
    '__spin_r': '1006599348',
    '__spin_b': 'trunk',
    '__spin_t': '1668445656',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'ComposerStoryCreateMutation',
    'variables': '{"input":{"composer_entry_point":"inline_composer","composer_source_surface":"timeline","idempotence_token":"977c5989-7d60-4230-b54d-76a96b75a117_FEED","source":"WWW","attachments":[],"audience":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}},"message":{"ranges":[],"text":"hi"},"with_tags_ids":[],"inline_activities":[],"explicit_place_id":"0","text_format_preset_id":"0","logging":{"composer_session_id":"977c5989-7d60-4230-b54d-76a96b75a117"},"navigation_data":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1668445658300,370977,190055527696468,"},"tracking":[null],"actor_id":"100087372807626","client_mutation_id":"1"},"displayCommentsFeedbackContext":null,"displayCommentsContextEnableComment":null,"displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"feedLocation":"TIMELINE","feedbackSource":0,"focusCommentID":null,"gridMediaWidth":230,"groupID":null,"scale":2,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"timeline","useDefaultActor":false,"inviteShortLinkKey":null,"isFeed":false,"isFundraiser":false,"isFunFactPost":false,"isGroup":false,"isEvent":false,"isTimeline":true,"isSocialLearning":false,"isPageNewsFeed":false,"isProfileReviews":false,"isWorkSharedDraft":false,"UFI2CommentsProvider_commentsKey":"ProfileCometTimelineRoute","hashtag":null,"canUserManageOffers":false}',
    'server_timestamps': 'true',
    'doc_id': '6076405069059091',
}

# response = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)



# ==========
# ==========
# ==========

import requests

cookies = {
    'sb': 'Lo2JYQUrqCvh2jCUcDg6Xja7',
    'datr': 'Lo2JYXbyV5qZVyDZncpXiZtr',
    'dpr': '2',
    'locale': 'en_US',
    'm_pixel_ratio': '2',
    'c_user': '100005768826578',
    'xs': '23%3ALzfxvhJldGmpgQ%3A2%3A1668444828%3A-1%3A6008',
    'fr': '0mZVLWMc2PNJ3qvQm.AWXbxEZFKMu7EQqHSU2Q2E3Xlbw.BjcmP4.og.AAA.0.0.BjcnKd.AWVtt6xzcbY',
    'i_user': '100087372807626',
    'usida': 'eyJ2ZXIiOjEsImlkIjoiQXJsY211cDE3ZjBvNmYiLCJ0aW1lIjoxNjY4NDQ4MTc3fQ%3D%3D',  # Changed
    'wd': '451x689',
}

headers = {
    'authority': 'www.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'sb=Lo2JYQUrqCvh2jCUcDg6Xja7; datr=Lo2JYXbyV5qZVyDZncpXiZtr; dpr=2; locale=en_US; m_pixel_ratio=2; c_user=100005768826578; xs=23%3ALzfxvhJldGmpgQ%3A2%3A1668444828%3A-1%3A6008; fr=0mZVLWMc2PNJ3qvQm.AWXbxEZFKMu7EQqHSU2Q2E3Xlbw.BjcmP4.og.AAA.0.0.BjcnKd.AWVtt6xzcbY; i_user=100087372807626; usida=eyJ2ZXIiOjEsImlkIjoiQXJsY211cDE3ZjBvNmYiLCJ0aW1lIjoxNjY4NDQ4MTc3fQ%3D%3D; wd=451x689',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/profile.php?id=100087372807626',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'viewport-width': '451',
    'x-fb-friendly-name': 'ComposerStoryCreateMutation',
    'x-fb-lsd': 'rG3sXYtcygIXQxe9AqzYYC',
}

data = {
    'av': '100087372807626',
    '__usid': '6-Trlckaf1uktajn:Prlckwo58lkyn:0-Arlcmup17f0o6f-RV=6:F=', # Changed
    '__user': '100087372807626',
    '__a': '1',
    '__dyn': '7AzHxqU5a5Q1ryaxG4VuC0BVU98nwgU765QdwSwAyUco5S3O2Saxa1NwJwpUe8hw6vwb-q7oc81xoswIK1Rwwwg8a8465o-cwfG12wOKdwGxu782lwv89kbxS2218wc61axe3S1lwlE-UqwsUkxe2GewyDwkUtxGm2SUbElxm3y1lUlDw-waCm7-8wywdqUuBwJCwLyES0Io88cA0z8c84qifxe3u362-2B0oobo8o',
    # Changed
    '__csr': 'giglNsoIvONcOR7kl99RiZsDHi6vXRAYLAWq9v8znlq9WvF9KXleZfOOup4taXVmSiXm-aDVdtGq8F7LVqh8Z7jF1dprLA8FAq8QUK5rRyFAEOagkO7WDXQGyFfK48Dx1rCJebF1bqHJamVkFpvBDQ5Kh5z9omWzpo-7bxq48ghAnxCt5zEJAx3gyUydABJ1eu8gcXQ68iUG8yUkGquiifxdABGcyUSquiqjxW8xq4VEcUWi2i4VpEW6o9Ebo88S1oBwCyUpCyoS6Uhz46okyZ1O2Ci7EvK2a3u2e4Enxmu6oqDwwwFzo23KE4y6E4K1UwHwrU0aeE0a1-0qe0anwcB03m806ZW02li15w2dk0hO0fTw7Bw2KU7y11g08KE087E78E0Se05iE2hyiQ0CC02IW3G094jxZ0x5BZ0aC0h619cm0Ko1iUfE1F8caw7qwzoKewwwNweO6o1MQ13waG',
    '__req': '1i',
    '__hs': '19310.HYP:comet_pkg.2.1.0.2.1',
    'dpr': '2',
    '__ccg': 'GOOD',
    '__rev': '1006599348',
    '__s': 'v5da9n:cyvflv:du3uqf',
    '__hsi': '7165919528791339508',
    '__comet_req': '15',
    'fb_dtsg': 'NAcPk90pWqUNkODWs1DjDa4OS3BnMVYmaXsPIf5bCTmOHcrN4DTvH8w:23:1668444828',
    'jazoest': '25380',
    'lsd': 'rG3sXYtcygIXQxe9AqzYYC',
    '__aaid': '220911458111147',
    '__spin_r': '1006599348',
    '__spin_b': 'trunk',
    '__spin_t': '1668445656',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'ComposerStoryCreateMutation',
    'variables': '{"input":{"composer_entry_point":"inline_composer","composer_source_surface":"timeline","idempotence_token":"14976166-8425-463b-9f1d-9528489a36d2_FEED","source":"WWW","attachments":[],"audience":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}},"message":{"ranges":[],"text":"First Automated Post"},"with_tags_ids":[],"inline_activities":[],"explicit_place_id":"0","text_format_preset_id":"0","logging":{"composer_session_id":"14976166-8425-463b-9f1d-9528489a36d2"},"navigation_data":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1668445658300,370977,190055527696468,"},"tracking":[null],"actor_id":"100087372807626","client_mutation_id":"2"},"displayCommentsFeedbackContext":null,"displayCommentsContextEnableComment":null,"displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"feedLocation":"TIMELINE","feedbackSource":0,"focusCommentID":null,"gridMediaWidth":230,"groupID":null,"scale":2,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"timeline","useDefaultActor":false,"inviteShortLinkKey":null,"isFeed":false,"isFundraiser":false,"isFunFactPost":false,"isGroup":false,"isEvent":false,"isTimeline":true,"isSocialLearning":false,"isPageNewsFeed":false,"isProfileReviews":false,"isWorkSharedDraft":false,"UFI2CommentsProvider_commentsKey":"ProfileCometTimelineRoute","hashtag":null,"canUserManageOffers":false}',
    'server_timestamps': 'true',
    'doc_id': '6076405069059091',
}

response = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
print(response.json()["errors"])
# import json
# txt = open("payload.txt","w")
# txt.write(json.dumps(response.json()))
# txt.close()