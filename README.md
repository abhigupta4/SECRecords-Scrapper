# SECRecords-Scrapper
A Python web crawler that will fetch and parse fund holdings records from EDGAR(SEC).

* Run $ sudo pip install requirements.txt

*** If error occurs after installing the dependencies from requirements.txt, try running
$ sudo apt-get install python-lxml or $ sudo pip install python-lxml

To run the program:

$ python run.py "ticker symbol" or "CIK number"

For example:

$ python run.py 0001166559 or $ python run.py AAPL
