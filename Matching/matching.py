from tutors import *
from tutees import *

def intersection(lst1, lst2):
    # we'll assume lst1 and lst2 contain no duplicates
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def possible_match(t: Tutor, s: Tutee)->bool:

    if (len(intersection(t.available, s.available)) == 0):
        return False
    elif (len(intersection(t.subjects, s.subjects)) == 0):
        return False
    