export CUDA_VISIBLE_DEVICES=0,1,2,3
NUM_GPU=4
PORT_ID=$(expr $RANDOM + 1000)
export OMP_NUM_THREADS=8
torchrun  --nnodes=1 --nproc_per_node $NUM_GPU --master_port $PORT_ID train_clm.py \
    --fp16 \
    --deepspeed ./configs/ds_offload_without_config.json \
    --model_name_or_path "./model_file/LLaMA-zh-base/"  \
    --train_file "../data/datasets/train_datasets.csv" \
    --validation_file "../data/datasets/test_datasets.csv" \
    --learning_rate 1e-4 \
    --do_train \
    --do_eval \
    --evaluation_strategy steps \
    --num_train_epochs 1 \
    --output_dir './result/total/' \
    --save_total_limit 3 \
    --per_device_train_batch_size 16 \
    --per_device_eval_batch_size 16 \
    --cache_dir './cache/' \
    --overwrite_output_dir \
    --eval_steps 5000 \
    --save_steps 5000 \
    --logging_steps 10 \
    --max_eval_samples 50 \
    --block_size 256 \
    --preprocessing_num_workers 32 \
    --dataloader_num_workers 8 \
    "$@"
