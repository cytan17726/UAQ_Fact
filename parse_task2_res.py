import json
from collections import defaultdict

import os

def load_jsonlines(path):
    output = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            output.append(json.loads(line))
    return output

def parse_task2_res(filepath, mertic="acc_norm"):
    input_data = load_jsonlines(filepath)
    score_dict = defaultdict(list)
    for data in input_data:
        rel_qid_list = data["doc"]["relevent_qid_list"]
        score = data[mertic]
        for _qid in rel_qid_list:
            score_dict[_qid].append(score)
    task2_score_list = []
    for qid, score_list in score_dict.items():
        if 'ab' in qid:
            continue
        if sum(score_list) == len(score_list):
            task2_score_list.append(1)
        else:
            task2_score_list.append(0)
    return sum(task2_score_list) / len(task2_score_list), task2_score_list

if __name__ == "__main__":
    lang="en" 
    # lang="zh"

    res_dir = "./output/llama3-8B-instruct/task2"   # the dir contain file named "samples_FUAQ_en_ ..." or "samples_FUAQ_zh_ ...". make sure the dir is correct and contain only one file for each language.


    if lang == "en":
        start_str = "samples_FUAQ_en_"
    else:
        start_str = "samples_FUAQ_zh_"
    filelist = os.listdir(res_dir)
    res_file_list = []
    for file in filelist:
        if file.startswith(start_str):
            res_file_list.append(os.path.join(res_dir, file))
    if len(res_file_list) != 1:
        raise ValueError(f"The dir {res_dir} should contain only one file for each language.")
    filelist = res_file_list
    # 90.81 80.22 62.08
    KPR_list = []
    score_list = []
    for filepath in filelist:
        _KPR, _score_list = parse_task2_res(filepath, mertic="acc_norm")
        score_list.extend(_score_list)
        KPR_list.append(_KPR)
    # print(sum(KPR_list) / len(KPR_list))
    print(f"{sum(score_list)*100 / len(score_list):.2f}")
