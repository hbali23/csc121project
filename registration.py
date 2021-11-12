#
# This is what I have in mind in regards to the layout of the main module
#


class Registration:
    def __init__(self): 
        pass


    def add_course(self, id, c_roster, c_max_size): #this is mefake123 writing this
        # ------------------------------------------------------------
        # This function adds a student to a course.  It has three
        # parameters: id is the ID of the student to be added; c_roster is the
        # list of class rosters; c_max_size is the list of maximum class sizes.
        # This function asks user to enter the course he/she wants to add.
        # If the course is not offered, display error message and stop.
        # If student has already registered for this course, display
        # error message and stop.
        # If the course is full, display error message and stop.
        # If everything is okay, add student ID to the course’s
        # roster and display a message if there is no problem.  This
        # function has no return value.
        pass


    def drop_course(self, id, c_roster):
        # ------------------------------------------------------------
        # This function drops a student from a course.  It has two
        # parameters: id is the ID of the student to be dropped;
        # c_roster is the list of class rosters. This function asks
        # the user to enter the course he/she wants to drop.  If the course
        # is not offered, display error message and stop.  If the student
        # is not enrolled in that course, display error message and stop.
        # Remove student ID from the course’s roster and display a message
        # if there is no problem.  This function has no return value.
       pass


    def list_courses(self, id, c_roster):
        # ------------------------------------------------------------
        # This function displays and counts courses a student has
        # registered for.  It has two parameters: id is the ID of the
        # student; c_roster is the list of class rosters. This function
        # has no return value.
        pass


    def calculate_hours_and_bill(self, id, s_in_state, c_rosters, c_hours):
        # ------------------------------------------------------------
        # This function calculate billing information. It takes four
        # parameters: id, the student id; s_in_state, the list of
        # in-state students; c_rosters, the rosters of students in
        # each course; c_hours, the number of hours in each course.
        # This function returns the number of course hours and tuition
        # cost.
        pass


    def display_hours_and_bill(self, hours, cost):
        # ------------------------------------------------------------
        # This function prints the number of course hours the student
        # is taking and the total tuition cost. It takes two parameters:
        # hours and cost. This function has no return value.
        pass


    def login(self, id, s_list):
        # ------------------------------------------------------------
        # This function allows a student to log in.
        # It has two parameters: id and s_list, which is the student
        # list. This function asks user to enter PIN. If the ID and PIN
        # combination is in s_list, display message of verification and
        # return True. Otherwise, display error message and return False.
        pass
