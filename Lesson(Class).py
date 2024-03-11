class Lesson:

    #PRIVATE LessonType : STRING
    #PRIVATE Instructor : STRING

    def __init__(self, LessonType:str, Instructor:str) -> None:
        self.__LessonType = LessonType
        self.__Instructor = Instructor
    
    
    def GetLessonType(self) -> str:
        return self.__LessonType
    

    def GetInstructor(self) -> str:
        return self.__Instructor


    def GetFee(self, Level:str) -> int:
        if Level == 'B':
            return 45
        elif Level == 'I':
            return 50
        elif Level == 'A':
            return 55
        return -1
    

    def SetLessonType(self, LessonTypeIn:str) -> None:
        self.__LessonType = LessonTypeIn
    

    def SetInstructor(self, InstructorIn:str) -> None:
        self.__Instructor = InstructorIn

# Psudeocode to declare an array LessonArray to store nine lesson objects
# DECLARE LessonArray : ARRAY[0:8] OF Lesson

LessonArray = ['', '', '', '', '', '', '', '', '']

LessonArray[2] = Lesson('Improve Your Serve', 'David')

print(LessonArray[2].GetInstructor())

print(LessonArray[2].GetFee('A'))



