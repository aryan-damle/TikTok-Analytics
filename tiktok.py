#imports
from TikTokApi import TikTokApi
import json
from helpers import process_results
import pandas as pd
import sys

def get_data(hashtag):
    #get cookie data
    verifyFp = "verify_lgk7gfaf_nByzMOYf_9YeR_4ZLr_AjZS_fWTx1yy6d2dN"
    api = TikTokApi.get_instance(custon_verifyFp=verifyFp, use_test_endpoints=True)
    trending = api.by_hashtag(hashtag)
    flattened_data = process_results(trending)
    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    df.to_csv('tiktokdata.csv', index=False)