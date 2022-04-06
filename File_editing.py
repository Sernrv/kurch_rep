# %% Opening with 'x' parameter
try:
    file = open('Results.txt', 'x')
except FileExistsError:
    print('File already exists')
    file.close()
# %% Writing in file
file = open('Results.txt', 'w')
for i in range(15):
    file.write(str(i) + '\n')
file.close()
