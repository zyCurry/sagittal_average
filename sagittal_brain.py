import numpy as np

def run_averages(file_input, file_output):
    """
    Calculates the average through the coronal planes
    The input file should has as many columns as coronal planes
    The rows are intersections of the sagittal/horizontal planes

    The result is an average for each sagittal/horizontal plane (rows)
    """
    # Open the file to analyse
    if file_input is None:
        file_input = 'brain_sample.csv'
    with open(file_input, 'r') as myfile:
            # Create a plane list to keep a list per row
            planes = []
            for line in myfile.readlines():
                planes.append([int(x) for x in line.split("\n")[0].split(',')])

    # Create new list to save the averages per each plane
    sagittal_averages = []
    # let's use NumPy! It's faster!!
    planes = np.array(planes)
    for sagittal_sect in planes:
        average = np.mean(sagittal_sect)
        sagittal_averages.append(str(average))

    # write it out on my file
    if file_output is None:
        file_output = 'brain_average.csv'
    with open(file_output, 'w') as myoutput:
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
