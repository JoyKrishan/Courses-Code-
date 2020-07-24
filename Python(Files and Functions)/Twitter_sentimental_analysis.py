tweet_file=open("project_twitter_data.csv")
def csv_reader(csv_file):
    reader=csv_file.readlines()
    doc_lst=[]
    for line in reader[1:]:
        text, num_retweets, num_replies=tuple(line.strip().split(","))
        pos_score=get_pos(text)
        neg_score=get_neg(text)
        doc_lst.append((text, num_retweets, num_replies, pos_score, neg_score))
    return doc_lst


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(string):
    for i in punctuation_chars:
        if i in string:
            string=string.replace(i,"")
    return string

def get_pos(sen):
    pos_count=0
    words=sen.split()
    for word in words:
        nw_word=strip_punctuation(word).lower()
        if nw_word in positive_words:
            pos_count+=1
    return pos_count

def get_neg(sen):
    neg_count=0
    words=sen.split()
    for word in words:
        nw_word=strip_punctuation(word).lower()
        if nw_word in negative_words:
            neg_count+=1
    return neg_count

with open("resulting_data.csv", "w") as fhandle:
    tweets_lst=csv_reader(tweet_file)
    fhandle.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    fhandle.write("\n")
    for tweet in tweets_lst:
        print(tweet)
        fhandle.write("{},{},{},{},{}".format(tweet[1], tweet[2],tweet[3], tweet[4], tweet[3]-tweet[4])+"\n")
