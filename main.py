from pkg.plugin.context import register, handler, BasePlugin, APIHost, EventContext
from pkg.plugin.events import PersonNormalMessageReceived, GroupNormalMessageReceived
import subprocess
import os
import re
import shutil
from mirai import Image, Plain

# 注册插件
@register(name="小程序运行插件", description="一个小插件运行插件不必开关程序直接运行程序简单（可以用gpt直接写功能添加）", version="0.1", author="小馄饨")
class CommandExecutorPlugin(BasePlugin):

    def __init__(self, host: APIHost):
        self.image_pattern = re.compile(r'!\[.*?\]\((https?://\S+)\)')  # 匹配图片 URL 的正则表达式
        self.at_pattern = re.compile(r'@\S+\s*')  # 匹配@提及及其后空格

        # 设置源和目标目录
        base_path = os.getenv('QCHATGPT_PATH')  # 从环境变量获取路径
        if not base_path:
            raise ValueError("请设置环境变量 'QCHATGPT_PATH'")

        self.source_data_dir = os.path.join(base_path, 'plugins', 'XiaocxPlugin', 'data')  # 源数据目录
        self.target_data_dir = os.path.join(base_path, 'data', 'pluginsXiaocxPlugin', 'data')  # 目标数据目录

        # 检查并创建目标目录
        if not os.path.exists(self.target_data_dir):
            os.makedirs(self.target_data_dir)  # 创建目标目录
        
        # 复制文件
        self.copy_files()

    def copy_files(self):
        # 复制源目录中的所有文件到目标目录
        for item in os.listdir(self.source_data_dir):
            source = os.path.join(self.source_data_dir, item)
            target = os.path.join(self.target_data_dir, item)
            if os.path.isfile(source):
                shutil.copy2(source, target)  # 复制文件
            elif os.path.isdir(source):
                shutil.copytree(source, target, dirs_exist_ok=True)  # 复制目录

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
        # 去掉所有@提及及其后空格
        cleaned_text = self.at_pattern.sub('', receive_text).strip()

        if cleaned_text.startswith('/'):
            parts = cleaned_text[1:].split(' ', 1)  # 分割命令和参数
            command = parts[0]  # 获取命令
            args = parts[1] if len(parts) > 1 else ''  # 获取参数（如果有）

            if command == "测试":
                ctx.add_return("reply", ["插件测试成功！"])
                ctx.prevent_default()
                return

            script_path = os.path.join(self.target_data_dir, f"{command}.py")

            if os.path.exists(script_path):
                try:
                    # 执行脚本并传递参数
                    result = subprocess.check_output(['python', script_path, args], text=True)
                    # 处理可能的图片链接
                    optimized_result = self.convert_message(result)
                    ctx.add_return("reply", optimized_result)
                except subprocess.CalledProcessError as e:
                    ctx.add_return("reply", [f"执行失败: {e.output}"])
            else:
                ctx.add_return("reply", ["脚本不存在，请检查命令。"])
            ctx.prevent_default()

    def convert_message(self, message):
        parts = []
        last_end = 0
        for match in self.image_pattern.finditer(message):
            start, end = match.span()
            # 添加图片前的文本
            if start > last_end:
                parts.append(Plain(message[last_end:start]))
            # 提取图片 URL 并添加图片
            image_url = match.group(1)
            parts.append(Image(url=image_url))
            last_end = end
        # 添加最后一个图片后的文本
        if last_end < len(message):
            parts.append(Plain(message[last_end:]))
        return parts if parts else message  # 如果没有修改，返回原始消息

    # 插件卸载时触发
    def __del__(self):
        pass
