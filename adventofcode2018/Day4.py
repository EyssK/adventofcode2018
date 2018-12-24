import re
from datetime import datetime, timedelta

pattern_date = re.compile(r"\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\]")
pattern_wake = re.compile(r"wakes up")
pattern_sleep = re.compile(r"falls asleep")
pattern_change = re.compile(r"Guard #(\d+) begins shift")

test_lines = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""


def search_info(s):
    change = pattern_change.search(s)
    wake = pattern_wake.search(s)
    sleep = pattern_sleep.search(s)
    cur_date = [int(x) for x in pattern_date.search(s).group(1, 2, 3, 4, 5)]
    if change:
        return {'cmd': "c", 'g': int(change.group(1)), 'date': datetime(*cur_date)}
    elif wake:
        return {'cmd': "w", 'date': datetime(*cur_date)}
    elif sleep:
        return {'cmd': "s", 'date': datetime(*cur_date)}


with open("Day4input.txt") as file:
    lines = sorted([x for x in map(search_info, file.read().splitlines())], key=lambda elem: elem['date'])
    # lines = sorted([x for x in map(search_info, test_lines.splitlines())], key=lambda elem: elem['date'])
    total = {}
    for log in lines:
        if log['cmd'] == 'c':
            cur_guard = log['g']
        elif log['cmd'] == 's':
            cur_start = log['date']
        elif log['cmd'] == 'w':
            cur_log = total.setdefault(cur_guard, {"delta": timedelta(0), "sched": []})
            cur_log["delta"] += log['date'] - cur_start
            cur_log["sched"] += range(cur_start.minute, log['date'].minute)

# find the highest delta
res = max(zip(total.values(), total.keys()), key=lambda elem: elem[0]["delta"])
# find the highest count in sched
print("part1 :", res[1] * max(set(res[0]["sched"]), key=res[0]["sched"].count))

for guard in total.items():
    # find the minute with the highest count in sched
    total[guard[0]]["minute"] = max(set(guard[1]["sched"]), key=guard[1]["sched"].count)
    # count the number of occurrence of this minute
    total[guard[0]]["freq"] = guard[1]["sched"].count(total[guard[0]]["minute"])
# find the guard with the highest number of minute occurrence
res = max(zip(total.values(), total.keys()), key=lambda elem: elem[0]["freq"])
print("part2 :", res[1] * res[0]["minute"])
