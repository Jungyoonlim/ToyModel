# Notes

# Experiment Setup
- Whether a neural net can project a higher dim. vector into a lower dim. vector and then recover it. 

# Basic Terms / Concepts
## Privileged Basis
Standard basis vectors are meaningful; they represent some human-understandable concepts.

The residual stream is not privileged because anything that reads from it and writes to it uses a linear map. 


## Differences between neuron superposition and neuron polysemanticity 

Polysemanticity -> When one neuron corresponds to multiple features. 

Superposition -> when there are more features than neurons. So it implies polysemanticity but the converse is not true. 

## Importance and Sparsity of Features - Do you expect more or less polysemantic neurons if sparsity is larger?

Importance = how useful is this feature for achieving lower loss?

Sparsity = how frequently is it in the input data?

If sparsity is larger, expect more polysemantic neurons. A single neuron can afford to rep. several different sparse features 

## Feature

Many defs. 
- a property of an input to the model 
- a scalar function of the input. 
- directions

Meaningful feature: genuinely responds to an articulable property of the input. 