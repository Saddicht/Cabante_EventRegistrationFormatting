#Versiom 2
# Input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
section = input("Enter your section: ")
event_name = input("Enter the event name: ")

event_year = input("Enter the event year: ")
event_month = input("Enter the event month: ")
event_day = input("Enter the event day: ")

# Formatting
proper_full_name = first_name.title() + " " + last_name.title()
uppercase_full_name = proper_full_name.upper()
uppercase_section = section.upper()
clean_event_name = event_name.title()

# Output
print("\nStudent Event Registration Summary")
print("\nName: " + proper_full_name)
print("\nName Code: " + uppercase_full_name)
print("\nSection: " + uppercase_section)
print("\nEvent: " + clean_event_name)
print("\nEvent Date: " + event_month + " " + event_day + ", " + event_year)
print("\nLanguage Used: Python")
print("String Feature Used: title(), upper()")
print("Date/Time Feature Used: None")
print("\nRegistration record created successfully.")
