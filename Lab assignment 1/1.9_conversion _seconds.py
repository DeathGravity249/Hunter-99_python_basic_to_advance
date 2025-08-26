def conversion(seconds):
    if seconds == 0:
        return "No. of seconds entered"

    hours = seconds // 3600         # 1 hour = 3600 seconds
    seconds = seconds % 3600        # leftover after hours

    minutes = seconds // 60         # 1 minute = 60 seconds
    seconds = seconds % 60          # leftover after minutes

    return f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}"


# --- Main program ---
seconds = int(input("Enter total seconds: "))
print(conversion(seconds))
