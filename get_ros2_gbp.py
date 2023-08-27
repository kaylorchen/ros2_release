import requests

start_page = 1
end_page = 18
filtered_lines =[]
all_urls = []
repos = []
repos.append('repositories:')

for page in range(start_page, end_page +1):
  url = f'https://github.com/orgs/ros2-gbp/repositories?page={page}'
  print( 'requests: ' + url )
  response = requests.get(url)
  for line in response.text.split('\n'):
    if 'name codeRepository' in line:
      print(line)
      start = line.find('data-hovercard-url="/ros2-gbp/') + len('data-hovercard-url="/ros2-gbp/')
      end = line.find('/hovercard')
      filtered_lines.append(line[start:end])
      all_urls.append('https://github.com/ros2-gbp/'+line[start:end]+'.git')
      repos.append('  ' + line[start:end]+':')
      repos.append('    type: git')
      repos.append('    url: https://github.com/ros2-gbp/'+line[start:end]+'.git')

with open('filtered_lines.txt','w',encoding='utf-8') as f1:
  f1.write('\n'.join(filtered_lines))

with open('all_urls.txt','w',encoding='utf-8') as f2:
  f2.write('\n'.join(all_urls))

with open('all_urls.repos','w',encoding='utf-8') as f3:
  f3.write('\n'.join(repos))
