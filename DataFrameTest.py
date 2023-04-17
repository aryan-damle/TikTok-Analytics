import pandas as pd
import json
#read json obj
df = pd.read_json('export.json')
#view first five rows
df.head()
#export to csv
df.to_csv('tiktokdata.csv')

#helper function to process data

with open('export.json', 'r') as f:
    data  = json.load(f)
    nested_values = ['video', 'author', 'music', 'stats', 'authorStats']
    skip_values = ['challenges', 'duetInfo', 'textExtra', 'stickersOnItem']
    #create balnk dictionary
    flattened_data = {}
    #loop through each video
    for idx, value in enumerate(data):
        flattened_data[idx] = {}
        #loop[ through each value in each video
        for prop_idx, prop_value in value.items():
            #check if nested
            if (prop_idx in nested_values):
                if (prop_idx in skip_values):
                    pass
                else:
                    #loop through each nested value
                    for nested_idx, nested_value in prop_value.items():
                        flattened_data[idx][prop_idx + '_' + nested_idx] = nested_value
            #if it's not nested, add it back to the flattened dictionary
            else:
                flattened_data[idx][prop_idx] = prop_value

    #output
    type(flattened_data)
    df_test = pd.DataFrame.from_dict(flattened_data, orient='index')
    df_test.head()
    df_test.to_csv('analytics.csv')
        