import requests

def get_bing_image_url(day=0, size=None):
    api_url = "https://uapis.cn/api/bing"
    params = {
        "rand": "false",  # 确保获取的图片是确定的
        "day": day
    }
    
    if size:
        params["size"] = size

    try:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            # 直接使用该URL链接的图片
            return response.url
        else:
            print("获取Bing图片失败")
            return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None

def main():
    # 获取今天的图片，使用默认大小
    image_url = get_bing_image_url(day=0, size="1920×1080")
    if image_url:
        markdown_image_link = f"![Bing Image]({image_url})"
        print(markdown_image_link)

if __name__ == "__main__":
    main()