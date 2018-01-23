class SMS:
    def __init__(self, number, time, message):
        self.has_been_viewed = False
        self.from_number = number
        self.time_arrived = time
        self.text_of_SMS = message

    def get_SMS(self):
        print("NUMBER: {0} \t | TIME: {1} \t | TEXT: {2}".format(self.from_number, self.time_arrived, self.text_of_SMS))

    def get_has_been_viewed(self):
        return self.has_been_viewed

    def set_has_been_viewed(self, value):
        self.has_been_viewed = value

