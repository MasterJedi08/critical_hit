# ---------------------------------------------- 
# bonfire.py - "central/main" piece of critical_hit 
#   -> interacts with user and calls other files/functions
# ----------------------------------------------
import scanner
import reporter

def main():
    # tells user that program is running
    print("----WELCOME TO CRITICAL_HIT----")
    print("will your computer pass the test?")

    # calls <function> (scanner.py) to begin scanning files
    scanner.scanner()

    # generate report (reporter.py)

    # print report

    # end
    pass

if __name__ == '__main__':
    main()