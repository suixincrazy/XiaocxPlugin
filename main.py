from pkg.plugin.context import register, handler, BasePlugin, APIHost, EventContext
from pkg.plugin.events import PersonNormalMessageReceived, GroupNormalMessageReceived
import subprocess
import os

# 注册插件
@register(name="小程序运行插件", description="一个小插件运行插件不必开关程序直接运行程序简单（可以用gpt直接写功能添加）", version="0.1", author="小馄饨")
class CommandExecutorPlugin(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        self.data_dir = os.path.join(os.path.dirname(__file__), 'data')  # 数据目录路径

    # 当收到个人消息时触发
    @handler(PersonNormalMessageReceived)
    async def person_normal_message_received(self, ctx: EventContext):
        await self.execute_command(ctx)

    # 当收到群消息时触发
    @handler(GroupNormalMessageReceived)
    async def group_normal_message_received(self, ctx: EventContext):
        await self.execute_command(ctx)

    async def execute_command(self, ctx: EventContext):
        receive_text = ctx.event.text_message
        if receive_text.startswith('/'):
            parts = receive_text[1:].split(' ', 1)  # 分割命令和参数
            command = parts[0]  # 获取命令
            args = parts[1] if len(parts) > 1 else ''  # 获取参数（如果有）

            if command == "测试":
                ctx.add_return("reply", ["插件测试成功！"])
                ctx.prevent_default()
                return

            script_path = os.path.join(self.data_dir, f"{command}.py")

            if os.path.exists(script_path):
                try:
                    # 执行脚本并传递参数
                    result = subprocess.check_output(['python', script_path, args], text=True)
                    ctx.add_return("reply", [result])
                except subprocess.CalledProcessError as e:
                    ctx.add_return("reply", [f"执行失败: {e.output}"])
            else:
                ctx.add_return("reply", ["脚本不存在，请检查命令。"])
            ctx.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass