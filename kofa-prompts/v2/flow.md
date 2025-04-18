智能体描述：
简历生成和优化

子任务列表：
{
  "name": "Resume",
  "type": "sequential",
  "mode": "crew",
  "works": [
    {"name": "write_resume", "description": "生成简历", "mode": "agent"},
    {"name": "optimizate_resume", "description": "优化简历", "mode": "agent"}
  ]
}


智能体描述：
翻译、简历生成和优化、销售对话洞察分析和总结

子任务列表：
{
  "name": "TranslateResumeSales",
  "type": "hierarchical",
  "mode": "crew",
  "works": [
    [
      {"name": "write_translate", "description": "初步翻译", "mode": "agent"},
      {"name": "optimizate_translate", "description": "翻译优化", "mode": "agent"}
    ],
    [
      {"name": "write_resume", "description": "生成简历", "mode": "agent"},
      {"name": "optimizate_resume", "description": "优化简历", "mode": "agent"}
    ],
    [
      {"name": "sales_analysis", "description": "销售对话洞察分析", "mode": "agent"},
      {"name": "sales_summary", "description": "销售对话分析总结", "mode": "agent"}
    ]
  ]
}



智能体描述：
根据岗位信息，对每个候选人信息进行打分来衡量候选人是否适合这个岗位，选取最适合该岗位的候选人，写一封邀请面试的信

子任务列表：
{
  "name": "CandidateEvaluationAndInterviewInvitation",
  "type": "flow",
  "works": [
    {
      "name": "iterate_candidates",
      "description": "遍历所有候选人",
      "mode": "function"
    },
    {
      "name": "CandidateScoringAndScoreOptimization",
      "mode": "crew",  // 只有 mode 为 "crew"，才能进一步设置 type 和 works 形成嵌套结构
      "type": "Hierarchical",
      "works": [
        [
          {
            "name": "candidate_scoring",
            "description": "简历生成",
            "mode": "agent"
          },
          {
            "name": "optimizate_scoring",
            "description": "简历优化",
            "mode": "agent"
          }
        ],
        [
          {
            "name": "candidate_write",
            "description": "客服对话分析",
            "mode": "agent"
          },
          {
            "name": "candidate_write",
            "description": "客服对话总结",
            "mode": "agent"
          }
        ]
      ]
    },
    {
      "name": "best_candidate_selection",
      "description": "从所有候选人中选择得分最高的候选人",
      "mode": "function"
    },
    {
      "name": "LetterWriter",
      "mode": "crew",
      "type": "Sequential",
      "works": [
        {
          "name": "interview_invitation_letter_generation",
          "description": "为选定的候选人生成一封邀请面试的信",
          "mode": "agent"
        },
        {
          "name": "letter_optimization",
          "description": "优化邀请面试的信件，使其更加专业和吸引人",
          "mode": "agent"
        }
      ]
    }
  ]
}


智能体描述：
根据当前的时间段编写不同的内容，上午时刻编写一段美好的童话故事，下午时刻编写一段美好的爱情故事，晚上时刻编写一段新闻实事

子任务列表：
{
  "name": "TimeBasedContentCreation",
  "type": "flow",
  "works": [
    {
      "name": "condition_check",
      "description": "根据当前的时间段判断应生成童话故事、爱情故事还是新闻实事",
      "mode": "function"
    },
    {
      "name": "fairy_tale_crew",
      "type": "Sequential",
      "mode": "crew",
      "works": [
        {
          "name": "fairy_tale_crew",
          "description": "在上午时段生成一段美好的童话故事",
          "mode": "agent"
        }
      ],
    },
    {
      "name": "romance_story_crew",
      "type": "Sequential",
      "mode": "crew",
      "works": [
        {
          "name": "romance_story_crew",
          "description": "在下午时段生成一段美好的爱情故事",
          "mode": "agent",
        }
      ]
    },
    {
      "name": "news_report_crew",
      "type": "Sequential",
      "mode": "crew",
      "works": [
        {
          "name": "news_report_crew",
          "description": "在晚上时段生成一段新闻实事",
          "mode": "agent",
        }
      ]
    },
    {
      "name": "content_optimization_crew",
      "type": "Sequential",
      "mode": "crew",
      "works": [
        {
          "name": "content_optimization_crew",
          "description": "对生成的所有内容进行优化，如调整情节、美化语言等，提高最终输出的质量",
          "mode": "agent",
        }
      ]
    }
  ]
}