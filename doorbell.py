from googlehomepush import GoogleHome
from pushover import init, Client
from time import sleep
import RPi.GPIO as GPIO
import random
import config as cfg

init(cfg.token)

GPIO.setmode(GPIO.BCM)
GPIO.setup(cfg.doorbell_input, GPIO.IN)


while True:
    if GPIO.input(cfg.doorbell_input) == 0:
        GoogleHome(host=cfg.google_home_ip).cc.set_volume(cfg.doorbell_volume)
        GoogleHome(host=cfg.google_home_ip).play("http://" + cfg.doorbell_ip + ":8000/" + cfg.audio[random.randrange(0, 2, 1)])
        for key in cfg.client_keys:
            Client(key).send_message("Der er besoeg", title="Ringklokke")
        sleep(2)
        while not GPIO.input(cfg.doorbell_input) == 1:
            sleep(0.1)

    sleep(0.2)

