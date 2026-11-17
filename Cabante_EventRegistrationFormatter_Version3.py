
import datetime

# Input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
section = input("Enter your section: ")
event_name = input("Enter the event name: ")

event_year = int(input("Enter the event year: "))
event_month = int(input("Enter the event month: "))
event_day = int(input("Enter the event day: "))

# Formatting
proper_full_name = first_name.title() + " " + last_name.title()
uppercase_full_name = proper_full_name.upper()
uppercase_section = section.upper()
clean_event_name = event_name.title()

event_date = datetime.datetime(event_year, event_month, event_day)
formatted_event_date = event_date.strftime("%B %d, %Y")

# Output
print("\nStudent Event Registration Summary")
print("\nName: " + proper_full_name)
print("\nName Code: " + uppercase_full_name)
print("\nSection: " + uppercase_section)
print("\nEvent: " + clean_event_name)
print("\nEvent Date: " + formatted_event_date)
print("\nLanguage Used: Python")
print("String Feature Used: title(), upper()")
print("Date/Time Feature Used: datetime")
print("\nRegistration record created successfully.")
