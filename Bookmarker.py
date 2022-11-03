import datetime


def convert_time(unformated_time):
    list_of_times = []
    time_in_seconds = []

    for i in unformated_time:
        list_of_times.append(i.split(':'))

    for time in list_of_times:
        if len(time) == 1:
            time_in_seconds.append(int(time[0]))
        elif len(time) == 2:
            time_in_seconds.append(int(time[0]) * 60 + int(time[1]))
        elif len(time) == 3:
            time_in_seconds.append(
                int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2]))
    return time_in_seconds


splitted = []
formatted_time = []
unformated_time = []
bookmark_name = []


with open("test.txt", "r") as f:
    for line in f:
        splitted.append(line.strip().split(" ", 1))


for entry in splitted:
    unformated_time.append(entry[0])
    bookmark_name.append(entry[1])

time_in_seconds = convert_time(unformated_time)


with open("bookmarks.txt", "w") as f:
    for time, name in zip(time_in_seconds, bookmark_name):
        f.write("bookmarks={name=%s,time=%s}," % (name, time))
