f=open("Untitled.txt","r")
text=f.readlines()
out=open("Out1.txt","w")
for ch in text:
    w='"'+ch+'",'
    out.write(w.replace("\n",""))
out.close()
