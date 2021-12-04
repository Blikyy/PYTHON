def bubble_sort(arr):

    neco = len(arr)

    for i in range(neco):

        for nvm in range(neco-i-1):

            if arr[nvm] > arr[nvm + 1]:
                arr[nvm], arr[nvm + 1] = arr[nvm + 1], arr[nvm]



OmegaLul = int(input("kolik mist"))
print("\n")
array=[]
for i in range(OmegaLul):
   array.append(int(input()))   

print("\n")

bubble_sort(array)

for p in range(len(array)):
    print("%d" % array[p])
