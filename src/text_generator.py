dictionary = {
    'facet_adventurousness_low':"You enjoy familiar routines and prefer not to deviate from them. " ,
    'facet_adventurousness_high':"You are eager to experience new things. " ,
    'facet_artistic_interests_low':"You are less concerned with artistic or creative activities than most people. " ,
    'facet_artistic_interests_high':"You enjoy beauty and seek out creative experiences. " ,
    'facet_emotionality_low':"You do not frequently think about or openly express your emotions. " ,
    'facet_emotionality_high':"You are aware of your feelings and how to express them. ",
    'facet_imagination_low':"You prefer facts over fantasy. ",
    'facet_imagination_high':"You have a wild imagination. ",
    'facet_intellect_low': "You prefer dealing with the world as it is, rarely considering abstract ideas. ",
    'facet_intellect_high':"You are open to and intrigued by new ideas and love to explore them. ",
    'facet_liberalism_low':"You prefer following with tradition to maintain a sense of stability. ",
    'facet_liberalism_high':"You prefer to challenge authority and traditional values to help bring about change. ", 
    'facet_achievement_striving_low':" You are content with your level of accomplishment and do not feel the need to set ambitious goals", 
    'facet_achievement_striving_high':" You set high goals for yourself and work hard to achieve them.", 
    'facet_cautiousness_low':" You would rather take action immediately than spend time deliberating making a decision", 
    'facet_cautiousness_high':" You carefully think through decisions before making them.",
    'facet_dutifulness_low':" You do what you want, disregarding rules and obligations.",
    'facet_dutifulness_high':" You take rules and obligations seriously, even when they are inconvenient.",
    'facet_orderliness_low':" You do not make a lot of time for organization in your daily life.",
    'facet_orderliness_high':" You feel a strong need for structure in your life. ",
    'facet_self_discipline_low':" You have a hard time sticking with difficult tasks for a long period of time.",
    'facet_self_discipline_high':" You have a hard time sticking with difficult tasks for a long period of time.",
    'facet_self_efficacy_low':" You frequently doubt your ability to achieve your goals.",
    'facet_self_efficacy_high':" You feel you have the ability to succeed in the tasks you set out to do.",
    'facet_activity_level_low':" You appreciate a relaxed pace in life.",
    'facet_activity_level_high':" You enjoy a fast-paced, busy schedule with many activities.",
    'facet_assertiveness_low':" You prefer to listen than to talk, especially in group settings.",
    'facet_assertiveness_high':" You tend to speak up and take charge of situations, and you are comfortable leading groups.",
    'facet_cheerfulness_low':" You are generally serious and do not joke much.",
    'facet_cheerfulness_high':" You are a joyful person and share that joy with the world.",
    'facet_excitement_seeking_low':" You prefer activities that are quiet, calm, and safe.",
    'facet_excitement_seeking_high':" You are excited by taking risks and feel bored without lots of action going on.",
    'facet_friendliness_low':" You are a private person and do not let many people in.",
    'facet_friendliness_high':" You make friends easily and feel comfortable around other people.",
    'facet_gregariousness_low':" You have a strong desire to have time to yourself.",
    'facet_gregariousness_high':" You enjoy being in the company of others.",
    'facet_altruism_low':" You are more concerned with taking care of yourself than taking time for others.",
    'facet_altruism_high':"You feel fulfilled when helping others and will go out of your way to do so.",
    'facet_cooperation_low':"You do not shy away from contradicting others. ",
    'facet_cooperation_high':"You are easy to please and try to avoid confrontation. ",
    'facet_modesty_low':"You hold yourself in high regard and are satisfied with who you are. ",
    'facet_modesty_high':"You are uncomfortable being the center of attention. ",
    'facet_morality_low':"You are comfortable using every trick in the book to get what you want. ",
    'facet_morality_high':"You think it is wrong to take advantage of others to get ahead.",
    'facet_sympathy_low':"You think people should generally rely more on themselves than on others.",
    'facet_sympathy_high':"You feel what others feel and are compassionate toward them.",
    'facet_trust_low':"You are wary of other people's intentions and do not trust easily.",
    'facet_trust_high':"You believe the best of others and trust people easily.",
    'facet_anger_low':"It takes a lot to get you angry. ",
    'facet_anger_high':"You have a fiery temper, especially when things do not go your way. ",
    'facet_anxiety_low':"You tend to feel calm and self-assured. ",
    'facet_anxiety_high':"You tend to worry about things that might happen. ",
    'facet_depression_low':"You are generally comfortable with yourself as you are. ",
    'facet_depression_high':"You think quite often about the things you are unhappy about. ",
    'facet_immoderation_low':"You have control over your desires, which are not particularly intense. ",
    'facet_immoderation_high':"You feel your desires strongly and are easily tempted by them. ",
    'facet_self_consciousness_low':"You are hard to embarrass and are self-confident most of the time. ",
    'facet_self_consciousness_high':"You are sensitive about what others might be thinking of you. ",
    'facet_vulnerability_low':"You handle unexpected events calmly and effectively. ",
    'facet_vulnerability_high':"You are easily overwhelmed in stressful situations. "
}

interest = {
    'Likely to like romance movies': "Romantic",
    'Likely to like adventure movies': "Adventureous",
    'Likely to like horror movies': "Horror",
    'Likely to like musical movies': "Musical",
    'Likely to like historical movies': "Historical ",
    'Likely to like science-fiction movies': "Sci-Fic",
    'Likely to like war movies': "War",
    'Likely to like drama movies': "Drama",
    'Likely to like action movies': "Action",
    'Likely to like documentary movies': "Documentary",
    'Likely to like rap music': "Rap",
    'Likely to like country music': "Country",
    'Likely to like R&B music': "R&B",
    'Likely to like hip hop music': "Hip Hop",
    'Likely to attend live musical events': "Live",
    'Likely to have experience playing music': "Like Playing",
    'Likely to like Latin music': "Latin",
    'Likely to like rock music': "Rock",
    'Likely to like classical music': "Classical",
    'Likely to read often': "Like Reading",
    'Likely to read entertainment magazines': "Like Magazine",
    'Likely to read non-fiction books': "Non-Fiction"
}

def big_four(p):
    """
    This function takes in a personality dictionary and returns the big 
    four personality traits which are:
    [Agreeablness, Concisnetous, Openness, Emotional Range]

    arg: dict from personality insight
    return : list

    """
    # Extract personality feature from data frame
    personalities = p["personality"]
    # Create neeeds dictionary
    ret = []
    # Get the big Four 
    result = {need['name']:round(need['percentile'],2) for need in personalities}
    del result['Extraversion']
    # Append into list
    ret.append( result['Agreeableness'])
    ret.append(result['Conscientiousness'])
    ret.append(result['Openness'])
    ret.append(result['Emotional range'])

    return ret

def sub_traits(p):
    """"
    This function takes in a personality dictionary and returns the sub traits
    with there coresponding scores in a form of a dictionary
    {'facet_adventurousness': 0.95, 'facet_artistic_interests': 0.88}

    arg: dict from personality insight
    return : dict

    """
    i=0
    traits = dict()
    while i<len(p["personality"]):
        profile = p["personality"][i]['children']
        ret = {a['trait_id']:round(a['percentile'],2) for a in profile}
        traits.update(ret)
        i+=1
    return traits

def summary(traits:dict, low:float=0.45, high:float=0.75, min_low:float = 0.10, max_high:float = .90) -> str:
    """"
    This function takes in a the sub traits with there corresponding scores
    and gives analysis on high and low trait marks.
    
    arg: dict, float , float 
    return : string

    """

    profile = ""
    for trait in traits:
        # EXTREMLY HIGH
        if(traits[trait] > high):
            trait += "_high"
        # EXTREMLY LOW
        elif(traits[trait] < low):
            trait += "_low"
        
        if trait in dictionary:
            response = dictionary[trait]
            profile += response

    if (len(profile)) > 650:
         # False Safe incase the personality is to vibrant 
        return summary(traits, min_low,max_high)
    return profile


def five_progresss_bara_data(traits, p):
    """"
    This function takes in a the sub traits and the big 5 and 
    chooses 5 traits that I have decided to show to the user 
    they include:
    [ facet_anxiety, facet_friendliness, facet_moralit,Extraversion,facet_trust ]
    
    arg: dict, dict
    return : list

    """
    extrovert = 0
    # Extract personality feature from data frame
    personalities = p["personality"]
    # Get the big Four 
    result = {need['name']:round(need['percentile'],2) for need in personalities}
    extrovert = result['Extraversion']
    progress = list()
    progress.append(traits['facet_anxiety'])
    progress.append(traits['facet_friendliness'])
    progress.append(traits['facet_morality'])
    progress.append(extrovert)
    progress.append(traits['facet_trust'])
    progress_ret = format_return(progress)
    return progress_ret

def format_return(lis):
    ret_value = list()
    for i in lis:
        first = "width:"
        value = round(int(i*100),0)
        ele = first + str(value) + "%"
        ret_value.append(ele)
    return ret_value

def sub_interest(p):
    """"
    This function takes in a personality dictionary and returns the interst in 
    the form of a list
    {'facet_adventurousness': 0.95, 'facet_artistic_interests': 0.88}

    arg: dict from personality insight
    return : list

    """
    ret=list()
    for i in range(0,len(p)):
        k = p["consumption_preferences"][i]
        g = k["consumption_preferences"]
        for ele in g:
            if(ele['score']==1):
                ret.append(ele['name'])
        retu = []
        for inte in ret:
            if(inte in interest.keys()):
                retu.append(interest[inte])
    return retu
            




