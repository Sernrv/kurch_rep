import datetime as dt


d = dt.datetime.now() + dt.timedelta(1)
dat = dt.datetime.date(d)
datstr = dt.datetime.strftime(dat, '%d.%m.%Y')
print(d)
print(dat)
print(datstr)
