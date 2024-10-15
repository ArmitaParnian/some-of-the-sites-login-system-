
import re
import sys



def main():
    
          email = input("what's your name?").strip()
          if re.search(r"^\w+@\w+\.(com|edu|gov|net|org|youtube)$",email):
             print("Valid")

             print((input("HTML: ")))
             youtube = input("what's your link?").strip()
             username,domain = youtube.split("//")
             if username and "." in domain:
                print()



          else :
              print("Invalid")
              while True:
            
                email = input("what's your link?").strip()
                if re.search(r"^\w+@\w+\.(com|edu|gov|net|org|youtube)$",email):
                    print("Valid")

                    print((input("HTML: ")))
                    youtube = input("what's your link?").strip()
                    username,domain = youtube.split("//")
                    if username and "." in domain:
                        print()


if __name__ == "__main__":
    main()
