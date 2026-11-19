import re

# Regular expression pattern
pattern = r"\[(.*?)\] username=(\S+) ip=(\S+) status=(\S+)"

records = []

total = 0
success = 0
failed = 0
invalid = 0

# Open log file
with open("sample_auth.log", "r") as file:

    for line in file:

        total += 1

        match = re.search(pattern, line)

        if match:

            timestamp = match.group(1)
            username = match.group(2)
            ip = match.group(3)
            status = match.group(4)

            record = {
                "timestamp": timestamp,
                "username": username,
                "ip": ip,
                "status": status
            }

            records.append(record)

            if status == "SUCCESS":
                success += 1

            elif status == "FAILED":
                failed += 1

            else:
                invalid += 1

        else:
            invalid += 1

# Display summary
print("\n===== LOGSENTRY SUMMARY =====")

print("Total Lines:", total)
print("Successful Logins:", success)
print("Failed Logins:", failed)
print("Invalid Lines:", invalid)

print("\n===== PARSED LOGS =====")

for record in records:
    print(record)