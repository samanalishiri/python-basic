def range_(start, stop, increment):
    while start < stop:
        yield start
        start += increment


for item in range_(0, 4, 0.5):
    print(item, end=" ")
