# STK Robotics Website

A VitePress site for the STK Robotics business homepage and CAM product specification library. The homepage presents the company offering, while `/cam/` provides sidebar navigation, local search, converted spec pages, and original Word downloads.

## Deploy
Deploy with EdgeOne Pages.

[![EdgeOne Pages deploy](https://cdnstatic.tencentcs.com/edgeone/pages/deploy.svg)](https://edgeone.ai/pages/new?template=vitepress-template)

## Features

- Product spec navigation grouped by resolution
- Company homepage
- Local full-text search
- Converted Word specification pages
- Original `.docx` downloads
- EdgeOne Pages deployment

## Directory Structure

```
.
├── .vitepress/          # VitePress configuration
│   ├── config.mts       # Site configuration
│   └── theme/           # Custom theme files
│       ├── components/  # Home page Vue components
│       ├── style.css    # Docs styles
│       └── robotics-home.css # Company homepage styles
├── pages/              # Documentation pages
│   ├── index.md        # Company homepage
│   ├── cam/            # Generated CAM spec pages
│   └── public/         # Images, source Word files, and static assets
├── scripts/            # Generation scripts
├── dist/               # Build output directory
├── package.json        # Project dependencies
├── edgeone.json        # Project deployment parameters
└── .gitignore         # Git ignore rules
```

## Getting Started

1. **Installation**

```bash
# Clone the repository
git clone [your-repo-url]

# Install dependencies
npm install
```

2. **Development**

```bash
# Start local development server
npm run dev
```

3. **Build**

```bash
# Build for production
npm run build
```

4. **Preview**

```bash
# Preview production build
npm run preview
```

## Updating Specs

Place Word specs in the sibling `CAM产品规格书资料库` directory, then run:

```bash
python3 scripts/generate_cam_docs.py
```

## Lead Form

The homepage lead form does not submit to an external service by default. Configure a deployment environment variable to enable a webhook:

```bash
VITE_STK_WEBHOOK_URL=https://example.com/webhook
```

Do not commit real webhook URLs to the repository.
