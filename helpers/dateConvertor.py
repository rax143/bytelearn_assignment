import datetime


def dateTimeConvertor(dates):
    for date in dates:
        for fmt in ["%Y/%m/%d", "%d-%m-%Y", "%Y%m%d", "%dst %b %Y", "%d %b %Y", "%dnd %b %Y", "%dth %b %Y", "%d, %b %Y"]:
            try:
                return str(datetime.datetime.strptime(date, fmt).date())
            except ValueError:
                continue
        raise ValueError(date)
