from tutors import *
from tutees import *

def intersection(lst1, lst2):
    # we'll assume lst1 and lst2 contain no duplicates
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def possible_match(t: Tutor, s: Tutee)->bool:
    """
    Checks if there's any availability and subject overlap. If there is, returns 
    a tuple of lists of the overlapping times and subjects, otherwise returns 
    False.
    """

    poss_times = intersection(t.available, s.available)
    poss_subjects = intersection(t.allsubjects, s.allsubjects)

    if (len(poss_times) == 0):
        return False
    elif (len(poss_subjects) == 0):
        return False
    
    return (poss_times, poss_subjects)

def no_match(ts, ss):
    """
    Considering lists of tutors and tutees, determines if there is any one tutee
    who does not "cleanly" match with any tutors.
    ts: List[Tutor]
    ss: List[Tutee]
    """
    no_matches = []
    for s in ss:
        counter = 0
        for t in ts:
            if type(possible_match(t, s)) == tuple:
                counter += 1
                break
        if counter == 0:
            no_matches.append(s)
