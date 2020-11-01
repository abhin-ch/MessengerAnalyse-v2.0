"""
AUTHORS: Abhinav Chaudhary 
DESCRIPTION: This script gets the personality insight of the person. It gives the big five personality traits.
            such as Agreableness,Extravertsion.... etc
"""

import json
import pandas as pd
import random
import sys
from unidecode import unidecode

# Text-Generator
import src.text_generator as generator 



# Personality Insight SDK
from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException




# IBM WATSON API Authentication 
url = 'https://api.jp-tok.personality-insights.watson.cloud.ibm.com/instances/1874f80a-f372-445a-bdd6-9dde92eaa49b'
apikey = 'BUi7V8DHWNLsmdiaAX8ILovvmKI4dZImb7C0YOEzSqi9'
authenticator = IAMAuthenticator(apikey)
personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    authenticator=authenticator
)
personality_insights.set_service_url(url)

def personality_insight_user(text):
    """ This function returns the personality of the user by 
    making an API call to ibm watson : Personality Insight Tool

    Return : JSON type 
    """

    # api requires at least 100 words otherwise error
    if len(text.split()) >= 100:
        personality_insights.set_service_url(url)
        profile = personality_insights.profile(
                text,
                'application/json',
                content_type='text/plain',
                consumption_preferences=True,
                raw_scores=True
            ).get_result()
        return profile
    return None

def get_script(d):
    """ This  fuction just get's the participants messages.
    EXAMPLE :
    {'Samuel Jackson': ['msg_n', ...msg_1], 'Abhinav Chaudhary': ['msg_n', ...msg_1]}
    """
    messages = d["messages"]
    p = get_participants(d)
    for content in messages:
        name = content["sender_name"]
        if "content" in content:
            p[name].append(content["content"])
    return p

def format_script(contents, minimum_word_count = 5):
    """
    ARG: dictionary of list : {'Samuel Jackson': ['msg_n', ...msg_1], 'Abhinav Chaudhary': ['msg_n', ...msg_1]}
    RETURN: dictionary of list : {'Samuel Jackson': ['msg_n-100', ...msg_1], 'Abhinav Chaudhary': ['msg_n-100', ...msg_1]}
    """
    msg = []
    for e in contents:
        # if number of words is greater than some amount, append to return message
        if len(e.split()) > minimum_word_count:
            msg.append(e)
    return msg
            
def get_participants(d):
    """ List of all participants in group chat
    EXAMPLE:
    {'Samuel Jackson': [], 'Abhinav Chaudhary': []}
    """
    p = {person['name']:[] for person in d['participants']}
    for msg in d['messages']:
        if msg['sender_name'] not in p:
            p[msg['sender_name']] = []
    return p

def throw_back(script, k=2):
    """
    ARG: dictionary of list 
    RETURN 
    """
    messages = format_script(script)
    if len(messages) > 2:
        # pick k random elements in message sample
        sample = random.choices(messages, k=k)
    else:
        sample = [""]

    # for ele in sampling:
    #     ele = unidecode(ele)
    # return sampling
    return sample

def execute2(d):
    """

    """
    # Get the script of messages 
    script = get_script(d)
    e = dict()
    data = dict()
    # Get Participant before NLP population
    big_four = get_participants(d)
    summary = get_participants(d)
    progress_bar = get_participants(d)
    throw_backs = get_participants(d)
    interst = get_participants(d)
    # open('personaility.txt', 'w').close()
    for name in script:
        throw_backs[name] = throw_back(script[name])        
        p = personality_insight_user(str(script[name]))
        if p:
            # debug
            # with open('./test/personaility_{}.json'.format(name), 'w') as f:
            #     json.dump({name: p}, f)

            # Big 4 personality types
            big_four[name] = generator.big_four(p)

            # get summary of big 4 from traits
            traits = generator.sub_traits(p)
            summary[name] = generator.summary(traits)

            #
            progress_bar[name] = generator.five_progresss_bara_data(traits, p)

            #
            interst[name] = generator.sub_interest(p)
        else:
            summary[name] = "Sorry, there is not enough information. Please try again when there is more data."

    data["big_four"]= big_four
    data["summary"] = summary
    data["progress_bar"] = progress_bar
    data["throw_back"] = throw_backs
    data["sub_interst"] = interst
    e.update(data)
    return e