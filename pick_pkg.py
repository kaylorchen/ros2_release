#!/usr/bin/env python3
import yaml
import argparse
import os

def argparse_repos():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg',type = str,default=r"kaylor-pkg.txt",help="...") # a.yaml中内容在文章开始给出
    args = parser.parse_args()
    filepath = os.path.join(os.getcwd(), args.cfg)
    return filepath

def save_dict_to_yaml(dict_value: dict, save_path: str):
    with open(save_path, 'w') as file:
        file.write(yaml.dump(dict_value, allow_unicode=True))

with open('ros2_release_humble.repos', 'r') as f:
    config = yaml.safe_load(f)

repo ={}
repo['repositories'] = {}
i = 0
with open(argparse_repos(), 'r') as f:
  for line in f:
    line = line.strip()
    i += 1
    # print(line + '*** %d' % i)
    for pkg in config.get('repositories').keys():
      # print(line + ' ' + pkg)
      if line == pkg:
        # print(line + ' %d' % i)
        # print(config.get('repositories').get(pkg))
        repo['repositories'][pkg] =  config.get('repositories').get(pkg)

save_dict_to_yaml(repo, "kaylor-pkg.repos")