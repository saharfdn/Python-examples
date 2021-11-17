class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.total_second = 0

    def time_to_int(self):
        self.total_second = self.hour * 3600 + self.minute * 60 + self.second
        return self.total_second

    @classmethod
    def int_to_time(cls, seconds):
        hour = seconds // 3600
        minute = (seconds % 3600) // 60
        second = (seconds % 3600) % 60
        return cls(hour, minute, second)

    # def __add__(self, other):
    #     hour = self.hour + other.hour
    #     minute = self.minute + other.minute
    #     second = self.second + other.second
    #     return f"{hour}:{minute}:{second}"
    def add_time(self, time):
        seconds = self.time_to_int() + time.time_to_int()
        time2 = Time.int_to_time(seconds)
        return f"time is {time2}"

    def __repr__(self):
        return f"{self.hour}:{self.minute}:{self.second}"

t1 = Time(4,50,10)
t2 = Time(1,37,25)
print(t1.add_time(t2))
