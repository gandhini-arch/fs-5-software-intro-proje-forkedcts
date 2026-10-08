import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    velocity: float = 25
    braking_force: float
    acceleration: float
    time: float
    xpos: float
    ypos: float

time_step = 0.01

def step (state:State) -> State:
    max_braking_capacity = 1850
    mass = 300

    if state.time <= 2.0:
        driver_input = 0.0
    else:
        driver_input = 1.0

    new_braking_force = driver_input * max_braking_capacity
    new_acceleration = state.acceleration - (new_braking_force/mass)
    new_velocity = state.velocity + (new_acceleration * time_step)

    new_xpos = state.xpos + state.velocity * time_step
    new_ypos = state.ypos
    
    new_time = state.time + time_step
    
    return State(
        velocity = new_velocity,
        braking_force = new_braking_force,
        time = new_time,
        acceleration = new_acceleration
    )
    

def animate (i):
    global s0
    s0 = step(s0)
    ax.clear()
    ax.scatter([s0.xpos],[s0.ypos],s = 700, c = "pink", marker = 's')
    ax.set_xlim(0,300)
    ax.set_ylim(0,10)
    return ax

s0 = state(
    xpos = 0
    ypos = 0
    time = 0
    velocity = 0
    braking_force = 0
    acceleration = 0
)

    


fig = plt.figure(figsize=(3,3), dpi=150)
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
# these lines are so the animation doesnt zoom in or out
plt.pause(3)
ani = animation.FuncAnimation(fig, animate, interval=0)
plt.show()
