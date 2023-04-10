# A bouncing ball simulation -- educational implementation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define physical constants, initial conditions, simulation parameters
g = 9.8   # acceleration due to gravity in m/s^2
y0 = 10.0; v0 = 0.0 # drop the ball from 10 m
r_ball = 0.5 # radius of ball

# Initialize the time, height, and velocity, and vectors
t = [0.0]
y = [y0]
v = [v0]

def bounce_ball(T_end, dt):
    """Bounce a ball."""

    # Run the simulation a fixed duration
    while t[-1] < T_end:
        # Beginning of time step
        y_i = y[-1]
        v_i = v[-1]

        # Forward euler step
        y_f = y_i + v_i*dt
        v_f = v_i - g*dt

        # Bounce event
        if (y_f - r_ball) <= 0.0:
            y_f = r_ball + 1e-15
            v_f = -v_f

        # State update (update in place, no return necessary)
        y.append(y_f)
        v.append(v_f)
        t.append(t[-1] + dt)

def _reset():
    t.clear(); t.append(0.0)
    y.clear(); y.append(10.0)
    v.clear(); v.append(0.0)

def plot_bounce(t, y, v):
    """Plot output of bouncy ball simulation."""

    fig = plt.figure()
    ax1 = plt.gca()

    plt.plot(t, y, 'b-', label='height')
    plt.xlabel('time [s]')
    plt.ylabel('ball height [m]', color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    ax2 = ax1.twinx()
    plt.plot(t, v, 'r--', label='velovity')
    plt.ylabel('ball velocity [m/s]', color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    plt.show(block=True)

def animate_bounce(t, y, r_ball):
    """Animate output of boncy ball simulation."""

    fig = plt.figure()
    ax1 = plt.gca()

    th = np.linspace(-np.pi, np.pi)
    bx = np.cos(th)*r_ball
    by = np.sin(th)*r_ball
    ball, = plt.plot(bx, by + y[0])

    plt.xticks([], [])
    plt.ylabel('height [m]')
    plt.axis('scaled')
    plt.ylim(0, 12)

    def move_ball(i):
        ball.set_data(bx, by + y[i])
        return ball,

    dt = t[1]
    ani = FuncAnimation(fig, move_ball, range(1,len(y)),
        interval=dt*1000, blit=True)

    plt.show()

if __name__ == '__main__':
    runtime = 20
    dt = 0.01
    bounce_ball(runtime, dt)
    # plot_bounce(t, y, v)
    animate_bounce(t, y, r_ball)