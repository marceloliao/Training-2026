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
