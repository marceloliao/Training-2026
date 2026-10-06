def weekday_message(day):
    match day:
        case 1:
            return "Today is Monday"
        case 2:
            return "Today is Tuesday"
        case 3:
            return "Today is Wednesday"
        case 4:
            return "Today is Thursday"
        case 5:
            return "Today is Friday"
        case 6:
            return "Today is Saturday"
        case 7:
            return "Today is Sunday"
        case _:
            return "Invalid day"


if __name__ == "__main__":
    day = 4
    print(weekday_message(day))

# Default value
# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")

"""
Combined values
"""
# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case
day = 8
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")
    case _:
        print("Not a weekday or weekend")

"""
If Statements as Guards
"""
# You can add if statements in the case evaluation as an extra condition-check:
month = 6
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
