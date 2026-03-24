# Modeling Plan
## Model Families Tried
Ordinary Least Square Regression, RandomForest, Generalized Linear Models
## Initial Attempt 
We first examined the histogram of the log-transformed target variable, which appeared to be approximately bell-shaped with slight right skewness. Based on this, we began our analysis by fitting both an ordinary least squares linear regression model and a generalized linear model with a Gamma distribution, log link, and offset = Tot_Benes as initial benchmarks. We also experimented with a Random Forest model; however, because Random Forests are not well suited to very large datasets such as ours (10M+ observations), we trained this model only on a random subset of the data to provide a baseline comparison. In addition, given the importance of interpretability in this setting, we did not pursue the Random Forest model further.
## Notes on GLM 
We ultimately did not proceed with the GLM, as the distribution of the response variable appeared to be nearly symmetric.
## Modeling and Feature Selectio 
We fit OLS models using both the raw payment variable and its log-transformed version, with and without an intercept. The reason we also considered a model without an intercep is based on the assumption that the payment should be zero when all predictor variables are equal to zero.

For the categorical predictors, we created dummy variables for each category and included them in the feature selection process, resulting in 53 candidate features in total. Because of the relatively large number of candidate variables, we used forward feature selection and stopped once the chosen performance metric, $R^2$, began to plateau.

For additional details, see [results/README.md](results/README.md).
## Model Selection
We ultimately identified four models with the strongest $R^2$ performance within their respective categories. We then compared these models using the average mean absolute log ratio (MALR), evaluated through walk-forward validation over the years 2018 through 2022. The best-performing model was an OLS regression on the log-transformed payment variable using 15 features. Details can be found in [final_model_metric_evaluation.ipynb](notebooks/final_model_metric_evaluation.ipynb).