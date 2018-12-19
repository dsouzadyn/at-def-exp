
def get_flag(r):
    try:
        r.sendline('ls -t | head -1 | xargs cat')
        flag = r.recv()
        print flag
        if 'FLG' in flag:
            return flag.split(':')[1]
        else:
            return -1
    except:
        return -1
