import courseStructure from '../../course-structure.json'

// 生成导航从课程结构配置
const level1 = courseStructure.levels.find(l => l.id === "1")!
const meta: Record<string, string> = {}

level1.modules.forEach(module => {
  meta[module.slug] = `${module.id}: ${module.title}`
})

export default meta

