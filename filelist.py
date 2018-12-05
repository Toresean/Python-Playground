import os
str = input("Enter the path: ")
results = os.listdir(str)

# Reverse order of sort
# sresults = sorted(results, reverse=True)

for file in results:
    print (file)
