import requests
import hashlib
import sys

def Check_response(argument):
    url = 'https://api.pwnedpasswords.com/range/' + argument
    res = requests.get(url)
    #print(res.text)
    if res.status_code != 200:
        print(f"Runtime Error The request is failed and the status code is {res.status_code} and try again!! ")
    return res

def password_count(response,tail):
    hashes= (line.split(':') for line in response.text.splitlines())
    for hash,count in hashes:
        if hash == tail:
            return count
    return 0
    #print(response.text)

def api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = Check_response(first5_char)
  print(response)
  return password_count(response,tail)

def main(password):
    for passwd in password:
        count = api_check(passwd)
        if count:
            print(f'the {passwd} password has comprimised by {count} this times , you need to change your password')
        else :
            print(f'the {passwd} password is secure ')
    return "done"

if __name__ == "__main__":
    sys.exit(main(["hello"]))