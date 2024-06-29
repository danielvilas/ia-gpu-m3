#check for gpu
import torch

if torch.backends.mps.is_available():
   mps_device = torch.device("mps")
   x = torch.ones#check for gpu
if torch.backends.mps.is_available():
   mps_device = torch.device("mps")
   x = torch.ones(1, device=mps_device)
   print (x)
else:
   print ("MPS device not found.")