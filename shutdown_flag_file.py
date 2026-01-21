# import RPi.GPIO as GPIO
import os
import platform
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Pin definitions
power_sw_pin = 5  # Shutdown button: GPIO 5 (physical pin 29)
power_led_pin = 13  # Power LED: GPIO 13 (PWM1) (physical pin 33)
# power_led_pin = None since we should use 3v3 pin instead
#   (always on when Pi is on)
SHUTDOWN_FLAG_NAME = "raspberry-pi-power-switch.conf"
SHUTDOWN_FLAG_PATH = os.path.join("/tmp", SHUTDOWN_FLAG_NAME)
if platform.system() == "Windows":
    TMP_DIR = os.environ.get('TEMP')
    if not TMP_DIR:
        TMP_DIR = os.environ['LOCALSETTINGS']
    SHUTDOWN_FLAG_PATH = os.path.join(TMP_DIR)
# os.system("echo 5 > /sys/class/gpio/unexport 2>/dev/null || true")

logging.info(f"Initialized {repr(SHUTDOWN_FLAG_PATH)} (flag file) path.")

def shutdown(reason):
    logging.info("{} found, shutting down..."
                 .format(reason))
    time.sleep(1)  # Debounce
    if platform.system() == "Windows":
        os.system("shutdown /s")
    os.system("shutdown -h now")  # Darwin (if root) or Linux


try:
    while True:
        time.sleep(1)
        if os.path.isfile(SHUTDOWN_FLAG_PATH):
            os.remove(SHUTDOWN_FLAG_PATH)
            logging.info("Removed {}".format(repr(SHUTDOWN_FLAG_PATH)))
            shutdown(SHUTDOWN_FLAG_PATH)
            break
except KeyboardInterrupt:
    logging.info("Script interrupted, cleaning up")
finally:
    logging.info("Cleaned up")
