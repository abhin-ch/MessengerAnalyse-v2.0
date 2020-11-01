"""
AUTHORS: Abhinav Chaudhary and Anthony Inthavong
DESCRIPTION: This script edits the file uploaded by the user. It will merge them and then delete
            them from the server. 
"""
from glob import glob
import json 
import os 

def get_filename():
    """ Return files in uploads folder
    """

    # search all files not named message.json
    f = os.path.join('.', 'uploads', '*.json')
    return glob(f)

def merge_content(paths):
    """ Given a list of paths of files, return the collected results as a json file
    {
        name: name
    }
    {
        sender_name,
    }
    """
    # Intializing
    data = []
    data = dict()
    data['participants'] = []
    data['messages'] = []

    participants = set()
    
    # iterate through all files
    for f in paths:

        # Open each file
        with open(f) as content:
            # Get the messages from each file
            container = json.load(content)
            container['participants']

            # collect names of all participants
            [participants.add(p['name']) for p in container['participants']]

            # add all messages to single array
            data['messages'] += container['messages']
    # convert participants to json notation
    [data['participants'].append({'name': name}) for name in participants]
    return data

def delete_files(paths):
    ''' Delete files from uploads folder
    '''
    [os.remove(f) for f in paths]

def main():
    filename = get_filename()
    data = merge_content(filename)
    delete_files(filename)
    return data
