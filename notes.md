# Notes

# Experiment Setup
- Whether a neural net can project a higher dim. vector into a lower dim. vector and then recover it. 

# Terms / Concepts
## Privileged Basis
Standard basis vectors are meaningful; they represent some human-understandable concepts.

The residual stream is not privileged because anything that reads from it and writes to it uses a linear map. 


## Differences between neuron superposition and neuron polysemanticity 

Polysemanticity -> When one neuron corresponds to multiple features. 

Superposition -> when there are more features than neurons. So it implies polysemanticity but the converse is not true. 

## Importance and Sparsity of Features - Do you expect more or less polysemantic neurons if sparsity is larger?

Importance = how useful is this feature for achieving lower loss?
The coefficient on the weighted mean squared error between the input and the output. 

Sparsity = how frequently is it in the input data?
The probability of the corresponding element in x being zero. 

If sparsity is larger, expect more polysemantic neurons. A single neuron can afford to rep. several different sparse features 

## Feature

Many defs. 
- a property of an input to the model 
- a scalar function of the input. 

Meaningful feature: genuinely responds to an articulable property of the input. 

# Superposition 

When a model represents more than n features in an n-dimensional activation space. aka features still correspond to directions, but the set of interpretable directions is larger than the number of features.

# The Superposition Hypothesis

# Demonstrating Superposition

Whether neural networks 
