from pkg.plugin.context import register, handler, BasePlugin, APIHost, EventContext
from pkg.plugin.events import PersonNormalMessageReceived, GroupNormalMessageReceived
import subprocess
import os
import re
from mirai import Image, Plain

@register(name="小程序运行插件", description="一个小插件运行插件不必开关程序直接运行程序简单（可以用gpt直接写功能添加）", version="0.1", author="小馄饨")
class CommandExecutorPlugin(BasePlugin):

    def __init__(self, host: APIHost):
        self.data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.image_pattern = re.compile(r'!\[.*?\]\((https?://\S+)\)')
        self.at_pattern = re.compile(r'@\S+\s*')

    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        await self.execute_command(ctx)

    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        await self.execute_command(ctx)

    async def execute_command(self, ctx: EventContext):
        receive_text = ctx.event.text_message
        cleaned_text = self.at_pattern.sub('', receive_text).strip()

        if cleaned_text.startswith('/'):
            parts = cleaned_text[1:].split(' ', 1)
            command = parts[0]
            args = parts[1] if len(parts) > 1 else ''

            if command == "测试":
                ctx.add_return("reply", ["插件测试成功！"])
                ctx.prevent_default()
                return

            script_path = os.path.join(self.data_dir, f"{command}.py")

            if os.path.exists(script_path):
                try:
                    result = subprocess.check_output(['python', script_path, args], text=True)
                    image_urls = self.extract_image_urls(result)
                    if image_urls:
                        for image_url in image_urls:
                            ctx.add_return("reply", [Image(url=image_url)])
                    else:
                        ctx.add_return("reply", ["没有找到图片。"])
                except subprocess.CalledProcessError as e:
                    ctx.add_return("reply", [f"执行失败: {e.output}"])
            else:
                ctx.add_return("reply", ["脚本不存在，请检查命令。"])
            ctx.prevent_default()

    def extract_image_urls(self, message):
        return [match.group(1) for match in self.image_pattern.finditer(message)]
