

print ("hi! foobar!")
import sys
import module_jxkh_main

if __name__=="__main__":
    print("main")
    if len(sys.argv) < 2:
        print("no enough arguments!! Please check args")
        sys.exit();
    if (sys.argv[1] == "jxkh"):
        module_jxkh_main.jxkh_main()
    else:
        print("no support commnad %s",sys.argv[1])
    
        

