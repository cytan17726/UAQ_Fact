model_path=XXX/Meta-Llama-3-8B-Instruct
output_path=./output/debug/
task=FUAQ_task1_en,FUAQ_task1_zh,FUAQ_task2_zh_ua_mc,FUAQ_task2_en_ua_mc,FUAQ_task3_en,FUAQ_task3_zh # eval all task
# Task 1: FUAQ_task1_en,FUAQ_task1_zh  
# Task 2: FUAQ_task2_zh_ua_mc,FUAQ_task2_en_ua_mc
# Task 3: FUAQ_task3_en,FUAQ_task3_zh

dtype=float16
gpu_id=0

CUDA_VISIBLE_DEVICES=${gpu_id} lm_eval \
    --model hf \
    --model_args pretrained=${model_path},dtype=${dtype},device_map=cuda,trust_remote_code=True\
    --include_path task/uaq_fact/ \
    --task $task\
    --output_path $output_path \
    --seed 42 \
    --apply_chat_template \
    --log_samples \
    --limit 10 \
    # --use_cache $output_path \
    
    