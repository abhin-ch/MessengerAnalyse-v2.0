"""
AUTHORS: Abhinav Chaudhary and Anthony Inthavong
DESCRIPTION: This script edits the file uploaded by the user. It will merge them and then delete
            them from the server. 
"""
from glob import glob
import json 
import os 
import os.path # for file path


# merged json path
MESSAGE_PATH = os.path.join('.', 'uploads', 'message.json')


def get_filename():
    """ Return files in uploads folder
    """
    f = os.path.join('.', 'uploads', 'message_*.json')
    filename = glob(f)
    return filename

def merge_message(filename):
    ''' This will extract message the Json Files and 
        output and save the merged messages'''
    # Intializing
    data = []
    
    # Interate through the files
    for file in filename:

        # Open each file
        with open(file) as msg:
            # Get the messages from each file
            d = json.load(msg)
            message = d['messages']
            data = data + message

    json_object = json.dumps(data, indent = 10) 

    # write json file object
    with open(MESSAGE_PATH, "w") as outfile: 
        outfile.write(json_object)

def merge_file(filename):
    """ merge Message.json and message_1.json
    """
    
    fil_url = os.path.join('.', 'uploads', 'message_1.json')

    with open(fil_url) as fil:
        data = json.load(fil)
    
    with open(MESSAGE_PATH) as msg:
        message = json.load(msg)
        data['messages'] = message

    return data

def delete_files(filename):
    ''' Delete files from uploads folder
    '''
    os.remove(MESSAGE_PATH)
    for file in filename:
        os.remove(file)

def main():
    filename = get_filename()
    merge_message(filename)
    json_file = merge_file(filename)
    delete_files(filename)
    return json_file
