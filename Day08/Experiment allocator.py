#Basic experiment allocator

from random import shuffle


roll_start = int(input("enter starting roll number : "))
roll_end   = int(input("enter ending roll number   : "))

roll_list  = [roll_no for roll_no in range(roll_start, roll_end+1)]

print(f"total students are {len(roll_list)}")

n_experiments = int(input("enter total number of experiments : "))

print("assigning experiments to each student...")

experiments = [i for i in range(1, n_experiments+1)] * int(len(roll_list)/n_experiments)

shuffle(experiments)

for roll_no, experiment in zip(roll_list, experiments):
    print(roll_no, experiment)
