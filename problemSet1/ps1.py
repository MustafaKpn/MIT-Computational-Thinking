###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_loaded = []
    ship_load = []
    l = len(cows)
    while len(cows_loaded) != l:
        weight = 0
        trip = []
        checked = []
        for i in range(len(cows)):
            heaviest_weight = 0
            for i, k in cows.items():
                if k > heaviest_weight and (i not in checked):
                    heaviest_weight = k
                    heaviest_cow = i

            if (heaviest_weight + weight) <= limit:
                trip.append(heaviest_cow)
                weight += heaviest_weight
                cows.pop(heaviest_cow)
                cows_loaded.append(heaviest_cow)
            else:
                checked.append(heaviest_cow)
        if len(trip) != 0 and (trip not in ship_load):
            ship_load.append(trip)
    return ship_load


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_list = get_partitions(list(cows.keys()))
    def weight_check(cows_list, limit):
        check = True
        for i in cows_list:
            weight = 0
            for x in i:
                weight += cows[x]
            if weight > limit:
                check = False
                break
        if check == True:
            return cows_list
    solutions = []
    for i in cows_list:
        status = weight_check(i, limit)
        if type(status) == list:
            solutions.append(status)
    min = 10
    for i in solutions:
        if len(i) < min:
            min = len(i)
            solution = i
    return solution

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    import time
    cows = load_cows("ps1_cow_data.txt")
    limit=100
    gready_time1 = time.time()
    greedy_cow_transport(cows, limit)
    gready_time2 = time.time()
    comp1 = gready_time2 - gready_time1


    brute_time1 = time.time()
    brute_force_cow_transport(cows, limit)
    brute_time2 = time.time()
    comp2 = brute_time2 - brute_time1

    if comp1 > comp2:
        print('The brute force algorithm is faster')
    elif comp2 > comp1:
        print('The gready algorithm is faster')


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


