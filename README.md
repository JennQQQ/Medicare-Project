# Medicare-Project

**Team Member**: Emmanuel Ameh, Blessing Adeleye, Aly Boyd, Malsha Jayasinghe, Junqing Qian

## Dataset
Our main dataset is [Medicare Physician & Other Practitioners - by Provider
](https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider) from the [Data.CMS.gov](https://data.cms.gov/) website. We will use data from 2013 to 2023 for this project.

## Backgrounds and Objectives
Medicare is the U.S. federal health insurance program primarily serving individuals aged 65 and older, as well as certain younger individuals with disabilities. Medicare Part B mainly covers outpatient and other medical services, including physician services, outpatient hospital care, many preventive services, durable medical equipment, ambulance services, some home health care, and certain limited outpatient prescription drugs, such as specific infusions. The cost of Medicare Part B has shown an upward trend over time, directly affecting beneficiaries. At the same time, providers are concerned with maintaining adequate equipment for patient care, appropriate staffing levels, and efficient scheduling, while the federal government seeks to control Medicare spending to preserve the program’s long-term sustainability and regulate drug costs.

In this project, we use Medicare provider datasets from 2013 through 2023 to predict future Medicare Part B spending per provider. Our modeling framework uses provider information from the previous year to predict spending in the current year, that is, a one-year lag structure. As a result, our analysis is restricted to providers that appear in two consecutive years of data. We use data from 2013 through 2022 for training and reserve 2023 for validation.

Our analysis does not attempt to account for current or historical policy changes that may influence Medicare costs, nor does it address incentives affecting pharmaceutical companies. In addition, we do not model geographic factors such as population size or urban versus rural status, although we do include state-level geographic features. We also do not incorporate beneficiaries’ diagnostic information or broader demographic characteristics.

## Project Details
### Dataset EDA
* Notebooks about EDA can be found in the folder [notebook/EDA](notebook/EDA), several important EDA plots can be access in the folder [figures](figures).

### Data Transformer and Preprocessing
* Due to the size of our dataset, we are only be able to showcase a snapshot of our raw and processed data. 
    - A snapshot of the raw data can be found here [raw_data](data/raw/data_snapshot_100_rows_2013.csv).
    - A snapshot of the processed data can be found at [modeling_data](data/processed/modeling_data.csv).
* See [transformers.py](src/features/transformers.py) and [preprocessing.py](src/features/preprocessing.py) for data transformation and preprocessing.
* See [pipeline_demo.ipynb](notebooks/pipeline_demo.ipynb) for a demo of data pipeline.
* A special note is that we performed a clustering and labeled our data, a plot of our clustering result can be found [here](figures/key_plots/Cluster_total_risk_vs_payment_with_legend.png).

### Modeling Plan and KPIs
* Our modeling plan is outlined in [modeling_plan.md](modeling_plan.md), and the main evaluation metrics are described in [kpis.md](kpis.md). 

### Baseline Model
* See notebook [Baseline](modeling/LR_lagged.ipynb).

### Model Experiments
* Experiments with GLM see notebook [modeling_experiments_glm.ipynb](modeling/modeling_experiments_glm.ipynb).

### Model Feature Selection
* OLS without intercept: [feature_selection_with_intercept.ipynb](modeling/feature_selection_with_intercept.ipynb) and results are storaged in [feature_selection_with_intercept.csv](results/feature_selection_with_intercept.csv).

* OLS without intercept: [feature_selection_without_intercept.ipynb](modeling/feature_selection_without_intercept.ipynb) and results are storaged in [feature_selection_without_intercept.csv](results/feature_selection_without_intercept.csv).

### Final Model and Final Model Selection
* See notebook [final_model_metric_evaluation.ipynb](notebooks/final_model_metric_evaluation.ipynb) for selecting the final model among the four best semifinal models. The final model's metrics are storaged in [best_model_metric_evaluation.csv](results/best_model_metric_evaluation.csv). The final model's coefficients are [best_model_coefficients.csv](results/best_model_coefficients.csv).
* A plot of our model on the test set can be found [here](figures/key_plots/final_model_test_results.png).
* The coefficients of our final model can be found at [best_model_coefficients.csv](results/interpretability/best_model_coefficients.csv).
* A formula to interpret our final model can be found [here](results/interpretability/interpreting_result.pdf).