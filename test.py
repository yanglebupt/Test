import json


arg1 = "{\n  \"name\": \"CandidateSelectionAndInterviewInvitation\",\n  \"mode\": \"crew\",\n  \"type\": \"flow\",\n  \"works\": [\n    {\n      \"name\": \"job_and_candidate_info_processing\",\n      \"description\": \"分析岗位需求和候选人简历，提取关键信息\",\n      \"mode\": \"crew\"\n    },\n    {\n      \"name\": \"iterate_candidates_for_scoring\",\n      \"description\": \"遍历所有候选人并为每位候选人打分\",\n      \"mode\": \"function\"\n    },\n    {\n      \"name\": \"candidate_scoring\",\n      \"description\": \"根据岗位与候选人之间的匹配程度，为每位候选人打分\",\n      \"mode\": \"crew\"\n    },\n    {\n      \"name\": \"select_best_candidate\",\n      \"description\": \"依据得分情况，选择最合适的候选人\",\n      \"mode\": \"crew\"\n    },\n    {\n      \"name\": \"draft_interview_invitation\",\n      \"description\": \"为被选中的候选人草拟一封面试邀请函\",\n      \"mode\": \"crew\"\n    },\n    {\n      \"name\": \"optimize_interview_invitation\",\n      \"description\": \"审查并优化面试邀请函的内容，使其更具吸引力\",\n      \"mode\": \"crew\"\n    }\n  ]\n}"

js = arg1.split("```json")[-1].split("```")[0].replace("\xa0", "").strip()

print(js)