months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    # Format: 9/8/1636
    if "/" in date:
        try:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except ValueError:
            pass

    # Format: September 8, 1636
    else:
        try:
            parts = date.split()
            if len(parts) == 3 and parts[1].endswith(","):
                name = parts[0]
                day = int(parts[1].rstrip(","))
                year = int(parts[2])
                if name in months and 1 <= day <= 31:
                    month = months.index(name) + 1
                    print(f"{year:04}-{month:02}-{day:02}")
                    break
        except ValueError:
            pass