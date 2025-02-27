import os
import time

def shutdown():
    """Function to shut down the Raspberry Pi."""
    print("Shutting down the Raspberry Pi...")
    os.system('sudo shutdown now')  # This will initiate the shutdown command

def monitor_shutdown_condition():
    """Function to monitor a condition and trigger the shutdown."""
    # waiting 10 seconds then Pi will shut down.
    print("Monitoring... The Raspberry Pi will shut down in 10 seconds.")
    time.sleep(10)
    shutdown()

if __name__ == "__main__":
    monitor_shutdown_condition()
