class Member:
    """A sample Member from ProjectKit class"""

    def __init__(self, name, address, phone_number, age, interests):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.age = age
        self.interests = interests

    @property
    def name(self):
        return ''.format(self.name)

    @property
    def address(self):
        return ''.format(self.address)

    @property
    def age(self):
        return ''.format(self.age)  

    @property
    def interests(self):
        return ''.format(self.interests)      

    # Contact information
    def __repr__(self):
        return "Member('{}', '{}', {})".format(self.name, self.phone_number, self.address)  