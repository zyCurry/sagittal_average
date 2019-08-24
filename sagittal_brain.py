import numpy as np

def run_averages(file_input, file_output):
    # Open the file to analyse
    if file_input is None:
        file_input = 'brain_sample.csv'
    with open('brain_sample.csv', 'r') as myfile:
            # Create a plane list to keep a list per row
            planes = []
            for line in myfile.readlines():
                planes.append([int(x) for x in line.split("\n")[0].split(',')])

    # Create new list to save the averages per each plane
    # The number of steps coronal planes may change in the future
    coronal_planes = 20
    # The number of sagittal sections from front to back, it may change in the future
    sagittal_sections = 20
    sagittal_averages = []
    # let's use NumPy! It's faster!!
    planes = np.array(planes)
    for i in range(sagittal_sections):
        total = 0
        for j in range(coronal_planes):
            total = total + int(planes[i][j])
        sagittal_averages.append(str(total/coronal_planes))

    # write it out on my file
    if file_output is None:
        file_output = 'brain_average.csv'
    with open('brain_average.csv', 'w') as myoutput:
             myoutput.write(','.join(sagittal_averages) +  '\n')

if __name__ == "__main__":
    import sys
    argumens = sys.argv
    file_input = None
    file_output = None
    if len(argumens) > 1:
         file_input = sys.argv[1]
    if len(argumens) > 2:
         file_output = sys.argv[2]
    run_averages(file_input, file_output)
