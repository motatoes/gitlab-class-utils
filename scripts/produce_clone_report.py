import os, sys
import argparse
import csv

"""
This script produces an availability matrix of the files that have been cloned with the 
clone_repositories.sh script. It will simply check for the existence of folders in each
student id subfolder that has been cloned with the aforementioned script and then produce
a Y/N matrix in a csv file
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="location of the root dir where all the repositories exist")
    parser.add_argument("-o", "--output", default="clone_report.csv", help="location of the output log file")
    parser.add_argument("-p", "--projects-file", default="projects.csv", help="location of the csv file where the names of the possible projects are stored")
    args = parser.parse_args()

    reportfile = args.output
    indir = args.input

    # The names of the expected projects
    with open(args.projects_file) as f:
        projects = f.readlines()
    # strip newlines
    projects = [x.strip() for x in projects] 

    f = open(reportfile, 'w', newline='')
    csvfile = csv.writer(f)
    headerRow = ["Student ID"]
    headerRow.extend(projects[:])

    csvfile.writerow(headerRow)

    print('**producing adjecency matrix')
    for studentDir in os.listdir(indir):
        availableProjects = os.listdir(os.path.join(indir,studentDir))
        availabilities = []
        for project in projects:
            if project in availableProjects:
                availabilities.append('Y')
            else:
                availabilities.append("N")
        towrite = [studentDir]
        towrite.extend(availabilities)
        csvfile.writerow(towrite)

    print('*DONE')