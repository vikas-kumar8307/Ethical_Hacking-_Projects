import hashlib
import bcrypt
import itertools
import string
import threading
import time

password_found = False

def hash_password(password, algorithm="sha256"):
    if algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == "sha512":
        return hashlib.sha512(password.encode()).hexdigest()
    elif algorithm == "bcrypt":
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    else:
        raise ValueError("Unsupported hash algorithm!!")

def brute_force_attack(hashed_password, length, algorithm="sha256",charset=string.ascii_lowercase + string.digits):

    global password_found

    def attempt_password(start_index, step):

        for guess_tuple in itertools.islice(itertools.product(charset, repeat=length), start_index, None, step):
            if password_found:
                return
            guess = ''.join(guess_tuple)
            hashed_guess = hash_password(guess, algorithm)
            if hashed_guess == hashed_password:
                print(f"\n[+] Brute Force Found: {guess}")
                password_found = True
                return
    
    num_threads = 4
    threads = []

    for i in range(num_threads):
        t = threading.Thread(target=attempt_password, args=(i, num_threads))
        threads.append(t)
        t.start()

    for t in threads:
            t.join()

    if not password_found:
        print("\n[-] Brute force failed!!")

if __name__ == "__main__":
    print("\n 🔥 Brute-Force Password Cracker 🔥 ")
    hash_type = input("Enter hash type (md5/sha1/sha256/sha512/bcrypt):-")
    password_to_test = input("Enter the password to hash (for testing):-")
    hashed_password = hash_password(password_to_test, hash_type)

    print(f"[*] Hashed Password : {hashed_password}")

    max_length = int(input("ENnter max length for brute force attack:-"))
    charset = input("Enter character set (default: lowercase+digits) or pressEnter")

    start_time = time.time()
    for length in range(1, max_length + 1):
        brute_force_attack(hashed_password, length, hash_type, charset)
        if password_found:
            break
    end_time = time.time()

    print(f"\n[+] Attack complete. Time taken:{end_time - start_time:.2f} seconds.")
