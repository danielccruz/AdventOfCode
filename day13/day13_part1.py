notes = [line.rstrip('\n') for line in open('../day13/input_file.txt')]

target = int(notes[0])
bus_ids = [int(x) for x in notes[1].split(',') if x.isdigit()]

time = 1

calendar = {}
looking_for_bus = False
while True:
    if time >= target:
        looking_for_bus = True
    for bus_id in bus_ids:
        if time % bus_id == 0:
            calendar[time] = 1
            if looking_for_bus:
                print(bus_id*(time-target))
                exit()
        else:
            calendar[time] = 0
    time += 1
