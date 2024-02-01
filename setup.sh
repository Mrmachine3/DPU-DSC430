#!/usr/bin/bash

echo "Enter assignment name: "
read assign

o_file="ARodriguez_HW$assign.py"

# Evaluate the variables
python3_path=$(which python3)
author="Anthony M. Rodriguez"
current_date=$(date +'%m/%d/%Y')
python3_usage="${python3_path} ${o_file}"
python3_m_usage="${python3_path} -m ${o_file%.*}"
source_usage="./${o_file}"
git_repo_url=$(git config --get remote.origin.url)

touch $o_file

cat <<EOF > $o_file
#!$python3_path
################################ Honor Statement ####################################
#    I have not given or received any unauthorized assistance on this assignment.
#####################################################################################
# Author: $author
# Date: $current_date
# Usage: $python3_usage
# Alternate Python Usage: $python3_m_usage
# Alternate CLI Usage: $source_usage
# Git Repo URL: $git_repo_url
# Video Explanation URL:
#
# Description:


# LIBRARIES

# FUNCTIONS

# MAIN PROGRAM FUNCTION
def main(name):
    print(f"Hello {name}!")


# MAIN PROGRAM INVOCATION
if __name__ == "__main__":
    main("Anthony")
EOF


# TODOS
# - [ ] TODO: Add function to capture header template info for python file
# - [ ] TODO: Add function to capture header template info for yaml file
# - [ ] TODO: Add function to capture header template info for markdown file
