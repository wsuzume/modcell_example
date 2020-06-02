# ../module_notebook/hello.ipynb ---------
# ---


class Hello:
    def show(self):
        print('Hello, world!!')

# ---
# --------- ../module_notebook/hello.ipynb
# ../module_notebook/fizzbuzz.ipynb ---------
# ---


def fizzbuzz(upto=100):
    for i in range(1, upto):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

# ---
# --------- ../module_notebook/fizzbuzz.ipynb
