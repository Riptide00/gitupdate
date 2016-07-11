
import copy as machine
import os
import subprocess
import sys

import config


def main():
    python_gists_location = config.gists_location
    dirs = get_immediate_subdirectories(python_gists_location)
    print()
    print("Python gists")
    print("============")
    print()
    for d in dirs:
        if d not in config.ignore:
            print(d)
            print("-" * len(d))
            print()
            testscript_directory = python_gists_location + "\\" + d
            testscript_path = testscript_directory + "\\test.py"
            filename = testscript_directory + "\\" + d + ".py"
            if config.python_test:
                check = os.path.isfile(testscript_path)
                if check:
                    print("[+] Found a " + d + " test script.")
                    sys.path.insert(0, testscript_directory)
                    import test
                    test = test.external_test()
                    if test:
                        print("[+] Test script for " + d + " was succesfull.")
                    else:
                        print("[-] Test script for " + d + " failed.")
                else:
                    print("[-] Couldn't find a " + d + " test script.")
                print()
            if config.coverage_report:
                print("Coverage:")
                subprocess.call(["coverage", "report", filename])
                print()
            if config.coverage_run:
                subprocess.call(["coverage", "run", filename])
            if config.coverage_html:
                subprocess.call(["coverage", "html", filename])
                reportname = d + "_html"
                machine.copy("htmlcov", reportname)
            if config.coverage_xml:
                subprocess.call(["coverage", "xml", filename])
                reportname = d + "_xml"
                machine.copy("coverage.xml", reportname)
            print()


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

if __name__ == '__main__':
    main()
