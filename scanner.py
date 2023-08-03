# ----------------------------------------------
# scanner.py - scans system for executable files and
#       the system itself to check against CVE
# ----------------------------------------------
import subprocess as sp
import platform

# -------------------------------------------------
    # CONSTANTS
# -------------------------------------------------
POWERSHELL = sp.getoutput("where powershell")

def scanner():

# -------------------------------------------------
# -------------------------------------------------
    # GET COMPUTER GENERAL DATA
# -------------------------------------------------
# -------------------------------------------------

    # create file using hostname_systemreport.log
	hostname = sp.getoutput("hostname")
	hostname_tokens = hostname.split('.')
	filename = hostname_tokens[0] + "_system_report.log"
	file = open(filename, "w")
	
	# get basic system info
	system_info = sp.getoutput("systeminfo")

	# get ip info
	ipconfig = sp.getoutput("ipconfig /all")
	
# -------------------------------------------------
# -------------------------------------------------
	# GET INSTALLED PACKAGES
# -------------------------------------------------
# -------------------------------------------------
	# get installed packages - save to diff file
	package_versions = sp.getoutput('powershell -command "Get-Package -MinimumVersion 0.0 | Sort-Object Name | ft Name,Version,ProviderName >> secretinfohehe.txt"', shell=True)
	
	# get installed packages (FUILL PROPERTIES) - save to diff file
	package_versions_extended = sp.getoutput('powershell -command "Get-Package -MinimumVersion 0.0 | Select-Object -Property * | Sort-Object Name >> secretinfohehe.txt"', shell=True)
	

    # clean txt file -> anything that doesn't have a version should not be used in next part

    # search JSON CVE for each program in txt file

    # record any hits in hits.txt + their severity

    # return to bonfire
	file.close()
	return()
        
scanner()