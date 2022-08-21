import json
import os
import datetime
import time
import typing

target_dir = 'blog'

ordered_list: typing.List = []
last_index = 0
monthly_archive: typing.Dict = {}
category_list: typing.Dict = {}
tag_list: typing.Dict = {}

# loading old list
with open(os.path.join(target_dir, 'ordered_list.json'), encoding='utf-8') as fp:
    ordered_list = json.load(fp)
    last_index = ordered_list[-1]['idx']

with open(os.path.join(target_dir, 'monthly_archive.json'), encoding='utf-8') as fp:
    monthly_archive = json.load(fp)

with open(os.path.join(target_dir, 'category_list.json'), encoding='utf-8') as fp:
    category_list = json.load(fp)

with open(os.path.join(target_dir, 'tag_list.json'), encoding='utf-8') as fp:
    tag_list = json.load(fp)


def get_post_by_path(path):
    global ordered_list
    if '\\' in path:
        path = path.replace('\\', '/')
    for p in ordered_list:
        if p['path'] == path:
            return p
    else:
        return []


for d in os.listdir(target_dir):
    if d[-5:] == '.json': continue
    old_item = get_post_by_path(os.path.join(target_dir, d))
    if old_item: continue

    confpath = os.path.join(target_dir, d, 'conf.json')
    if not os.path.isfile(confpath):
        print('not found', confpath)
    conf = {}
    with open(confpath, encoding='utf-8') as fp:
        conf = json.load(fp)
    # print(conf)
    last_index += 1
    item: typing.Dict = {}
    item['idx'] = last_index
    _dt = datetime.datetime.strptime(conf['date'], "%H:%M %d/%m/%Y")
    item['timestamp'] = time.mktime(_dt.timetuple())
    item['path'] = os.path.join(target_dir, d)
    ordered_list.append(item)
    # print(item)

    month_key = _dt.strftime("%Y_%b")
    monthly_archive.setdefault(month_key, []).append(item['idx'])

    if 'taxonomy' not in conf or not isinstance(conf['taxonomy']['category'], typing.List):
        # print('no taxonomy/category')
        continue

    taxonomy = conf['taxonomy']
    for c in taxonomy['category']:
        category_list.setdefault(c, []).append(item['idx'])

    for t in taxonomy['tag']:
        tag_list.setdefault(t, []).append(item['idx'])

# save json all
with open(os.path.join(target_dir, 'ordered_list.json'), 'w') as fp:
    json.dump(ordered_list, fp, indent=2)

with open(os.path.join(target_dir, 'category_list.json'), 'w') as fp:
    json.dump(category_list, fp, sort_keys=True, indent=2)

with open(os.path.join(target_dir, 'monthly_archive.json'), 'w') as fp:
    json.dump(monthly_archive, fp, sort_keys=True, indent=2)

with open(os.path.join(target_dir, 'tag_list.json'), 'w') as fp:
    json.dump(tag_list, fp, sort_keys=True, indent=2)
    
