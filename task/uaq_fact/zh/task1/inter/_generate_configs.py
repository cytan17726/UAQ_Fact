"""
Take in a YAML, and output all "other" splits with this YAML
"""
import os
import yaml
from tqdm import tqdm
BASE_DIR = "/public/home/wlchen/cytan/llm_eval/data/FUAQ"

dataset = {
    # "inter_ua_zh": f"{BASE_DIR}/data/final_main_que/inter_ua_zh.json",
    "inter_ua_en": f"{BASE_DIR}/inter_ua_en.json",
    # "inter_ab_zh": f"{BASE_DIR}/data/final_main_que/inter_ab_zh.json",
    "inter_ab_en": f"{BASE_DIR}/inter_ab_en.json",
}

dev_sets = {
    # "inter_ua_zh": f"{BASE_DIR}/data/dev/inter_zh_dev.json",
    "inter_ua_en": f"{BASE_DIR}/dev/inter_en_dev.json",
    # "inter_ab_zh": f"{BASE_DIR}/data/dev/inter_zh_dev.json",
    "inter_ab_en": f"{BASE_DIR}/dev/inter_en_dev.json",
}

# task
description_dict = {
    "base": {
        # "zh":"在1句话以内回答给定问题。确保你的答案简短并简洁。如果你认为不存在合适答案，返回##None##。\n\n",
        "en":"Answer the given question in no more than one sentence. Please keep your answer short and concise. Return ##None## if there is no suitable answer.\n\n"
    },
    # "cls":{
    #     "zh": "判断问题是否存在合适的答案。回复##是##或##否##。\n\n",
    #     "en": "Determine whether a suitable answer exists for the question. Relpy ##Yes## or ##No##.\n\n"
    # }
}
doc_to_text_dict = {
    "base": {
        "zh":"问题: {{question}}\n答案:",
        "en":"Q: {{question}}\nA:"
    },
    # "cls":{
    #     "zh": "问题: {{question}}\n是否有答案:",
    #     "en": "Question: {{question}}\nDoes the answer exist:"
    # }
}

doc_to_target_dict = {
    "base": {
        "zh":f'!function utils.arr_doc_to_target_base',
        "en":f'!function utils.arr_doc_to_target_base'
    },
    # "cls":{
    #     "zh": "{{cls_target}}",
    #     "en": "{{cls_target}}"
    # }
}

base_yaml_dict = {
    "base": "_arr_generate_until_template_base_yaml",
    # "cls": "_arr_generate_until_template_cls_yaml"
}

def dump_yaml(data:dict, filename, **kargs):
    with open(filename, "w", encoding="utf-8") as yaml_file:
        yaml.dump(
            data,
            yaml_file,
            **kargs
        )

if __name__ == "__main__":
    save_prefix_path = "./"# 保存的目录

    language = ["en"]
    answerable = ["ua", "ab"]
    que_type = ["inter"]
    # test_task = ["base", "cls"]
    test_task = ["base",]

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
                    task_name = f"FUAQ_{_lan}_{_que_type}_{_task}_{_answerable}"
                    file_save_path = os.path.join(save_prefix_path,task_name+".yaml")
                    group_name = "FUAQ_ABQ" if _answerable=="ab" else "FUAQ_UAQ"
                    yaml_dict = {
                        "task": task_name,
                        # "group": group_name,
                        "dataset_kwargs":{
                            "data_files":{
                                "test": dataset[f"{_que_type}_{_answerable}_{_lan}"],
                                "validation": dev_sets[f"{_que_type}_{_answerable}_{_lan}"]
                            }
                        },
                        "doc_to_text": doc_to_text_dict[_task][_lan],
                        "description": description_dict[_task][_lan],
                        "include": base_yaml_name
                    }
                    if task_name not in ALL_CATEGORIES:
                        ALL_CATEGORIES.append(task_name)
                    ALL_TASK.append(task_name)
                    dump_yaml(yaml_dict, file_save_path, allow_unicode=True, default_style='"')


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
