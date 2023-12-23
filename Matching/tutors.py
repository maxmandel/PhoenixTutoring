
# type inputList = list[str]

class Tutor:
    """
    A class to represent a tutor applicant. 
    
    Includes attributes inputted as:
    inputLst: List[str]
    - Name: str
    - Year: str
    - Email: str
    - Phone# (optional): str
    - Subject comfort: str
    - Grade tutoring comfort: str
    - Availability: str

    These will be converted as follows:

    - Name: str
    - Year: int
    - Email: str
    - Phone# (optional): str
    - Subject comfort: dict{str:int}
    - Grade tutoring comfort: List[int]
    - Availability: List[str]
    """

    def __init__(self, inputLst):
        self.name = inputLst[0] # str name
        self.year = int(inputLst[1]) # int year (can compare w/ others via <>=)
        self.email = inputLst[2] # str email (to be used for contact info directory)
        self.phone = inputLst[3] # ^

        subjects = inputLst[4]
        sblst = subjects.split(",") # list: [subj1, ranking1, s2, r2, ...]
        sbdict = {}
        for i in range(len(sblst)):
            if (i % 2 != 0):
                continue
            else:
                sbdict[sblst[i]] = int(sblst[i+1]) # subject-ranking dictionary
        self.subjects = sbdict

        grades = inputLst[5].split(",")
        glst = []
        for group in grades: # e.g. "1-4"
            a = int(group[0]) # int("1") = 1
            b = int(group[2]) # int("4") = 4
            for gval in range(a, b+1):
                if gval not in glst:
                    glst.append(gval)
        self.grades = glst # e.g. ["1-4", "9-12"] -> [1, 2, 3, 4, 9, 10, 11, 12]

        availablity = inputLst[6]
        self.available = availablity.split(",")
    
    def num_subjects(self):

        return len(self.subjects.keys())
    
    def can_tutor(self, subj: str) -> bool:
        # make sure we're checking a real subject
        assert(subj in self.subjects.keys())
        return (not (self.subjects[subj] == 0))
    
    def available_on(self, day:str) -> bool:

        return (day in self.available)

def makeTutor(inputLst):
    """
    Inputs:
        inputLst: List[str]
    Returns: Tutor

    Creates a Tutor object from a legitimate input list, otherwise returns None.
    """
    if len(inputLst) == 7:
        return Tutor(inputLst)
    else:
        return None
    
def makeTutors(inputLsts):
    """
    Inputs:
        inputLsts: List[List[str]]
    Returns: List[Tutor]

    Takes a list of legitimate input lists and produces a list of tutor objects.
    """
    lstTuts = []
    for il in inputLsts:
        lstTuts.append(makeTutor(il))
    return lstTuts




        
