import datetime

global previous_log
previous_log = datetime.datetime.now()


def time_log(s):
    global previous_log
    eclipse = datetime.datetime.now() - previous_log
    previous_log = datetime.datetime.now()
    return print(
        datetime.datetime.now().strftime('--%Y-%m-%d %H:%M:%S.%f---') + str(eclipse) + '---' + str(s))
