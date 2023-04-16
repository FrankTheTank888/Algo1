import random

      
N = 10
arr = [random.randint(1, 100) for _ in range(N)]
max_hill = None

def print_array(arr, current=None):
    for i in range(N):
        if i == current:
            print(f"\033[94m{arr[i]}\033[0m", end=" ") # blue
        elif current is not None and abs(i - current) == 1:
            if arr[i] > arr[current]:
                print(f"\033[91m{arr[i]}\033[0m", end=" ") # red
            elif arr[i] < arr[current]:
                print(f"\033[92m{arr[i]}\033[0m", end=" ") # green
            else:
                print(f"\033[93m{arr[i]}\033[0m", end=" ") # orange
        else:
            print(arr[i], end=" ")
    if current is not None and current == max_hill:
        print("*", end="")
    print()

print ("\n--- Finde den maximalen Hügel in einem Array ---")
       
print("\nArray:")
print_array(arr)
print()

for i in range(N):
    left_neighbor = arr[i-1] if i > 0 else None
    right_neighbor = arr[i+1] if i < N-1 else None
    
    if (left_neighbor is None or arr[i] > left_neighbor) and (right_neighbor is None or arr[i] > right_neighbor):
        if max_hill is None or arr[i] > arr[max_hill]:
            max_hill = i
    
    print_array(arr, i)

print()
print("Max Hill:")
if max_hill is not None:
    print(f"Position: {max_hill}, Value: \033[91m{arr[max_hill]}\033[0m") # red
else:
    print("No hills found")

print("\n--- Programm beendet. ---\n")