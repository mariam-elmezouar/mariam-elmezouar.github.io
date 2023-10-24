from sorting_algorithms import bubble_sort, insertion_sort, selection_sort, sort_compare


def test_sorting_algorithms():
    # You can modify aList to test with other lists.
    aList = [5, 3, 8, 4, 1]
    print("Sorting the list:", aList)

    # Bubble Sort
    l1 = aList.copy()
    bubble_sort(l1)
    print("Output from Bubble sort:", l1)

    # Selection Sort
    l2 = aList.copy()
    selection_sort(l2)
    print("Output from Selection sort:", l2)

    # Insertion Sort
    l3 = aList.copy()
    insertion_sort(l3)
    print("Output from Insertion sort:", l3)

### READ AND UNDERSTAND THE MAIN FUNCTION ###
### BUT DO NOT MODIFY THE MAIN FUNCTION ###
def main():
    print("Welcome to the Sorting Algorithm Comparison")

    print("\nMenu:")
    print("1. Test the three sorting algorithms with a simple test case")
    print("2. Run a time comparison of the three algorithms")

    choice = input("Enter your choice (1/2): ")

    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            test_sorting_algorithms()
        elif choice == 2:
            sort_compare()
        else:
            print("Invalid choice. Please select a valid option.")
    else:
        print("Invalid input. Please enter a valid choice (1/2).")


main()


