#!/bin/bash
CUDA_VISIBLE_DEVICES=0 python train_ditto.py --task Structured/Beer --batch_size 64 --max_len 64 --lr 3e-5 --n_epochs 40 --finetuning --lm distilbert --fp16 --da del --dk product --summarize
