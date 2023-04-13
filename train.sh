export CUDA_VISIBLE_DEVICES=0,1,2,3
NUM_GPU=4
PORT_ID=$(expr $RANDOM + 1000)
export OMP_NUM_THREADS=8
torchrun  --nnodes=1 --nproc_per_node $NUM_GPU --master_port $PORT_ID train_bloomZ.py \
    --fp16 \
    --deepspeed ./configs/ds_config.json \
    --model_name_or_path "./model_file/bloomz-1b-zh/"  \
    --train_file "./data/datasets/train_datasets.csv" \
    --validation_file "./data/datasets/test_datasets.csv" \
    --source_lang zh_XX \
    --target_lang zh_XX \
    --learning_rate 3e-5 \
    --do_train \
    --do_eval \
    --evaluation_strategy steps \
    --num_train_epochs 1 \
    --output_dir './result/total/' \
    --save_total_limit 3 \
    --per_device_train_batch_size 10 \
    --per_device_eval_batch_size 10 \
    --cache_dir './cache/' \
    --overwrite_output_dir \
    --predict_with_generate \
    --eval_steps 5000 \
    --save_steps 5000 \
    --logging_steps 10 \
    --max_eval_samples 50 \
    --max_source_length 768 \
    --max_target_length 768 \
    --generation_max_length 768 \
    --preprocessing_num_workers 32 \
    --predict_with_generate \
    --dataloader_num_workers 8 \
    "$@"

#     --fp16 \