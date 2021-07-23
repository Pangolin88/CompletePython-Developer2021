import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError('Error fetching!!!')
    return res


def get_pwd_leaks_count(res, data_to_check):
    hashes = tuple(i.split(':') for i in res.text.splitlines())
    for h, count in hashes:
        if h == data_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = sha1pwd[:5], sha1pwd[5:]
    res = request_api_data(head)
    return get_pwd_leaks_count(res, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'Password {password} was found {count} times... You should change your password.')
        else:
            print(f'Password {password} was NOT found. Carry on!!!')
    return


main(sys.argv[1:])