Simple backend app example


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

# Anaconda
In summary, Anaconda is a distribution of python that provides an easy-to-use platform for data science and machine learning. It has many pre-installed packages and tools that are commonly used in these fields, and it also has a package manager that makes it easy to install and manage dependencies and packages. Python, however, is a general-purpose programming language that can be used for machine learning. Still, it requires more effort to set up and manage the environment, and the libraries need to be installed separately.


TODO:
- how to add swagger (anything to render API)
- config + env var (virtualenv)
- tests
- middlewares + auth


