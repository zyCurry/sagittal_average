# Open the file to analyse
myfile = open('brain_sample.csv', 'r')

# Create a plane list to keep a list per row
planes = []
for line in myfile.readlines():
    planes.append([int(x) for x in line.split("\n")[0].split(',')])
myfile.close()

# Create new list to save the averages per each plane
sagittal_averages = []
for i in range(20):
    total = 0
    for j in range(20):
        total = total + int(planes[i][j])
    sagittal_averages.append(str(total/20))

# write it out on my file
myoutput = open('brain_average.csv', 'w')
myoutput.write(','.join(sagittal_averages) +  '\n')
myoutput.close()
