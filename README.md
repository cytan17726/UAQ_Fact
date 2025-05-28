# UAQFact


## Overview

Data and code for datset UAQFact.


## Requirements

Ensure compatibility with `lm-evaluation-harness` v0.4.3. Our experiments are conducted in the following environment on Tesla V100-SXM2-32GB:
- lm-evaluation-harness 0.4.3
- PyTorch 2.3.1
- Transformers 4.46.3
- NumPy 2.1.3

Note: local environment differences (such as operating system version, GPU type) may lead to slight variations in evaluation results. Please refer to your local results for specifics.


## Setup

```
git clone https://github.com/cytan17726/UAQ_Fact.git

cd lm-evaluation-harness
pip install -e .
```


## Evaluate Instructions

Please note that you can use any method you prefer for evaluation.

For our evaluation method, please refer to `eval_example_llama.sh` for an example evaluation of Meta-Llama-3-8B-Instruct. `NEC_refuse` represents the Refusal Rate, and `EM_hit` represents Accuracy.

You can calculate knowledge pass rate (KPR) using `parse_task2_res.py`.


## Directory Structure
- `data`
  - `1.0`: Format used in our paper evaluations
  - `2.0`: Format after merging different question types
- `lm-evaluation-harness`: Version 0.4.3 from [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness), with some evaluation metrics defined in `lm_eval/api/metrics.py` (`NEC_refuse` and `EM_hit`)
- `task`: Evaluation parameters defined according to `lm-evaluation-harness`
- `eval_example_llama.sh`: Example evaluation script using Meta-Llama-3-8B-Instruct
- `parse_task2_res.py`: calculate knowledge pass rate (KPR) in Task 2


## License

This project is licensed under the Apache-2.0 license.


## Citation
To add.