import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# change clustered label columns into 'object' datatype
# label_cols = ['APP_Tot_Risk','PrimaryCare_Tot_Risk','MedicalSpecialtyOther_Tot_Risk','LabPathology_Tot_Risk','PharmacyNutrition_Tot_Risk']
# run label_num_to_cat(df,label_cols)
def label_num_to_cat(df,cols):
    for c in cols:
        df[c] = df[c].astype(int).astype('object')
    return df

# OneHotEncoding, get categorical columns dummy variables
def enc_df(df):
    num_cols = df.select_dtypes(include='number').columns.tolist()
    cat_cols = df.select_dtypes(exclude='number').columns.tolist()
    cat_cols = [c for c in cat_cols if c!='Rndrng_Prvdr_State_Abrvtn'] # we grouped 'Rndrng_Prvdr_State_Abrvtn' into the new column 'state'

    cat_orders = []

    for c in cat_cols:
        cat_orders.append(df[c].unique().tolist())

    enc = OneHotEncoder(
        categories=cat_orders,
        handle_unknown='ignore',
        sparse_output=False,
        feature_name_combiner=lambda feature,category: f'{feature.split('_')[-1]}_{category}' if 'Rndrng' in feature else f'{feature}_{category}'
    )

    X_cat = enc.fit_transform(df[cat_cols])

    dummy_names = enc.get_feature_names_out(cat_cols)

    X_cat_df = pd.DataFrame(X_cat,columns=dummy_names,index=df.index)
    X = pd.concat([df[num_cols],X_cat_df],axis=1)
    return X