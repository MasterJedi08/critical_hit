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
FILENAME = ""
INFO_FILE = ""

def scanner():

# -------------------------------------------------
# -------------------------------------------------
    # GET COMPUTER GENERAL DATA
# -------------------------------------------------
# -------------------------------------------------

    # create file using 
	#	hostname_systeminfo.txt for general system info
	# 	hostname_packages.txt for packages report
	hostname = sp.getoutput("hostname")
	hostname_tokens = hostname.split('.')
	FILENAME = hostname_tokens[0] + "_packages.txt"
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
	#sp.run('powershell.exe "Get-Package -MinimumVersion 0.0 | Sort-Object Name | ft Name,Version,ProviderName >> secretinfohehe.txt"')
	
	# get installed packages (FULL PROPERTIES) - save to diff file
	#sp.run('powershell.exe "Get-Package -MinimumVersion 0.0 | Select-Object -Property * | Sort-Object Name >> secretinfohehe.txt"')
	
    

    # return to bonfire
	#file.close()
	return()
        
scanner()