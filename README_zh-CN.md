# CAM 产品规格书中心

基于 VitePress 的摄像头产品规格书资料库。站点提供左侧产品导航、全文搜索、规格书内容浏览和原始 Word 文件下载。

## 部署
部署到 EdgeOne Pages。

[![EdgeOne Pages deploy](https://cdnstatic.tencentcs.com/edgeone/pages/deploy.svg)](https://console.cloud.tencent.com/edgeone/pages/new?template=vitepress-template)

## 特性

- 结构化文档中心导航
- 按像素规格分组的摄像头产品列表
- 本地全文搜索
- Word 规格书内容转 Markdown 展示
- 原始 `.docx` 文件下载
- EdgeOne Pages 自动部署

## 目录结构

```
.
├── .vitepress/          # VitePress 配置
│   ├── config.mts       # 站点配置
│   └── theme/           # 自定义主题文件
│       └── style.css    # 自定义样式
├── pages/              # 文档页面
│   ├── index.md        # 首页
│   ├── cam/            # 自动生成的摄像头规格书页面
│   └── public/         # 原始 Word 附件和规格书图片
├── scripts/            # 文档生成脚本
├── dist/               # 构建输出目录
├── package.json        # 项目依赖
├── edgeone.json        # 项目部署参数
└── .gitignore         # Git 忽略规则
```

## 快速开始

1. **安装**

```bash
# 克隆仓库
git clone [your-repo-url]

# 安装依赖
npm install
```

2. **开发**

```bash
# 启动本地开发服务器
npm run dev
```

3. **构建**

```bash
# 构建生产版本
npm run build
```

4. **预览**

```bash
# 预览生产构建
npm run preview
```

## 更新产品资料

将新的 Word 规格书放入仓库上级目录的 `CAM产品规格书资料库` 后，在仓库根目录运行：

```bash
python3 scripts/generate_cam_docs.py
```

脚本会自动跳过 Word 临时文件，重新生成 `pages/cam/` 页面、`pages/public/source-docx/` 下载附件和 `pages/public/spec-images/` 图片资源，并更新 VitePress 侧边栏。
