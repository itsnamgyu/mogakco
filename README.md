# Mogak Co
A service to help hip-happenin' developers find cafes with good wifi and power plugs!

![DONT LIE TO ME](https://media1.tenor.com/images/98753515461c9cec721477bca6e7131d/tenor.gif?itemid=7875134)



# Installation

## Pre-requisites

Python3 and stuff in requirements.txt

### Python venv Part (not required)
```bash
python3 -m venv venv
source venv/bin/activate
```

### Using requirements.txt
```bash
pip3 install -r requirements.txt
```


## Deployment

### For Development
For a simple development deployment using `runserver`, do this.

```bash
python3 manage.py runserver
```

For more info, look at [this](https://github.com/itsnamgyu/django-two/wiki/Deployment-on-AWS-Part-1).

### For Production

For production deployment using Apache and WSGI, look at [this](https://github.com/itsnamgyu/django-two/wiki/Deployment-on-AWS-Part-2) for Ubuntu 16.04 running on AWS EC2.



# Contribution

## Project Structure

~~Will employ [this structure](https://www.revsys.com/blog/2014/nov/21/recommended-django-project-layout/)...~~~

Too [complicated](https://www.youtube.com/watch?v=5NPBIwQyPWE) and doesn't really tell you how to divide the project into apps.

Lets try to use common sense and group things into apps based on the models they interact with, i.e., everything about showing, editing cafes should be grouped into the `cafe` app.

Thanks to [J. C. Leitão@StackOverlflow](https://stackoverflow.com/questions/18270898/django-best-practice-for-splitting-up-project-into-apps)


## Coding Convensions

Follow the pep8 coding guide (no-brainer for Python). Try to check your code with flake8 before committing. It's included in requirements.txt! Just do this.

```bash
flake8 ho.py
```



# License

MIT License

Copyright (c) 2018 Mogak Co. Ltd.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
