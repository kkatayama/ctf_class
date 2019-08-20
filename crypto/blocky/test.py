import string
import multiprocessing as mp
import itertools

alphabet = string.ascii_letters+string.digits+"!@#$%^&*?,()-=+[]/;"
num_parts = 4
part_size = len(alphabet) // num_parts

def do_job(first_bits):
    for x in itertools.product(first_bits, alphabet, alphabet, alphabet):
        y = ''.join(x)
        print(y)

if __name__ == "__main__":
    pool = mp.Pool()
    results = []
    for i in xrange(num_parts):
        if i == num_parts - 1:
            first_bit = alphabet[part_size * i :]
        else:
            first_bit = alphabet[part_size * i : part_size * (i+1)]
        results.append(pool.apply_async(do_job(first_bit)))

    pool.close()
    pool.join()
