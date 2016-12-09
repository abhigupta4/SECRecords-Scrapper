"""
Generate output from the target XML.
"""
def headerInfo(soup):
	root = soup.find("XML").find("headerData")
	if root.submissionType:
		print "\n"
		print "Submission Type: {}".format(root.submissionType.string)
	if root.filerInfo:
		child = root.filerInfo
		if child.liveTestFlag:
			print "Live Test Flag: {}".format(child.liveTestFlag.string)
		if child.filer.credentials:
			print "Filter:"
			print "Credentials:"
			print "CIK: {}  CCC: {}".format(child.filer.credentials.cik.string,child.filer.credentials.ccc.string)
		if child.periodOfReport:
			print "Period of Report: {}".format(child.periodOfReport.string)
		print "\n"

	formData = soup.find("XML").find("formData")
	if formData.coverPage:
		child = formData.coverPage
		if child.reportCalendarOrQuarter:
			print "Report Calendar or Quarter: {}".format(child.reportCalendarOrQuarter.string)
		if child.isAmendment:
			print "isAmendment: {}".format(child.isAmendment.string)		
		if child.filingManager:
			print "Filing Manager:"

			if child.filingManager.find("name"):
				print "Name: {}".format(child.filingManager.find("name").getText())
			if child.filingManager.address:
				address = child.filingManager.address
				street,city,state,zipcode=None,None,None,None
				street,city,state,zipcode= address.street1.string,address.city.string,address.stateOrCountry.string,address.zipCode.string
				print "Address:{} {} {} {}".format(street,city,state,zipcode)

		if child.reportType:
			print "Report Type: {}".format(child.reportType.string)
		if child.form13FFileNumber:
			print "Form 13F File Number: {}".format(child.form13FFileNumber.string)
		if child.provideInfoForInstruction5:
			print "Provide Info for Instruction5: {}".format(child.provideInfoForInstruction5.string)				
		print "\n"

	if formData.signatureBlock:
		child = formData.signatureBlock
		print "Signature Block:"
		if child.find("name"):
			print "Name: {}".format(child.find("name").getText())
		if child.title:
			print "Title: {}".format(child.title.string)
		if child.phone:
			print "Phone: {}".format(child.phone.string)	
		if child.signature:
			print "Signature: {}".format(child.signature.string)
		if child.city:
			print "City: {}".format(child.city.string)	
		if child.stateOrCountry:
			print "State or Country: {}".format(child.stateOrCountry.string)	
		if child.signatureDate:
			print "Signature Date: {}".format(child.signatureDate.string)						
		print "\n"

	if formData.summaryPage:
		child = formData.summaryPage	
		print "Summary Page:"
		if child.otherIncludedManagersCount:
			print "Other Included Managers Count: {}".format(child.otherIncludedManagersCount.string)
		if child.tableEntryTotal:
			print "Table Entry Total: {}".format(child.tableEntryTotal.string)
		if child.tableValueTotal:
			print "Table Value Total: {}".format(child.tableValueTotal.string)	
		if child.isConfidentialOmitted:
			print "isConfidential Omitted: {}".format(child.isConfidentialOmitted.string)				
		print "\n"


def infoTable(soup):
	try:
		root = soup.find_all("XML")[1].find("informationTable").find_all("infoTable")
		print "Information Table:"
		for child in root:
			print "\n"
			# print "Info Table: "
			if child.nameOfIssuer:
				print "Name of Issuer: {}".format(child.nameOfIssuer.string)	
			if child.titleOfClass:
				print "Title of Class: {}".format(child.titleOfClass.string)	
			if child.cusip:
				print "CUSIP: {}".format(child.cusip.string)
			if child.value:
				print "Value: {}".format(child.value.string)		

			if child.shrsOrPrnAmt:
				print "Shrs or PrnAmt:"
				nested = child.shrsOrPrnAmt
				if nested.sshPrnamt:
					print "sshPrnamt: {}".format(nested.sshPrnamt.string)	
				if nested.sshPrnamtType:
					print "sshPrnamt Type: {}".format(nested.sshPrnamtType.string)	
			
			if child.votingAuthority:
				print "Voting Authority:"
				nested = child.votingAuthority
				if nested.Sole:
					print "Sole: {}".format(nested.Sole.string)	
				if nested.Shared:
					print "Shared: {}".format(nested.Shared.string)				
				if nested.None:
					print "None: {}".format(nested.None.string)	

			if child.investmentDiscretion:
				print "Investment Discretion: {}".format(child.investmentDiscretion.string)	

			print " "		

	except:
		pass