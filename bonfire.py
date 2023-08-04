# ---------------------------------------------- 
# bonfire.py - "central/main" piece of critical_hit 
#   -> interacts with user and calls other files/functions
# ----------------------------------------------
import scanner
import reporter
import hits

def main():
    # tells user that program is running
    print("----WELCOME TO CRITICAL_HIT----")
    print("will your computer pass the test?")

    # calls <function> (scanner.py) to begin scanning files
    VERSION_FILE = scanner.scanner()

    # check for any CVE hits
    hits.hits(VERSION_FILE)

    # generate report (reporter.py)

    # print report

    # end
    pass

if __name__ == '__main__':
    main()

# --------------------------
# maybe use https://docs.opencve.io/
# --------------------------