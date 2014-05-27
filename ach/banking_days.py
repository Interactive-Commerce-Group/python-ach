import datetime
from dateutil import rrule


def banking_days_from_now(days, start_date=None):
    holidays = [
        #2014
        datetime.datetime(2014, 01, 01,),
        datetime.datetime(2014, 01, 20,),
        datetime.datetime(2014, 02, 17,),
        datetime.datetime(2014, 05, 26,),
        datetime.datetime(2014, 07, 04,),
        datetime.datetime(2014, 9, 01,),
        datetime.datetime(2014, 10, 13,),
        datetime.datetime(2014, 11, 11,),
        datetime.datetime(2014, 11, 27,),
        datetime.datetime(2014, 12, 25,),
        #2015
        datetime.datetime(2015, 01, 01,),
        datetime.datetime(2015, 01, 19,),
        datetime.datetime(2015, 02, 16,),
        datetime.datetime(2015, 05, 25,),
        datetime.datetime(2015, 07, 04,),
        datetime.datetime(2015, 9, 07,),
        datetime.datetime(2015, 10, 12,),
        datetime.datetime(2015, 11, 11,),
        datetime.datetime(2015, 11, 26,),
        datetime.datetime(2015, 12, 25,),
        #2016
        datetime.datetime(2016, 01, 01,),
        datetime.datetime(2016, 01, 18,),
        datetime.datetime(2016, 02, 15,),
        datetime.datetime(2016, 05, 30,),
        datetime.datetime(2016, 07, 04,),
        datetime.datetime(2016, 9, 05,),
        datetime.datetime(2016, 10, 10,),
        datetime.datetime(2016, 11, 11,),
        datetime.datetime(2016, 11, 24,),
        datetime.datetime(2016, 12, 26,),
    ]
    # New York Federal Reserve Bank Holidays from http://www.newyorkfed.org/aboutthefed/holiday_schedule.html

    # Create a rule to recur every weekday starting at specified date
    if start_date==None:
        start_date = datetime.datetime.today()

    r = rrule.rrule(rrule.DAILY,
                    byweekday=[rrule.MO, rrule.TU,
                    rrule.WE, rrule.TH, rrule.FR],
                    dtstart=start_date,
                    until=start_date + datetime.timedelta(days=days+5)
                    )

    # Create a rruleset
    rs = rrule.rruleset()

    # Attach our rrule to it
    rs.rrule(r)

    # Add holidays as exclusion days
    for day in holidays:
        rs.exdate(day)

    # Return the X day in the ruleset
    return rs[days]
