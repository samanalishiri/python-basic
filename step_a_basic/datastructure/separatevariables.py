# Saman Alishiri samanalishiri@gmail.com


point = (1, 2)
x, y = point
print('point = ({},{})'.format(x, y))
print('---------------------------------------------')

date = ['yyy-MM-dd', 1987, 8, 29]
date_format, year, month, day = date
print('date = {}-{}-{}'.format(year, month, day))
print('---------------------------------------------')

contact = ('Saman Alishiri', 'samanalishiri@gmail.com', '9193647230', '9193647231')
name, email, *phones = contact
print('name:\t{}\nemail:\t{}\nphone:\t{}'.format(name, email, phones))
print('---------------------------------------------')

records = [
    ('Saman Alishiri', 'samanalishiri@gmail.com', '9193647230', '9193647231'),
    ('Samira Talebi', 'samiratalebi@gmail.com', '9193647232', '9193647233')
]

for name, email, *phones in records:
    print('name:\t{}\nemail:\t{}\nphone:\t{}'.format(name, email, phones))
print('---------------------------------------------')
