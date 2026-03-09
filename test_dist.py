import torch
import torch.distributed as dist
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--master_ip", type=str)
parser.add_argument("--master_port", type=str)
parser.add_argument("--world_size", type=int)
parser.add_argument("--local_rank", type=int)
args = parser.parse_args()

dist.init_process_group(
    backend='gloo',
    init_method=f"tcp://{args.master_ip}:{args.master_port}",
    world_size=args.world_size,
    rank=args.local_rank
)

print(f"Hello from rank {args.local_rank} of {args.world_size}!")
