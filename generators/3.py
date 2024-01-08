def generate_integers(how_many_numbers):
    return (i for i in range(how_many_numbers))

num_of_integers_to_generate = 15

result = generate_integers(num_of_integers_to_generate)

for _ in range(num_of_integers_to_generate):
    print(next(result))

