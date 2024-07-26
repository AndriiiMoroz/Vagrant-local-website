#this code generatse secret
import string, random

def gen_secret():
    str = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(32))
    with open("secret.txt", "w") as text_file:
        print(f"{str}", file=text_file)
    return str

gen_secret()