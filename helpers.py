#processing code to function

def process_results(data):
    nested_values = ['video', 'author', 'music', 'stats', 'authorStats', 'stickersOnItem']
    skip_values = ['challenges', 'duetInfo', 'textExtra', 'stickersOnItem']

    #blank dictionary
    flattened_data = {}
    #loop through each video
    for idx, value in enumerate(data):
        flattened_data[idx] = {}
        #loop through each property in video
        for prop_idx, prop_value in value.items():
            #see if its a nested property
            if prop_idx in nested_values:
                if prop_idx in skip_values:
                    pass
                else:
                    #loop through nested property
                    for nested_idx, nested_value in prop_value.items():
                        flattened_data[idx][prop_idx + '_' + nested_idx] = nested_value
            #if its not nested, add it to the flattened dictionary
            else:
                flattened_data[idx][prop_idx] = prop_value
    return
    flattened_data