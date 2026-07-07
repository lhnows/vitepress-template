<template>
  <div class="robotics-home" id="top">
    <header class="site-header" :class="{ 'is-scrolled': isScrolled, 'is-open': isMenuOpen }">
      <a class="brand" href="#top" aria-label="晟泰克机器人事业部首页" @click="closeMenu">
        <img class="brand-logo" src="/robotics/softec-logo.svg" alt="Softec 晟泰克" />
        <span class="brand-unit">机器人事业部</span>
      </a>
      <nav class="nav" aria-label="主导航">
        <a href="#platform" @click="closeMenu">开发平台</a>
        <a href="#products" @click="closeMenu">产品体系</a>
        <a href="/cam/" @click="closeMenu">规格书中心</a>
        <a href="#scenes" @click="closeMenu">场景方案</a>
        <a href="#quality" @click="closeMenu">车规能力</a>
        <a href="#contact" @click="closeMenu">联系咨询</a>
      </nav>
      <button class="menu-button" type="button" :aria-label="isMenuOpen ? '关闭导航' : '打开导航'" @click="isMenuOpen = !isMenuOpen">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </header>

    <main>
      <section class="hero" aria-label="机器人事业部介绍">
        <img class="hero-media" src="/robotics/factory-line-27.png" alt="晟泰克数字化生产车间" />
        <div class="hero-overlay"></div>
        <div class="hero-content">
          <p class="eyebrow">车规感知能力进入机器人现场</p>
          <h1>机器人全域感知与域控开发加速平台</h1>
          <p class="hero-copy">
            面向具身智能创业团队、机器人公司预研部门、高校实验室与智能装备厂商，提供 GMSL 车规相机、多目同步采集、激光雷达导航与避障、超声波近场安全冗余、Jetson 域控与 ROS2 / Isaac ROS Demo，帮助客户从样机验证走向量产迁移。
          </p>
          <div class="hero-actions" aria-label="主要操作">
            <a class="button primary" href="#contact">预约方案沟通</a>
            <a class="button secondary" href="#products">查看产品体系</a>
            <a class="button secondary" href="/cam/">摄像头规格书</a>
          </div>
          <dl class="hero-metrics" aria-label="能力指标">
            <div>
              <dt>10M+</dt>
              <dd>车规产品年级别出货经验</dd>
            </div>
            <div>
              <dt>多模态</dt>
              <dd>视觉、激光、超声组合感知</dd>
            </div>
            <div>
              <dt>ROS2</dt>
              <dd>开发镜像、驱动与 Demo</dd>
            </div>
          </dl>
        </div>
      </section>

      <section class="intro band">
        <div class="section-heading compact">
          <p class="eyebrow">Positioning</p>
          <h2>做机器人客户的工程底座，而不是另一家整机公司</h2>
        </div>
        <div class="intro-grid">
          <article>
            <span class="icon-dot"></span>
            <h3>前期跑起来</h3>
            <p>提供硬件接入、系统镜像、ROS2 驱动、采集录制、检测识别、标定和同步工具，缩短从接线到 Demo 的周期。</p>
          </article>
          <article>
            <span class="icon-dot"></span>
            <h3>中期做闭环</h3>
            <p>围绕巡检、AMR、割草、叉车、清洁配送等真实场景，沉淀可复用的多传感器感知包和算法 Demo。</p>
          </article>
          <article>
            <span class="icon-dot"></span>
            <h3>后期可量产</h3>
            <p>依托车规级设计、验证、供应链和制造体系，帮助客户从开发板样机迁移到可靠、可追溯、可交付的量产方案。</p>
          </article>
        </div>
      </section>

      <section class="capabilities" id="platform">
        <div class="section-heading">
          <p class="eyebrow">Platform</p>
          <h2>从传感器到域控，从驱动到 Demo 的一体化平台</h2>
          <p>把开源算法、Jetson、GMSL 摄像头、激光雷达、超声波雷达、Docker、ROS2 和工程文档串起来，让机器人开发团队少踩底层集成的坑。</p>
        </div>
        <div class="platform-layout">
          <div class="platform-panel">
            <div class="flow">
              <div>相机 / 激光 / 超声</div>
              <span></span>
              <div>多传感器接入与同步</div>
              <span></span>
              <div>Jetson 域控</div>
              <span></span>
              <div>ROS2 数据流</div>
            </div>
            <div class="platform-note">
              <h3>开发者拿到的是完整工作流</h3>
              <p>系统镜像、设备树与驱动适配、相机标定、多目同步、激光雷达接入、超声近场防护、数据录制回放、YOLO 检测、视觉避障、Visual SLAM 入门 Demo。</p>
            </div>
          </div>
          <div class="capability-list">
            <article>
              <h3>GMSL 多目接入</h3>
              <p>支持长距离传输、低延迟、多摄像头同步与车规级接插件，适合机器人头部、胸部、腰部、盲区和环视布置。</p>
            </article>
            <article>
              <h3>安全冗余感知</h3>
              <p>超声波雷达补足视觉和激光雷达近场盲区，对透明、黑色、强反光、粉尘和强光环境具备工程价值。</p>
            </article>
            <article>
              <h3>激光雷达导航补充</h3>
              <p>覆盖 270°、360°、固态广角和多线环视产品形态，为 AMR、AGV、无人叉车和巡检机器人提供轮廓、避障和区域防护能力。</p>
            </article>
            <article>
              <h3>边缘计算域控</h3>
              <p>以 NVIDIA Jetson 快速验证，后续可按成本、功耗、国产化和量产需求迁移到地瓜、瑞芯微等平台。</p>
            </article>
          </div>
        </div>
      </section>

      <section class="products band" id="products">
        <div class="section-heading">
          <p class="eyebrow">Products</p>
          <h2>全域感知产品矩阵，覆盖开发、预研和场景落地</h2>
        </div>
        <div class="product-grid">
          <article class="product-card">
            <img src="/robotics/camera-product-21.png" alt="晟泰克车规摄像头产品" />
            <div>
              <p class="tag">GMSL Camera</p>
              <h3>车规相机与多目 GMSL 接入</h3>
              <p>基于车规摄像头模组和 GMSL 长距离低延迟链路，支持多相机同步、环视布置、头部/胸部/腰部视觉和数据采集。</p>
              <ul>
                <li>适合机器人头部、环视、盲区和远程视频回传</li>
                <li>可与 Jetson、ROS2、标定工具和算法 Demo 配套</li>
              </ul>
              <a class="inline-link" href="/cam/">查看摄像头产品规格书</a>
            </div>
          </article>
          <article class="product-card">
            <img src="/robotics/ultrasonic/uss-product-20.png" alt="晟泰克超声波雷达产品" />
            <div>
              <p class="tag">Ultrasonic Radar</p>
              <h3>超声波近场安全雷达</h3>
              <p>面向机器人和智能装备近场安全冗余，补足视觉和激光雷达在 0-50 cm、防撞、防跌落和特殊材质探测中的不足。</p>
              <ul>
                <li>适合 AMR、AGV、无人叉车、清洁配送和割草机器人</li>
                <li>车规级一致性、验证体系和供应链能力可迁移</li>
              </ul>
            </div>
          </article>
          <article class="product-card">
            <img src="/robotics/lidar/LIDAR360mini1-1.png" alt="晟泰克 LIDAR360mini 激光雷达" />
            <div>
              <p class="tag">LiDAR</p>
              <h3>自研激光雷达系列</h3>
              <p>覆盖紧凑型 270°、360°、轻量 slim、全固态广角和 48 线环视产品，用于导航、轮廓测量、区域防护和复杂环境避障。</p>
              <ul>
                <li>LIDAR270mini、LIDAR360mini、LIDAR360-slim</li>
                <li>LIDARX-S50、LIDARX-360-48</li>
              </ul>
            </div>
          </article>
          <article class="product-card">
            <img src="/robotics/lab-equipment-17.png" alt="晟泰克实验室验证设备" />
            <div>
              <p class="tag">Development Kit</p>
              <h3>域控开发套件与场景 Demo</h3>
              <p>Jetson Orin Nano / Orin NX + GMSL 摄像头 + 激光/超声接口，配套系统镜像、Docker、ROS2 驱动、采集和检测 Demo。</p>
              <ul>
                <li>适合高校、实验室、预研部门和新创业团队</li>
                <li>目标体验：1 天跑起来，1 周改 Demo</li>
              </ul>
            </div>
          </article>
        </div>
        <div class="sensor-panels">
          <article>
            <p class="tag">Ultrasonic Role</p>
            <h3>超声波雷达：近场、低速、安全冗余</h3>
            <p>重点解决机器人贴近人、墙面、货架、玻璃、黑色物体、强反光物体时的防撞和防跌落问题，适合和视觉、激光雷达形成低速安全冗余。</p>
          </article>
          <article>
            <p class="tag">LiDAR Role</p>
            <h3>激光雷达：导航、轮廓、区域防护</h3>
            <p>270°/360° 扫描、固态广角和多线环视产品可覆盖 AMR 导航、无人叉车避障、巡检机器人区域防护和户外低速无人设备轮廓感知。</p>
          </article>
        </div>
      </section>

      <section class="scenes" id="scenes">
        <div class="section-heading">
          <p class="eyebrow">Scenes</p>
          <h2>优先服务有真实业务场景、缺工程闭环的成长型客户</h2>
        </div>
        <div class="scene-grid">
          <article>
            <span>01</span>
            <h3>巡检 / 防爆 / 电力化工机器人</h3>
            <p>可见光 + 红外 + 超声 + 激光雷达融合，支撑异常识别、缺陷识别、远程视频回传和复杂环境避障。</p>
          </article>
          <article>
            <span>02</span>
            <h3>AMR / AGV / 无人叉车</h3>
            <p>围绕盲区检测、人员靠近预警、货叉区域视觉、托盘识别、激光导航和超声近场防撞，提供低速移动安全感知包。</p>
          </article>
          <article>
            <span>03</span>
            <h3>农业 / 割草 / 园区无人设备</h3>
            <p>面向低速户外感知，支持草地边界、低矮障碍物、人和宠物识别、激光轮廓感知、园区道路边界与可靠性验证。</p>
          </article>
          <article>
            <span>04</span>
            <h3>清洁 / 配送 / 服务机器人</h3>
            <p>多摄像头全景感知、儿童和行人识别、低矮障碍物检测、复杂光照鲁棒性和成本优化。</p>
          </article>
          <article>
            <span>05</span>
            <h3>传统机械设备智能化</h3>
            <p>帮助叉车、工程机械、清扫车、物流装备和特种车辆补齐智能感知、安全避障和远程运维能力。</p>
          </article>
          <article>
            <span>06</span>
            <h3>高校 / 实验室 / 开发者</h3>
            <p>提供课程、文档、视频、软件包和技术支持，让开发者更低成本完成硬件、算法、系统闭环。</p>
          </article>
        </div>
      </section>

      <section class="quality band" id="quality">
        <div class="quality-media">
          <img src="/robotics/company-intro-04.png" alt="晟泰克公司介绍" />
        </div>
        <div class="quality-copy">
          <p class="eyebrow">Automotive-Grade</p>
          <h2>车规级研发、验证与制造体系，是机器人业务的确定性资产</h2>
          <p>
            晟泰克机器人事业部继承汽车电子领域沉淀的产品设计、实验验证、供应链管理、数字化制造和质量追溯能力，以更高的一致性和可靠性服务机器人与智能装备客户。
          </p>
          <div class="quality-points">
            <div>
              <strong>一致性</strong>
              <span>批量产品稳定交付，降低客户调试成本。</span>
            </div>
            <div>
              <strong>验证体系</strong>
              <span>面向 EMC、环境、耐久、功能和可靠性做工程验证。</span>
            </div>
            <div>
              <strong>量产迁移</strong>
              <span>从开发套件、半定制方案到可追溯量产交付。</span>
            </div>
          </div>
        </div>
      </section>

      <section class="roadmap">
        <div class="section-heading compact">
          <p class="eyebrow">Customer Path</p>
          <h2>从 Demo 到量产的合作路径</h2>
        </div>
        <ol class="timeline">
          <li>
            <span>1</span>
            <h3>需求澄清</h3>
            <p>明确机器人形态、传感器布置、算力平台、通信接口、环境约束和成本目标。</p>
          </li>
          <li>
            <span>2</span>
            <h3>样机验证</h3>
            <p>提供套件、驱动、镜像、Demo、标定与采集工具，完成可演示闭环。</p>
          </li>
          <li>
            <span>3</span>
            <h3>场景适配</h3>
            <p>围绕客户真实现场调试算法、接口、结构安装、可靠性和数据采集流程。</p>
          </li>
          <li>
            <span>4</span>
            <h3>量产迁移</h3>
            <p>优化 BOM、国产化平台、线束接插件、测试规范、供应链和质量追溯。</p>
          </li>
        </ol>
      </section>

      <section class="contact" id="contact">
        <div>
          <p class="eyebrow">Contact</p>
          <h2>把你的机器人场景跑起来</h2>
          <p>告诉我们你的机器人形态、目标场景、现有算力平台和传感器需求，晟泰克机器人事业部将协助评估全域感知、超声安全冗余、激光导航避障和域控开发方案。</p>
          <div class="contact-direct">
            <a href="tel:+8655165735706">
              <span>电话</span>
              <strong>0551-65735706</strong>
            </a>
            <a href="mailto:stk@hfstk.com">
              <span>邮箱</span>
              <strong>stk@hfstk.com</strong>
            </a>
            <a href="https://www.hfstk.com" target="_blank" rel="noreferrer">
              <span>官网</span>
              <strong>www.hfstk.com</strong>
            </a>
            <p>
              <span>总部</span>
              <strong>安徽省合肥市经济技术开发区合掌路 27 号</strong>
            </p>
          </div>
        </div>
        <form class="contact-form" @submit.prevent="submitLead">
          <label>
            <span>项目类型</span>
            <select v-model="lead.type">
              <option>机器人全域感知开发套件</option>
              <option>多目 GMSL 感知套件</option>
              <option>超声波近场安全雷达</option>
              <option>激光雷达导航 / 避障</option>
              <option>AMR / 无人叉车安全感知</option>
              <option>巡检 / 防爆 / 电力化工机器人</option>
              <option>农业 / 割草 / 园区无人设备</option>
            </select>
          </label>
          <label>
            <span>联系方式</span>
            <input v-model="lead.contact" type="text" placeholder="手机号 / 邮箱 / 微信" required />
          </label>
          <label>
            <span>需求描述</span>
            <textarea v-model="lead.message" rows="4" placeholder="例如：4 路 GMSL 相机 + LIDAR360mini + 超声近场防撞 + Jetson Orin NX，应用在无人叉车盲区检测" required></textarea>
          </label>
          <button class="button primary" type="submit" :disabled="isSubmitting">{{ submitText }}</button>
          <p class="form-status" aria-live="polite">{{ formStatus }}</p>
        </form>
      </section>
    </main>

    <footer class="site-footer">
      <p>合肥晟泰克汽车电子股份有限公司 · 机器人事业部</p>
      <p>电话：0551-65735706 · 邮箱：stk@hfstk.com · 官网：www.hfstk.com</p>
      <p>车规全域感知 · GMSL 多目接入 · 激光雷达 · 超声波安全冗余 · 域控开发平台</p>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, reactive, ref } from 'vue'

const isScrolled = ref(false)
const isMenuOpen = ref(false)
const isSubmitting = ref(false)
const formStatus = ref('')
const submitState = ref<'idle' | 'success' | 'retry'>('idle')
const lead = reactive({
  type: '机器人全域感知开发套件',
  contact: '',
  message: ''
})

const submitText = computed(() => {
  if (isSubmitting.value) return '提交中...'
  if (submitState.value === 'success') return '提交成功'
  if (submitState.value === 'retry') return '重新提交'
  return '提交需求'
})

function syncHeader() {
  isScrolled.value = window.scrollY > 12
}

function closeMenu() {
  isMenuOpen.value = false
}

async function submitLead() {
  const webhookUrl = import.meta.env.VITE_STK_WEBHOOK_URL || ''
  if (!webhookUrl) {
    formStatus.value = '请直接通过电话或邮箱联系晟泰克，线上提交通道暂未配置。'
    submitState.value = 'retry'
    return
  }

  const payload = formatWebhookPayload(webhookUrl, {
    source: '晟泰克机器人事业部官网',
    projectType: lead.type,
    contact: lead.contact,
    message: lead.message,
    page: window.location.href,
    userAgent: navigator.userAgent,
    language: navigator.language,
    submittedAt: new Date().toISOString()
  })

  isSubmitting.value = true
  formStatus.value = ''

  try {
    const response = await fetch(webhookUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`)
    }

    const result = await response.json().catch(() => null)
    if (result && typeof result.errcode === 'number' && result.errcode !== 0) {
      throw new Error(result.errmsg || `Webhook error ${result.errcode}`)
    }

    lead.type = '机器人全域感知开发套件'
    lead.contact = ''
    lead.message = ''
    formStatus.value = '需求已提交，我们会尽快联系您。'
    submitState.value = 'success'
  } catch {
    formStatus.value = '提交失败，请稍后重试或直接联系晟泰克。'
    submitState.value = 'retry'
  } finally {
    isSubmitting.value = false
  }
}

function formatWebhookPayload(webhookUrl: string, payload: Record<string, string>) {
  if (webhookUrl.includes('qyapi.weixin.qq.com/cgi-bin/webhook/send')) {
    return {
      msgtype: 'markdown',
      markdown: {
        content: [
          '### 晟泰克机器人事业部官网新留言',
          `> 项目类型：${payload.projectType || '未填写'}`,
          `> 联系方式：${payload.contact || '未填写'}`,
          `> 需求描述：${payload.message || '未填写'}`,
          `> 来源页面：${payload.page}`,
          `> 提交时间：${payload.submittedAt}`
        ].join('\n')
      }
    }
  }

  return payload
}

onMounted(() => {
  syncHeader()
  window.addEventListener('scroll', syncHeader, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('scroll', syncHeader)
})
</script>
