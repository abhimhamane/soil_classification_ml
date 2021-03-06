{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from typing import Tuple\n",
    "import numpy as np\n",
    "from scipy.special import logsumexp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def assert_same_shape(output: np.ndarray,\n",
    "                      output_grad: np.ndarray):\n",
    "    assert output.shape == output_grad.shape, \\\n",
    "        '''\n",
    "        Two tensors should have the same shape;\n",
    "        instead, first Tensor's shape is {0}\n",
    "        and second Tensor's shape is {1}.\n",
    "        '''.format(tuple(output_grad.shape), tuple(output.shape))\n",
    "    return None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "Batch = Tuple[np.ndarray, np.ndarray]\n",
    "\n",
    "\n",
    "def generate_batch(X: np.ndarray,\n",
    "                   y: np.ndarray,\n",
    "                   start: int = 0,\n",
    "                   batch_size: int = 10) -> Batch:\n",
    "\n",
    "    assert (X.dim() == 2) and (y.dim() == 2), \\\n",
    "        \"X and Y must be 2 dimensional\"\n",
    "\n",
    "    if start+batch_size > X.shape[0]:\n",
    "        batch_size = X.shape[0] - start\n",
    "\n",
    "    X_batch, y_batch = X[start:start+batch_size], y[start:start+batch_size]\n",
    "\n",
    "    return X_batch, y_batch"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def to_2d(a: np.ndarray,\n",
    "          type: str=\"col\") -> np.ndarray:\n",
    "    '''\n",
    "    Turns a 1D Tensor into 2D\n",
    "    '''\n",
    "\n",
    "    assert a.ndim == 1, \\\n",
    "        \"Input tensors must be 1 dimensional\"\n",
    "\n",
    "    if type == \"col\":\n",
    "        return a.reshape(-1, 1)\n",
    "    elif type == \"row\":\n",
    "        return a.reshape(1, -1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def permute_data(X: np.ndarray, y: np.ndarray):\n",
    "    perm = np.random.permutation(X.shape[0])\n",
    "    return X[perm], y[perm]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def assert_dim(t: np.ndarray,\n",
    "               dim: int):\n",
    "    assert t.ndim == dim, \\\n",
    "        '''\n",
    "        Tensor expected to have dimension {0}, instead has dimension {1}\n",
    "        '''.format(dim, len(t.shape))\n",
    "    return None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def softmax(x, axis=None):\n",
    "    return np.exp(x - logsumexp(x, axis=axis, keepdims=True))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
