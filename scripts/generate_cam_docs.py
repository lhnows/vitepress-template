from __future__ import annotations

import hashlib
import html
import json
import re
import shutil
from pathlib import Path

from docx import Document
from docx.document import Document as DocumentObject
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT.parent / "CAM产品规格书资料库"
PAGES_DIR = ROOT / "pages"
CAM_DIR = PAGES_DIR / "cam"
PUBLIC_DIR = PAGES_DIR / "public"
SOURCE_DOCX_DIR = PUBLIC_DIR / "source-docx"
IMAGE_DIR = PUBLIC_DIR / "spec-images"
CONFIG_PATH = ROOT / ".vitepress" / "config.mts"


def main() -> None:
    CAM_DIR.mkdir(parents=True, exist_ok=True)
    SOURCE_DOCX_DIR.mkdir(parents=True, exist_ok=True)
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    clean_generated_files()

    files = sorted(
        [
            item
            for item in SOURCE_DIR.iterdir()
            if item.is_file()
            and item.suffix.lower() == ".docx"
            and not item.name.startswith(("~$", ".~", "."))
        ],
        key=lambda item: natural_key(item.name),
    )

    products = []
    for index, source_path in enumerate(files, start=1):
        title = source_path.stem.strip()
        product = {
            "index": index,
            "title": title,
            "file_name": source_path.name,
            "slug": make_slug(title, index),
            **parse_meta(title),
        }
        products.append(product)
        write_product_page(source_path, product)

    write_index(products)
    write_config(products)
    print(f"Generated {len(products)} CAM product pages.")


def clean_generated_files() -> None:
    for directory in (CAM_DIR, SOURCE_DOCX_DIR, IMAGE_DIR):
        if not directory.exists():
            continue
        for item in directory.iterdir():
            if item.is_file() and item.name != "index.md":
                item.unlink()


def write_product_page(source_path: Path, product: dict) -> None:
    copied_name = f"{product['slug']}.docx"
    shutil.copy2(source_path, SOURCE_DOCX_DIR / copied_name)

    document = Document(source_path)
    image_writer = ImageWriter(document, product["slug"])
    body = "\n\n".join(render_block(block, image_writer) for block in iter_blocks(document))
    body = normalize_markdown(body)

    page = f"""---
title: {json.dumps(product["title"], ensure_ascii=False)}
---

# {product["title"]}

{meta_block(product)}

<a class="spec-download" href="/source-docx/{copied_name}" download>下载原始 Word 规格书</a>

## 文档内容

{body or "_原始 Word 文档未解析出可展示的正文内容，请下载原件查看。_"}
"""

    (CAM_DIR / f"{product['slug']}.md").write_text(page, encoding="utf-8")


def write_index(products: list[dict]) -> None:
    table_rows = "\n".join(
        "| [{title}](/cam/{slug}) | {resolution} | {purpose} | {sensor} | {solution} |".format(
            title=escape_table(product["title"]),
            slug=product["slug"],
            resolution=escape_table(product["resolution"]),
            purpose=escape_table(product["purpose"]),
            sensor=escape_table(product["sensor"]),
            solution=escape_table(product["solution"]),
        )
        for product in products
    )

    sections = []
    for group in group_products(products):
        cards = "\n".join(
            f"""<a class="spec-card" href="/cam/{product["slug"]}">
  <div class="spec-card-title">{html.escape(product["title"])}</div>
  <div class="spec-card-meta">{html.escape(card_meta(product))}</div>
</a>"""
            for product in group["products"]
        )
        sections.append(f"## {group['label']}\n\n<div class=\"spec-grid\">\n{cards}\n</div>")

    page = f"""# 摄像头产品规格书

当前共收录 **{len(products)}** 份摄像头产品规格书。可通过左侧导航按像素规格浏览，也可以使用右上角搜索按传感器型号、用途或方案关键词检索。

## 快速总览

| 产品 | 像素 | 用途 | 传感器 / 芯片 | 方案 |
| --- | --- | --- | --- | --- |
{table_rows}

{chr(10).join(sections)}
"""

    (CAM_DIR / "index.md").write_text(page, encoding="utf-8")


def write_config(products: list[dict]) -> None:
    cam_groups = [
        {
            "text": group["label"],
            "collapsed": False,
            "items": [
                {"text": sidebar_title(product), "link": f"/cam/{product['slug']}"}
                for product in group["products"]
            ],
        }
        for group in group_products(products)
    ]

    cam_groups_literal = json.dumps(cam_groups, ensure_ascii=False, indent=2)
    cam_groups_literal = cam_groups_literal[1:-1].strip()
    cam_groups_literal = indent(cam_groups_literal, 8)

    config = f"""import {{ defineConfig }} from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({{
  title: 'CAM 产品规格书中心',
  description: '摄像头产品规格书资料库',
  srcDir: 'pages',
  outDir: 'dist',
  ignoreDeadLinks: true,
  cleanUrls: true,
  lang: 'zh-CN',
  themeConfig: {{
    // https://vitepress.dev/reference/default-theme-config
    outline: {{
      level: [1, 3],
      label: '本页目录'
    }},
    search: {{
      provider: 'local'
    }},
    nav: [
      {{ text: '首页', link: '/' }},
      {{ text: '规格书', link: '/cam/' }}
    ],

    sidebar: {{
      '/cam/': [
        {{
          text: '产品资料库',
          items: [
            {{ text: '规格书索引', link: '/cam/' }}
          ]
        }},
{cam_groups_literal}
      ]
    }},

    socialLinks: [
      {{ icon: 'github', link: 'https://github.com/lhnows/vitepress-template' }}
    ],

    docFooter: {{
      prev: '上一篇',
      next: '下一篇'
    }},
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '菜单',
    darkModeSwitchLabel: '外观',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式'
  }}
}})
"""

    CONFIG_PATH.write_text(config, encoding="utf-8")


class ImageWriter:
    def __init__(self, document: DocumentObject, slug: str) -> None:
        self.document = document
        self.slug = slug
        self.index = 0
        self.written: dict[str, str] = {}

    def src_for(self, rel_id: str) -> str | None:
        if rel_id in self.written:
            return self.written[rel_id]

        part = self.document.part.related_parts.get(rel_id)
        if part is None:
            return None

        self.index += 1
        suffix = Path(part.partname).suffix or ".png"
        image_name = f"{self.slug}-{self.index:02d}{suffix}"
        (IMAGE_DIR / image_name).write_bytes(part.blob)
        src = f"/spec-images/{image_name}"
        self.written[rel_id] = src
        return src


def iter_blocks(parent: DocumentObject):
    for child in parent.element.body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def render_block(block, image_writer: ImageWriter) -> str:
    if isinstance(block, Paragraph):
        return render_paragraph(block, image_writer)
    if isinstance(block, Table):
        return render_table(block, image_writer)
    return ""


def render_paragraph(paragraph: Paragraph, image_writer: ImageWriter) -> str:
    text = "".join(render_run(run, image_writer) for run in paragraph.runs).strip()
    if not text:
        return ""

    style = (paragraph.style.name if paragraph.style else "").lower()
    visible_text = paragraph.text.strip()
    has_image = bool(paragraph._element.xpath(".//a:blip"))
    if ("heading" in style or "标题" in style) and visible_text and not has_image:
        return f"{'#' * heading_level(style)} {text}"
    return text


def render_run(run, image_writer: ImageWriter) -> str:
    pieces = []
    for drawing in run.element.xpath(".//a:blip"):
        rel_id = drawing.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
        if rel_id:
            src = image_writer.src_for(rel_id)
            if src:
                pieces.append(f"\n\n![规格书图片]({src})\n\n")

    if run.text:
        value = run.text.replace("\n", " ")
        if run.bold and value.strip():
            value = f"**{value}**"
        pieces.append(value)

    return "".join(pieces)


def render_table(table: Table, image_writer: ImageWriter) -> str:
    rows = []
    for row in table.rows:
        cells = []
        for cell in row.cells:
            cell_parts = []
            for paragraph in cell.paragraphs:
                value = render_paragraph(paragraph, image_writer)
                if value:
                    cell_parts.append(value)
            cells.append("<br>".join(escape_table(part) for part in cell_parts) or " ")
        rows.append(cells)

    if not rows:
        return ""

    width = max(len(row) for row in rows)
    rows = [row + [" "] * (width - len(row)) for row in rows]
    body = rows[1:] or [[" "] * width]
    lines = [
        "| " + " | ".join(rows[0]) + " |",
        "| " + " | ".join("---" for _ in range(width)) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in body)
    return "\n".join(lines)


def parse_meta(title: str) -> dict:
    parts = [part.strip() for part in title.split("-") if part.strip()]
    first = parts[0] if parts else title
    match = re.match(r"^(\d+(?:\.\d+)?M)", first, re.IGNORECASE)
    resolution = match.group(1) if match else "未标注"
    purpose = first[match.end() :].strip() if match else first
    sensor = parts[1] if len(parts) > 1 else "未标注"
    solution = "-".join(parts[2:]).replace("SPEC", "").strip("- ").strip() or "未标注"
    resolution_value = float(resolution[:-1]) if resolution != "未标注" else 9999
    return {
        "resolution": resolution,
        "resolution_value": resolution_value,
        "purpose": purpose or "未标注",
        "sensor": sensor,
        "solution": solution,
    }


def group_products(products: list[dict]) -> list[dict]:
    grouped = {}
    for product in products:
        grouped.setdefault(product["resolution"], []).append(product)

    groups = []
    for resolution, items in grouped.items():
        groups.append(
            {
                "label": f"{resolution} 规格",
                "resolution_value": items[0]["resolution_value"],
                "products": sorted(items, key=lambda item: natural_key(item["title"])),
            }
        )
    return sorted(groups, key=lambda group: group["resolution_value"])


def make_slug(title: str, index: int) -> str:
    digest = hashlib.sha1(title.encode("utf-8")).hexdigest()[:6]
    ascii_part = title.lower().replace("&", " and ").replace("+", " plus ")
    ascii_part = re.sub(r"[^a-z0-9]+", "-", ascii_part).strip("-")
    return f"{index:02d}-{ascii_part or 'spec'}-{digest}"


def natural_key(value: str):
    return [
        float(part) if re.fullmatch(r"\d+(?:\.\d+)?", part) else part
        for part in re.split(r"(\d+(?:\.\d+)?)", value)
    ]


def heading_level(style: str) -> int:
    match = re.search(r"(\d+)", style)
    if match:
        return min(max(int(match.group(1)) + 1, 2), 4)
    return 2


def meta_block(product: dict) -> str:
    rows = [
        ("像素规格", product["resolution"]),
        ("用途类型", product["purpose"]),
        ("传感器 / 芯片", product["sensor"]),
        ("结构 / 方案", product["solution"]),
    ]
    items = "\n".join(
        f'  <div class="spec-meta-item"><strong>{html.escape(label)}</strong><span>{html.escape(value)}</span></div>'
        for label, value in rows
    )
    return f'<div class="spec-meta">\n{items}\n</div>'


def card_meta(product: dict) -> str:
    return " / ".join(
        value
        for value in [product["purpose"], product["sensor"], product["solution"]]
        if value and value != "未标注"
    ) or "摄像头规格书"


def sidebar_title(product: dict) -> str:
    title = re.sub(r"-?SPEC\b", "", product["title"], flags=re.IGNORECASE).rstrip("- ")
    return title if len(title) <= 34 else title[:33] + "..."


def normalize_markdown(value: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", value).strip()


def escape_table(value: str) -> str:
    return str(value).replace("|", "\\|").replace("\n", "<br>").strip()


def indent(value: str, spaces: int) -> str:
    padding = " " * spaces
    return "\n".join(f"{padding}{line}" for line in value.splitlines())


if __name__ == "__main__":
    main()
