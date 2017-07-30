length_core = 8
length_big = 4
bigideas = ['bigidea 1', 'bigidea 2', 'bigidea 3', 'bigidea 4']
corecomps = ['cc1', 'cc2', 'cc3', 'cc4', 'cc5', 'cc6', 'cc7', 'cc8']
grid = [[(0,0) for x in range(length_core)] for y in range(length_big)]
for big in range(len(bigideas)-1):
    grid[big][0]='BigIdea'
    for cor in range(6):
        grid[big][cor+1]=(1,1)

print (grid)