import requests
import hashlib
import sys

def requests_api_data(query_char):
	url = "https://api.pwnedpasswords.com/range/" + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f"error fetching: {res.status_code}, check the api and try again")
	return res	


def get_password_leaks_count(hashes, hash_to_check):
	hashes = (line.split(":") for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0


def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
	first5_char,tail = sha1password[:5], sha1password[5:]
	responce = requests_api_data(first5_char)
	return get_password_leaks_count(responce, tail)

def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f"{password} was found {count} times ..... it is the right timr to change your password!")
		else:
		    print(f"{password} was good to go!")
	return "password check is done!"		




f = open(r' TEXT FILE PATH','r')
pas = f.readlines()

if __name__ == "__main__":
	main(pas)



	# main(sys.argv[1:])

