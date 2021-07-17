class calculator:
    def add(self,a,b):
        print(a+b)

    def sub(self,a,b):
        print(a-b)

    def mul(self,a,b):
        print(a*b)

    def div(self,a,b):
        print(a//b)

    def expo(self,a,b):
        print(a**b)

    def swap(self,a,b):
        temp=a
        a=b
        b=temp
        print("values befor swapping",a,b)
        print("values after swapped",a,b)
class real:
    def main(self):
        cal=calculator()



if __name__=="__main__":
    r=real()
    r.main()
