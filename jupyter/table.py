from IPython.display import HTML, display
import tabulate

tweets = ["ID", "Tweet"]
tweetcount = 0
while (True):
    print("Enter your tweet: (-1 to exit)")
    tweet = input()
    if (tweet == "-1"):
        break
    tweetcount = tweetcount + 1
    tweets.append([tweetcount, tweet])

# this line works in Jupyter, but not in console
display(HTML(tabulate.tabulate(tweets, tablefmt="html") ))