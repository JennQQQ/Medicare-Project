# Documentation
## MODEL_1: OLS
 **TARGET**: 'Log_Tot_Mdcr_Pymt_Amt_current' W/O intercept\
 **METHOD**: Walkforward validation\
 **METRIC**: $\text{R}^2\text{(log)} = 1 - \frac{\sum(\text{log(actual)}_i - \text{log(pred)}_i)^2}{\sum(\text{log(actual)}_i - \text{mean}(\text{log(actual)}_i))^2}$ for feature selection\
 **NOTE**:
   1. At a number of feature = 10, the best $R^2(log)$ model is with features ['Log_Tot_Mdcr_Pymt_Amt','current_year','Log_Tot_Mdcr_Alowd_Amt','Tot_HCPCS_Cds','Type_Anesthesia','Bene_Avg_Age','Log_Tot_Benes','Type_MedicalSpecialtyOther','Type_OBGYN',*'Tot_Mdcr_Alowd_Amt'*]; however, it performs badly on the $R^2$ of the actual prediction (un-logged) due to the feature *'Tot_Mdcr_Alowd_Amt'*. Thus we choose the second best $R^2(log)$ features - ['Log_Tot_Mdcr_Pymt_Amt','current_year','Log_Tot_Mdcr_Alowd_Amt','Tot_HCPCS_Cds','Type_Anesthesia','Bene_Avg_Age','Log_Tot_Benes','Type_MedicalSpecialtyOther','Type_OBGYN',*'Type_Cardiology'*]\
   2. The same situation happened when there were 12 features; it was dealt with the same way.\
## MODEL_2: OLS
 **TARGET**: 'Tot_Mdcr_Pymt_Amt_current' W/O intercept\
 **METHOD**: Walkforward validation\
 **METRIC**: $\text{R}^2 = 1 - \frac{\sum(\text{actual}_i - \text{pred}_i)^2}{\sum(\text{actual}_i - \text{mean}(\text{actual}_i))^2}$ for feature selection\
 **NOTE**:
   1. At number of feature = 7, the best $R^2$ model plateaued with features ['Tot_Mdcr_Pymt_Amt',
 'LabPathology_Tot_Risk_0',
 'Type_APP',
 'PharmacyNutrition_Tot_Risk_1',
 'state_Territory',
 'state_Military',
 'state_Unknown']; we proceed with the third best $R^2$ model with features ['Tot_Mdcr_Pymt_Amt',
 'LabPathology_Tot_Risk_0',
 'Type_APP',
 'PharmacyNutrition_Tot_Risk_1',
 'state_Territory',
 'state_Military',
 'state_Unknown',
 'Ind_N'] for further feature selection.\
2. At number of feature = 8, it plateaued. We end the iteration here.
## MODEL_3: OLS
 **TARGET**: 'Log_Tot_Mdcr_Pymt_Amt_current' WITH intercept\
 **METHOD**: Walkforward validation\
 **METRIC**: $\text{R}^2\text{(log)} = 1 - \frac{\sum(\text{log(actual)}_i - \text{log(pred)}_i)^2}{\sum(\text{log(actual)}_i - \text{mean}(\text{log(actual)}_i))^2}$ for feature selection\
 **NOTE**:
   1. At a number of features = 15, the same situation happened; the next best model with 15 features is ranked 8th with features ['Log_Tot_Mdcr_Pymt_Amt',
 'Log_Tot_Mdcr_Alowd_Amt',
 'Tot_HCPCS_Cds',
 'Type_Anesthesia',
 'Bene_Avg_Age',
 'Log_Tot_Benes',
 'Type_MedicalSpecialtyOther',
 'Type_OBGYN',
 'Type_Cardiology',
 'APP_Tot_Risk_2',
 'Type_RehabTherapy',
 'state_Territory',
 'Type_BehavioralHealth',
 'PrimaryCare_Tot_Risk_2',
 'PharmacyNutrition_Tot_Risk_2']. \
## MODEL_4: OLS
 **TARGET**: 'Tot_Mdcr_Pymt_Amt_current' WITH intercept\
 **METHOD**: Walkforward validation\
 **METRIC**: $\text{R}^2 = 1 - \frac{\sum(\text{actual}_i - \text{pred}_i)^2}{\sum(\text{actual}_i - \text{mean}(\text{actual}_i))^2}$ for feature selection\
 **NOTE**:
   1. At a number of features = 10, it plateaued. We end the iteration here.