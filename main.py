import algorithm as algo
import visualizer as viz

# still need to work on the texts xD

ASK_ALGO_TEXT = """
Algorithm:
1. Quick Sort
2. Merge Sort
0. Exit
Enter choice: """

ASK_TYPE_TEXT = """
Which type of array?
1. randomly generated array
2. I'll provide the array
0. Exit
Enter choice: """

ASK_RANDOM_TEXT = f"""
Enter the number (between {viz.Visualier.MIN_ARRAY_LENGTH} and {viz.Visualier.MAX_ARRAY_LENGTH}) of elements you would like to have in the array.
Enter 0 to exit.
Enter number: """

ASK_ARRAY_TEXT = f"""
Enter your 1 dimensional array. Please enter an array of length between {viz.Visualier.MIN_ARRAY_LENGTH} and {viz.Visualier.MAX_ARRAY_LENGTH}.
Example: [1,4,2,3]
Enter 0 to exit.
Enter array: """


def get_algo_response():
    try:
        response = int(input(ASK_ALGO_TEXT).strip())
    except Exception:
        return get_algo_response()

    if response==0:
        exit()
    elif response==1:
        return algo.QuickSort()
    elif response==2:
        return algo.MergeSort()
    else:
        return get_algo_response()


def get_type_response(sort_algo):
    try:
        response = int(input(ASK_TYPE_TEXT).strip())
    except Exception:
        get_type_response(sort_algo)

    if response==0:
        exit()
    elif response==1:
        get_random_array_response(sort_algo)
    elif response==2:
        get_array_response(sort_algo)
    else:
        get_type_response(sort_algo)


def get_random_array_response(sort_algo):
    try:
        response = int(input(ASK_RANDOM_TEXT).strip())
        if response>viz.Visualier.MAX_ARRAY_LENGTH: raise
    except:
        get_random_array_response(sort_algo)

    if response==0: exit()
    sort_algo.set_random_array(response)


def get_array_response(sort_algo):
    try:
        response = input(ASK_ARRAY_TEXT).strip()
        response = response.strip('[').strip(']')       # remove square brackets
        array = response.split(',')                     # turn given array into list
        array = list(map(int, array))                   # turn elements into integers

        if len(array)>viz.Visualier.MAX_ARRAY_LENGTH: raise
    except:
        get_array_response(sort_algo)

    if response=='0': exit()
    sort_algo.set_array(array)


if __name__ == "__main__":
    sort_algo = get_algo_response()
    get_type_response(sort_algo)
    sort_algo.sort()
