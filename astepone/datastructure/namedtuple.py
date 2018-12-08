# Saman Alishiri samanalishiri@gmail.com


from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['address', 'joined'])
subscriber_prototype = Subscriber('samanalishiri@gmail.com', '1987-08-29')
print('address: {}, joined: {}'.format(subscriber_prototype.address, subscriber_prototype.joined))