from course import Course
from courselist import CourseList
import csv


def load_courses():
    file = "G:\\development\\CS2420\\projectThree\\data.txt"
    courses = []
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            courses.append(Course(int(row[0]), row[1], float(row[2]), float(row[3])))

    return courses


def main():
    my_courses = load_courses()
    course_list = CourseList()
    for course in my_courses:
        course_list.insert(Course(course.course_number, course.course_name, course.course_credit_hr,
                                  course.course_grade))

    for course in course_list:
        print(course)


if __name__ == "__main__":
    main()
