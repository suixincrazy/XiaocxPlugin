import requests

def get_anime_avatar_url():
    api_url = "https://api.vvhan.com/api/avatar/dm?type=json"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                image_url = data['url']
                return image_url
            else:
                print("获取头像失败:", data.get('message', '无详细信息'))
                return None
        else:
            print("请求失败，状态码:", response.status_code)
            return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None

def main():
    avatar_url = get_anime_avatar_url()
    if avatar_url:
        markdown_image_link = f"![Anime Avatar]({avatar_url})"
        print(markdown_image_link)

if __name__ == "__main__":
    main()