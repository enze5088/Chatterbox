export CUDA_VISIBLE_DEVICES=0,1,2,3
NUM_GPU=4
PORT_ID=$(expr $RANDOM + 1000)
export OMP_NUM_THREADS=8
torchrun  --nnodes=1 --nproc_per_node $NUM_GPU --master_port $PORT_ID run_clm_sft.py \
    --fp16 \
    --deepspeed ./configs/ds_zero2_no_offload.json \
    --model_name_or_path model_dir \
    --train_file ../../data/sft/train_datasets.csv \
    --validation_file ../../data/sft/test_datasets.csv \
    --learning_rate 3e-5 \
    --do_train \
    --do_eval \
    --evaluation_strategy steps \
    --num_train_epochs 2 \
    --output_dir './result/' \
    --save_total_limit 3 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --cache_dir './cache/' \
    --overwrite_output_dir \
    --eval_steps 50 \
    --save_steps 50 \
    --logging_steps 10 \
    --max_eval_samples 200 \
    --block_size 850 \
    --preprocessing_num_workers 32 \
    --dataloader_num_workers 8 \
    --load_best_model_at_end \
    "$@"
