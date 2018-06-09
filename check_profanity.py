from urllib import urlopen


def read_file():

    quotes = open("Z:\movie_quotes\movie_quotes.txt")
    content_of_file = quotes.read()
    # print(content_of_file)
    quotes.close()
    check_profanity(content_of_file)


def check_profanity(text_to_check):

    connection = urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    # print output
    connection.close()
    if "true" in output:
        print "PROFANITY ALERT!!!"
    else:
        print " No curse words were found"

read_file()
