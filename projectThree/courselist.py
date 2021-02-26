class CourseList:
    """Ordered Link list of courses"""
    def __init__(self):
        """Constructor for the linked list"""
        self.head = None
        self.last = None
        self.count = 0

    def __iter__(self):
        """To help iterate through the list"""
        self.current_iter = None
        return self

    def __next__(self):
        """Helper function for __iter__"""
        if self.current_iter is None:
            self.current_iter = self.head
        elif self.current_iter.next is None:
            raise StopIteration()
        else:
            self.current_iter = self.current_iter.next
        return self.current_iter

    def insert(self, course):
        """Inserts a course sorted by the course number"""
        if self.head is None:
            self.head = self.last = course
        elif self.last.course_number < course.course_number:
            self.last = self.__set_links(self.last, course, None)
        elif self.head.course_number >= course.course_number:
            self.head = self.__set_links(None, course, self.head)
        else:
            current = self.head
            while current.course_number < course.course_number:
                current = current.next
            self.__set_links(current.prev, course, current)
        self.count += 1

    def remove(self, number):
        """Removes a course from the list"""
        if number <= self.last.course_number or number >= self.head.course_number:
            current = self.head
            while current.course_number != number and current.next is not None:
                current = current.next
            if current.course_number == number:
                self.__remove_item(current)

    def remove_all(self, number):
        """Removes all courses from the list"""
        current = self.head
        while current.next is not None:
            if current.course_number == number:
                self.__remove_item(current)
            current = current.next

    def find(self, number):
        """Finds a course number and returns the index"""
        index = 0
        if number <= self.last.course_number or number >= self.head.course_number:
            current = self.head
            while current.course_number != number and current.next is not None:
                current = current.next
                index += 1
            if current.course_number == number:
                return current
        return -1

    def size(self):
        """Returns the size of the list"""
        result = 0
        if self.head is None:
            return result

        item = self.head
        result += 1
        while item.next is not None:
            item = item.next
            result += 1
        return result

    def calculate_gpa(self):
        """Calculates the GPA for all courses"""
        result = 0
        grades = 0
        total_credits = 0
        if self.head is None:
            return result

        item = self.head
        while item.next is not None:
            grades += item.course_grade * item.course_credit_hr
            total_credits += item.course_credit_hr
            item = item.next
        if item.next is None:
            grades += item.course_grade * item.course_credit_hr
            total_credits += item.course_credit_hr

        result = (grades / total_credits)

        return result

    def is_sorted(self):
        """Checks the list to make sure it's ordered"""
        flag = True
        if self.head is None:
            return flag

        item = self.head
        item_two = self.head.next
        while item.next is not None:
            if item.course_number > item_two.course_number:
                flag = False
            item = item_two
            item_two = item_two.next
        return flag

    def __remove_item(self, current):
        """Helper function for removing an item"""
        if current == self.head:
            self.head = current.next
        if current == self.last:
            self.last = current.prev
        self.__set_links(current.prev, None, current.next)
        self.count -= 1

    def __set_links(self, before, item, after):
        """Helper function to set up the links between courses"""
        if item is None:
            if before is not None:
                before.next = after
            if after is not None:
                after.prev = before
        else:
            if before is not None:
                before.next = item
            if after is not None:
                after.prev = item
            item.prev = before
            item.next = after

        return item
