import datetime

def dateTimeConvertor(date):
    for value in date:
        formatedDate = datetime.datetime.strptime(value, "%dst %b %Y" or "%d %b %Y" or "%dnd %b %Y" or "%dth %b %Y" or "%d, %b %Y" or"%Y/%m/%d" or "%d-%m-%Y" or "%Y%m%d")
        formatedDate = formatedDate.strftime('%Y-%m-%d')
    return formatedDate
