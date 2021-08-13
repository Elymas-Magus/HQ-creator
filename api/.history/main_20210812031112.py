from App import App
import sys

def main():
    app = App(getDestinationPath(), sys.argv)

    print(sys.argv)

def getDestinationPath():
    return sys.argv[1]

def getOriginPaths():
    return sys.argv[2:]
        
if __name__  == "__main__":
    main()
        