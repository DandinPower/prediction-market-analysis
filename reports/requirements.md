# Project Guidelines: Dataset Construction and Analysis

In this project, the objective is for you to go through the process of constructing and analyzing a dataset. Most of the time (including in our own classes), algorithms are talked about more than the data. However, to build good models in machine learning, you need good data to learn from. As a result, this is one aspect that usually consumes a large portion of efforts and resources when building models.

---

## Dataset Requirements and Suggestions

* You **cannot use a dataset that is already available**. You need to create one yourself.
* However, you can look at public datasets and their documentations to get an idea of how to construct datasets.
* Choose a topic such that:

  1. You can obtain reasonable labels and/or target outputs.
  2. It does not require a huge amount of data to produce reasonable results.
* The grade will include part on the **"creativity" or "novelty"** of your dataset.

  * Very trivial datasets (e.g., digit recognition or dogs-vs-cats) will receive fewer points.
  * Possible directions include:

    * Text
    * Sound
    * Smartphone sensor data
    * Open data sources (population, weather, stock markets, etc.)
* You can try automatic or semi-automatic data collection methods:

  * Web crawlers
  * Simulations
    These usually require data cleaning, which should be addressed in your report.
* You can construct your dataset for:

  * Classification
  * Regression
* Carefully consider:

  * Characteristics
  * Constraints
  * Composition of samples

---

## Algorithms / Models

* Experiment with **at least two supervised learning methods**.
* At most **one method can be deep-learning based**.
* You may use:

  * Publicly available code
  * AI-generated code
  * Pretrained weights

---

## Analysis

* Evaluate performance using appropriate metrics:

  * **Classification:**

    * Accuracy
    * Confusion matrix
    * Precision / Recall / F1 / AUROC (for binary tasks)
  * **Regression:**

    * MSE or similar metrics
* Use **cross-validation** to obtain evaluation metrics.

---

## Experiments

You must design experiments exploring different dataset-related aspects. The following are examples:

* Effect of **training data size**:

  * How do results change with more or less data?
  * Are methods or hyperparameters affected differently?
* Effect of **data composition / balance**:

  * Does class imbalance affect results?
  * Do techniques like weighting or resampling (e.g., SMOTE) help?
* Apply **data augmentation** (if applicable):

  * Compare results with and without augmentation
* Use **dimensionality reduction** (for high-dimensional data):

  * PCA
  * Autoencoder
  * Compare performance with and without reduction

---

## Discussion

* Are the results consistent with expectations?
* What factors influence the results?

  * Especially dataset characteristics
* What additional experiments would you conduct with more time?
* What did you learn?
* What questions remain?

---

## Submission Requirements

### Report (PDF)

* Maximum **10 pages**, single-spaced
* Must include:

  * Web link to your dataset
  * Research question and motivation (plain text)
  * Dataset documentation:

    * Data type
    * External sources (if any)
    * Size and composition
    * Collection conditions
    * Collection process (hardware/software used)
    * Examples
  * Methods description:

    * Include references for:

      * Libraries
      * Open-source code
      * Pretrained models
    * Include other techniques:

      * Feature extraction
      * Resampling
      * Dimensionality reduction
  * Experiment descriptions:

    * Results
    * Examples
  * Discussion section
  * References
  * Appendix:

    * Program code (not counted in page limit)
    * Written in C/C++ or Python
    * Must be well-organized and commented

---

## Report Notes

* Submit via **E3**
* Late submissions:

  * Accepted up to 5 days
  * Penalty: **10% per day**
* Include **student ID**:

  * In filename
  * On first page
* Writing expectations:

  * Methods section must be understandable **without reading code**
  * Do **not** write like program documentation
* Results presentation:

  * Always explain what readers should learn from results
  * Use:

    * Tables (not screenshots)
    * Charts/plots when appropriate
* Formatting:

  * Minimum font size:

    * 12 for main text
    * 10 for tables/figures
  * Avoid cramming content into 10 pages with small fonts or plots

---

## Dataset Submission

* Upload dataset to **GitHub**
* Include dataset documentation
* Include GitHub link at the **beginning of your report**