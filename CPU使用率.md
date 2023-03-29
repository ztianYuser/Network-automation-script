import psutil

# Get the CPU usage of the current process
cpu_usage = psutil.cpu_percent()

# Print the CPU usage as a percentage
print(f"CPU usage: {cpu_usage}%")
