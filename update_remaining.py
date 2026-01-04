# -*- coding: utf-8 -*-
import re

# 读取文件
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

count = 0

# 1. 更新 Process 步骤卡片
old_process = '''      <div class="grid gap-8 md:grid-cols-2">
        <!-- Block 1 -->
        <article class="rounded-2xl border border-slate-800 bg-slate-900/70 p-5 sm:p-6">
          <h3 class="text-base font-semibold mb-3">01 · 需求澄清 & 目标对齐</h3>
          <p class="text-sm text-slate-400 leading-relaxed mb-3">
            先把问题讲清楚，再开始画图。和团队或负责人对齐：这次任务是为了什么？要影响谁？成功的标志是什么？
          </p>
          <ul class="text-xs text-slate-400 space-y-1.5">
            <li>· 通过飞书问卷 / 表单收集关键信息</li>
            <li>· 用模型做"需求澄清稿"，反向给到需求方确认</li>
            <li>· 同步到多维表格，形成任务记录</li>
          </ul>
        </article>

        <!-- Block 2 -->
        <article class="rounded-2xl border border-slate-800 bg-slate-900/70 p-5 sm:p-6">
          <h3 class="text-base font-semibold mb-3">02 · 工作流拆解 & 配置</h3>
          <p class="text-sm text-slate-400 leading-relaxed mb-3">
            把一个需求拆成若干"节点"：输入 → 处理 → 输出。每个节点交给"最适合"的工具做：AI / 自动化 / 人。
          </p>
          <ul class="text-xs text-slate-400 space-y-1.5">
            <li>· 在 n8n 里搭建流程：例如接收 Webhook → 调用模型 → 回写结果</li>
            <li>· 规划哪些步骤由 AI 完成，哪些需要人工判断</li>
            <li>· 对关键节点设置日志和监控</li>
          </ul>
        </article>

        <!-- Block 3 -->
        <article class="rounded-2xl border border-slate-800 bg-slate-900/70 p-5 sm:p-6">
          <h3 class="text-base font-semibold mb-3">03 · 设计执行 & 版本管理</h3>
          <p class="text-sm text-slate-400 leading-relaxed mb-3">
            在 AI 工具和 DCC 软件之间切换：一部分通过模型探索，一部分在 PS / Figma / 3D 软件里精修，并做好版本管理。
          </p>
          <ul class="text-xs text-slate-400 space-y-1.5">
            <li>· 建立"版本号 + 备注"的命名规则</li>
            <li>· 用多维表格或 Notion 记录关键里程碑</li>
            <li>· 固定一个"最终交付"目录，方便团队查找</li>
          </ul>
        </article>

        <!-- Block 4 -->
        <article class="rounded-2xl border border-slate-800 bg-slate-900/70 p-5 sm:p-6">
          <h3 class="text-base font-semibold mb-3">04 · 复盘 & 资产沉淀</h3>
          <p class="text-sm text-slate-400 leading-relaxed mb-3">
            每一次项目结束，都会有一些"可复用的东西"：Prompt 模板、流程配置、SOP、素材库，这些都是以后节省时间的关键。
          </p>
          <ul class="text-xs text-slate-400 space-y-1.5">
            <li>· 记录哪些 Prompt / 模型配置效果最好</li>
            <li>· 把流程截图 / 配置导出整理成文档</li>
            <li>· 逐步搭建属于自己的"设计 × 自动化"资产库</li>
          </ul>
        </article>
      </div>'''

new_process = '''      <div class="grid gap-6 md:grid-cols-2">
        <!-- Block 1 -->
        <article class="group rounded-2xl border border-slate-700/50 bg-gradient-to-br from-slate-900/90 to-slate-800/30 backdrop-blur-sm p-6 sm:p-7 hover:border-brand/40 transition-all duration-300 relative overflow-hidden">
          <div class="absolute top-0 right-0 w-24 h-24 bg-brand/5 rounded-full -translate-y-1/2 translate-x-1/2"></div>
          <div class="flex items-start gap-4 mb-4">
            <div class="flex-shrink-0 w-12 h-12 rounded-xl bg-brand/10 border border-brand/30 flex items-center justify-center">
              <span class="text-xl font-bold text-brand">01</span>
            </div>
            <div>
              <h3 class="text-lg font-semibold text-white mb-1">需求澄清</h3>
              <span class="text-xs text-brand/70 uppercase tracking-wider">Clarify & Align</span>
            </div>
          </div>
          <p class="text-sm text-slate-400 leading-relaxed mb-4">
            先把问题讲清楚，再开始画图。对齐目标、受众和成功标志。
          </p>
          <ul class="text-xs text-slate-400 space-y-2 pl-1 border-l-2 border-brand/20">
            <li class="pl-3">飞书问卷 / 表单收集关键信息</li>
            <li class="pl-3">模型输出"需求澄清稿"确认</li>
            <li class="pl-3">同步多维表格形成任务记录</li>
          </ul>
        </article>

        <!-- Block 2 -->
        <article class="group rounded-2xl border border-slate-700/50 bg-gradient-to-br from-slate-900/90 to-slate-800/30 backdrop-blur-sm p-6 sm:p-7 hover:border-cyan-500/40 transition-all duration-300 relative overflow-hidden">
          <div class="absolute top-0 right-0 w-24 h-24 bg-cyan-500/5 rounded-full -translate-y-1/2 translate-x-1/2"></div>
          <div class="flex items-start gap-4 mb-4">
            <div class="flex-shrink-0 w-12 h-12 rounded-xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center">
              <span class="text-xl font-bold text-cyan-400">02</span>
            </div>
            <div>
              <h3 class="text-lg font-semibold text-white mb-1">工作流拆解</h3>
              <span class="text-xs text-cyan-400/70 uppercase tracking-wider">Workflow Design</span>
            </div>
          </div>
          <p class="text-sm text-slate-400 leading-relaxed mb-4">
            把需求拆成节点：输入 → 处理 → 输出，分配给最适合的工具。
          </p>
          <ul class="text-xs text-slate-400 space-y-2 pl-1 border-l-2 border-cyan-500/20">
            <li class="pl-3">n8n 搭建流程：Webhook → 模型 → 回写</li>
            <li class="pl-3">规划 AI 与人工判断的分工</li>
            <li class="pl-3">关键节点设置日志和监控</li>
          </ul>
        </article>

        <!-- Block 3 -->
        <article class="group rounded-2xl border border-slate-700/50 bg-gradient-to-br from-slate-900/90 to-slate-800/30 backdrop-blur-sm p-6 sm:p-7 hover:border-emerald-500/40 transition-all duration-300 relative overflow-hidden">
          <div class="absolute top-0 right-0 w-24 h-24 bg-emerald-500/5 rounded-full -translate-y-1/2 translate-x-1/2"></div>
          <div class="flex items-start gap-4 mb-4">
            <div class="flex-shrink-0 w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center">
              <span class="text-xl font-bold text-emerald-400">03</span>
            </div>
            <div>
              <h3 class="text-lg font-semibold text-white mb-1">设计执行</h3>
              <span class="text-xs text-emerald-400/70 uppercase tracking-wider">Execute & Version</span>
            </div>
          </div>
          <p class="text-sm text-slate-400 leading-relaxed mb-4">
            AI 工具与 DCC 软件切换：模型探索 + PS / Figma 精修，做好版本管理。
          </p>
          <ul class="text-xs text-slate-400 space-y-2 pl-1 border-l-2 border-emerald-500/20">
            <li class="pl-3">"版本号 + 备注"命名规则</li>
            <li class="pl-3">多维表格记录关键里程碑</li>
            <li class="pl-3">固定"最终交付"目录</li>
          </ul>
        </article>

        <!-- Block 4 -->
        <article class="group rounded-2xl border border-slate-700/50 bg-gradient-to-br from-slate-900/90 to-slate-800/30 backdrop-blur-sm p-6 sm:p-7 hover:border-purple-500/40 transition-all duration-300 relative overflow-hidden">
          <div class="absolute top-0 right-0 w-24 h-24 bg-purple-500/5 rounded-full -translate-y-1/2 translate-x-1/2"></div>
          <div class="flex items-start gap-4 mb-4">
            <div class="flex-shrink-0 w-12 h-12 rounded-xl bg-purple-500/10 border border-purple-500/30 flex items-center justify-center">
              <span class="text-xl font-bold text-purple-400">04</span>
            </div>
            <div>
              <h3 class="text-lg font-semibold text-white mb-1">复盘沉淀</h3>
              <span class="text-xs text-purple-400/70 uppercase tracking-wider">Review & Assets</span>
            </div>
          </div>
          <p class="text-sm text-slate-400 leading-relaxed mb-4">
            沉淀可复用资产：Prompt 模板、流程配置、SOP、素材库。
          </p>
          <ul class="text-xs text-slate-400 space-y-2 pl-1 border-l-2 border-purple-500/20">
            <li class="pl-3">记录最佳 Prompt / 模型配置</li>
            <li class="pl-3">流程截图 / 配置导出整理</li>
            <li class="pl-3">搭建"设计 × 自动化"资产库</li>
          </ul>
        </article>
      </div>'''

if old_process in content:
    content = content.replace(old_process, new_process)
    count += 1
    print("✓ Process 步骤卡片已更新")
else:
    print("✗ Process 卡片未找到匹配")

# 2. 更新 About 信息卡片
old_about = '''        <!-- 右侧：个人信息小卡片 -->
        <div class="space-y-5 text-sm text-slate-300/90">
          <div class="rounded-2xl border border-slate-800 bg-slate-900/70 p-5">
            <h3 class="text-sm font-semibold text-slate-400 mb-3">Current Focus</h3>
            <ul class="text-sm space-y-2">
              <li>· 电商视觉 / 品牌延展</li>
              <li>· n8n / Dify / RPA 自动化</li>
              <li>· 飞书多维表格中台搭建</li>
              <li>· AI 图像工作流（Flux / ComfyUI 等）</li>
            </ul>
          </div>
          <div class="rounded-2xl border border-slate-800 bg-slate-900/70 p-5">
            <h3 class="text-sm font-semibold text-slate-400 mb-3">Stack</h3>
            <ul class="text-sm space-y-2">
              <li>· 设计：PS / Figma / C4D（基础）</li>
              <li>· 自动化：n8n / Dify / 实在 RPA / 少量 Python</li>
              <li>· 文档 & 协作：飞书多维表格 / 文档 / 知识库</li>
            </ul>
          </div>
        </div>'''

new_about = '''        <!-- 右侧：个人信息小卡片 -->
        <div class="space-y-5 text-sm text-slate-300/90">
          <div class="rounded-2xl border border-slate-700/50 bg-gradient-to-br from-slate-900/90 to-brand/5 backdrop-blur-sm p-6 relative overflow-hidden group hover:border-brand/40 transition-all duration-300">
            <div class="absolute -top-4 -right-4 w-16 h-16 bg-brand/10 rounded-full blur-xl group-hover:bg-brand/20 transition-all"></div>
            <div class="flex items-center gap-3 mb-4">
              <div class="w-8 h-8 rounded-lg bg-brand/10 border border-brand/30 flex items-center justify-center">
                <span class="text-brand text-sm">📍</span>
              </div>
              <h3 class="text-sm font-semibold text-white">Current Focus</h3>
            </div>
            <ul class="text-sm space-y-2.5 pl-1 border-l-2 border-brand/20">
              <li class="pl-3 text-slate-300">电商视觉 / 品牌延展</li>
              <li class="pl-3 text-slate-300">n8n / Dify / RPA 自动化</li>
              <li class="pl-3 text-slate-300">飞书多维表格中台搭建</li>
              <li class="pl-3 text-slate-300">AI 图像工作流（Flux / ComfyUI）</li>
            </ul>
          </div>
          <div class="rounded-2xl border border-slate-700/50 bg-gradient-to-br from-slate-900/90 to-cyan-500/5 backdrop-blur-sm p-6 relative overflow-hidden group hover:border-cyan-500/40 transition-all duration-300">
            <div class="absolute -top-4 -right-4 w-16 h-16 bg-cyan-500/10 rounded-full blur-xl group-hover:bg-cyan-500/20 transition-all"></div>
            <div class="flex items-center gap-3 mb-4">
              <div class="w-8 h-8 rounded-lg bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center">
                <span class="text-cyan-400 text-sm">🛠️</span>
              </div>
              <h3 class="text-sm font-semibold text-white">Stack</h3>
            </div>
            <ul class="text-sm space-y-2.5 pl-1 border-l-2 border-cyan-500/20">
              <li class="pl-3 text-slate-300">设计：PS / Figma / C4D（基础）</li>
              <li class="pl-3 text-slate-300">自动化：n8n / Dify / 实在 RPA / Python</li>
              <li class="pl-3 text-slate-300">协作：飞书多维表格 / 文档 / 知识库</li>
            </ul>
          </div>
        </div>'''

if old_about in content:
    content = content.replace(old_about, new_about)
    count += 1
    print("✓ About 信息卡片已更新")
else:
    print("✗ About 卡片未找到匹配")

# 3. 更新 Blog 文章卡片
old_blog = '''        <div class="stagger-grid grid gap-8 lg:gap-10 md:grid-cols-2">
          <article class="rounded-2xl border border-slate-800 bg-slate-900/70 p-6 sm:p-8 flex flex-col gap-4">
            <h3 class="text-lg font-semibold">
              用 n8n + 飞书多维表格搭一个「设计任务中台」
          </h3>
          <p class="text-sm text-slate-400 line-clamp-3 leading-relaxed">
            从"需求收集 → 任务分发 → 结果归档"三个阶段拆解，把飞书多维表格当成一个轻量级的项目管理中台。
            通过 n8n 把机器人消息、表格和文档串起来，让任务流转变得更顺滑。
          </p>
          <div class="mt-3 flex flex-wrap gap-2 text-xs text-slate-400">
            <span class="pill-soft">n8n</span>
            <span class="pill-soft">飞书多维表格</span>
            <span class="pill-soft">Workflow</span>
          </div>
        </article>

        <article class="rounded-2xl border border-slate-800 bg-slate-900/70 p-5 sm:p-6 flex flex-col gap-3">
          <h3 class="text-base font-semibold">
            电商主图的 Prompt 结构：从信息到画面
          </h3>
          <p class="text-sm text-slate-400 line-clamp-3 leading-relaxed">
            把一次电商主图的设计拆成信息要素：产品 / 卖点 / 结构 / 场景 / 光影 / 质感，
            用 Prompt 去描述这些，而不是只写"某某风格""某某摄影"，让输出更稳定可控。
          </p>
          <div class="mt-3 flex flex-wrap gap-2 text-xs text-slate-400">
            <span class="pill-soft">Prompt</span>
            <span class="pill-soft">电商视觉</span>
            <span class="pill-soft">结构化思考</span>
          </div>
        </article>
        </div>'''

new_blog = '''        <div class="stagger-grid grid gap-8 lg:gap-10 md:grid-cols-2">
          <article class="group rounded-2xl border border-slate-700/50 bg-gradient-to-br from-slate-900/90 to-slate-800/30 backdrop-blur-sm p-6 sm:p-8 flex flex-col gap-4 hover:border-brand/40 hover:shadow-[0_0_30px_rgba(56,189,248,0.08)] transition-all duration-500 relative overflow-hidden">
            <!-- 装饰元素 -->
            <div class="absolute top-0 right-0 w-32 h-32 bg-gradient-to-bl from-brand/10 to-transparent rounded-bl-full opacity-0 group-hover:opacity-100 transition-opacity"></div>
            <!-- 元信息 -->
            <div class="flex items-center gap-4 text-xs text-slate-500">
              <span class="flex items-center gap-1.5">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                约 8 分钟
              </span>
              <span class="flex items-center gap-1.5">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5"></path>
                </svg>
                2024.12
              </span>
            </div>
            <h3 class="text-lg font-semibold text-white group-hover:text-brand transition-colors leading-tight">
              用 n8n + 飞书多维表格搭一个「设计任务中台」
            </h3>
            <p class="text-sm text-slate-400 line-clamp-3 leading-relaxed">
              从"需求收集 → 任务分发 → 结果归档"三个阶段拆解，把飞书多维表格当成一个轻量级的项目管理中台。
            </p>
            <div class="mt-auto flex flex-wrap gap-2 pt-4 border-t border-slate-800/50">
              <span class="px-2.5 py-1 rounded-full bg-brand/10 border border-brand/20 text-[11px] text-brand/90">n8n</span>
              <span class="px-2.5 py-1 rounded-full bg-purple-500/10 border border-purple-500/20 text-[11px] text-purple-400/90">飞书多维表格</span>
              <span class="px-2.5 py-1 rounded-full bg-slate-800/80 border border-slate-700/50 text-[11px] text-slate-400">Workflow</span>
            </div>
          </article>

          <article class="group rounded-2xl border border-slate-700/50 bg-gradient-to-br from-slate-900/90 to-slate-800/30 backdrop-blur-sm p-6 sm:p-8 flex flex-col gap-4 hover:border-cyan-500/40 hover:shadow-[0_0_30px_rgba(6,182,212,0.08)] transition-all duration-500 relative overflow-hidden">
            <div class="absolute top-0 right-0 w-32 h-32 bg-gradient-to-bl from-cyan-500/10 to-transparent rounded-bl-full opacity-0 group-hover:opacity-100 transition-opacity"></div>
            <div class="flex items-center gap-4 text-xs text-slate-500">
              <span class="flex items-center gap-1.5">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                约 6 分钟
              </span>
              <span class="flex items-center gap-1.5">
                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5"></path>
                </svg>
                2024.11
              </span>
            </div>
            <h3 class="text-lg font-semibold text-white group-hover:text-cyan-400 transition-colors leading-tight">
              电商主图的 Prompt 结构：从信息到画面
            </h3>
            <p class="text-sm text-slate-400 line-clamp-3 leading-relaxed">
              把一次电商主图的设计拆成信息要素：产品 / 卖点 / 结构 / 场景 / 光影 / 质感，用 Prompt 描述让输出更稳定可控。
            </p>
            <div class="mt-auto flex flex-wrap gap-2 pt-4 border-t border-slate-800/50">
              <span class="px-2.5 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 text-[11px] text-cyan-400/90">Prompt</span>
              <span class="px-2.5 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-[11px] text-emerald-400/90">电商视觉</span>
              <span class="px-2.5 py-1 rounded-full bg-slate-800/80 border border-slate-700/50 text-[11px] text-slate-400">结构化思考</span>
            </div>
          </article>
        </div>'''

if old_blog in content:
    content = content.replace(old_blog, new_blog)
    count += 1
    print("✓ Blog 文章卡片已更新")
else:
    print("✗ Blog 卡片未找到匹配")

# 4. 更新 Contact 联系卡片
old_contact = '''          <div class="rounded-2xl border border-slate-800 bg-slate-900/70 p-6 sm:p-8 space-y-6 text-base text-slate-300">
            <div>
            <div class="text-sm text-slate-400 mb-2">Email</div>
            <a href="mailto:your_email@example.com" class="text-base hover:text-brand transition">
              your_email@example.com
            </a>
          </div>
          <div>
            <div class="text-sm text-slate-400 mb-2">Feishu / 飞书</div>
            <p class="text-sm text-slate-400 leading-relaxed">
              可通过邮件交换飞书联系方式，或后续视情况开放机器人入口。
            </p>
          </div>
          <div>
            <div class="text-sm text-slate-400 mb-2">其他</div>
            <p class="text-sm text-slate-400 leading-relaxed">
              也欢迎通过 Telegram / 微信等方式联系（视实际方便程度决定是否公开）。
            </p>
          </div>
          </div>'''

new_contact = '''          <div class="rounded-2xl border border-slate-700/50 bg-gradient-to-br from-slate-900/90 to-slate-800/30 backdrop-blur-sm p-6 sm:p-8 space-y-6 text-base text-slate-300 relative overflow-hidden">
            <!-- 装饰背景 -->
            <div class="absolute -bottom-8 -right-8 w-32 h-32 bg-brand/5 rounded-full blur-2xl"></div>
            <div class="relative">
              <div class="flex items-center gap-3 mb-3">
                <div class="w-8 h-8 rounded-lg bg-brand/10 border border-brand/30 flex items-center justify-center">
                  <svg class="w-4 h-4 text-brand" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"></path>
                  </svg>
                </div>
                <div class="text-sm font-medium text-white">Email</div>
              </div>
              <a href="mailto:your_email@example.com" class="text-base text-slate-300 hover:text-brand transition pl-11 block">
                your_email@example.com
              </a>
            </div>
            <div class="relative border-t border-slate-800/50 pt-6">
              <div class="flex items-center gap-3 mb-3">
                <div class="w-8 h-8 rounded-lg bg-purple-500/10 border border-purple-500/30 flex items-center justify-center">
                  <svg class="w-4 h-4 text-purple-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M8.625 12a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 01-2.555-.337A5.972 5.972 0 015.41 20.97a5.969 5.969 0 01-.474-.065 4.48 4.48 0 00.978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25z"></path>
                  </svg>
                </div>
                <div class="text-sm font-medium text-white">飞书 / Feishu</div>
              </div>
              <p class="text-sm text-slate-400 leading-relaxed pl-11">
                可通过邮件交换飞书联系方式，或后续开放机器人入口。
              </p>
            </div>
            <div class="relative border-t border-slate-800/50 pt-6">
              <div class="flex items-center gap-3 mb-3">
                <div class="w-8 h-8 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center">
                  <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582m15.686 0A11.953 11.953 0 0112 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0121 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0112 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 013 12c0-1.605.42-3.113 1.157-4.418"></path>
                  </svg>
                </div>
                <div class="text-sm font-medium text-white">其他方式</div>
              </div>
              <p class="text-sm text-slate-400 leading-relaxed pl-11">
                欢迎通过 Telegram / 微信等方式联系。
              </p>
            </div>
          </div>'''

if old_contact in content:
    content = content.replace(old_contact, new_contact)
    count += 1
    print("✓ Contact 联系卡片已更新")
else:
    print("✗ Contact 卡片未找到匹配")

# 写回文件
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ 完成！共更新了 {count} 个卡片区域")
