from .linkedlist.linkedlist import LinkedList


def answer_one():
    """Answer to question 1. Calls create_and_move.sh shell script."""
    import subprocess

    result = subprocess.run(
        ["bash", "../scripts/create_and_move.sh"], capture_output=True, text=True
    )
    return f"Shell script executed. Output:\n{result.stdout}\nError (if any):\n{result.stderr}"


def answer_two():
    """Create and demo linked list in python"""
    # Example: using the new 'except*' syntax (PEP 654) for demonstration

    try:
        print("Inside the try block")
        ll = LinkedList()
        print("Created the linked list")
        ll.insert_at_beginning(5)
        ll.insert_at_beginning(4)
        ll.insert_at_beginning(3)
        ll.insert_at_beginning(2)
        ll.insert_at_beginning(1)

        print(ll)

    except Exception:
        print("Handled exception group: ")


if __name__ == "__main__":
    pass
