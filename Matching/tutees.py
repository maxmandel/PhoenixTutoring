
class Tutee:
    """
    A class to represent tutees enrolled in Phoenix Tutoring.
    """

    def __init__(self, inputLst):
        self.name = inputLst[0]
        self.grade = int(inputLst[1])
        self.prtEmail = inputLst[2]
        if inputLst[3] == " ":
            self.stEmail is None
        else:
            self.stEmail = inputLst[3]
        
