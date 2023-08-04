# ----------------------------------------------
# hits.py - searches CVEs for hits given the data from 
#       scanner.py function
# ----------------------------------------------

packages_dict = {}

def hits(version_file):
    # clean txt file 
    version_file = ".\\" + version_file
    print("file: " + version_file)
    clean_text(version_file)    
    # search JSON CVE for each program in txt file

    # record any hits in crit_hits.txt + their severity
    pass

def clean_text(version_file):
    # parse name and version into dictionary
    temp_package_name = ""
    temp_package_version = ""

    #try:
    with open(version_file) as file:
        for line in file:

            if line.split() == ["\x00"]:
                pass
            else:
                # because the data came straight from CMD, we have to do a little extra cleanup
                # this is the only method I found that put the data in a usable state
                split_line = line.split("\x00")
                new_str = "".join(split_line)
                tokens = new_str.split(" : ")                    
                print(tokens)
                
                if tokens[0] == "Name   ":
                    # add name to temp var
                    temp_package_name = "".join(tokens[1].split("\n"))
                elif tokens[0] == "Version":
                    # add version to temp var
                    temp_package_version = "".join(tokens[1].split("\n"))
                    # add package name and version to dictionary
                    packages_dict[temp_package_name] = temp_package_version
                    
                    # clear out values for next pair
                    temp_package_name = ""
                    temp_package_version = ""

                    
    #except:
        #print("issue opening file: " + version_file)
        #return

        file.close()



        # line_hex = line.split("\x00")
        #             new_line = "".join(line_hex)
        #             new_line = new_line.split()
        #             print(new_line)

    print(packages_dict)
    return

hits(".\LAPTOP-1SL7MVV3_version_packages.txt")