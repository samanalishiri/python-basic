# Saman Alishiri samanalishiri@gmail.com


sequence = '123456789'
print(sequence[slice(1, 4)])

sequence = 'abcdefghijklmnopqrstuvxyz'
slice_ = slice(0,26,2)
for i in range(*slice_.indices(len(sequence))):
    print(sequence[i], end=' ')