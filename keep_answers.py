
# @bendog - extending the class of dict is a bit redundant, i like that you're doing it, but it might be a bit much.

class answer_dictionary(dict):
    # __init__ function
    def __init__(self):
        self = dict()
        # Function to add key:value

    def add(self, key, value):
        self[key] = value
