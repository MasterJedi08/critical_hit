# ---------------------------------------------- 
# bonfire.py - "central/main" piece of critical_hit 
#   -> interacts with user and calls other files/functions
# ----------------------------------------------
import scanner
import reporter
import hits

def main():
    # tells user that program is running
    print("\n----WELCOME TO CRITICAL_HIT----\n")
    #print("will your computer pass the test?")

    # calls <function> (scanner.py) to begin scanning files
    VERSION_FILE, hostname = scanner.scanner()

    # check for any CVE hits[not rn]
    # currently just cleans up the data
    packages_dict = hits.hits(VERSION_FILE)

    # generate report (reporter.py)
    reporter.reporter(packages_dict, hostname)

    # print report
    print("\nREPORT GENERATED...\n")
    print("FILES: \n-" + hostname + "_detailed_packages.txt : detailed information for each software")
    print("-" + hostname + "_version_packages.txt : basic information (name and version) for each software")
    print("-" + hostname + "_systeminfo.txt : system, IP, and user information ")
    print("-" + hostname + "_REPORT.txt : report of software name and version, divided by Microsoft and Non-Microsoft softwares")
    print("\n----GAME OVER----\n")

    # end
    return

if __name__ == '__main__':
    main()

# --------------------------
# maybe use https://docs.opencve.io/
# --------------------------