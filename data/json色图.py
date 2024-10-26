import httpx
import asyncio

async def fetch_color_image():
    api_url = "https://moe.jitsu.top/img/?size=original&type=json&num=1"

    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)  # 使用 GET 请求
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("code") == 200:
                pics = response_data.get("pics", [])
                if pics:
                    return pics[0]  # 只返回第一个图片链接
    return None

async def main():
    image_url = await fetch_color_image()
    if image_url:
        markdown_image_link = f"![Anime Image]({image_url})"  # 转换为 Markdown 格式
        print(markdown_image_link)  # 打印 Markdown 图片链接
    else:
        print("可能这张图被吞了~再试试吧")  # 修改失败提示

if __name__ == "__main__":
    asyncio.run(main())  # 运行主函数
