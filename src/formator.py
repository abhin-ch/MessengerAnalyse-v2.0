"""
AUTHORS: Abhinav Chaudhary and Anthony Inthavong
DESCRIPTION: This script edits the file uploaded by the user. It will merge them and then delete
            them from the server. 
"""
from glob import glob
import json 
from itertools import chain
from operator import add
import os
import itertools
import functools
import operator
import sys

# No Python Cache
sys.dont_write_bytecode = True

# Get the Path 

def get_filename():
    filename = glob('..//Analysis 2.0/uploads/message_*.json')
    return filename

def merge_message(filename ):
    ''' This will extract message the Json Files and 
        output and save the merged messages'''
    # Intializing
    data = []
    num_file = 0
    msg = "..//Analysis 2.0/uploads/message.json"
    # Interate through the files
    for file in filename:
        num_file += 1
        # Open each file
        with open(file) as msg:
            # Get the messages from each file
            d = json.load(msg)
            message = d['messages']
            data = data + message
    print("This is my data "+ str(len(data)))
    json_object = json.dumps(data, indent = 10) 
    with open('..//Analysis 2.0/uploads\\message.json', "w") as outfile: 
        outfile.write(json_object)
    return None

def merge_file(filename ):
    ''' This will Merge the Json Files and 
        output and save the merged file'''
    # intializing
    data = {}
    fil_url = '..//Analysis 2.0/uploads\\message_1.json'
    msg_url = '..//Analysis 2.0/uploads\\message.json'
    # data_url = '..//Analysis 2.0/data\\data.json'
    # Open file 
    # -> Making a proper file
    with open(msg_url) as msg:
            message = json.load(msg)
            data['messages'] = message

    with open(fil_url) as fil:
            file = json.load(fil)
            data['participants'] = file['participants']
            data['title'] = file['title']
            data['is_still_participant'] = file['is_still_participant']
            data['thread_type'] = file['thread_type']
            data['thread_path'] = file['thread_path']
    # Write file 
    # json_object = json.dumps(data, indent = 4) 
    # with open(data_url, "w") as outfile: 
    #     outfile.write(json_object)
    print("The return type is:  "+ str(type(data)))
    return data

def delete_files(filename):
    ''' Deleteing the files from the folder 
    '''
    message = '..//Analysis 2.0/uploads\\message.json'
    os.remove(message)
    for file in filename:
        os.remove(file)


def main():
    filename = get_filename()
    merge_message(filename)
    json_file = merge_file(filename)
    delete_files(filename)
    return json_file


# if __name__ == "__main__":
#      main()