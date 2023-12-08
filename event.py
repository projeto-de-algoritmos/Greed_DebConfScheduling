class Event:
    def __init__(self, name, start, end, date):

        self.name = name
        self.start = start
        self.end = end
        self.date = date

    def as_dict(self):
        return {'name': self.name, 'start_time': self.start, 'end_time': self.end, 'date': self.date}


def sort_by_finish_time(agenda):
    # Ordena eventos por ordem de término e transforma em dicionário
    event_objects = []
    for i in agenda:
        event_objects.append(Event(i['titulo'], i['horario_inicio'], i['horario_fim'], i['data']))
    
    sorted_events = sorted(event_objects, key=lambda event: event.end)
    sorted_events_as_dicts = [event.as_dict() for event in sorted_events]
    
    return sorted_events_as_dicts
