import urllib


def read_txt():
    path = open(r'C:\Users\Oss\Desktop\pro27\movie_quotes.txt')
    info = path.read()
    check_profanity(info)
    path.close()


def check_profanity(txt_to_check):
    connect = urllib.urlopen('http://www.wdylike.appspot.com/?q=' + txt_to_check)
    output = connect.read()
    if 'true' in output:
        print 'Warning there is a curse words !'
    else:
        print 'The document is clean'
    connect.close()


read_txt()
