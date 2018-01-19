#The function verify is a correct URL
def getUrl(uri):
    heard = uri[0:8]
    correctUri=""
    if heard.find("https://")>-1 or heard.find("http://")>-1:
        i=uri.find(" ")
        if i>0:
            correctUri= uri[0:i]
            if not(correctUri[(len(correctUri) - 4)] == "." or correctUri[(len(correctUri) - 3)] == "."):
                correctUri=""

    return correctUri

#Use the function
url="https://www.google.com "
print("The URL is: "+getUrl(url))