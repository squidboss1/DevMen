def generator():
    values = [1, 2, 3]
    try:
        for value in values:
            yield value
    except StopIteration as e:
        print("Generator zakończył bieg. Wyjątek!", e)


gen = generator()

for _ in range(5):
    result = next(gen)
    print("next():", result)
    gen.throw(ValueError("Generator zakończył bieg. Wyjątek 2!"))

for _ in range(5):
    result = gen.__next__()
    print("__next__():", result)
    gen.throw(ValueError("Generator zakończył bieg. Wyjątek 3!"))
