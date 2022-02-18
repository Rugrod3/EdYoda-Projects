def log_in(username,password):
    pw = login_info.get(username)
    if pw != password:
        print('Wrong username or password')
        return False
    else:
        return True

login_info = {'M':'@',
              'Krunal':'3333',
              'Kartik':'call'}


