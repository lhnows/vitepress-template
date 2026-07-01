// https://vitepress.dev/guide/custom-theme
import { h } from 'vue'
import { useData, type Theme } from 'vitepress'
import DefaultTheme from 'vitepress/theme'
import './style.css'
import './robotics-home.css'
import RoboticsHome from './components/RoboticsHome.vue'

const Layout = {
  setup() {
    const { page } = useData()

    return () => {
      if (page.value.relativePath === 'index.md') {
        return h(RoboticsHome)
      }

      return h(DefaultTheme.Layout)
    }
  }
}

export default {
  extends: DefaultTheme,
  Layout
} satisfies Theme
