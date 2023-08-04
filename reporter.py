# ----------------------------------------------
# reporter.py - generates report given the data from 
#       hits.py function
# ----------------------------------------------

def reporter(packages, hostname):
    """
    main() function of this file
    """
    # sort into microsoft and non-microsoft software
    microsoft, non_microsoft = sorter(packages)

    # pretty_print(microsoft, non_microsoft)

    # put info into txt document "hostname_REPORT.txt"
    pretty_report(microsoft, non_microsoft, hostname)

    return


def sorter(packages):
    """
    sorts dictionary values in variable packages into microsoft and non microsoft pakages
    returns two values: dictionary "microsoft" and dictionary "non_microsoft"
    """
    microsoft = {}
    non_microsoft = {} 

    # iterate through keys of packages
    for key in packages:
        if "Win" in key or "Microsoft" in key or "MS" in key:
            microsoft[key] = packages[key]
        else:
            non_microsoft[key] = packages[key]

    return microsoft, non_microsoft


def pretty_print(microsoft, non_microsoft):
    """
    prints dictionaries in a nice format
    """

    print("----\nREPORT GENERATED\n----")
    print("\nMICROSOFT SOFTWARE\n")
    for key in microsoft:
        print(key + "  :  Version " + microsoft[key])
    print("\n----\n\nNON-MICROSOFT SOFTWARE\n")
    for key in non_microsoft:
        print(key + "  :  Version " + non_microsoft[key])

    return

def pretty_report(microsoft, non_microsoft, hostname):
    """
    write results to file
    """

    filename = hostname + "_REPORT.txt"
    # create and open file
    file = open(filename, 'w')

    # formatting
    file.write("REPORT GENERATED FOR HOST " + hostname)
    file.write("\n--------------------------------------\n")

    # write microsoft
    file.write("\nMICROSOFT SOFTWARE\n\n")
    for key in microsoft:
        file.write(key + "  :  Version " + microsoft[key] + "\n")

    # write non-microsoft
    file.write("\n----\n\nNON-MICROSOFT SOFTWARE\n\n")
    for key in non_microsoft:
        file.write(key + "  :  Version " + non_microsoft[key] + "\n")

    file.close()
    return