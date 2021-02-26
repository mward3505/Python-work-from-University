class Course:
    """This class is to create a course object to be used in a list"""
    def __init__(self, number=0, name="", credit_hr=0.0, grade=0.0):
        """Constructor to build the course"""
        if not isinstance(number, int) or number < 0:
            raise ValueError
        self.course_number = number
        if isinstance(name, str):
            self.course_name = name
        else:
            raise ValueError
        if not isinstance(credit_hr, float) or credit_hr < 0:
            raise ValueError
        self.course_credit_hr = credit_hr
        if not isinstance(grade, float) or grade < 0:
            raise ValueError
        self.course_grade = grade
        self.next = None
        self.prev = None

    def name(self):
        """Returns course name which should be a string"""
        return self.course_name

    def number(self):
        """Returns the course number and should be an integer"""
        return self.course_number

    def credit_hr(self):
        """Returns the course credit hours for the course and should be a float"""
        return self.course_credit_hr

    def grade(self):
        """"Returns the course grade and should be a float"""
        return self.course_grade

    def __str__(self):
        """Outputs the course"""
        return f"{self.number()} {self.name()} Grade:{self.grade()} Credit Hours: {self.credit_hr()}"
