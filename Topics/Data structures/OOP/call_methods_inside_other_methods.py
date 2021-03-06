"""
    Chamar um método dentro de outro
"""
import datetime
class Person:
    def __init__(self, name, photo, date_of_birth):
        self.name = name
        self.photo = photo
        self.dob = date_of_birth
    
    def get_age(self):
        return int((datetime.datetime.now() - self.dob).days / 365.25)

    # dentro deste método, chamar o outro método
    def __str__(self):
        return self.name + ', age ' + str(self.get_age()) # aqui chamo o método get_age()