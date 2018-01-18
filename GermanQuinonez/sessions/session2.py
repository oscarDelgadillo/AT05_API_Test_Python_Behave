def is_url(url):
    """
    this function extracts and print the full url if it is present.
    :param url:
    :return: url if it is present
    """
    index_target = url.find("http://")
    index_end = url.find(" ")
    if index_target >= 0:
        if index_end >= 0:
            print(url[index_target:index_end])
            print("It is a url")
    else:
        print(url)
        print("It is not url")


is_url("url=http://www.google.com ")
is_url("url=google.com")
