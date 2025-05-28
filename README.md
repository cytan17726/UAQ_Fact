# UAQFact


## Overview

Data and code for datset UAQFact.

## Requirements

Ensure compatibility with `lm-evaluation-harness` v0.4.3. Our experiments are conducted in the following environment:
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
Refer to `eval_example_llama.sh` for an example evaluation of Meta-Llama-3-8B-Instruct. `NEC_refuse` represents the Refusal Rate, and `EM_hit` represents Accuracy.


## Directory Structure
- `data`
  - `1.0`: Format used in our paper evaluations
  - `2.0`: Format after merging different question types
- `lm-evaluation-harness`: Version 0.4.3 from [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness), with some evaluation metrics defined in `lm_eval/api/metrics.py` (`NEC_refuse` and `EM_hit`)
- `task`: Evaluation parameters defined according to `lm-evaluation-harness`
- `eval_example_llama.sh`: Example evaluation script using Meta-Llama-3-8B-Instruct


## License

This project is licensed under the Apache-2.0 license.

## Citation
To add.