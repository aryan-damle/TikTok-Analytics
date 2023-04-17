from TikTokApi import TikTokApi
import json
from helpers import process_results
import pandas as pd

#cookie data
verifyFp = "verify_lgk7gfaf_nByzMOYf_9YeR_4ZLr_AjZS_fWTx1yy6d2dN"
api = TikTokApi(custom_verifyFp=verifyFp, use_test_endpoints=True)
#get data by hashtag
trending = TikTokApi.hashtag(name='fyp')
#process data
flattended_data = process_results(trending)

#export to json
# with open('export.json', 'w') as f:
#     json.dump(trending, f)

#Convert preprocessed data to dataframe

df = pd.DataFrame.from_dict(flattended_data, orient='index')
df.to_csv('tiktokdata.csv')