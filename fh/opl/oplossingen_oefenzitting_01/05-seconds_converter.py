seconds = int(input("Time in seconds: "))

seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24
seconds_per_hour = seconds_per_minute * minutes_per_hour
seconds_per_day = seconds_per_hour * hours_per_day

# // : is a floor division
# % : modulo operator
days = seconds // seconds_per_day
seconds_remaining = seconds % seconds_per_day
hours = seconds_remaining // seconds_per_hour
seconds_remaining = seconds_remaining % seconds_per_hour
minutes = seconds_remaining // seconds_per_minute
seconds_remaining = seconds_remaining % seconds_per_minute

message = str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, " + str(seconds_remaining) + " seconds"
print(message)
