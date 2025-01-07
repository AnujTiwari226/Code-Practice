import DLL as dll


class DLLMain:
    print('Doubly Linked List - ', end='\n')
    print('Insert node in different ways')
    llist = dll.DLL()
    llist.insert_first(10)
    llist.insert_first(5)
    llist.display()
    llist.insert_in_end(20)
    llist.insert_in_end(25)
    llist.insert_in_end(40)
    llist.insert_in_end(50)
    llist.display()
    llist.insert_in_middle(target=25, data=30)
    llist.display()
    print('Delete node in different ways')
    print('Deleted First node : ', llist.delete_first())
    llist.display()
    llist.delete_from_middle(target=20, data=25)
    llist.display()
    llist.delete_from_end()
    llist.display()


