import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
  propulsion_force: float
  acceleration: float
  time: float
  velocity: float
  temperature: float
  heat_energy: float
  xpos: float
  ypos: float
     

time_step = 0.01

def step (state:State) -> State:
  max_propulsion_force = 2000
  vmax = 27
  mass = 300

  voltage = 400
  resistance = 0.5
  motor_mass = 50
  specific_heat = 385
    

  if state.time <= 3.0:
      throttle = state.time / 3.0
  elif state.time <= 23.0:
      throttle = 1.0
  else:
      throttle = 0.0


  propulsion_force = max_propulsion_force * throttle * (1 - (state.velocity/vmax))
  new_acceleration = propulsion_force / mass
  new_velocity = state.velocity + (new_acceleration * time_step)
  new_time = state.time + time_step
  
  current = voltage / resistance
  heat_power = current**2 * resistance
  heat_added = heat_power * time_step
  new_heat_energy = state.heat_energy + heat_added
  temperature_change = heat_added / (motor_mass * specific_heat)
  new_temperature = state.temperature + temperature_change

  new_xpos = state.xpos + state.velocity * time_step
  new_ypos = state.ypos

  return State(
    propulsion_force=propulsion_force,
    acceleration=new_acceleration,
    velocity=new_velocity,
    temperature=new_temperature,
    heat_energy=new_heat_energy,
    xpos = new_xpos,
    ypos = new_ypos,
    time=new_time
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
  propulsion_force= 0
  acceleration = 0
  velocity = 0
  temperature = 0
  heat_energy = 0
  time = 0
    
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


