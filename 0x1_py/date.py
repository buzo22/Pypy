import smtplib 
import datetime as dt
import random

my_email = "cruxakana@gmail.com"
my_password = "ilovesenami"

now = dt.datetime.now()
weekday = now.weekday
if weekday == 3:
    with open("quote.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = my_password,
            msg = f"Subject:Energy and Vibe\n\n{quote}") 