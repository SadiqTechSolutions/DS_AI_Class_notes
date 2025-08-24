log_entry = "INFO:2025-07-04T09:54:01Z;User 'alex_p' logged in successfully from IP 192.168.1.101.   "

# Day_5_sol.py
# Solution for the Day 5 "Log File Formatter" assignment.

# The raw log entry string
log_entry = "INFO:2025-07-04T09:54:01Z;User 'alex_p' logged in successfully from IP 192.168.1.101.   "

# 1. Clean up trailing whitespace.
cleaned_log = log_entry.strip()

# 2. Extract the log level.
colon_index = cleaned_log.find(':')
log_level = cleaned_log[:colon_index]

# 3. Extract the timestamp.
semicolon_index = cleaned_log.find(';')
timestamp = cleaned_log[colon_index + 1 : semicolon_index]

# 4. Extract the username.
start_quote_index = cleaned_log.find("'")
print(start_quote_index)
end_quote_index = cleaned_log.find("'", start_quote_index + 1)
print(end_quote_index)
username = cleaned_log[start_quote_index + 1 : end_quote_index]
print(username)

# 5. Extract the IP address.
ip_start_index = cleaned_log.find("IP ") + 3 # Add 3 to get past "IP "
print("The index of ip : ", ip_start_index)
i_index = cleaned_log.find("I", 5)
print("The index of i is: ", i_index)
print(cleaned_log[72])
ip_address = cleaned_log[ip_start_index:-1] # Slice until the last character (the period)
print(ip_address)

# 6. Extract the message.
message_start_index = end_quote_index + 2 # After the closing quote and space
message_end_index = cleaned_log.find(" from IP")
message = cleaned_log[message_start_index:message_end_index]
print(message)

# 7. Format and print the report with transformations.
print("--- Log Analysis Report ---")
print(f"Timestamp: {timestamp[:10]}")      # Slice the timestamp to get just the date
print(f"Log Level: {log_level}")
print(f"Username:  {username.upper()}")    # Convert username to uppercase
print(f"IP Address:{ip_address}")
print(f"Message:   {message.capitalize()}") # Capitalize the message
print("---------------------------")