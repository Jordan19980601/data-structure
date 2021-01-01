#反轉節點
class SLinkedList:
    def regress(self):
        prev=None
        while self.head is not None:
            current=self.head
            self.head=current.next
            current.next=prev
            prev=current
        self.head=prev
single=SLinkedList()
print('連接串列')
for item in range(10,20):
    item= random.randint(1,10)
    single.append(item)
single.show()
single.regress()
print('\n翻轉節點:')
single.show()

