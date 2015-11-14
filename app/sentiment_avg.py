# B_raxEatsSnacks

# GET THE AVERAGE SENTIMENT OF THE "index.html" TEXT WITHIN <BODY> TAGS

sentiment_file = "sentiments.csv"

def sentiment_dictionary(sentiment_file):
    """Creates dictionary from csv file data frame """
    # (with) open csv file
    with open(sentiment_file, "r", encoding="utf8") as sentiments:

        # empty dictionary to which add words and values
        sentiment_dictionary = {}

        contents = 0
        # read lines until empty
        while contents != "":
            contents = sentiments.readline()
            contents = contents.rstrip("\n")
            # splits str data by comma into list
            split_data = contents.split(",")

            # ensure line has two components
            if len(split_data) == 2:
                word = split_data[0]
                value = float(split_data[1])

                # add new key and value to sentiment dictionary
                sentiment_dictionary[word] = value

    return sentiment_dictionary


def avg_sentiment(body):
    """Returns the average sentiment of body"""
    # count of words with sentiment value
    counter = 0
    total = 0

    # create sentiment dictionary to reference
    sentiments = sentiment_dictionary(sentiment_file)

    text = body.split() # split into list

    for word in text:
        print(word)

        if word in sentiments:
            counter += 1
            total += sentiments[word]
        else:
            pass

    # average sentiment over tweet
    
    
    if counter  > 0:
        avg = total / counter

        return avg
    else:
        return None


print(avg_sentiment("He is an outcast"))