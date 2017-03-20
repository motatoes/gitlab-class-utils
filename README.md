# Introduction

This repo includes some utility functions that were used for a programming module at kingston (see [here](https://gitlab.com/gitlab-org/gitlab-ce/issues/26681) and [here](http://stackoverflow.com/questions/41600241/gitlab-accessing-a-fork-of-a-private-repository)). We wanted the students of a programming module at Kingston to use gitlab for downloand and submit their exercises (one repo per exercise). We have a private deployment of gitlab and wanted to utilise that to host the exercise. However, some of the requirements that we needed for the module were not acheivable directly out of the box, such as:

- Add all the students to a course group where all the exercises are: This can be automated through the API
- Allow students to make private forks of each exercise, while still giving lecturers access to their exercise for marking: Private forks of private repositories are possible in Gitlab, but the lectureres would not have access to their 

The image bellow explains what we were trying to acheive through gitlab:

![](https://raw.githubusercontent.com/motatoes/gitlab-class-utils/master/docs/intro.png)

This repository contains some of the scripts that were used to automate the tasks mentioned above. The solution to giving markers access to the student repository submissions was acheived using [deploy keys](https://docs.gitlab.com/ce/ssh/README.html#deploy-keys) (This is more of a hack, but it worked for our purposes).

The repository currently contains the following:

- Modifiable students and groups list (students.csv and projects.csv)
- Server to allow students to add themselves to the groups (using their ID, they get added to the module group only if they are on the classlist)
- Script to clone all student exercises
- Script to show which of the cloned repositories was successful

