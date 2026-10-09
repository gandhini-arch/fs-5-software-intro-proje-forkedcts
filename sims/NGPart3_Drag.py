import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    net_acceleration: float
    drag: float
    time: float
    velocity: float
    xpos: float = 0.0


time_step = 0.05


def step (state:State) -> State:
    mass = 300
    cross_sectional_area = 1.2
    drag_coefficient = 0.7
    air_density = 1.2

    if state.time <= 10.0:
        acceleration = 5.0
    else:
        acceleration = 0.0


    new_drag = 0.5 * cross_sectional_area * drag_coefficient * air_density * state.velocity**2
    new_net_acceleration = acceleration - new_drag/mass
    new_velocity = state.velocity + new_net_acceleration * time_step

    new_xpos = state.xpos + state.velocity * time_step
    new_time = state.time + time_step

    return State(
        net_acceleration = new_net_acceleration,
        velocity = new_velocity,
        time = new_time,
        drag = new_drag,
        xpos = new_xpos
    )

def animate(i):
    global s0
    s0 = step(s0)
    ax.clear()
    ax.scatter([s0.xpos], [0], s=700, c="pink", marker='s')
    ax.set_xlim(0, 300)
    ax.set_ylim(-2, 2)
    return ax


s0 = State(
    net_acceleration = 0.0,
    drag = 0.0,
    time = 0.0,
    velocity = 0.0,
    xpos = 0.0
)


fig = plt.figure(figsize=(3,3), dpi=200)
ax = fig.add_subplot(111)
ax.grid()

ax.set_xlim(0, 300)
ax.set_ylim(-2, 2)

# these lines are so the animation doesnt zoom in or out
plt.pause(3)
ani = animation.FuncAnimation(fig, animate, interval=20)
plt.show()
