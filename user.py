class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print('Personal Details:\n')
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Gender: ', self.gender)

