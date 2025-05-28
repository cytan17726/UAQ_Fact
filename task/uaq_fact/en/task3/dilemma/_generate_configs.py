"""
Take in a YAML, and output all "other" splits with this YAML
"""
import os

import yaml
from tqdm import tqdm

BASE_DIR = "/public/home/wlchen/cytan/llm_eval/data/FUAQ"
# /data2/wbshao/LLM/lm-evaluation-harness-main/my_eval/data/final_sup_que/logic/dilemma/dev/

dataset = {
    "dilemma_ua_zh": f"{BASE_DIR}/task3/dilemma/dilemma_sup_logic_ua_zh.json",
    "dilemma_ua_en": f"{BASE_DIR}/task3/dilemma/dilemma_sup_logic_ua_en.json",
    "dilemma_ab_zh": f"{BASE_DIR}/task3/dilemma/dilemma_sup_logic_ab_zh.json",
    "dilemma_ab_en": f"{BASE_DIR}/task3/dilemma/dilemma_sup_logic_ab_en.json",
}

dev_sets = {
    "dilemma_ua_zh": f"{BASE_DIR}/task3/dev/dilemma_zh.json",
    "dilemma_ua_en": f"{BASE_DIR}/task3/dev/dilemma_en.json",
    "dilemma_ab_zh": f"{BASE_DIR}/task3/dev/dilemma_zh.json",
    "dilemma_ab_en": f"{BASE_DIR}/task3/dev/dilemma_en.json",
}
# task
description_dict = {
    "zh": "在1句话以内回答给定问题。确保你的答案简短并简洁。如果你认为不存在合适答案，返回##None##。\n\n",
    "en": "Answer the given question in no more than one sentence. Please keep your answer short and concise. Return ##None## if there is no suitable answer.\n\n"
}


base_yaml_dict = {
    "sup_logic_CoT_QA": "_arr_generate_until_template_base_yaml",
}

def dump_yaml(data:dict, filename, **kargs):
    with open(filename, "w", encoding="utf-8") as yaml_file:
        yaml.dump(
            data,
            yaml_file,
            **kargs
        )

if __name__ == "__main__":
    save_prefix_path = "./"

    language = ["en", "zh"]
    answerable = ["ua", "ab"]
    # que_type = ["inter", "time", "dilemma"]
    que_type = ["dilemma"]
    test_task = ["sup_logic_CoT_QA"]

    ALL_CATEGORIES = []
    ALL_TASK = []
    # _lan = "en"
    # _answerable = "ab"
    # _task = "base"
    # _que_type = "inter"
    for _lan in language:
        for _que_type in que_type:
            for _task in test_task:
                for _answerable in answerable:
                    base_yaml_name = base_yaml_dict[_task]
                    task_name = f"arr_generate_until_sup_{_lan}_{_que_type}_{_task}_{_answerable}"
                    file_save_path = os.path.join(save_prefix_path,task_name+".yaml")
                    group_name = f"arr_generate_until_sup_{_lan}_{_task}"
                    yaml_dict = {
                        "task": task_name,
                        "group": group_name,
                        "dataset_kwargs":{
                            "data_files":{
                                "test": dataset[f"{_que_type}_{_answerable}_{_lan}"],
                                "validation": dev_sets[f"{_que_type}_{_answerable}_{_lan}"]
                            }
                        },
                        # "doc_to_text": doc_to_text_dict[_lan],
                        "description": description_dict[_lan],
                        "include": base_yaml_name
                    }
                    if group_name not in ALL_CATEGORIES:
                        ALL_CATEGORIES.append(group_name)
                    ALL_TASK.append(task_name)
                    dump_yaml(yaml_dict, file_save_path, allow_unicode=True, default_style='"')

    file_save_path = os.path.join(save_prefix_path, "_arr_generate_until_sup_logic_CoT_QA_dilemma_4_shot.yaml")
    arr_subcategories = [category for category in ALL_CATEGORIES]
    group_data = {
        "group": f"arr_generate_until_sup_logic_CoT_QA_dilemma_4_shot",
        "task": arr_subcategories,
        "num_fewshot": 4
    }
    dump_yaml(group_data, file_save_path, indent=4, default_flow_style=False)
    dump_yaml({"task": ALL_TASK}, "_all_task_name", indent=4, default_flow_style=False)
    # file_save_path = ""
    # # 保存group
    # with open(file_save_path, "w", encoding="utf-8") as yaml_file:
    #     yaml.dump(
    #         {
    #             "group": group_name,
    #             "task": mmlu_subcategories,
    #         },
    #         yaml_file,
    #         indent=4,
    #         default_flow_style=False,
    #     )
