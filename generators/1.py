def generator():
    values = [1, 2, 3]
    for value in values:
        yield value
        if value == 4:
            raise StopIteration("Generator zakończył bieg. Wyjątek!")

gen = generator()

print(next(gen))
print(next(gen))
print(gen.__next__())
print(gen.__next__())

