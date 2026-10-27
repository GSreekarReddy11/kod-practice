names=["Amit","Arjun","Amit","Ansh","Ajay","Arjun","Arav","Amit","amit"]
freq={}   
for i in names:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
