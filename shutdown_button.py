import RPi.GPIO as GPIO
import os
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Pin definitions
power_sw_pin = 5  # Shutdown button 29=GPIO 5
power_led_pin = None  # 33=GPIO 13 (PWM1)  # Power LED

GPIO.setmode(GPIO.BCM)
GPIO.setup(power_sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Shutdown button
# Commented power_led_pin since we should use 3v3 pin instead
#   (always on when Pi is on)
if power_led_pin:
    GPIO.setup(power_led_pin, GPIO.OUT)  # Power LED
    GPIO.output(power_led_pin, GPIO.HIGH)  # Turn LED on
    logging.info(f"Initialized GPIO {power_led_pin} (LED)")
logging.info(f"Initialized GPIO {power_sw_pin} (button)")

def shutdown(channel):
    logging.info("Button pressed, shutting down...")
    if power_led_pin:
        GPIO.output(power_led_pin, GPIO.LOW)  # Turn LED off
    time.sleep(1)  # Debounce
    os.system("shutdown -h now")

GPIO.add_event_detect(power_sw_pin, GPIO.FALLING, callback=shutdown,
                      bouncetime=200)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    logging.info("Script interrupted, cleaning up")
finally:
    if power_led_pin:
        GPIO.output(power_led_pin, GPIO.LOW)
    GPIO.cleanup()
    logging.info("GPIO cleaned up")
