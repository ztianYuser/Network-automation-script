import collections

# Open the access.log file
with open('/var/log/nginx/access.log', 'r') as f:
    # Read all the lines in the file
    lines = f.readlines()

# Extract the IP addresses from each line
ips = [line.split()[0] for line in lines]

# Count the occurrences of each IP address
ip_counts = collections.Counter(ips)

# Get the top 10 IP addresses
top_ips = ip_counts.most_common(10)

# Print the top 10 IP addresses
for ip, count in top_ips:
    print(f"{ip}: {count}")

import matplotlib.pyplot as plt

# Open the access.log file
with open('/var/log/nginx/access.log', 'r') as f:
    # Read all the lines in the file
    lines = f.readlines()

# Extract the IP addresses from each line
ips = [line.split()[0] for line in lines]

# Count the occurrences of each IP address
ip_counts = collections.Counter(ips)

# Get the top 10 IP addresses
top_ips = ip_counts.most_common(10)

# Create a bar chart of the top 10 IP addresses
plt.barh(range(len(top_ips)), [count for ip, count in top_ips], align='center')
plt.yticks(range(len(top_ips)), [ip for ip, count in top_ips])

# Set the X-axis label to 'Number of Requests'
plt.xlabel('Number of Requests')

# Set the Y-axis label to 'IP Address'
plt.ylabel('IP Address')

# Set the title of the chart to 'Top 10 IP Addresses'
plt.title('Top 10 IP Addresses')

# Rotate the X-axis labels by 90 degrees
plt.xticks(rotation=90)

# Display the chart
plt.show()
plt.xticks(rotation=90)
