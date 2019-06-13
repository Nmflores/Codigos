class No:
    def __init__(self,valor):
        self.dado=valor
        self.next=None
        self.previous=None
    def get_next(self):
        return self.next

    def set_next(self,novo_next):
        self.next = novo_next
    def get_previous(self):
        return self.previous
    def set_previous(self,novo_previous):
        self.previous = novo_previous  
    def get_dado(self):
        return self.dado 
    def set_dado(self,novo_dado):
        self.dado = novo_dado     
class Lista:
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self,valor):

        if self.head is None:
            self.head = self.tail =No(valor)
         

        else:
            self.tail.set_next(No(valor))
            self.tail=self.tail.get_next()
          

    def remove(self):
        i = self.head
        anterior = None
        while i is not None:
            if i.get_next() is self.tail:
                anterior = i

            i = i.next

        anterior.set_next(None)

    def adicionaPrimeiro(self,valor):
        novoNo = No(valor)
        novoNo.set_next(self.head)
        self.head =  novoNo 
                
       

    def mostrarLista(self):
        i = lista.head
        while i is not None:
            print(i.dado)
            i = i.next

lista = Lista()

for i in range(0,10):
    lista.append(i)
    
lista.mostrarLista()
lista.remove()
lista.mostrarLista()


        