
class Tutee:
    """
    A class to represent tutees enrolled in Phoenix Tutoring.

    Includes attributes inputted as:
    inputLst: List[str]
    - Parent Name
    - Parent Email
    - Tutee Name
    - Tutee Email (could be None)
    - Tutee Grade
    - Ranked List of Subjects
    - List of Available Times
    - Previous Tutor (could be None)
    - Misc Instructions (could be None)

    These will be converted as follows:
    - Parent Name: str
    - Parent Email: str
    - Tutee Name: str
    - Tutee Email: Optional[str]
    - Tutee Grade: int
    - Ranked Subjects: dict{str:int}
    - List Times: List[str]
    - Previous Tutors: Optional[str]
    - Misc Instructions: Optional[str]

    """

    def __init__(self, inputLst):

        self.prtname = inputLst[0]
        self.prtEmail = inputLst[1]
        self.stname = inputLst[2]
        self.stEmail = inputLst[3] # can be empty

        self.grade = int(inputLst[4])
        

        
    
def makeTutee(inputLst):
    if len(inputLst) == 9:
        return Tutee(inputLst)
    else:
        return None
