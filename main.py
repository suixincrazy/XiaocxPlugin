from pkg.plugin.context import register, handler, BasePlugin, APIHost, EventContext
from pkg.plugin.events import PersonNormalMessageReceived, GroupNormalMessageReceived
import subprocess
import os
import re
import asyncio  # 导入 asyncio
from mirai import Image, Plain

@register(name="小程序运行插件", description="一个小插件运行插件不必开关程序直接运行程序简单（可以用gpt直接写功能添加）", version="0.1", author="小馄饨")
class CommandExecutorPlugin(BasePlugin):
    lock = asyncio.Lock()  # 创建一个锁作为类变量

    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        await self.execute_command(ctx)

    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        await self.execute_command(ctx)

    async def execute_command(self, ctx: EventContext):
        async with self.lock:  # 使用锁
            receive_text = ctx.event.text_message
            cleaned_text = re.sub(r'@\S+\s*', '', receive_text).strip()  # 清理文本

            if cleaned_text.startswith('/'):
                parts = cleaned_text[1:].split(' ', 1)
                command = parts[0]
                args = parts[1] if len(parts) > 1 else ''

                if command == "测试":
                    ctx.add_return("reply", ["插件测试成功！"])
                    ctx.prevent_default()
                    return

                script_path = os.path.join(os.path.dirname(__file__), 'data', f"{command}.py")

                if os.path.exists(script_path):
                    try:
                        result = subprocess.check_output(['python', script_path, args], text=True)
                        messages = self.convert_message(result)
                        ctx.add_return("reply", messages)
                    except subprocess.CalledProcessError as e:
                        ctx.add_return("reply", [f"执行失败: {e.output}"])
                else:
                    ctx.add_return("reply", ["脚本不存在，请检查命令。"])
                ctx.prevent_default()

    def convert_message(self, message):
        parts = []
        last_end = 0
        image_pattern = re.compile(r'!\[.*?\]\((https?://\S+)\)')
        
        for match in image_pattern.finditer(message):
            start, end = match.span()
            if start > last_end:
                parts.append(Plain(message[last_end:start]))
            image_url = match.group(1)
            parts.append(Image(url=image_url))
            last_end = end
        if last_end < len(message):
            parts.append(Plain(message[last_end:]))
        return parts if parts else [Plain(message)]
