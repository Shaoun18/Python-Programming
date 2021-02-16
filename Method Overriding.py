class phone:
    def __init__(self):                  # constructor
        print("I am in my class")

class samsung(phone):
    def __init__(self):
        super().__init__()
        print("I am a CSE student")

s = samsung()