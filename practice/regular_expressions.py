import re

text = "Base camp is located at 40.2338 N, 111.6585 W. The secondary site is at 34.0522 N, 118.2437 W."

# extract decimail numbers and direction
print(re.findall(r'\d+\.\d+ \w', text))

log_data = """
[2026-09-15 10:22:01] INFO: Server started successfully.
[2026-09-15 11:58:23] ERROR: Connection timeout from 192.168.1.50
[2026-09-15 12:05:11] WARNING: High memory usage detected.
[2026-09-15 12:14:59] ERROR: Authentication failed for 10.0.0.25
"""

pattern = r'ERROR:.*?(\d+\.\d+\.\d\.\d+)'
# write script that extracts only the IP addresses from the lines marked as ERROR
print(re.findall(r'\d+\.\d+\.\d\.\d+', log_data))
ips = re.findall(pattern, log_data)
print(ips)

records = "ItemID: 492-A, itemid: 583-B, ITEM_ID: 991-C, ItemID: 104-D"

# standardize labels ID: number-letter
# item matches the literal word
# _? matches zero or one underscore (making it optional)
# id matches the literal word
pattern2 = r'item_?id'
clean_records = re.sub(pattern2, 'ID', records, flags=re.IGNORECASE)
print(clean_records)

dimensions = "Excavation logged: 39x39x11 blocks cleared in sector A."
pattern3 = r'(\d+)x(\d+)x(\d+)' # each dimension in grouping ()

match = re.search(pattern3, dimensions)
if match:
    print("Full match (Group 0):", match.group(0))
    print("Length (Group 1):", match.group(1))
    print("Width (Group 2):", match.group(2))
    print("Height (Group 3):", match.group(3))

concat = match.group(1) + match.group(2)
print(concat)

# string to int then find volume
length = int(match.group(1))
width = int(match.group(2))
height = int(match.group(3))

volume = length * width * height
print(f"Volume: {volume}")
