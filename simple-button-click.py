import urllib.request

def get_unread_msgs(user, passwd):
    auth_handler = urllib.request.HTTPBasicAuthHandler()
    auth_handler.add_password(
        realm='New mail feed',
        uri='https://mail.google.com',
        user='%s@gmail.com' % user,
        passwd=passwd
    )
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)
    feed = urllib.request.urlopen('https://mail.google.com/mail/feed/atom')
    return feed.read()

print (get_unread_msgs("",""))



