from bs4 import BeautifulSoup
import urllib
import generator

'''
Retrieve the CIK number of a company by providing a ticker symbal.
For example: Ticker symbol for Apple Inc. is AAPL
'''
def getCIK(ticker):
	tickerURL = "https://www.sec.gov/cgi-bin/browse-edgar?CIK=" + ticker + "&Find=Search&owner=exclude&action=getcompany&output=atom"
	reader = urllib.urlopen(tickerURL).read()
	soup = BeautifulSoup(reader, "html.parser")
	cikContainer = soup.select("cik")
	cik = cikContainer[0].getText()
	return cik

'''
Retrieve and parse a list of link for all 13F reports of a company. Since default display number is 40 records, the next batch of links will
be fetched if Next 40 is found
'''
def getReportList(ticker):
	reportLinks = []
	cik = getCIK(ticker)
	resultURL = "https://www.sec.gov/cgi-bin/browse-edgar?CIK=" + cik + "&Find=Search&owner=exclude&action=getcompany"
	reader = urllib.urlopen(resultURL).read()
	soup = BeautifulSoup(reader, "html.parser")
	rows = soup.find("table", {"class": "tableFile2"}).find_all("tr")
	for row in rows:
		try:
			targets = row.findAll("td")
			target = targets[0].get_text()
			if target.split("-")[0] == "13F":
				reportLinks.append(targets[1].find("a").get("href"))
		except:
			pass

	moreRecord = soup.find("input", {"value": "Next 40"})
	start = 40
	count = 40
	while moreRecord:
		nextURL = "https://www.sec.gov/cgi-bin/browse-edgar?CIK=" + cik + "&Find=Search&owner=exclude&action=getcompany&start=%s&count=%s" % (start, count)
		nextReader = urllib.urlopen(nextURL).read()
		nextSoup = BeautifulSoup(nextReader, "html.parser")
		nextRows = nextSoup.find("table", {"class": "tableFile2"}).find_all("tr")
		for row in nextRows:
			try:
				nextTargets = row.findAll("td")
				nextTarget = nextTargets[0].get_text()
				if nextTarget.split("-")[0] == "13F":
					reportLinks.append(nextTargets[1].find("a").get("href"))
			except:
				pass

		start += 40
		moreRecord = nextSoup.find("input", {"value": "Next 40"})

	if len(reportLinks) > 0:
		'''
		Only one report is return for demo purposes (defualt 13F-HR). To see the generated text for other types of 13F reports,
		please change reportLinks[0] to reportLinks[-1] for 13F-NT or reportlinks[51] for 13F-HR/A.
		'''
		# return reportLinks[-1]
		# return reportLinks[51]
		return reportLinks[0]
	else:
		return None

'''
Retrieve and parse the link of the 13F report where the fund holding information is stored in a txt file.
'''
def getReportLink(reportURL):
	resultURL = "https://www.sec.gov" + reportURL
	reader = urllib.urlopen(resultURL).read()
	soup = BeautifulSoup(reader, "html.parser")
	rows = soup.find("table", {"class": "tableFile"})
	for row in rows:
		try:
			targets = row.findAll("td")
			target = targets[1].get_text()
			if target == "Complete submission text file":
				return targets[2].find("a").get("href")
		except:
			pass

	return None

'''
Determine whether the txt file is xml formatted. If it is xml formatted, the file will be feeded to the generator to
generate tab-delimited text. If not, text will be extracted from the file and displayed.
'''
def infoScrapping(txtURL):
	resultURL = "https://www.sec.gov/" + txtURL
	reader = urllib.urlopen(resultURL).read()
	soupXML = BeautifulSoup(reader, "lxml-xml")
	isXML = soupXML.find("XML")
	if not isXML:
		soup = BeautifulSoup(reader, "html.parser")
		print (soup.get_text())
	else:
		generator.headerInfo(soupXML)
		generator.infoTable(soupXML)

