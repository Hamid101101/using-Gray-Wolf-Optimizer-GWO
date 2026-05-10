# Gray Wolf Optimizer (GWO)

Academic project applying the Gray Wolf Optimizer metaheuristic to three different problems.

## Contents

- **`GWO_hyperparameters/`** — Uses GWO to tune neural network hyperparameters (number of hidden layers, neurons per layer, learning rate) on MNIST.
  - `gwo_optimazer.py` — GWO driver and fitness evaluation.
  - `neural_network.py` — Custom feed-forward network used for fitness evaluation.
- **`GWO_parameters/`** — Uses GWO to optimize the weights and biases of a deep neural network directly.
  - `GwoDnn.py` — DNN definition and GWO-based parameter search.
- **`GWO_tsp/`** — Applies GWO to the Traveling Salesman Problem.
  - `gwoTotsp.py` — TSP encoding and GWO search loop (example over Moroccan cities).
- **`rapport_&_presentation/`** — Project report (PDF) and presentation slides (PPTX).

## Requirements

- Python 3.x
- `numpy`
- `keras` / `tensorflow` (for the MNIST experiments in `GWO_hyperparameters/`)

## Usage

Run any of the scripts directly, e.g.:

```bash
python GWO_hyperparameters/gwo_optimazer.py
python GWO_parameters/GwoDnn.py
python GWO_tsp/gwoTotsp.py
```
