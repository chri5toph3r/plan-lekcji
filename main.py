import json


class Plan:

    def __init__(self):
        self.plan = {'Mon': {}, 'Tue': {}, 'Wen': {}, 'Thu': {}, 'Fri': {}}
        self.days = ['Mon', 'Tue', 'Wen', 'Thu', 'Fri']
        self.hours = {'normalna': ['8:00 – 8:45',
                                   '8:50 – 9:35',
                                   '9:45 – 10:30',
                                   '10:40 – 11:25',
                                   '11:40 - 12:25',
                                   '12:35 – 13:20',
                                   '13:30 – 14:15',
                                   '14:20 – 15:05',
                                   '15:10 – 15:55',
                                   '16:00 – 16:45',
                                   '16:50 – 17:35'],
                      'muzyczna': ['15:40 – 16:25',
                                   '16:30 – 17:15',
                                   '17:20 – 18:05',

                                   '17:15 – 18:00',

                                   '16:00 – 17:30',
                                   '17:30 – 18:15',
                                   '18:15 – 18:45']}
        self.subjects = {'normalna': ['matematyka', 'j. polski', 'systemy serwerowe', 'sieci komputerowe',
                                      'projektowanie stron internetowych'],
                         'muzyczna': ['saksofon', 'fortepian', 'kształcenie słuchu', 'zasady muzyki',
                                      'literatura muzyczna']}
        self.classrooms = {'normalna': [], 'muzyczna': []}

    def write_plan(self):
        for day in self.plan:
            print(day)
            for hour in self.plan[day]:
                print(f'{hour} | {self.plan[day][hour][0]} ({self.plan[day][hour][1]})')

    def write_in_plan(self, day, hour, subject, classroom):
        if type(hour) is tuple:
            for h in hour:
                self.plan[day][h] = (subject, classroom)
        else:
            self.plan[day][hour] = (subject, classroom)
        return

    def read_plan(self):
        with open('plan_lekcji.txt') as plan_file:
            plan_str = plan_file.read()
        self.plan = json.loads(plan_str)
        return

    def save_plan(self):
        with open('plan_lekcji.txt', 'w') as plan_file:
            plan_file.write(json.dumps(self.plan))
        return


if __name__ == '__main__':
    plan = Plan()
    flag = True
    while flag:
        exec(input(': '))

