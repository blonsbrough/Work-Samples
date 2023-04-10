import sys
import os
import socket
import psutil
import platform

# Message from computer
host = socket.gethostname() #figure out how to get the computer's name (host name)
user = os.getlogin() #figure out how to get the user name
opsys = platform.system() #Figure out how to get the operating system name
cpumodel = platform.processor() #Figure out how to get the cpu model name
cpuspeed = psutil.cpu_freq()[-1] # cpu clock speed, I gave you this one for free
workdir = os.getcwd() #figure out how to get the current working directory (hint)
max_integer = sys.maxsize # figure out largest integer number the computer can handle

comp_message = f"""\
Alo world.
My name is {host}. I am {user}'s computer.
A little about me:
My brain is a {cpumodel} CPU, capable of thinking approximately \
{cpuspeed} thoughts per-minute. I don't have any fingers but I can count to \
{max_integer}.

I am running a {opsys} operating system, and currently working in the
directory {workdir}.

My user wants to say something next. See you in class,
-{host}
"""
print(comp_message)

# Message from student (you can fill in this part "by-hand")
st_name = 'Bryn Lonsbrough' # your preferred name
st_year = '2nd-year' # 1st-year | 2nd-year | graduate | ...
st_major = 'physics(Astrophysics)'
st_feelings = 'Ecstatic' # excited | anxious | indifferent | nauseous | ...
st_fav_task = 'simplify and beautify complex problems' # make pretty plots | solve impossible equations |
                            # run physical simulations | design cool apps | ...

st_message = f"""
Hi ASTR119,

My name is {st_name}. I am a {st_year} student, studying {st_major}. I feel \
{st_feelings} about learning scientific computing. What I look forward to most \
is learning how to use my computer to {st_fav_task}.

I'll see you all in class. Cheers,
-{st_name}
"""
print(st_message)