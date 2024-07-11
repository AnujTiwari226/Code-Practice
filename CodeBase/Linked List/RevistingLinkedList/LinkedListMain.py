import BasicSinglyLinkedListSolutions as BsL
import AdvancedSinglyLinkedListSolutions as AsL
import  LinkedListPS as llps

def BasicSinglyLinkedListMethods():
    obj = BsL.BasicSolution(10)
    print('Original LinkedList : ', end='')
    obj.display()
    obj.insert_at_beginning(20)
    obj.insert_at_beginning(30)
    obj.insert_at_beginning(40)
    obj.insert_at_beginning(50)
    obj.display()
    obj.insert_at_middle(25, 30)
    obj.display()
    obj.insert_at_last(5)
    obj.display()
    obj.delete_first()
    obj.display()
    obj.insert_at_middle(27, 25)
    obj.display()
    obj.delete_from_middle(25)
    obj.display()
    obj.delete_from_middle(27)
    obj.display()
    obj.delete_from_last()
    obj.display()


def create_lls(obj):
    headA, headB = obj.create_ll_with_intersection([4, 1], [5, 6, 1], [8, 4, 5])
    # gives Time limit exceeds error as you're travering both the lists
    # pa = obj.getIntersectionNode(headA=headA, headB=headB)
    pa = obj.getIntersectionNodeInOptimizedWay(headA, headB)

    print("Linked List A:")
    obj.display_list(headA)

    print("Linked List B:")
    obj.display_list(headB)

    print("Intersect Linked List: ")
    obj.display_list(pa)


def AdvancedSinglyLinkedListMethods():
    obj = AsL.Solution(10)
    print('Original LinkedList : ', end='')
    obj.display()
    obj.insert_at_last(20)
    obj.insert_at_last(30)
    obj.insert_at_last(40)
    obj.insert_at_last(50)
    obj.display()
    obj.create_a_cycle(30)
    print(f"Checking if Cycle present in Linked list- {obj.hasCycle()}")
    obj.display_cycle()
    create_lls(obj)


def LinkedListProblemStatementsMain():
    obj = llps.Solution(5)
    obj.insert_at_beginning(5)
    obj.insert_at_beginning(3)
    obj.insert_at_beginning(3)
    obj.insert_at_beginning(2)
    obj.insert_at_beginning(2)
    obj.insert_at_beginning(1)
    head = obj.get_curr_head()
    val= obj.RemoveDuplicate(head)
    obj.display()



if __name__ == '__main__':

    # BasicSinglyLinkedListMethods()
    # AdvancedSinglyLinkedListMethods()
    LinkedListProblemStatementsMain()