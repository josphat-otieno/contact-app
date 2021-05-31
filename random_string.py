import random, string
# x = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
# print(x)

size = 8
alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase
password = ''.join(random.choice(alphanum) for num in range(size))
print(password)