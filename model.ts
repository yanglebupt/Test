/**
 * 工作流描述所需字段类型
 */
interface CrewJsonSchema {
  /**
   * 固定标记位
   */
  mode: "crew"
  /**
   * 工作流描述
   */
  description: string
  /**
   * 简短的概括性任务名称英文版(大驼峰命名法)
   */
  name: string
  /**
   * 智能体编排类型
   */
  type: "sequential" | "hierarchical" | "flow"
  /**
   * 拆分出来的子任务数组
   */
  works: Array<SingleWorkSchema | CrewJsonSchema>
}

/**
 * 单一子任务所需字段类型
 */
interface SingleWorkSchema {
  /**
   * 子任务名称的英文版(下划线命名法)
   */
  name: string
  /**
   * 子任务工作模式
   */
  mode: "function" | "agent"
  /**
   * 子任务描述
   */
  description: string
}