#!/bin/bash
# rm -f version.txt
# rm -f tags.txt
rm -f ros2_release_humble.repos
echo "repositories:" > ros2_release_humble.repos
ls $1 | while read repo; do
  echo "repo is $repo"
  top_dir=$(pwd)
  pushd ${1}/$repo
    tags=$(git tag -l | grep humble | grep debian | grep jammy)
    if [ "$tags" != "" ]; then
      version=$(git tag -l | grep humble | grep debian | grep jammy| awk -F '_' '{print $2}')
      version=$(echo "$version" | awk 'END{print}')
      tags=$(git tag -l | grep humble | grep debian | grep jammy | grep $version)
      echo tags is $tags
      echo version is $version
      # echo $tags >> ${top_dir}/tags.txt
      # echo $version >> ${top_dir}/version.txt
      count=0
      echo $tags |tr " " "\n" | while read tag; do
        echo "  $repo$count:" >> ${top_dir}/ros2_release_humble.repos
        ((count++))
        echo "    type: git" >> ${top_dir}/ros2_release_humble.repos
        echo "    url: https://github.com/ros2-gbp/$repo.git" >> ${top_dir}/ros2_release_humble.repos
        echo "    version: $tag" >> ${top_dir}/ros2_release_humble.repos
      done
    fi
  popd
done