import random
import time
import matplotlib.pyplot as plt

def print_array(arr, current=None, start=None, end=None):
    for i in range(len(arr)):
        if i == current:
            print(f"\033[94m{arr[i]}\033[0m", end=" ") # blue
        elif current is not None and abs(i - current) == 1:
            if arr[i] > arr[current]:
                print(f"\033[91m{arr[i]}\033[0m", end=" ") # red
            elif arr[i] < arr[current]:
                print(f"\033[92m{arr[i]}\033[0m", end=" ") # green
            else:
                print(f"\033[93m{arr[i]}\033[0m", end=" ") # orange
        elif start is not None and end is not None and start <= i <= end:
            print(f"\033[93m{arr[i]}\033[0m", end=" ") # yellow
        else:
            print(arr[i], end=" ")
    if current is not None and current == hill:
        print("*", end="")
    print()

def find_hill(arr, start=0, end=None, verbose=False):
    global call_count
    call_count += 1
    if end is None:
        end = len(arr) - 1
    if start > end:
        return None
    mid = (start + end) // 2
    if verbose:
        print_array(arr, mid)
    if (mid == 0 or arr[mid] > arr[mid-1]) and (mid == len(arr)-1 or arr[mid] > arr[mid+1]):
        return mid
    elif mid > 0 and arr[mid-1] > arr[mid]:
        if verbose:
            print_array(arr, start=start, end=mid-1)
        return find_hill(arr, start, mid-1, verbose)
    else:
        if verbose:
            print_array(arr, start=mid+1, end=end)
        return find_hill(arr, mid+1, end, verbose)

print ("\n--- Finde einen Hügel in Arrays (Schleife von 100.000 Feldern bis 1 Million Felder), mit einem >>rekursiven Algorithmus<< ---")

sizes = range(100000, 1000000+1, 100000)
times = []

for N in sizes:
    arr = [random.randint(1, 100) for _ in range(N)]
    hill = None
    call_count = 0

    start_time = time.time()
    hill = find_hill(arr)
    end_time = time.time()

    times.append(end_time - start_time)

    print(f"\nArray-Größe: {N:,}".replace(",", "."))
    if hill is not None:
        print(f"Hügel: Position {hill:,}, Wert {arr[hill]}".replace(",", "."))
    else:
        print("Kein Hügel gefunden")
    print(f"Anzahl der rekursiven Aufrufe: {call_count}")
    print(f"Laufzeit: {end_time - start_time:.6f} Sekunden")

plt.plot(sizes, times)
plt.xlabel("Array-Größe")
plt.ylabel("Laufzeit (Sekunden)")
plt.show()

print("\n--- Programm beendet. ---\n")