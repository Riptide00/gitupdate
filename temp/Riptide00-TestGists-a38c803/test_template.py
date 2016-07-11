import os
import shutil


def main():
    try:
        print("Test functions with verbal output.")
        print("[+] Test is succesfull.")
    except:
        print("[-] Test failed.")
        raise
    print("[!] Test done.")


def external_test():
    try:
        # Re-do test here without verbal output for automated test
        return True
    except:
        return False


def cleanup(verbal):
    # Add files created by your test script, if any (Add to or remove cleanup
    # freely)
    remove = []
    for r in remove:
        try:
            os.remove(r)
            if verbal:
                print("[+] Removed " + r)
        except:
            try:
                shutil.rmtree(r)
                print("[+] Removed " + r)
            except:
                if verbal:
                    print("[-] Cleanup failed to remove " + r)
    if verbal:
        print("[!] Cleanup done.")

if __name__ == '__main__':
    main()
