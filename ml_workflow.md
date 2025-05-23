# The 7 steps of machine learning
## 1. Gathering data
## 2. Preparing that data
## 3. Choosing a model
Visualization methods like pair plotting helps determine the right model, which saves a lot of compute and effort in hyperparameter tuning.
## 4. Training
## 5. Evaluation
## 6. Hyperparameter Tuning
Domain specific expertise involved and is more artisanal in nature.
## 7. Prediction

# Data preprocessing
## Data cleaning
* Removing duplicates
* Handling missing values 
* Correcting inconsistent formats
## Data integration
* Schema matching
* Data deduplication
## Data transformation
* Scaling
* Encoding
* Feature engineering
## Data reduction
* Sampling
* Feature selection
* Dimensionality reduction

# Python library guide

## Data handling & manipulation
| LIBRARY   | PURPOSE                                                                       |
| ---       | ---                                                                           |
| NumPy     | Efficient numerical computations (arrays, linear algebra)                     |
|           | Base for libraries like *Pandas*, *Scikit-learn* and *SciPy*.                 |
|           | Key features: Array-oriented computing, broadcasting, mathematical functions. |
| Pandas    | Data manipulation and analysis with **DataFrames** and **Series**.            |
|           | Key features: Data cleaning and preparation, data exploration, data analysis, feature engineering |

## Data visualization
| LIBRARY | PURPOSE |
| --- | --- |
| Matplotlib | Basic plotting |
| Seaborn | Statistical plotting |

## Machine learning frameworks
| LIBRARY | PURPOSE |
| --- | --- |
| Scikit-learn | Classical ML models (SVM, Random Forest, etc..), preprocessing, evaluation |
| XGBoost | Gradient boosting, excellent for tabular data | 
| LightGBM | Fast, efficient gradient boosting  |
| CatBoost | Gradient boosting with categorical support |

## Deep learning
| LIBRARY | PURPOSE |
| --- | --- |
| TensorFlow | Scalable deep learning framework by Google |
| Keras | High-level API for TensorFlow |
| PyTorch | Flexible deep learning by Meta |
| Hugging Face transformers | Pretrained NLP models (BERT, GPT, etc..) |

## Model evaluation & experiment tracking
| LIBRARY | PURPOSE |
| --- | --- |
| scikit-learn.metrics | Accuracy, F1, ROC, etc.. |
| MLflow | Experiment tracking |
| Weights & biases | Visualization, experiment management |

## Utilites & environment
| LIBRARY | PURPOSE |
| --- | --- |
| Joblib | Model serialization, parallelism |
| Optuna | Hyperparameter optimization |
| DVC | Data version control for ML projects |

## Advanced
| LIBRARY | PURPOSE |
| --- | --- |
| OpenCV | Image processing |
| NLTK / spaCy | NLP |
| NetworkX / DGL/ PyG | Graph-based learning |
| FastAI | Simplififed PyTorch API for rapid prototyping |
