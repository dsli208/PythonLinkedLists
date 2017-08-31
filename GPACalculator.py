class ClassNode(object):
    def __init__(self, className, credits, grade):
        self.course = Course(className, credits,grade)
        self.nextClassNode = None
    def __init__(self, course):
        self.course = course
        self.nextClassNode = None

    def getCourse(self):
        return self.course

    def getNextClass(self):
        return self.nextClassNode

    def setClassName(self, newClassName):
        self.course.className = newClassName

    def setCredits(self, newCredits):
        self.course.credits = newCredits

    def setGrade(self, newGrade):
        self.course.grade = newGrade

class Course(object):
    def __init__(self, className, credits, grade):
        self.className = className
        self.credits = credits
        self.grade = grade


class CourseList(object): #Linked list type data structure
    def __init__(self):
        self.firstCourseNode = None
        self.lastCourseNode = None

    def addCourse(self, className, credits, grade):
        newCourse = Course(className, credits, grade)
        newCourseNode = ClassNode(newCourse)
        if (self.firstCourseNode == None):
            self.firstCourseNode = newCourseNode
        else:
            traverseCourseNode = self.firstCourseNode
            while (traverseCourseNode.getNextClass() != None):
                traverseCourseNode = traverseCourseNode.getNextClass()
            traverseCourseNode.nextClassNode = newCourseNode

    def getCourse(self, className):
        traverseNode = self.firstCourseNode
        while (traverseNode != None):
            if (traverseNode.course.className == className):
                return traverseNode.course
        return None # modify for exception handling in Python?

    def getCourseNode(self, className):
        traverseNode = self.firstCourseNode
        while (traverseNode != None):
            if (traverseNode.course.className == className):
                return traverseNode
        return None  # modify for exception handling in Python?

    def editCourse(self, className, credits, grade):
        courseToEdit = self.getCourse(className)
        if (courseToEdit != None):
            courseToEdit.className = className
            courseToEdit.credits = credits
            courseToEdit.grade = grade

    def removeCourse(self, className, credits, grade):
        courseToRemove = self.getCourseNode(className)
        if (courseToRemove != None):
            traverseNode = self.firstCourseNode
            while (traverseNode.nextClassNode != courseToRemove):
                traverseNode = traverseNode.nextClassNode
            traverseNode.nextClassNode = courseToRemove.nextClassNode