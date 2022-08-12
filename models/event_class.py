from datetime import date as dt


class Event:
    def __init__(self, name, description, repeat, date, location, max_guests):
        self.name = name
        self.description = description
        self.repeat = repeat
        self.date = self.get_date(date)
        self.location = location
        self.max_guests = max_guests
    
    
    def get_date(self, date):
        year, month, day = map(int, date.split("-"))
        return dt(year, month, day)