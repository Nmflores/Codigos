class No:
    def __init__(self,valor):
        self.dado=valor
        self.next=None
        self.previous=None


class Lista:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,valor):

        if self.head is None:
            self.head = self.tail =No(valor)
        else:
            self.tail.next=No(valor)
            self.tail=self.tail.next


lista = Lista()

for i in range(0,10):
    lista.append(i)

  
i = lista.head
while i is not None:
    print(i.dado)
    i = i.next

        