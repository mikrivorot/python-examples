# python-examples

https://www.activestate.com/resources/quick-reads/python-dependencies-everything-you-need-to-know/#:~:text=Dependencies%20are%20all%20of%20the,to%20web%20development%2C%20and%20more.

1. Get `pipreqs`
```
pip3 install pipreqs
```

2. Generate `requirements.txt`

```
pipreqs /<projectlocation>
```


3. Install dependencies
```
pip install -r requirements.txt -t <path-to-the-lib-directory>
```