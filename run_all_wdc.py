datasets = ["all","computers", "cameras", "shoes", "watches"]
sizes = ["xlarge"]

import os
import time

gpu_id = 0

for d in datasets:
    for size in sizes:
        dataset = '_'.join(['wdc', d, size])
        for probability in [0.0, 0.1, 0.2, 0.4, 0.6]:
            for run_id in range(5):
                cmd = """CUDA_VISIBLE_DEVICES=%d python train_ditto.py \
                    --task %s \
                    --logdir results_wdc/ \
                    --fp16 \
                    --finetuning \
                    --batch_size 64 \
                    --lr 3e-5 \
                    --n_epochs 10 \
                    --run_id %d \
                    --test_typing_error %f \
                    --seed %d \
                    --summarize""" % (gpu_id, dataset, run_id, probability, run_id)
                # if da:
                #     cmd += ' --da del'
                # if dk:
                #     cmd += ' --dk product'
                # if attr != 'title':
                #     cmd += ' --summarize'
                print(cmd)
                #os.system(cmd)
