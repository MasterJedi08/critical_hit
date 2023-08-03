# critical_hit

<h3>What is it? </h3>
Python program that takes a list of all programs on your Windows device and checks it against CVE records to determine if their is a "critical hit".  

<h3>Files and What They Do</h3>
<ul style="list-style-type:none;">
  <li>bonfire.py - main() function, calls all other files</li>
  <li>scanner.py - uses command prompt to scan for system information and installed packages</li>
  <li>hits.py - takes the information from scanner.py to see if any installed software (based on its version) was flagged in a CVE</li>
  <li>reporter.py - takes info from hits.py and generates a report based on how many hits came back</li>
</ul>

<h3>Project Status</h3>
Currently a work in progress

<h3>Known Errors: </h3>


<h3>DISCLAIMER</h3>
This program is not made to accuractely depict all possible vulnerabilities in your Windows system. This should NOT be used as a security measure and is merely a fun personal project. Any harm that comes from using this program or making security decisions based on the results of this program is not the GitHub creator's (MasterJedi08) responsibility. Please do not take this as true cybersecurity advice.
