from TikTokApi import TikTokApi
import json


with TikTokApi() as api:
    for trending_video in api.trending.videos():
        print(trending_video)