import json

class Event:
    def __init__(self, titulo, horario_inicio, horario_fim):

        self.titulo = titulo
        self.horario_inicio = horario_inicio
        self.horario_fim = horario_fim

    def as_dict(self):
        return {'titulo': self.titulo, 'horario_inicio': self.horario_inicio, 'horario_fim': self.horario_fim}

def sort_by_finish_time(agenda):
    # Ordena eventos por ordem de término e transforma em dicionário
    event_objects = []
    for i in agenda:
        event_objects.append(Event(i['titulo'], i['horario_inicio'], i['horario_fim']))
    
    sorted_events = sorted(event_objects, key=lambda event: event.horario_fim)
    sorted_events_as_dicts = [event.as_dict() for event in sorted_events]
    
    return sorted_events_as_dicts

def find_best_schedule(agenda):
    # Encontra os melhores horário levendo em consideração o menor tempo de ócio
    sorted_events = sort_by_finish_time(agenda)
    best_programming = []

    for event in sorted_events:
        if best_programming:
            if best_programming[-1]['horario_fim'] <= event['horario_inicio']:
                best_programming.append(event)
        else:
            best_programming.append(event)
    return best_programming

def get_data(day):
    with open('./debconf/schedule.json', 'r') as fp:
        data_json = json.load(fp)
    
    return find_best_schedule(data_json[day])
