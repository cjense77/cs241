import math

class Time:
    def __init__(self):
        self._hours = 0.0
        self._minutes = 0.0
        self._seconds = 0.0

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if hours < 0:
            hours = 0
        elif hours > 23:
            hours = 23
        self._hours = hours

    hours = property(get_hours, set_hours)

    def get_minutes(self):
        return self._minutes

    def set_minutes(self, minutes):
        if minutes < 0:
            minutes = 0
        elif minutes > 59:
            minutes = 59
        self._minutes = minutes

    minutes = property(get_minutes, set_minutes)

    def get_seconds(self):
        return self._seconds

    def set_seconds(self, seconds):
        if seconds < 0:
            seconds = 0
        elif seconds > 59:
            seconds = 59
        self._seconds = seconds

    seconds = property(get_seconds, set_seconds)

    @property
    def hours_simple(self):
        if self._hours == 12:
            return 12
        else:
            return self._hours % 12

    @property
    def period(self):
        if self._hours < 12:
            return 'AM'
        else:
            return 'PM'

class Time2:
    def __init__(self):
        self._seconds = 6400

    def get_hours(self):
        return math.floor(self._seconds / 60.0 / 60.0)

    def set_hours(self, hours):
        if hours < 0:
            hours = 0
        elif hours > 23:
            hours = 23
        self._hours = hours

    hours = property(get_hours, set_hours)

    def get_minutes(self):
        return math.floor(self._seconds / 60.0 % 60)
    def set_minutes(self, minutes):
        if minutes < 0:
            minutes = 0
        elif minutes > 59:
            minutes = 59
        self._minutes = minutes

    minutes = property(get_minutes, set_minutes)

    def get_seconds(self):
        return self._seconds % 60

    def set_seconds(self, seconds):
        if seconds < 0:
            seconds = 0
        elif seconds > 59:
            seconds = 59
        self._seconds = seconds

    seconds = property(get_seconds, set_seconds)

    @property
    def hours_simple(self):
        if self._hours == 12:
            return 12
        else:
            return self._hours % 12

    @property
    def period(self):
        if self._hours < 12:
            return 'AM'
        else:
            return 'PM'

def main():
    # t1 = Time()
    # hours = int(input('Enter hours: '))
    # t1.hours = hours
    #
    # minutes = int(input('Enter minutes: '))
    # t1.minutes = minutes
    #
    # seconds = int(input('Enter seconds: '))
    # t1.seconds = seconds
    #
    # print('The time is {}:{}:{}'.format(t1.hours,
    #                                     t1.minutes,
    #                                     t1.seconds))
    # print('Simple time is {}:{}:{} {}'.format(t1.hours_simple,
    #                                           t1.minutes,
    #                                           t1.seconds,
    #                                           t1.period))

    t2 = Time2()
    print('The time is {}:{}:{}'.format(t2.hours,
                                        t2.minutes,
                                        t2.seconds))

if __name__ == '__main__':
    main()