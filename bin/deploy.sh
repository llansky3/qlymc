#!/bin/bash

VERSION_FILE="version.txt"
echo "DEPLOYMENT" 
echo "Version file:" $VERSION_FILE
echo "┏━━━━━"

if [ $# -eq 0 ]; then
    if [ ! -f $VERSION_FILE ]; then 
        echo "┣ Error: No tag argument supplied and $VERSION_FILE doesn't exists! Please provide a version tag!"
        echo "┻"
        exit 1
    fi
    tag=$(git describe --tags --abbrev=0)
    newtag=false
else
    tag=$1
    if echo ${tag} | grep -qe '^v[0-9]\+\.[0-9]\+\.[0-9]\+$'; then
        echo "┣ Version format OK"
    else
        echo "┣ Error: Requested version tag does not match required format: vX.Y.Z"
        echo "┻"
        exit 1
    fi
    newtag=true
fi

commit=$(git rev-parse --short HEAD)
version=${tag}
if grep -q $version $VERSION_FILE; then
  echo "┣ Nothing to do! This version $version is already there."
  echo "┻"
  exit 1
fi

echo "┣ Setting version to: $version"
echo  $version > $VERSION_FILE
echo "┣ Appending changes to last commit"
git add ${VERSION_FILE}
git commit --amend --no-edit

if [ "$newtag" = true ]; then
    # TODO: Check if this tag version is higher than last tag
    echo "┣ Applying new tag to git!"
    git tag ${tag}
fi

echo "┻"
