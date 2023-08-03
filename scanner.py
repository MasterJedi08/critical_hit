# ----------------------------------------------
# scanner.py - scans system for executable files and
#       the system itself to check against CVE
# ----------------------------------------------
import subprocess as sp
import os
import platform

# -------------------------------------------------
    # CONSTANTS
# -------------------------------------------------
# POWERSHELL = sp.getoutput("where powershell")
DETAIL_FILE = ""
VERSION_FILE = ""
INFO_FILE = ""

def scanner():

# -------------------------------------------------
# -------------------------------------------------
    # GET COMPUTER GENERAL DATA
# -------------------------------------------------
# -------------------------------------------------

    # create file using 
	#	hostname_systeminfo.txt for general system info
	# 	hostname_full_report_packages.txt for full detail packages report
	# 	hostname_version_packages.txt for package names + versions
	hostname = sp.getoutput("hostname")
	hostname_tokens = hostname.split('.')
	DETAIL_FILE = hostname_tokens[0] + "_full_report_packages.txt"
	VERSION_FILE = hostname_tokens[0] + "_version_packages.txt"
	INFO_FILE = hostname_tokens[0] + "_systeminfo.txt"
	# file = open(FILENAME, "w")
	#infofile = open(FILENAME, "w")

	# get basic system info
	sp.getoutput(str("echo 'SYSTEM' >> " + INFO_FILE))
	sp.getoutput(str("systeminfo >> " + INFO_FILE))
	
	# get ip info
	sp.getoutput(str("echo . >> " + INFO_FILE + " && echo . >> " + INFO_FILE + "&& echo 'IP' >> " + INFO_FILE))
	sp.getoutput(str("ipconfig /all >> " + INFO_FILE))

	# get user info
	sp.getoutput(str("echo . >> " + INFO_FILE + " && echo . >> " + INFO_FILE + "&& echo 'USER' >> " + INFO_FILE))
	sp.getoutput(str("net user >> " + INFO_FILE))
	
# -------------------------------------------------
# -------------------------------------------------
	# GET INSTALLED PACKAGES
# -------------------------------------------------
# -------------------------------------------------
	# get installed packages - save to diff file
	sp.getoutput('powershell.exe "Get-Package -MinimumVersion 0.0 | Sort-Object Name | ft Name,Version,ProviderName >> %s"' % (VERSION_FILE))
	
	# get installed packages (FULL PROPERTIES) - save to diff file
	sp.getoutput('powershell.exe "Get-Package -MinimumVersion 0.0 | Select-Object -Property * | Sort-Object Name >> %s"' % (DETAIL_FILE))
	
    

    # return to bonfire
	#file.close()
	return()
        