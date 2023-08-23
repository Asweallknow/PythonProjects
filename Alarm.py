# Import necessary libraries
from datetime import datetime
from playsound import playsound

# Get user input for the desired alarm time
alarm_time = input("Enter the time of the alarm to be set : HH:MM:SS AM/PM\n")

# Extract hours, minutes, and seconds from the user input and convert them to integers
alarm_hour, alarm_minute, alarm_seconds = map(int, alarm_time[:8].split(':'))

# Extract the alarm period (AM or PM) from the user input and convert it to uppercase
alarm_period = alarm_time[9:].upper()

# Display a message indicating that the alarm is being set up
print("Setting up the alarm...")

# Start an infinite loop to constantly check the current time
while True:
    # Get the current time using the datetime module
    now = datetime.now()

    # Extract the current hour, minute, second, and period (AM or PM)
    current_hour = int(now.strftime("%I"))
    current_minute = int(now.strftime("%M"))
    current_seconds = int(now.strftime("%S"))
    current_period = now.strftime("%p")
    
    # Check if the alarm period matches the current period (AM or PM)
    if alarm_period == current_period:
        # Check if the alarm hour matches the current hour
        if alarm_hour == current_hour:
            # Check if the alarm minute matches the current minute
            if alarm_minute == current_minute:
                # Check if the alarm seconds matches the current seconds
                if alarm_seconds == current_seconds:
                    # If all conditions are met, print a wake-up message
                    print("Wake Up!")
                    
                    # Play the specified audio file using the playsound library
                    playsound('audio.mp3')
                    
                    # Break out of the loop, as the alarm has been triggered
                    break
