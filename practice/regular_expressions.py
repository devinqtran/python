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