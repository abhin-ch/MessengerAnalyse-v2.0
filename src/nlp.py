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
    personality_insights.set_service_url(url)
    profile = personality_insights.profile(
            text,
            'application/json',
            content_type='text/plain',
            consumption_preferences=True,
            raw_scores=True
        ).get_result()
    user_personality = json.dumps(profile, indent=2)
    return user_personality

def get_script(d):
    """ This  fuction just get's the participants messages.
    EXAMPLE :
    {'Samuel Jackson': ['msg_n', ...msg_1], 'Abhinav Chaudhary': ['msg_n', ...msg_1]}
    """
    # Get message
    messages = d["messages"]
    script = ''
    p = get_participants(d)
    for msg in messages:
        sender_name = msg["sender_name"]
        try:
            lis = p[sender_name]
            lis.append( msg["content"])
        except:
            lis = p[sender_name]
            lis.append(script)
    return p

def format_script(contents):
    """
    ARG: dictionary of list : {'Samuel Jackson': ['msg_n', ...msg_1], 'Abhinav Chaudhary': ['msg_n', ...msg_1]}
    RETURN: dictionary of list : {'Samuel Jackson': ['msg_n-100', ...msg_1], 'Abhinav Chaudhary': ['msg_n-100', ...msg_1]}
    """
    msg= []
    for ele in contents:
        res = len(ele.split())
        if(res > 7):
            msg.append(ele)
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

def throw_back(script):
    """
    ARG: dictionary of list 
    RETURN 
    """
    script_formated = format_script(script)
    #print(script_formated)
    sampling = random.choices(script_formated, k=2)
    for ele in sampling:
        ele = unidecode(ele)
    return sampling



def execute2(d):
    """

    """
    # Get the script of messages 
    script = get_script(d)
    e = dict()
    inner_dict = dict()
    # Get Participant before NLP population
    big_four = get_participants(d)
    summary = get_participants(d)
    progress_bar = get_participants(d)
    throw_backs = get_participants(d)
    interst = get_participants(d)
    for name in script:
        # Throwback 
        throw_backs[name] = throw_back(script[name])
        q = personality_insight_user(str(script[name]))
        p = json.loads(q)
        big_four[name] = generator.big_four(p)
        traits = generator.sub_traits(p)
        summary[name] = generator.summary(traits)
        progress_bar[name] = generator.five_progresss_bara_data(traits, p)
        interst[name] = generator.sub_interest(p)
    inner_dict["big_four"]= big_four
    inner_dict["summary"] = summary
    inner_dict["progress_bar"] = progress_bar
    inner_dict["throw_back"] = throw_backs
    inner_dict["sub_interst"] = interst
    e.update(inner_dict)
    return e