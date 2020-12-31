import os
import time

datasets = """Dirty/DBLP-ACM
Dirty/DBLP-GoogleScholar
Dirty/iTunes-Amazon
Dirty/Walmart-Amazon
Structured/Amazon-Google
Structured/Beer
Structured/DBLP-ACM
Structured/DBLP-GoogleScholar
Structured/Fodors-Zagats
Structured/iTunes-Amazon
Structured/Walmart-Amazon
Textual/Abt-Buy
Textual/Company""".split('\n')

special_datasets = {
    'Structured/Beer': (16, 40),
    'Structured/iTunes-Amazon': (16, 40),
    'Structured/Fodors-Zagats': (16, 40),
    'Dirty/iTunes-Amazon': (16, 40),
    'Textual/Company': (16, 3)
}

# ops = """swap
# swap
# append_col
# del
# swap
# drop_col
# swap
# swap
# append_col
# drop_col
# drop_col
# swap
# del""".split('\n')

lms = ['roberta', 'roberta', 'roberta', 'roberta', 'roberta', 'roberta',
       'roberta', 'roberta', 'roberta', 'roberta', 'roberta', 'roberta', 'bert']

# lms = ['xlnet', 'roberta', 'roberta', 'roberta', 'xlnet', 'bert',
#        'bert', 'xlnet', 'roberta', 'bert', 'roberta', 'roberta', 'bert']

# lms = """distilbert
# bert
# xlnet
# roberta""".split('\n')

for dataset, lm in zip(datasets, lms):
    if dataset in special_datasets:
        batch_size, epochs = special_datasets[dataset]
    else:
        batch_size, epochs = 16, 15
    
    for probability in [0.0, 0.1, 0.2, 0.4, 0.6]:
        for run_id in range(5):
            cmd = """CUDA_VISIBLE_DEVICES=0 python train_ditto.py \
                --task %s \
                --logdir results_ditto/ \
                --finetuning \
                --batch_size %d \
                --lr 3e-5 \
                --fp16 \
                --lm %s \
                --n_epochs %d \
                --run_id %d \
                --test_typing_error %f \
                --seed %d""" % (dataset, batch_size, lm, epochs, run_id, probability, run_id)
            if 'Company' in dataset:
                cmd += ' --summarize'
            print(cmd)
            # os.system(cmd)
