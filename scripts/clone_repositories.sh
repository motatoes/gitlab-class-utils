#!/bin/bash
# author: David Livingstone, Kingston University, 3/12/2013
# user story:
# get all the repositories
# Modified to use a blank suffix for any repository - e.g. CI5100 Software Company repositories - 02/02/2016
# Using a list of the repositories which are assumed correct unless requiring a suffix - the default suffix is blank
# Using a current list of the students in Prog III attempt to create clone of all the students repositories
# If the repository doesn't exist write out the students name with a 'not exist' and 'empty code' into the  'Feedback log file' 
# with the current date [default name Feedback.log]
# Clone all other repositories into a ForFeedback directory
# script must be run in ssh agent shell with authorised private key
# ssh-agent bash
# ssh-add <open ssh private key>

# usage of the command
usage()
{
cat << EOF

usage: $0 -f <log_file> -d <output_dir> -g <git server url> -s <repository suffix> <repository_list>

This script gets all repositories from the secgit repository to change the default repository you must edit the script.
For a protected repository you must provide an authorised key pair
script must be run in ssh agent shell with the authorised private key e.g. id_rsa
ssh-agent bash
ssh-add <open_ssh private key >
 
ARGUMENTS:
	<student_id_list>	Specify a valid list of student ids - one per line

OPTIONS:
   -f      Specify a log file to write the output to the default is 'Feedback.log'
   -d      Specify a directory to clone the git repositories into - default is 'ForFeedback'
   -g      Specify another base url for the git server - default is 'ssh://git@secgit.kingston.ac.uk/'
   -s      Specify another suffix to append to student it for repository name - default is 'main'
EOF
}

# exit if command-line error
die () {
    echo >&2 "$@"
    echo
    usage
    exit 1
}

# set up program variables - change if defaults change

gitsuffix=""
groupname="dad-workshop1"
giturl="git@gitlab.kingston.ac.uk"
outfile="Feedback.log"
outdir="repos"
currentdir=`pwd`
currentdate=`date +%H:%M,%d-%m-%Y`
args=( $@ )
# parse the options

while getopts “f:d:” OPTION
do
     case $OPTION in
         f)
             outfile=$OPTARG
             ;;
         d)
             outdir=$OPTARG
             ;;
         g)
             giturl=$OPTARG
             ;;
         s)
             gitsuffix=$OPTARG
             ;;
         ?)
             usage
             exit
             ;;
     esac
done

# test mandatory argument
[ $# -eq $OPTIND ] || die "one <repository list> required"

# make output directory
mkdir -p $outdir

# for each repository in the file 
while read studentid || [[ -n "$line" ]]; 
do
  # for each group in the groups file
  echo -n "*Now cloning repositories for: $studentid"
  while read groupname || [[ -n "$line" ]];
  do
      #  when testing for commit then no need
      reponame=$(printf "%s:%s/%s.git" "$giturl" "$studentid" "$groupname")
    	( cd $outdir ; git clone "$reponame" "$studentid/$groupname" ; cd $currentdir ; )
  done < "projects.csv"
done < ${args[$OPTIND-1]}
exit 1

