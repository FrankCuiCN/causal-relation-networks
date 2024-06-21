# hyperparameter tuning
enable_hyperparameter_tuning_mode = True
# dataset
context_window = 257
num_class = 10
# dataloader
num_worker_dataloader = 8  # note: use 0 to disable
# model
# note: Transformer, Linear Transformer
#       Relation Network, Linear Relation Network
#       Relation Network Ablation
model_name = "Linear Relation Network"
model_load_path = "./../saved_weights/cifar5m/LRN_Cifar5m_final.pth"
enable_causal_mode = False
emb_size = 768
hid_size = 3072
num_block = 12
if model_name in ["Transformer", "Linear Transformer"]:
    num_head = 12
    head_size = 64
elif model_name in ["Relation Network", "Linear Relation Network", "Relation Network Ablation"]:
    num_head = 1
    head_size = 3072
normalization_type = "Layer Normalization"  # "Layer Normalization" or "RMS Normalization"
normalization_eps = 0.0
enable_relation_network_bias_1 = True
enable_relation_network_bias_2 = False
enable_relation_network_bias_3 = True
# optimization
enable_grad_clip = True
grad_clip_max_norm = 1.0
adamw_beta_1 = 0.9
adamw_beta_2 = 0.999
adamw_weight_decay = 0.0
adamw_eps = 1e-8
# learning rate schedule
# note: when training, the total number of iterations for one epoch is 18758
#     therefore, idx_end_decay should be 18757 (0~18757)
#     i.e.: f(idx=18757) = 5e-5
# note: the maximum lr s.t. lr don't plateau before 2k iters
lr_schedule_param = (1e-4, 1e-5, 2000, 18757)  # (lr_max, lr_terminal, idx_end_warm_up, idx_end_decay)
# training
num_epoch = 1
# note: effective_batch_size = num_grad_accu * batch_size
num_grad_accu = 1
batch_size = 1  # debug: should be 320
enable_torch_compile = True
# other
num_iter_train = None  # deprecated
num_iter_eval = 1
ablation_parameters = {"PreNorm": "approx",  # "exact", "approx", "no"
                       "PostNorm": "yes",  # "yes", "no"
                       "Activation": "exp"}  # "exp", "gelu", "elu"

# general
if enable_hyperparameter_tuning_mode:
    random_seed = 42
else:
    random_seed = None
wandb_project_name = "proj240517_cifar5m"
wandb_run_name = "{}-{}".format(model_name, context_window)
# save and load model
model_save_path = "./{}.pth".format(wandb_run_name)


print("# ----- #")
print("# Messages from config.py")
print("# ----- #")
print("Hyperparameter Tuning Mode:", enable_hyperparameter_tuning_mode)
print("context_window is", context_window)
print("model shape is ({}, {}, {})".format(emb_size, hid_size, num_block))
print("normalization type is", normalization_type)
print("learning rate schedule: ", lr_schedule_param)
print("effective batch size is ", num_grad_accu * batch_size)
print("run_name is", wandb_run_name)
print("# ----- #")

# [x] proofread
