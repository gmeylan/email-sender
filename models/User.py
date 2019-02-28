import hashlib
class User:

    first_name = ""
    last_name = ""
    department_number = ""
    telephone_number = ""
    email = ""

    def __init__(self, first_name, last_name, department_number, telephone_number, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.department_number = department_number
        self.telephone_number = telephone_number
        self.email = email
        self.password = hashlib.md5(password.encode()).hexdigest()

    def get_complete_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
