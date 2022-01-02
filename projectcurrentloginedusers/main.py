def get_event_date(event):
    return event.date


def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines


def generte_report(machines):
    for machine, user in machines.items():
        if len(users) > 0:
            user_list = ", ".join(user)
            print("{}: {}".format(machine, user_list))


class event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user
events = [
    event('2021-3-2 12:56', 'login', "myworkstation", "acesp"),
    event('2021-3-2 12:57', 'login', "mailserver", "acesps"),
    event('2021-3-2 12:58', 'login', "myworkstation", "acesp"),
    event('2021-3-2 12:59', 'logout', "myworkstation", "acesp"),
    event('2021-3-2 13:00', 'login', "myworkstation", "acesp")
]

users = current_users(events)
print(users)
print(generte_report(users))