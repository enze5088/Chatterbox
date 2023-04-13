def sum_parameters(model):
    total_params = sum(p.numel() for p in model.parameters())
    print('模型参数总数：', total_params)