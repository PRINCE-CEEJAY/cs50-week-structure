from datetime import datetime, date
import inflect

def main():
    user_input = get_user_input()
    dob = validate_date(user_input)
    if dob is None:
      return
    minutes = get_minutes(dob)
    print(convert_to_words(minutes))

def get_user_input():
   return input("Date of Birth: ").strip()

def validate_date(user):
   try:
    return datetime.strptime(user, "%Y-%m-%d")
   except ValueError:
      # print("Invalid date")
      return None

def get_minutes(dob):
    today = date.today()
    dob_date = dob.date()
    diff = today - dob_date
    return diff.days * 1440

def convert_to_words(minutes):
   p = inflect.engine()
   suffix = "minutes"
   if minutes == 1:
      suffix = "minute"
   words = f"{p.number_to_words(minutes)} {suffix}"
   initial_letter = words[0:1].upper()
   remaining_texts =  words.replace(" and ", " ")[1:]
   return initial_letter + remaining_texts

if __name__ == "__main__":
    main()
