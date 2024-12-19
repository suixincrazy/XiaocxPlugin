import requests
import sys

def generate_blue_archive_logo_markdown(start_text="Blue", end_text="Archive", x=-18, y=0, color="white"):
    """生成蔚蓝档案风格 logo 的 Markdown 图片链接。"""
    base_url = "https://oiapi.net/API/BlueArchive"
    params = {
        "startText": start_text,
        "x": x,
        "y": y,
        "color": color
    }
    if end_text:  # 只有当 end_text 不为空时才添加到参数中
        params["endText"] = end_text

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        image_url = response.url
        markdown_image_link = f"![Blue Archive Logo]({image_url})"
        return markdown_image_link

    except requests.exceptions.RequestException as e:
        print(f"生成 logo 图片失败: {e}")
        return None

def main():
    start_text = "Blue"
    end_text = "Archive"

    if len(sys.argv) == 2:  # 提供了一个参数
        parts = sys.argv[1].split(" ", 1)  # 以第一个空格分割，最多分割成两部分
        start_text = parts[0]
        if len(parts) > 1:  # 如果有第二部分，则将其作为 end_text
            end_text = parts[1]
        else:
            end_text = "" # 否则 end_text 为空


    elif len(sys.argv) > 2:  # 提供了两个或以上参数
        print("使用方法: python BA.py \"<start_text> <end_text>\"")
        print("或: python BA.py \"<start_text>\"")  # 注意引号，允许输入带有空格的start_text
        print("或: python BA.py (使用默认值)")
        return

    markdown_link = generate_blue_archive_logo_markdown(start_text, end_text)
    if markdown_link:
        print(markdown_link)

if __name__ == "__main__":
    main()

