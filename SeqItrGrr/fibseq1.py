class Fibonacci:
    def __init__(self):
        self.seq = [0,1,1]
        self.maxKey = 10000

    def computeTo(self,key):
        for idx in range(len(self.seq), key + 1):
            v = self.seq[idx - 1] + self.seq[idx - 2]
            self.seq.append(v)

    def __getitem__(self,key):
        if not isinstance(key,int):
            raise TypeError
        if key <=0 or key > self.maxKey:
            raise IndexError
        if key > len(self.seq):
            self.computeTo(key)
        return self.seq[key]

    def __setitem__(self,key,value):
        if not isinstance(key,int):
            raise TypeError
        if key <=0 or key > self.maxKey:
            raise IndexError
        if key > len(self.seq):
            self.computeTo(key)
        self.seq[key] = value

    def __len__(self):
        return self.maxKey

f = Fibonacci()
print("f[20]=",f[20])
f[10] = "熊孩子"
for i in range(1,21):
    print(f[i],end=",")
print("")
print("Length of f:",len(f))