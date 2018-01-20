# Suppose any line of text can contain at most one url that starts with “http://”
# and ends at the next space in the line.
# Write a fragment of code to extract and print the full url if it is present.

print('---------------- VALIDATE URL ----------------')
goodURL = 'http://google.com '
badURL = 'google'
badURL2 = 'http://google.com'
badURL3 = 'google.com '


def validateURL(url):
    if (url.startswith('http://') and url.endswith(' ') and url.find('.')):
        print("'{0}' => is VALID".format(url))
    else:
        print("'{0}' => is INVALID".format(url))

validateURL(goodURL)
validateURL(badURL)
validateURL(badURL2)
validateURL(badURL3)