class Event:
    def __init__(self, name, start, end, date):

        self.name = name
        self.start = start
        self.end = end
        self.date = date

    def as_dict(self):
        return {'name': self.name, 'start_time': self.start, 'end_time': self.end, 'date': self.date}
