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

    # write it out on my file
    with open(file_output, 'w') as myoutput:
             np.savetxt(myoutput, averages.reshape((1, averages.shape[0])), fmt='%.1f', delimiter=',')

if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description = "Calculates the average for each sagittal-horizontal plane.")
    parser.add_argument('file_input', nargs='?', help="Input CSV file with the results from scikit-brain binning algorithm. If not provided it looks at brain_sample.csv")
    parser.add_argument('--file_output', '-o', help="Name of the output CSV file. Defaults to brain_average.csv")
    arguments = parser.parse_args()

    if arguments.file_input and arguments.file_output:
         run_averages(arguments.file_input, arguments.file_output)
    elif arguments.file_input or arguments.file_output:
         if arguments.file_input:
             run_averages(arguments.file_input)
         else:
             run_averages(file_output=arguments.file_output)
    else:
         run_averages()
