from stl import mesh
from numpy import linalg
import atexit
import pulse

your_mesh = mesh.Mesh.from_file('stl/circle.stl')
print("just use y and z")
last = None
ticks = 50000


def end():
    pulse.cleanup()


atexit.register(end)

def tick_rate(val):
    # e.g. y should move every 20 ticks
    if val == 0:
        return -1

    return int(ticks / val)


def move(movedict):
    y_rate = tick_rate(movedict['y'])
    z_rate = tick_rate(movedict['z'])

    pulse.dir_y(y_rate > 0)
    pulse.dir_z(z_rate > 0)

    for i in range(ticks):
        if y_rate != -1 and i % y_rate == 0:
            pulse.pulse_y()

        if z_rate != -1 and i % z_rate == 0:
            pulse.pulse_z()

for face in your_mesh.vectors:
    for v in face:
        if last is None:
            last = v
            continue

        towards = {'y': v[1]-last[1], 'z': v[2]-last[2], 'distance': linalg.norm(v-last)}
        move(towards)
        print(towards)
