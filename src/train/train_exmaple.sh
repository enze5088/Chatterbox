export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
NUM_GPU=8
PORT_ID=$(expr $RANDOM + 1000)
export OMP_NUM_THREADS=8
torchrun  --nnodes=1 --nproc_per_node $NUM_GPU --master_port $PORT_ID train_clm.py \
    --deepspeed ./configs/ds_bf16_config.json \
    --bf16 \
    --model_name_or_path "./data/models/LLaMA-zh-base/"  \
    --train_file "./data/output/train.csv" \
    --validation_file "./data/output/test.csv" \
    --learning_rate 1e-4 \
    --do_train \
    --do_eval \
    --evaluation_strategy steps \
    --num_train_epochs 1 \
    --output_dir './result/LLaMA-zh-base/' \
    --save_total_limit 3 \
    --per_device_train_batch_size 36 \
    --per_device_eval_batch_size 36 \
    --cache_dir './cache/' \
    --overwrite_output_dir \
    --eval_steps 20000 \
    --save_steps 20000 \
    --logging_steps 20 \
    --max_eval_samples 50 \
    --block_size 512 \
    --preprocessing_num_workers 400 \
    --ddp_timeout 72000 \
    --dataloader_num_workers 36 \
    --lr_scheduler_type cosine \
     "$@"
