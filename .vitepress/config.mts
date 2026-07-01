import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: '晟泰克机器人事业部',
  description: '机器人全域感知与域控开发平台',
  srcDir: 'pages',
  outDir: 'dist',
  ignoreDeadLinks: true,
  cleanUrls: true,
  lang: 'zh-CN',
  head: [
    ['link', { rel: 'icon', href: '/robotics/favicon.svg', type: 'image/svg+xml' }]
  ],
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    outline: {
      level: [1, 3],
      label: '本页目录'
    },
    search: {
      provider: 'local'
    },
    nav: [
      { text: '首页', link: '/' },
      { text: '规格书', link: '/cam/' }
    ],

    sidebar: {
      '/cam/': [
        {
          text: '产品资料库',
          items: [
            { text: '规格书索引', link: '/cam/' }
          ]
        },
        {
            "text": "0.3M 规格",
            "collapsed": false,
            "items": [
              {
                "text": "0.3M标清后视-OV7958-带甩线方案",
                "link": "/cam/01-0-3m-ov7958-spec-ccec43"
              },
              {
                "text": "0.3M标清后视-OV7958-无甩线方案",
                "link": "/cam/02-0-3m-ov7958-spec-97fd2a"
              },
              {
                "text": "0.3M标清后视-PCB030K-带甩线方案",
                "link": "/cam/03-0-3m-pcb030k-spec-3b5cac"
              }
            ]
          },
          {
            "text": "1M 规格",
            "collapsed": false,
            "items": [
              {
                "text": "1M模拟高清全景-OV9706",
                "link": "/cam/04-1m-ov9706-spec-6c6a00"
              },
              {
                "text": "1M模拟高清全景-PV4109K派视尔",
                "link": "/cam/05-1m-pv4109k-spec-e93912"
              },
              {
                "text": "1M模拟高清全景-SC121AT",
                "link": "/cam/06-1m-sc121at-spec-0527a2"
              }
            ]
          },
          {
            "text": "1.3M 规格",
            "collapsed": false,
            "items": [
              {
                "text": "1.3M高清全景-MAT130A-一体式前盖方案",
                "link": "/cam/07-1-3m-mat130a-spec-6f93b4"
              },
              {
                "text": "1.3M高清全景-OX01G20-金属方案",
                "link": "/cam/08-1-3m-ox01g20-spec-e8a4b2"
              },
              {
                "text": "1.3M高清后视&全景-GC1904格科-塑料方案",
                "link": "/cam/09-1-3m-and-gc1904-spec-76812b"
              },
              {
                "text": "1.3M高清后视&全景-OX01G20-塑料方案",
                "link": "/cam/10-1-3m-and-ox01g20-spec-41dc39"
              },
              {
                "text": "1.3M高清后视&全景-OX01K10-塑料方案",
                "link": "/cam/11-1-3m-and-ox01k10-spec-7202a2"
              },
              {
                "text": "1.3M高清后视&全景-SC120AT-塑料方案",
                "link": "/cam/12-1-3m-and-sc120at-spec-bfda35"
              },
              {
                "text": "1.3M高清后视&全景-SC121AT-塑料方案",
                "link": "/cam/13-1-3m-and-sc121at-spec-f923e9"
              },
              {
                "text": "1.3M高清后视-OX01G20-金属方案",
                "link": "/cam/14-1-3m-ox01g20-spec-d12918"
              }
            ]
          },
          {
            "text": "2M 规格",
            "collapsed": false,
            "items": [
              {
                "text": "2M高清乘客监控摄像头-OV02778+FH8310+TI953",
                "link": "/cam/15-2m-ov02778-plus-fh8310-plus-ti953-spec-7d8836"
              },
              {
                "text": "2M高清行车记录仪摄像头-OVX2D+FH8332+MAX9671...",
                "link": "/cam/16-2m-ovx2d-plus-fh8332-plus-max96717f-spec-f3febb"
              },
              {
                "text": "2M高清驾驶员监控摄像头-OV2311+FH8332+MAX967...",
                "link": "/cam/17-2m-ov2311-plus-fh8332-plus-max96717f-spec-8d29c9"
              }
            ]
          },
          {
            "text": "2.5M 规格",
            "collapsed": false,
            "items": [
              {
                "text": "2.5M高清后视&周视-OX01C10-金属方案",
                "link": "/cam/18-2-5m-and-ox01c10-spec-5aaab4"
              }
            ]
          },
          {
            "text": "3M 规格",
            "collapsed": false,
            "items": [
              {
                "text": "3M高清全景-ISX031-金属方案",
                "link": "/cam/19-3m-isx031-spec-e7778b"
              },
              {
                "text": "3M高清全景-OX03J10-金属方案",
                "link": "/cam/20-3m-ox03j10-spec-80a507"
              }
            ]
          },
          {
            "text": "8M 规格",
            "collapsed": false,
            "items": [
              {
                "text": "8M高清前视摄像头-OX08D10-金属方案",
                "link": "/cam/21-8m-ox08d10-spec-a9406a"
              }
            ]
          }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/lhnows/vitepress-template' }
    ],

    docFooter: {
      prev: '上一篇',
      next: '下一篇'
    },
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '菜单',
    darkModeSwitchLabel: '外观',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式'
  }
})
