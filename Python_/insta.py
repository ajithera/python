import requests
import os

# specify the Instagram username
username = 'zhagarann'

# fetch the posts using the `/<INSTAGRAM_USERNAME>` endpoint
response = requests.get(f'https://www.instagram.com/zhagarann')


# parse the JSON data from the response
data = response.json()

# create a directory to store the photos and videos
if not os.path.exists(username):
    os.makedirs(username)

# loop through the posts and download the media
for edge in data['graphql']['user']['edge_owner_to_timeline_media']['edges']:
    node = edge['node']
    
    # check if the post is a photo or a video
    if node['is_video']:
        url = node['video_url']
    else:
        url = node['display_url']
    
    # download the media
    response = requests.get(url)
    with open(f'{username}/{node["id"]}.{url.split(".")[-1]}', 'wb') as f:
        f.write(response.content)
