# Wiki Summarizer
##### Justin Romeo
## _Fall 2019_
##### _Summary Generation_

First, you must have _Python3_ installed on your system. When you install _Python3_, be sure to 
check the box to add _Python3_ to your computer's PATH. 

Now that _Python3_ is installed on your system, you need to install _pip3_. Enter the following commands to install _pip_:

    ~ curl -O https://bootstrap.pypa.io/get-pip.py
    ~ sudo python3 get-pip.py
    
Now that pip is installed, run the following commands to install _NLTK_, _numpy_, _bs4_, and _urllib.requests_.

    ~ sudo pip3 install -U nltk
    ~ sudo pip3 install -U numpy
    ~ sudo pip3 install -U beautifulsoup4
    ~ sudo pip3 install -U urllib
    ~ sudo pip3 install -u requests
    

In order to run this application, run _Python3_ in the terminal window and import the following:

    >>> import nltk
    >>> import bs4
    >>> import numpy
    >>> import urllib
    >>> import requests
    >>> nltk.download('punkt')
    >>> nltk.download('stopwords')

Using a Python3 specific IDE will ensure all imports are installed automatically if needed.
_Pycharm_ was used for development in this case for its autocomplete and automatic updating abilities.


In order to run _term.py_, you must navigate to its directory and run:

    ~ python3 term.py
    
The output of the program will be named _output.txt_. It is located in the same directory as _term.py_.

## _Implementation_
The current implementation is as follows. The program, will generate a URL for a random wiki page. The URL and will first parse every word (taking out some unnecessary characters). Next, the occurrences of each word are calculated and then entered into a frequency dictionary with the specified names being explicitly placed at the highest frequency. Next, the website is parsed into sentences, where the frequency of each word in the sentence is summed to achieve a finished sentence frequency. Finally, the 7 sentences with the highest frequencies are taken and added to the output file.
