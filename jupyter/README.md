#  Starts a new container, executes a command inside it, and pulls an image if needed
docker run jupyter/minimal-notebook

# Cannot connect to the Docker daemon at unix:/var/run/docker.sock. Is the docker daemon running? <- check if Docker is running


Commands for jupyter:

```python
tweets = ["ID", "Tweet"]
tweetcount = 0
while (True):
    print("Enter your tweet: (-1 to exit)")
    tweet = input()
    if (tweet == "-1"):
        break
    tweetcount = tweetcount + 1
    tweets.append([tweetcount, tweet])

from IPython.display import HTML, display
import tabulate

display(HTML(tabulate.tabulate(tweets, tablefmt="html") ))
```
