import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    description = repo_dict['description']
    if description is None:
        description = 'No Description'

    print(description)
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)
    # stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.lable_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15   # 将较长的项目名显示为15个字符，
my_config.show_y_guides = False #隐藏表中的水平线
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=True)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
# print("Repositories returned:", len(repo_dicts))
#
# # 研究第一个仓库
repo_dict = repo_dicts[0]
print("\nkey:", len(repo_dict) )
for key in sorted(repo_dict.keys()):
    print(key)
# print("Owner: %s" % repo_dict['owner'])
# # 处理结果
# print(repo_dict)