class PrimeGenerator:
    def __init__(self):
        self.x = 1
        self.primes = self.Sieve(self.x)
    def Sieve(self,x):
        prime_list = []
        n = self.x
        for i in range(2, n+1):
            if i not in prime_list:
                print (i)
                for j in range(i*i, n+1, i):
                    prime_list.append(j)
        return prime_list     
    def Next(self):
        self.x +=1
        return self.Sieve(self.x)       
    def Get(self):
        return self.primes 

t = PrimeGenerator()
for i in range(100):
    print("================")
    print(t)
    t.Next()
