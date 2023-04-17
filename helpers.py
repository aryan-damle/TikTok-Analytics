#Convert processing code to function
def process_results(data):
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

    return flattened_data