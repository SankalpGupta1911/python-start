# Healthy Program
# 9am - 5pm
# Water - water.mp3 (3.5 ltr) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - Eyedone - log - Every 30 min
# Physical activity - physical.mp3 - Exdone - log - Every 45 min
# Rules - pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("health.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Water drinking time. Enter 'drank' to stop the alarm")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank water at")
        if time() - init_eyes > eyessecs:
            print("Eye relaxed time. Enter 'eyedone' to stop the alarm")
            musiconloop('eyes.mp3', 'eyedone')
            init_eyes = time()
            log_now("Eye relaxed at")
        if time() - init_exercise > exsecs:
            print("Physical exercise time. Enter 'exdone' to stop the alarm")
            musiconloop('physical.mp3', 'exdone')
            init_exercise = time()
            log_now("Physical exercise at")