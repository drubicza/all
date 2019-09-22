import os
import sys
import time

os.system('clear')
time.sleep(1)
username = 'edi'
password = 'bismilah321'
print '\x1b[34m+--------------------------------+'
print '\x1b[33;1m| \x1b[32mMASUKKAN USERNAME / PASSWORD   \x1b[33;1m|'
print '\x1b[34m+--------------------------------+'

def ketik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(20.0 / 500)


def restart():
    ulang = sys.executable
    os.execl(ulang, ulang, *sys.argv)


def main():
    user = raw_input('\x1b[0;1m[\x1b[31m+\x1b[0;1m]\x1b[32m USERNAME  \x1b[0;1m: ')
    if user == username:
        pwd = raw_input('\x1b[0;1m[\x1b[31m+\x1b[0;1m]\x1b[32m KATA SANDI\x1b[0;1m: ')
        if pwd == password:
            print '\x1b[34m----------------------------------'
            print '\x1b[0;1m[\x1b[31m+\x1b[0;1m]\x1b[32m SEDANG MASUK...'
            time.sleep(2)
            print '\x1b[34m----------------------------------'
            print '\x1b[0;1m[\x1b[31m+\x1b[0;1m]\x1b[32m SUKSES BROW\x1b[0;1m'
            sys.exit()
        else:
            ketik('\x1b[32mMaaf Masukkan Kata sandi Anda salah')
            time.sleep(1)
            ketik('\x1b[32msilahkan Masukkan kembali')
            time.sleep(1)
            ketik('\x1b[32mTerima kasih...')
            time.sleep(5)
            restart()
    else:
        ketik('\x1b[32mmaaf Masukkan Username Anda salah')
        time.sleep(1)
        ketik('\x1b[32msilahkan Masukkan kembali')
        time.sleep(1)
        ketik('\x1b[32mTerima kasih...')
        time.sleep(5)
        restart()


try:
    main()
except KeyboardInterrupt:
    restart()
