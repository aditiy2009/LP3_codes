import random
from fractions import gcd

def check_prime(no):
    for i in (2,no):
        if(no%i == 0):
            break
        else:
            return no
    return 0;

def two_prime_no():
    no1 = check_prime(random.randint(2,50))
    no2 = check_prime(random.randint(2,50))
    while True:
        if(no1 != 0 and no2 == 0):
            no2 = check_prime(random.randint(2,50))
        elif(no1 == 0 and no2 != 0):
            no1 = check_prime(random.randint(2,50))
        elif(no1 == 0 and no2 == 0):
            no1 = check_prime(random.randint(2,50))
            no2 = check_prime(random.randint(2,50))
        else:
            break
    return(no1,no2)

class rsa_algo:

    def __init__(self,p,q):
        self.ek_set = []
        self.dk_set = []
        self.em_set = []
        self.dm_set = []
        self.p = p
        self.q = q
        self.phi = (p-1)*(q-1)
        self.n = p*q

    def find_ek(self):
        for i in range(2,self.phi):
            if(gcd(i,self.phi) == 1):
                self.ek_set.append(i)

    def find_dk(self):
        for val in self.ek_set:
            for i in range(1,100):
                n = ((self.phi*i)+1)/val
                if(isinstance(n,int)):
                    self.dk_set.append(n)
                    break

    def encrypt(self,m):
        for ek in self.ek_set:
            self.em_set.append((m**ek)%self.n)

    def decrypt(self):
        for dk,em in zip(self.dk_set,self.em_set):
            self.dm_set.append((em**dk)%self.n)

    def printvalues(self):
        for ek,dk,em,dm in zip(self.ek_set,self.dk_set,self.em_set,self.dm_set):
            print(ek,dk,em,dm)

def main():
    n1,n2 = two_prime_no()
    user = rsa_algo(3,11)
    user.find_ek()
    user.find_dk()
    print('\n')
    print("msg to be encrpted: 25")
    user.encrypt(25)
    user.decrypt()
    print('printing various keys and their results......')
    print('\n')
    print('encryption key, decryption key, encrpted msg, decrypted msg')
    user.printvalues()

if __name__ == '__main__':
    main()
