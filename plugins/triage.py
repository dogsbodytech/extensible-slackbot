from dateutil import rrule
from datetime import date, timedelta, datetime

def get_holidays(a=datetime.today(), b=datetime.today()+timedelta(days=365)):
    rs = rrule.rruleset()
    # Include all potential holidays
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=1, bymonthday=1))                       # New Years Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=1, bymonthday=2, byweekday=rrule.MO))   # New Years Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=1, bymonthday=3, byweekday=rrule.MO))   # New Years Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, byeaster=-2))                                   # Good Friday
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, byeaster=1))                                    # Easter Monday
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=5, byweekday=rrule.MO, bysetpos=1))     # May Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=5, byweekday=rrule.MO, bysetpos=-1))    # Spring Bank Holiday
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=8, byweekday=rrule.MO, bysetpos=-1))    # Late Summer Bank Holiday
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=25))                     # Christmas
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=26, byweekday=rrule.MO)) # Christmas
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=27, byweekday=rrule.MO)) # Christmas
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=26))                     # Boxing Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=27, byweekday=rrule.MO)) # Boxing Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=27, byweekday=rrule.TU)) # Boxing Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=28, byweekday=rrule.MO)) # Boxing Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=28, byweekday=rrule.TU)) # Boxing Day
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=24, byweekday=rrule.MO)) # Christmas Shutdown
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=27))                     # Christmas Shutdown
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=28))                     # Christmas Shutdown
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=29))                     # Christmas Shutdown
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=30))                     # Christmas Shutdown
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=12, bymonthday=31))                     # Christmas Shutdown
    rs.rrule(rrule.rrule(rrule.YEARLY, dtstart=a, until=b, bymonth=1, bymonthday=2, byweekday=rrule.FR))   # Christmas Shutdown
    # Exclude potential holidays that fall on weekends
    rs.exrule(rrule.rrule(rrule.WEEKLY, dtstart=a, until=b, byweekday=(rrule.SA,rrule.SU)))
    return rs

def get_workingdays(a=datetime.today(), b=datetime.today()+timedelta(days=365)):
    rs = rrule.rruleset()
    rs.rrule(rrule.rrule(rrule.DAILY, dtstart=a, until=b))                         # Get all days between a and b
    rs.exrule(rrule.rrule(rrule.WEEKLY, dtstart=a, byweekday=(rrule.SA,rrule.SU))) # Exclude weekends
    rs.exrule(get_holidays(a,b))                                                   # Exclude holidays
    return rs

def get_whosontriage(a=datetime(2018, 1, 1), b='Today'):
    if b is 'Today':   # Have to do this due to https://stackoverflow.com/questions/27843317/datetime-datetime-now-returns-old-value
        b = datetime(date.today().year, date.today().month, date.today().day)
    if b.weekday() > 4:
        return "Dan"
    elif b in list(get_holidays(a, b)):
        return "Dan"
    else:
        person = ["Rob", "Gary", "Jim"]
        days = len(list(get_workingdays(a, b)))
        count = days % len(person)
        return person[count]

def msg_contains_reply_on_triage(message):
    # We are matching ontriage and then performing a second more
    # specific check in this function after the main function calls it
    if 'whosontriage' in re.sub('[\W_]+', '', message.lower()):
        name = get_whosontriage()
        return '{} is on triage today'.format(name)

if __name__ == '__main__':
    print(get_whosontriage())
