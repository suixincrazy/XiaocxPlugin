import requests
import sys
import re

def get_tarot_reading(horoscope_type="today"):
    """获取塔罗牌解读，包括文字和图片链接。"""
    try:
        url = "https://oiapi.net/API/Tarot"
        params = {"type": horoscope_type}
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        if data and data.get("code") == 1:
            tarot_readings = []
            image_urls = []

            for card in data['data']:
                # 过滤掉不需要的字段，只保留 name_cn, name_en, 正位/逆位
                filtered_card = {k: v for k, v in card.items() if k in ["name_cn", "name_en", card.get("type")]}
                tarot_readings.append("\n".join([f"{value}" for value in filtered_card.values()]))
                image_urls.append(card.get("pic"))

            return {"text": "\n\n".join(tarot_readings), "images": image_urls}
        else:
            return {"error": f"获取塔罗牌解读失败: {data.get('message', '未知错误')}"}

    except requests.exceptions.RequestException as e:
        return {"error": f"网络请求错误: {e}"}
    except Exception as e:
        return {"error": f"发生其他错误: {e}"}

def main():
    reading = get_tarot_reading()

    if "error" in reading:
        print(reading["error"])
    else:
        text_parts = reading["text"].split("\n\n")
        for i, image_url in enumerate(reading["images"]):
            print(text_parts[i])
            print(f"![Tarot]({image_url})")
            print()


if __name__ == "__main__":
    main()
