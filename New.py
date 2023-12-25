import subprocess
import time

def toggle_airplane_mode_linux(enable):
    command = "nmcli r wifi {}".format("on" if enable else "off")
    subprocess.run(command, shell=True)

# Example usage:
toggle_airplane_mode_linux(True)  # Enable airplane mode
time.sleep(5)  # Wait for 5 seconds
toggle_airplane_mode_linux(False)  # Disable airplane mode
