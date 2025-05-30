# UAQFact


## Overview

Data and code for datset UAQFact. The relevant paper is accepted by ACL 2025 Findings: [[ArXiv]](https://arxiv.org/pdf/2505.23461).


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
```
@misc{tan2025uaqfact,
      title={UAQFact: Evaluating Factual Knowledge Utilization of LLMs on Unanswerable Questions}, 
      author={Chuanyuan Tan and Wenbiao Shao and Hao Xiong and Tong Zhu and Zhenhua Liu and Kai Shi and Wenliang Chen},
      year={2025},
      eprint={2505.23461},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2505.23461}, 
}
```