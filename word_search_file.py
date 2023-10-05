with open('poem.txt','r') as f:
     text=f.read().lower().split()

found=False
if "twinkle" in text:
   found=True

if found:
    print("found it")
else: print("did not found")