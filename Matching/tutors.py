
class Tutor:
    """
    A class to represent a tutor applicant. Includes attributes inputted as:
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
        self.name = inputLst[0]
        self.year = int(inputLst[1])
        self.email = inputLst[2]
        self.phone = inputLst[3]

        subjects = inputLst[4]
        sblst = subjects.split(",")
        sbdict = {}
        for i in range(len(sblst)):
            if (i % 2 != 0):
                continue
            else:
                sbdict[sblst[i]] = int(sblst[i+1])
        
        self.subjects = sbdict
        grades = inputLst[5]
        self.grades = grades.split(",")
        availablity = inputLst[6]
        self.available = availablity.split(",")
    
    def num_subjects(self):

        return len(self.subjects.keys())
    
    def can_tutor(self, subj: str) -> bool:

        assert(subj in self.subjects.keys())
        return (not (self.subjects[subj] == 0))
    
    def available_on(self, day:str) -> bool:

        return (day in self.available)
    
    def ok_grades(self):
        res = []
        for range in self.grades:
            low = int(range[0])
            high = int(range[2])
            for grade in range(low, high+1):
                if grade not in res:
                    res.append(grade)
        return res

def makeTutor(inputLst):
    if len(inputLst) == 7:
        return Tutor(inputLst)
    else:
        return None



        
