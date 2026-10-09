import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    time: float
    slip_angle: float
    lateral_velocity: float = 0.0
    xpos: float = 0.0
    ypos: float = 0.0
    

time_step = 0.05

def step (state:State) -> State:
    forward_speed = 15
    cornering_stiffness = 36000
    mass = 300

    if state.time <= 3:
        steer_angle = state.time * 5/3
    elif state.time <= 10:
        steer_angle = 5.0
    else:
        steer_angle = 5.0

    steer_radians = steer_angle * np.pi / 180
    new_slip_angle = steer_radians - state.lateral_velocity/forward_speed
    new_lateral_force = cornering_stiffness * new_slip_angle
    new_lateral_acceleration = new_lateral_force/mass
    new_lateral_velocity = state.lateral_velocity + new_lateral_acceleration * time_step
    
    new_ypos = state.ypos + state.lateral_velocity * time_step
    new_xpos = state.xpos + forward_speed * time_step
    new_time = state.time + time_step

    return State(
        lateral_velocity = new_lateral_velocity,
        slip_angle = new_slip_angle,
        time = new_time,
        xpos = new_xpos,
        ypos = new_ypos,
    )

def animate (i):
    global s0
    s0 = step(s0)
    ax.clear()
    ax.scatter([s0.xpos],[s0.ypos],s = 700, c = "pink", marker = 's')
    ax.set_xlim(0,300)
    ax.set_ylim(0,10)
    return ax

s0 = State(
    time = 0.0,
    slip_angle = 0.0,
    lateral_velocity = 0.0,
    xpos = 0.0,
    ypos = 0.0
)


fig = plt.figure(figsize=(3,3), dpi=200)
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
# these lines are so the animation doesnt zoom in or out
plt.pause(3)
ani = animation.FuncAnimation(fig, animate, interval=20)
plt.show()
