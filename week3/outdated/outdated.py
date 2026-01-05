valid_months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        userInput = input("Date: ").strip()

        # CASE 1:  Slash format  (M/D/YYYY)

        if "/" in userInput:
            try:
                m, d, y = userInput.split("/")
                m = int(m)
                d = int(d)
                y = int(y)

                # Validate month/day/year
                if not (1 <= m <= 12):
                    continue
                
                if not (1 <= d <= 31):
                    continue

                if not (1000 <= y <= 9999):
                    continue

                print(f"{y:04d}-{m:02d}-{d:02d}")
                break

            except:
                continue


        # CASE 2: Word format (Month Day, Year)

        else:
            parts = userInput.replace(",", "").split()

            if len(parts) != 3:
                continue

            if not "," in userInput:
                continue

            month = parts[0].title()
            day = parts[1]
            year = parts[2]

            if month not in valid_months:
                continue

            if not day.isdigit():
                continue

            day = int(day)
            if not (1 <= day <= 31):
                continue

            if not year.isdigit() or len(year) != 4:
                continue
            year = int(year)

            month_number = valid_months.index(month) + 1

            print(f"{year:04d}-{month_number:02d}-{day:02d}")
            break

    except EOFError:
        break
