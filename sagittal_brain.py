import numpy as np

def run_averages(file_input='brain_sample.csv', file_output='brain_average.csv'):
    """
    Calculates the average through the coronal planes
    The input file should has as many columns as coronal planes
    The rows are intersections of the sagittal/horizontal planes

    The result is an average for each sagittal/horizontal plane (rows)
    """
    # Open the file to analyse
    with open(file_input, 'r') as myfile:
            # Create a plane list to keep a list per row
            planes = []
            for line in myfile.readlines():
                planes.append([int(x) for x in line.split("\n")[0].split(',')])

    # let's use NumPy! It's faster!!
    planes = np.array(planes)
    averages = np.mean(planes, axis=0)
    # Convert the np array into a list
    averages = [str(x) for x in averages]

    # write it out on my file
    with open(file_output, 'w') as myoutput:
             myoutput.write(','.join(averages) +  '\n')

if __name__ == "__main__":
    import sys
    arguments = sys.argv
    if len(arguments) == 1:
         run_averages()
    elif len(arguments) == 2:
         file_input = sys.argv[1]
         run_averages(file_input)
    if len(arguments) > 2:
         file_input = sys.argv[1]
         file_output = sys.argv[2]
         run_averages(file_input, file_output)
