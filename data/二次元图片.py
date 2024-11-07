import requests

def get_anime_image_url():
    api_url = "https://api.vvhan.com/api/wallpaper/acg?type=json"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            image_url = data['url']
            return image_url
        else:
            print("获取图片失败")
            return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None

def main():
    image_url = get_anime_image_url()
    if image_url:
        markdown_image_link = f"![Anime Image]({image_url})"
        print(markdown_image_link)

if __name__ == "__main__":
    main()
