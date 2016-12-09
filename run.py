import scrapper
from sys import argv

ticker = argv[1]
cikURL = scrapper.getReportList(ticker)
if cikURL:
	resultURL = scrapper.getReportLink(cikURL)
	if resultURL:
		scrapper.infoScrapping(resultURL)
	else:
		print "Page not found."
else:
	print "No 13F-HR Record found for " + ticker

