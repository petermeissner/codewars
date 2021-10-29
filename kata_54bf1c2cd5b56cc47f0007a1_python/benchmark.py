from my_solution import duplicate_count as my_solution
from use_collections import duplicate_count as use_collections
from use_sets import duplicate_count as use_sets
from use_list_comprehension import duplicate_count as use_list_comprehension

from time import time


def timereps(func_dict: dict, arg_list: list = [], reps = 10000):
  res = {}
  
  for func_name in  func_dict:
    func = func_dict[func_name]
    # measure timing
    start = time()
    for i in range(0, reps):
        func(*arg_list)
    end = time()
    # store results
    print(f'{func_name:>25}:  ' + f'{(reps / (end - start)):,.0f} runs per second')


timereps(
  func_dict = dict(
    my_solution=my_solution, 
    use_collections=use_collections, 
    use_sets=use_sets, 
    use_list_comprehension=use_list_comprehension
  ),
  arg_list=['klasbfgiwurlkansdfgkbsndfglkbsdflgkbsdlfgbldfbsglkdfsbglkdfsbglkdfsbglkdsbfglkdsbfglkbdflblLKBLKBLKBLKBLIBIUBÜPLP)U)$ebvlkybvluwrehwe2p549624506723986741283z4ÄÜÖAÜSDFRWEAGJERBDFSBNERGOBJSFBGDSDFB']
)



