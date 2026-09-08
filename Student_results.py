"""A small student-results program using MVC architecture."""


# Model: stores the data and applies the result rule.
class StudentModel:
    def __init__(self):
        self.marks = {"Osama": 85, "Ali": 40}

    def get_result(self, name):
        mark = self.marks[name]
        status = "Pass" if mark >= 50 else "Fail"
        return name, mark, status


# View: only displays the information it receives.
class StudentView:
    def show_result(self, name, mark, status):
        print(f"{name}: {mark}/100 - {status}")


# Controller: receives the request and connects the Model to the View.
class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def display_student(self, name):
        result = self.model.get_result(name)
        self.view.show_result(*result)



model = StudentModel()
view = StudentView()
controller = StudentController(model, view)

controller.display_student("Osama")
controller.display_student("Ali")
