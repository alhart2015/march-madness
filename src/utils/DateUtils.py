'''
Utility functions around parsing the date and stuff.

todo: docs
todo: type hints
'''

'''
todo: docs. I think this is supposed to be below the function declaration in pep-8?
'''
def progression_through_season(date):
    #first_day_of_season = '2016-09-24' # todo: this is bad
    last_day_of_season = '2017-03-12' # todo: this is bad
    last_time_id = date_to_time_id(last_day_of_season)
    this_time_id = date_to_time_id(date)
    weight = this_time_id / last_time_id
    return weight + 0.5

'''
todo: docs
todo: constants for this stuff
todo: check date format?
'''
def date_to_time_id(date):
    split_date = date.split('-')
    year = int(split_date[0])
    month = int(split_date[1])
    day = int(split_date[2])

    time_id = 0.0
    if year > 2016:
        # add days for the rest of september, all of october,
        # november, december
        time_id += (6 + 31 + 30 + 31)
        if month == 2:
            # add days for january
            time_id += 31
        elif month == 3:
            # add days for january and february
            time_id += (31 + 28)
    else:
        if month == 10:
            # add days for september
            time_id += 6
        elif month == 11:
            # add days for september and october
            time_id += (6 + 31)
        elif month == 12:
            # add days for september, october, november
            time_id += (6 + 31 + 30)
    if month != 9:
        time_id += day
    return time_id
