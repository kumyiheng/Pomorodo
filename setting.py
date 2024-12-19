import json

def pomodoro_set(work, short, long,circulation):
    f = open("pomodoro_setting.json")
    data = json.load(f)
    data["pomodoro time"] = float(work)
    data["short break time"] = float(short)
    data["long break time"] = float(long)
    data["circulation"] = int(circulation)
    f = open("pomodoro_setting.json",'w')
    json.dump(data,f)
