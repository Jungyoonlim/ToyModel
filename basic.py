import torch as t 
import matplotlib as plt

# initialize the model
t.manual_seed(2)
W = t.randn(2,5)
W_normed = W/W.norm(dim=0, keepdim=True)

# Cosine Similarities 
cos_sim = W_normed.T @ W_normed

# Plot Cosine Similarities
plt.figure(figsize=(10,8))



