"""
AUTHORS: Abhinav Chaudhary and Anthony Inthavong
DESCRIPTION: This script in the backend to get all the analysis. It uses the power 
            of pandas to show diffrent things such as total message, participants etc
"""
import json
import pandas as pd

import src.nlp as ex


from src.db import DataGateway # importing database class

db = DataGateway('messages.db')

def get_participants(d=None):
    """ list of all participants in group chat
    """
    q = 'SELECT *, 0 from participants'
    data = {k:v for k,v in db.select(q)}
    return data

def get_message_count(d):
    """ Return total message count per person
    including everything
    {
        "name" : int
    }
    """

    q = 'SELECT sender_name, COUNT(content) FROM messages GROUP BY sender_name;'
    data = {k:v for k,v in db.select(q)}
    return {"message_count": json.dumps(data)}


def get_word_count(d):
    """ Return total word count per person
    not include images, gifs
    {
        "name" : int
    }
    """

    q = "SELECT sender_name, SUM(length(content) - length(replace(content, ' ', '')) + 1) from messages group by sender_name;"
    data = {k:v for k,v in db.select(q)}
    return {"word_count": json.dumps(data)}

def get_message_by_day_year(d):
    """ Return total messages by day in year
    {
        "day": int
    }
    """


    q = """
    SELECT day, count(day)
        FROM 
        (
            SELECT strftime('%j', timestamp_ms / 1000, 'unixepoch') AS day 

            FROM messages
        ) GROUP BY day ORDER BY day
    """
    data = {k:v for k,v in db.select(q)}
    return {"message_by_day_year_count": json.dumps(data)}

def get_message_by_day_week(d):
    """ Return message by day of week
    {
        "weekday": int
    }
    """
    q = """
    SELECT CASE day
        WHEN '0' THEN 'Sunday'
        WHEN '1' THEN 'Monday'
        WHEN '2' THEN 'Tuesday'
        WHEN '3' THEN 'Wednesday'
        WHEN '4' THEN 'Thursday'
        WHEN '5' THEN 'Friday'
        WHEN '6' THEN 'Saturday'
        END,
        count(day)
    FROM 
    (
        SELECT strftime('%w', timestamp_ms / 1000, 'unixepoch') AS day 

        FROM messages
    ) GROUP BY day ORDER BY day;
    """
    data = {k:v for k,v in db.select(q)}
    return {"message_by_day_week_count": json.dumps(data)}


def get_message_by_day_week_percent(d):
    """ Return message by day of week
    {
        "weekday": int
    }
    """

    q = """
    SELECT CASE day
        WHEN '0' THEN 'Sunday'
        WHEN '1' THEN 'Monday'
        WHEN '2' THEN 'Tuesday'
        WHEN '3' THEN 'Wednesday'
        WHEN '4' THEN 'Thursday'
        WHEN '5' THEN 'Friday'
        WHEN '6' THEN 'Saturday'
        END,
        round(count(day)*(100.0) / (SELECT COUNT(timestamp_ms) from messages), 2) as percentage
    FROM 
    (
        SELECT strftime('%w', timestamp_ms / 1000, 'unixepoch') AS day 

        FROM messages
    ) GROUP BY day ORDER BY day;
    """
    data = {k:v for k,v in db.select(q)}
    return {"message_by_day_week_percent": json.dumps(data)}

def get_message_by_day_week_group(d):
    """ Return message by day of week
    {
        "name": {
            "weekday": int
        }
    }
    """
    df = pd.DataFrame.from_dict(d["messages"])
    df['timestamp_ms'] = pd.to_datetime(df['timestamp_ms'], unit='ms')
    people = get_participants(d)
    for p in list(people):
        people[p] = {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0,'Friday':0,'Saturday':0, 'Sunday':0}

    for time, person in zip(df['timestamp_ms'], df['sender_name']):
        # Monday == 0
        v = time.day_name()
        people[person][v] += 1
    return {"message_by_day_week_group": json.dumps(people)}


def get_message_by_day_week_g(d):
    """ Return message by day of week
    {
        "name": {
            "weekday": int
        }
    }
    """
    df = pd.DataFrame.from_dict(d["messages"])
    df['timestamp_ms'] = pd.to_datetime(df['timestamp_ms'], unit='ms')
    people = get_participants(d)
    pep = get_participants(d)
    for p in list(people):
        people[p] = {'Monday':0, 'Tuesday':0, 'Wednesday':0, 'Thursday':0,'Friday':0,'Saturday':0, 'Sunday':0}

    for time, person in zip(df['timestamp_ms'], df['sender_name']):
        # Monday == 0
        v = time.day_name()
        people[person][v] += 1

    for human in list(pep) :
        pep[human] = list(people[human].values())

    return {"message_by_day_week_g": json.dumps(pep)}


colour = ["#51BCDA","#CCCCCC", "#cf4e72", "#aa4ecf", "#cfbe4e", "#82a15e" ]
def get_name_to_colour(d):
    "Takes in a name and assigns them a colour"
    people = get_participants(d)
    col = {}
    i = 0
    for p in list(people):
        col[p] = colour[i]
        i = i+1
    return {"get_name_to_colour": json.dumps(col)}

def get_message_by_month(d):
    """ Return messages by month
    {
        "month": int
    }
    """
    df = pd.DataFrame.from_dict(d["messages"])
    df['timestamp_ms'] = pd.to_datetime(df['timestamp_ms'], unit='ms')
    d = {'January': 0, 'February': 0, 'March':0, 'April':0, 'May':0, 'June':0,
    'July':0, 'August':0, 'September':0, 'October':0, 'November':0, 'December':0}
    for data in df['timestamp_ms']:
        v = data.month_name()
        d[v] += 1
    return {"message_by_month_count": json.dumps(d)}

def get_message_by_month_group(d):
    """ Return messages by month
    {
        "name" : {
            "month": int
        }
    }
    """
    df = pd.DataFrame.from_dict(d["messages"])
    df['timestamp_ms'] = pd.to_datetime(df['timestamp_ms'], unit='ms')
    people = get_participants(d)
    pep = get_participants(d)
    for p in list(people):
        people[p] = {'January': 0, 'February': 0, 'March':0, 'April':0, 'May':0, 'June':0,
        'July':0, 'August':0, 'September':0, 'October':0, 'November':0, 'December':0}

    for time, person in zip(df['timestamp_ms'], df['sender_name']):
        v = time.month_name()
        people[person][v] += 1

    for human in list(pep):
        pep[human] = list(people[human].values())

    return {"message_by_month_group": json.dumps(pep)}

def get_message_by_quarter(d):
    """ Return message count by quarter of year
    {
        "quarter": int
    }
    """
    df = pd.DataFrame.from_dict(d["messages"])
    df['timestamp_ms'] = pd.to_datetime(df['timestamp_ms'], unit='ms')
    d = dict()
    for data in df['timestamp_ms']:
        v = data.quarter
        if v in d:
            d[v] += 1
        else:
            d[v] = 1
    return {"message_by_quarter_count": json.dumps(d)}

def get_message_by_hour(d):
    """ Return messages by hour (24)
    {
        "hour": int
    }
    """
    df = pd.DataFrame.from_dict(d["messages"])
    df['timestamp_ms'] = pd.to_datetime(df['timestamp_ms'], unit='ms')
    d = dict()
    for data in df['timestamp_ms']:
        v = (data.hour - 5) % 24
        if v in d:
            d[v] += 1
        else:
            d[v] = 1
    return {"message_by_hour_count": json.dumps(d)}

def get_message_by_year(d):
    """ Return message count per year
    {
        "year": int
    }
    """
    df = pd.DataFrame.from_dict(d["messages"])
    df['timestamp_ms'] = pd.to_datetime(df['timestamp_ms'], unit='ms')
    d = dict()
    for data in df['timestamp_ms']:
        v = data.year
        if v in d:
            d[v] += 1
        else:
            d[v] = 1
    return {"message_by_year_count": json.dumps(d)}

def get_message_by_year_percent(d):
    """ Return message count per year
    {
        "year": int
    }
    """
    df = pd.DataFrame.from_dict(d["messages"])
    df['timestamp_ms'] = pd.to_datetime(df['timestamp_ms'], unit='ms')
    d = dict()
    for data in df['timestamp_ms']:
        v = data.year
        if v in d:
            d[v] += 1
        else:
            d[v] = 1
    total = sum(d.values())
    d = {i:round(d[i]/total) for i in list(d)}
    return {"message_by_year_percent": json.dumps(d)}

### TODO: test
def get_len_of_message(d):
    """ Return length of messages sent by person
    not include images, gifs
    {
        "name": int
    }
    """
    # participants
    p = {person['name']:dict() for person in d['participants']}
    for msg in d['messages']:
        if 'content' in msg:
            k = len(msg['content'])
            if k in p[msg['sender_name']]:
                p[msg['sender_name']][k] += 1
            else:
                p[msg['sender_name']][k] = 1
    # convert to json
    return {"len_of_message" : json.dumps(p)}

def get_message_by_hour_group(d): #TODO: check if can do faster than iterating through rows
    """ Return the number of messages per hour for each
    person within the group conversation
    Index(['audio_files', 'call_duration', 'content', 'files', 'gifs', 'missed',
       'photos', 'reactions', 'sender_name', 'share', 'sticker',
       'timestamp_ms', 'type'],
      dtype='object')

      {
          "name" : {
              "word": int
          }
      }
    """
    df = pd.DataFrame.from_dict(d["messages"])
    df['timestamp_ms'] = pd.to_datetime(df['timestamp_ms'], unit='ms')
    pep = get_participants(d)
    people = get_participants(d)
    for p in list(people):
        people[p] = {t:0 for t in range(0, 24)}

    for time, person in zip(df['timestamp_ms'], df['sender_name']):
        v = (time.hour - 5) % 24
        people[person][v] += 1

    for human in list(pep):
        pep[human] = list(people[human].values())
    return {"message_by_hour_group": json.dumps(pep)}

def get_message_count_percent(d):
    v = get_message_count(d)
    dct = json.loads(v["message_count"])
    total = sum(dct.values())
    for k in list(dct):
        dct[k] /= total
        dct[k] = round(dct[k], 2)
    return {"message_count_percent": json.dumps(dct)}

def get_word_count_percent(d):
    v = get_word_count(d)
    dct = json.loads(v["word_count"])
    total = sum(dct.values())
    for k in list(dct):
        dct[k] /= total
        dct[k] = round(dct[k], 2)
    return {"word_count_percent": json.dumps(dct)}

def get_message_by_day_month(d):
    df = pd.DataFrame.from_dict(d["messages"])
    df['timestamp_ms'] = pd.to_datetime(df['timestamp_ms'], unit='ms')
    d = {i:0 for i in range(1, 32)} # 31 days in month
    for data in df['timestamp_ms']:
        v = data.day
        d[v] += 1
    return {"message_by_day_month_count": json.dumps(d)}

def total_message(d):
    q = """
    SELECT COUNT(sender_name) from messages;
    """
    data = db.select(q)[0]
    return {"total_message": json.dumps(data[0])}

def total_word(d):
    
    q = """SELECT SUM(length(content) - length(replace(content, ' ', '')) + 1)
    FROM messages"""
    data = db.select(q)[0]
    return {"total_word": data[0]}

def total_call(d):
    # participants
    sum = 0
    for msg in d['messages']:
        if('call_duration' in msg):
            sum = sum + 1
    # convert to json
    return {"total_call": json.dumps(sum)}

def personality_insight(d):
    """ Get the personality Insight from 
    nlp.py. It's gonna make an api call to watson """
    insight = ex.execute2(d)
    return {"personality_insight": json.dumps(insight)}

def main(d):
    """ Read python dict and do stuff
    Returns statistical summary as JSON
    """
    summary = dict()
    data = [
        personality_insight(d),
        total_message(d),
        total_word(d),
        total_call(d),

        get_message_count(d),
        get_word_count(d),
        get_len_of_message(d),
        
        get_message_by_year(d),
        get_message_by_day_year(d),
        get_message_by_month(d),
        get_message_by_quarter(d),
        get_message_by_day_week(d),
        get_message_by_hour(d),
        get_message_by_day_month(d),
        get_message_by_hour_group(d), # method currently slow
        get_message_by_day_week_group(d),
        get_message_by_day_week_g(d),
        get_message_by_month_group(d),
        # TODO
        # get_message_by_day_year_group(d), ?
        # get_message_by_hour_percent(d),
        # get_message_by_month_percent(d),
        # get_message_by_quarter_percent(d),
        # get_message_by_quarter_group(d),
        # get_message_by_year_group(d),
        get_message_by_year_percent(d),
        get_message_by_day_week_percent(d),
        get_message_count_percent(d),
        get_word_count_percent(d),
        get_name_to_colour(d)
        # get_len_of_message(d)
        ]
    for element in data:
        summary.update(element)

    return json.dumps(summary)

if __name__ == "__main__":
    # with open('../data.json', 'r') as data:
    #     d = json.load(data)
    #     print(get_participants(d))
    pass