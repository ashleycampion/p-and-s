# Write a program that outputs whether or not today is a weekday.

#import datetime module
import datetime

# Store weekday value for the current moment
# information on the datetime module is readily
# available online. For example see the Python docs:
# https://docs.python.org/3/library/datetime.html
x = datetime.datetime.now().weekday()

# if weekday value 'x' is less than 5 then it is a weekday,
# otherwise it is the weekend
if x < 5:
    print("I'm afraid today's a weekday, up you get now...")
else:
    print("Sleep in a while yet, 'tis the weekend yet.")

