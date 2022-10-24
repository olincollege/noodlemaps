#!/usr/bin/env bash


set -e
if [ -n "$VIRTUAL_ENV" ]; then
    PATH="$VIRTUAL_ENV"/bin:"$PATH"
fi

FILES=$(python << EOF
import subprocess
import re
import sys
output = subprocess.run(["git", "diff-index", "--cached", "--name-only", "--diff-filter=MA", "HEAD"],
                        stdout=subprocess.PIPE)
# this may not be the optimum. it is not safe to say that the output here is unicode...
output = output.stdout.decode("utf-8")
files = output.split("\n")
# exit if there are no files in the commit
if len(files)==1 and not files[0]:
  exit()
# search all python files and convert their paths to module names
files = [ file.rstrip('.py').replace("/", ".")
          for file in files
          if re.match(r".*\.py", file) ]
for file in files:
  # dashes could be mistaken for pylint arguments when running eval
  if file.startswith('-'):
    print(f'python module: {file}', file=sys.stderr)
    print("dashes at the file name beginning are not allowed due to security concerns!", file=sys.stderr)
    exit(1)
  # prevent code injection through filenames
  if "'" in file or ";" in file:
    print(f'python module: {file}', file=sys.stderr)
    print("single quotes and semicoli are not allowed in file names due to security concerns!", file=sys.stderr)
    exit(1)
  print(f"'{file}'", end=' ')
EOF
)

if [ -z "$FILES" ]; then
  exit 0
fi

echo "linting..."
echo "pylint $FILES"
eval pylint $FILES