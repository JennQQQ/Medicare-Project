import pandas as pd
import numpy as np
from sklearn.cluster import Birch
from sklearn.preprocessing import MinMaxScaler

# combine all 10 years and add year labels
def combine_keep_cols_add_year_label_df(path,file):
    dfs = []
    keep_cols = ['Rndrng_NPI',
                'Rndrng_Prvdr_Ent_Cd',
                'Rndrng_Prvdr_State_Abrvtn',
                'Rndrng_Prvdr_Type',
                'Rndrng_Prvdr_Mdcr_Prtcptg_Ind',
                'Tot_HCPCS_Cds',
                'Tot_Benes',
                'Tot_Srvcs',
                'Tot_Sbmtd_Chrg',
                'Tot_Mdcr_Alowd_Amt',
                'Tot_Mdcr_Pymt_Amt',
                'Bene_Avg_Age',
                'Bene_Avg_Risk_Scre']
    for year in range(2013,2024): # only have 10 years of data
        temp = pd.read_csv(f'{path}/{file}_{year}.csv',usecols=keep_cols)
        temp['year'] = year
        dfs.append(temp)
    
    df = pd.concat(dfs,ignore_index = True)
    return df

# cleaning up 'Rndrng_Prvdr_Type' columns
def clean_up_type(df):
    # delete all the spaces in 'Rndrng_Prvdr_Type'
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].astype(str).str.replace(" ", "", regex=False)

    # change AmbulanceServiceSupplier to AmbulanceServiceProvider
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'AmbulanceServiceProvider' if x=='AmbulanceServiceSupplier' else x)

    # change Hematology/Oncology to Hematology-Oncology
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'Hematology-Oncology' if x=='Hematology/Oncology' else x)

    # change AnesthesiologistAssistants to AnesthesiologyAssistant
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'AnesthesiologyAssistant' if x=='AnesthesiologistAssistants' else x)

    # change CardiovascularDisease(Cardiology) to Cardiology
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'Cardiology' if x=='CardiovascularDisease(Cardiology)' else x)

    # change CRNA to CertifiedRegisteredNurseAnesthetist(CRNA)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'CertifiedRegisteredNurseAnesthetist(CRNA)' if x=='CRNA' else x)

    # change CardiacElectrophysiology to ClinicalCardiacElectrophysiology
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'ClinicalCardiacElectrophysiology' if x=='CardiacElectrophysiology' else x)

    # change ColorectalSurgery(formerlyproctology) to ColorectalSurgery(Proctology)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'ColorectalSurgery(Proctology)' if x=='ColorectalSurgery(formerlyproctology)' else x)

    # change Audiologist(billingindependently) to Audiologist
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'Audiologist' if x=='Audiologist(billingindependently)' else x)

    # change Gynecological/Oncology to GynecologicalOncology
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'GynecologicalOncology' if x=='Gynecological/Oncology' else x)

    # change IndependentDiagnosticTestingFacility to IndependentDiagnosticTestingFacility(IDTF)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'IndependentDiagnosticTestingFacility(IDTF)' if x=='IndependentDiagnosticTestingFacility' else x)

    # more changes
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'RegisteredDietitianorNutritionProfessional' if x=='RegisteredDietician/NutritionProfessional' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'RadiationTherapyCenter' if x=='RadiationTherapy' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'PublicHealthorWelfareAgency' if x=='PublicHealthWelfareAgency' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'Psychologist,Clinical' if x=='Psychologist(billingindependently)' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'MammographyCenter' if x=='MammographicScreeningCenter' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'MassImmunizerRosterBiller' if x=='MassImmunizationRosterBiller' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'Obstetrics&Gynecology' if x=='Obstetrics/Gynecology' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'OccupationalTherapistinPrivatePractice' if x=='Occupationaltherapist' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'OralSurgery(Dentistonly)' if x=='OralSurgery(Dentistsonly)' or x=='OralSurgery(dentistsonly)' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'PhysicalTherapistinPrivatePractice' if x=='PhysicalTherapist' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'PortableX-RaySupplier' if x=='PortableX-ray' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'UnknownSupplier/ProviderSpecialty' if x=='UnknownSupplier/Provider' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'ClinicorGroupPractice' if x=='MultispecialtyClinic/GroupPractice' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'Psychologist,Clinical' if x=='ClinicalPsychologist' else x)
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].apply(lambda x: 'UndefinedPhysiciantype' if x=='UnknownPhysicianSpecialtyCode' else x)

    return df

# map specialized types into umbrella types based on domain knowledge
def umbrella_types(df):
    mapping = {
            # ---------- Primary care ----------
            "FamilyPractice": "PrimaryCare",
            "InternalMedicine": "PrimaryCare",
            "GeneralPractice": "PrimaryCare",
            "PediatricMedicine": "PrimaryCare",
            "GeriatricMedicine": "PrimaryCare",

            # ---------- Cardiology / cardiovascular (non-surgical) ----------
            "Cardiology": "Cardiology",
            "InterventionalCardiology": "Cardiology",
            "ClinicalCardiacElectrophysiology": "Cardiology",
            "AdvancedHeartFailureandTransplantCardiology": "Cardiology",
            "AdultCongenitalHeartDisease": "Cardiology",
            "PeripheralVascularDisease": "Cardiology",
            "IntensiveCardiacRehabilitation": "Cardiology",

            # ---------- Cardiothoracic / vascular surgery ----------
            "CardiacSurgery": "CardioVascularSurgery",
            "ThoracicSurgery": "CardioVascularSurgery",
            "VascularSurgery": "CardioVascularSurgery",

            # ---------- Oncology / hematology ----------
            "Hematology": "OncologyHeme",
            "Hematology-Oncology": "OncologyHeme",
            "MedicalOncology": "OncologyHeme",
            "GynecologicalOncology": "OncologyHeme",
            "SurgicalOncology": "OncologyHeme",
            "RadiationOncology": "OncologyHeme",
            "HematopoieticCellTransplantationandCellularTherapy": "OncologyHeme",

            # ---------- Surgery (other) ----------
            "GeneralSurgery": "SurgeryOther",
            "ColorectalSurgery(Proctology)": "SurgeryOther",
            "HandSurgery": "SurgeryOther",
            "Neurosurgery": "SurgeryOther",
            "OrthopedicSurgery": "SurgeryOther",
            "PlasticandReconstructiveSurgery": "SurgeryOther",
            "Urology": "SurgeryOther",
            "Otolaryngology": "SurgeryOther",
            "MaxillofacialSurgery": "SurgeryOther",
            "OralSurgery(Dentistonly)": "SurgeryOther",
            "Podiatry": "SurgeryOther",
            "MicrographicDermatologicSurgery": "SurgeryOther",

            # ---------- OB/GYN ----------
            "Obstetrics&Gynecology": "OBGYN",
            "CertifiedNurseMidwife": "OBGYN",

            # ---------- Anesthesia ----------
            "Anesthesiology": "Anesthesia",
            "CertifiedRegisteredNurseAnesthetist(CRNA)": "Anesthesia",
            "AnesthesiologyAssistant": "Anesthesia",
            "DentalAnesthesiology": "Anesthesia",

            # ---------- Acute care / hospital ----------
            "EmergencyMedicine": "AcuteCare",
            "CriticalCare(Intensivists)": "AcuteCare",
            "Hospitalist": "AcuteCare",

            # ---------- Behavioral health / addiction ----------
            "Psychiatry": "BehavioralHealth",
            "GeriatricPsychiatry": "BehavioralHealth",
            "Neuropsychiatry": "BehavioralHealth",
            "Psychologist,Clinical": "BehavioralHealth",
            "LicensedClinicalSocialWorker": "BehavioralHealth",
            "AddictionMedicine": "BehavioralHealth",
            "OpioidTreatmentProgram": "BehavioralHealth",

            # ---------- Radiology / imaging ----------
            "DiagnosticRadiology": "RadiologyImaging",
            "InterventionalRadiology": "RadiologyImaging",
            "NuclearMedicine": "RadiologyImaging",
            "MammographyCenter": "RadiologyImaging",
            "PortableX-RaySupplier": "RadiologyImaging",

            # ---------- Lab / pathology ----------
            "ClinicalLaboratory": "LabPathology",
            "Pathology": "LabPathology",
            "SlidePreparationFacility": "LabPathology",

            # ---------- Rehab / therapy / conservative MSK ----------
            "PhysicalMedicineandRehabilitation": "RehabTherapy",
            "PhysicalTherapistinPrivatePractice": "RehabTherapy",
            "OccupationalTherapistinPrivatePractice": "RehabTherapy",
            "SpeechLanguagePathologist": "RehabTherapy",
            "Chiropractic": "RehabTherapy",
            "OsteopathicManipulativeMedicine": "RehabTherapy",
            "SportsMedicine": "RehabTherapy",

            # ---------- Vision / hearing ----------
            "Ophthalmology": "VisionHearing",
            "Optometry": "VisionHearing",
            "Audiologist": "VisionHearing",

            # ---------- Other medical specialties ----------
            "Allergy/Immunology": "MedicalSpecialtyOther",
            "Endocrinology": "MedicalSpecialtyOther",
            "Gastroenterology": "MedicalSpecialtyOther",
            "InfectiousDisease": "MedicalSpecialtyOther",
            "Nephrology": "MedicalSpecialtyOther",
            "Neurology": "MedicalSpecialtyOther",
            "PulmonaryDisease": "MedicalSpecialtyOther",
            "Rheumatology": "MedicalSpecialtyOther",
            "SleepMedicine": "MedicalSpecialtyOther",
            "PreventiveMedicine": "MedicalSpecialtyOther",
            "MedicalGeneticsandGenomics": "MedicalSpecialtyOther",
            "MedicalToxicology": "MedicalSpecialtyOther",
            "UnderseaandHyperbaricMedicine": "MedicalSpecialtyOther",
            "PainManagement": "MedicalSpecialtyOther",
            "InterventionalPainManagement": "MedicalSpecialtyOther",
            "Dermatology": "MedicalSpecialtyOther",
            "Dentist": "MedicalSpecialtyOther",
            "Dentistonly": "MedicalSpecialtyOther",  # (in case of weird variants)
            "DentalAnesthesiology": "Anesthesia",     # already above, kept here for clarity

            # ---------- Advanced practice providers ----------
            "NursePractitioner": "APP",
            "PhysicianAssistant": "APP",
            "CertifiedClinicalNurseSpecialist": "APP",
            "CertifiedNurseMidwife": "OBGYN",  # already above

            # ---------- Pharmacy / nutrition ----------
            "Pharmacy": "PharmacyNutrition",
            "RegisteredDietitianorNutritionProfessional": "PharmacyNutrition",

            # ---------- Facilities / suppliers / programs ----------
            "ClinicorGroupPractice": "FacilitySupplierProgram",
            "AmbulatorySurgicalCenter": "FacilitySupplierProgram",
            "AmbulanceServiceProvider": "FacilitySupplierProgram",
            "IndependentDiagnosticTestingFacility(IDTF)": "FacilitySupplierProgram",
            "HomeInfusionTherapyServices": "FacilitySupplierProgram",
            "HospiceandPalliativeCare": "FacilitySupplierProgram",
            "PublicHealthorWelfareAgency": "FacilitySupplierProgram",
            "MassImmunizerRosterBiller": "FacilitySupplierProgram",
            "CentralizedFlu": "FacilitySupplierProgram",
            "MedicareDiabetesPreventiveProgram": "FacilitySupplierProgram",
            "AllOtherSuppliers": "FacilitySupplierProgram",

            # ---------- Unknown / undefined ----------
            "UndefinedPhysiciantype": "UnknownOther",
            "UnknownSupplier/ProviderSpecialty": "UnknownOther",
        }

    # apply mapping
    df['Rndrng_Prvdr_Type'] = df['Rndrng_Prvdr_Type'].map(mapping).fillna('MedicalSpecialtyOther')
    
    return df

# map geographic information into umbrella types based on domain/geographic knowledge
def umbrella_states(df):
    NE = {"CT","ME","MA","NH","RI","VT","NJ","NY","PA"}
    MW = {"IL","IN","MI","OH","WI","IA","KS","MN","MO","NE","ND","SD"}
    S  = {"DE","DC","FL","GA","MD","NC","SC","VA","WV","AL","KY","MS","TN","AR","LA","OK","TX"}
    W  = {"AZ","CO","ID","MT","NV","NM","UT","WY","AK","CA","HI","OR","WA"}

    TERR = {"PR","VI","GU","AS","MP","PW","FM"}     # territories / compacts in your data
    MIL  = {"AA","AE","AP"}                         # military “states”
    UNK  = {"ZZ","XX"}                              # unknown / invalid catchalls (custom)

    # define mapping
    def group_geo(code: str) -> str:
        if pd.isna(code): return "Unknown"
        code = str(code).strip().upper()
        if code in NE:   return "Northeast"
        if code in MW:   return "Midwest"
        if code in S:    return "South"
        if code in W:    return "West"
        if code in TERR: return "Territory"
        if code in MIL:  return "Military"
        if code in UNK:  return "Unknown"
        return "Other/Unknown"
    
    df["state"] = df["Rndrng_Prvdr_State_Abrvtn"].map(group_geo)
    return df

# round a non integer to an integer if the percentage of non integer of a column is less than a threshold 'percentage'
def check_non_integer_columns(percentage,df): # we take percentage = 0.005
    cols = df.select_dtypes('number')

    for c in cols:
        mask_temp = (df[c]%1!=0)
        if df[mask_temp].shape[0]/df.shape[0]<percentage:
            df[mask_temp]=round(df[mask_temp])
    return df

############################################
# add subsetting columns once we decide on exact columns we want to use
############################################

# get total_risk
# may delete if not needed
def total_risk(df):
    df['Tot_Risk'] = df['Bene_Avg_Risk_Scre']*df['Tot_Benes']
    return df

# labeling data due to their Tot_Risk vs Tot_Mdcr_Pymt_Amt scattor plot
# apply birch clustering, KMean does not work as good as hierarchical clustering, hierarchical can't handle large dataset, birch as an alternative
# may delete if not needed
# type = ['APP','PrimaryCare','MedicalSpecialtyOther','LabPathology','PharmacyNutrition']
# run label_data(df,types,'Tot_Risk','Tot_Mdcr_Pymt_Amt')
def label_data(df,types,col1,col2): 
    for type in types:
        type_mask = df['Rndrng_Prvdr_Type']==type
        X = df[type_mask][[col1]+[col2]].copy()
        scaler = MinMaxScaler()
        X[f'scaled_{col1}'] = scaler.fit_transform(X[[col1]])
        X[f'scaled_{col2}'] = scaler.fit_transform(X[[col2]])
        m = (round((df['Tot_Mdcr_Pymt_Amt']/df['Tot_Risk']).quantile(0.99999)/10000)+1)*10000 # get large slope
        X['Slope'] = (X[f'scaled_{col2}']/X[f'scaled_{col1}']).apply(lambda x:x if x<=m else m) # replace potential inf slopes

        if type=='LabPathology':
            birch = Birch(threshold=0.17, branching_factor=50, n_clusters=3) # threshold = 0.17 works the best for three clusters after trying different threshold
            labels = birch.fit_predict(np.arctan(X[['Slope']]))
            df.loc[X.index,f'{type}_Tot_Risk'] = labels
            df[f'{type}_Tot_Risk'] = df[f'{type}_Tot_Risk'].fillna(3) # fill the rest as the fourth cat
        else:
            birch = Birch(threshold=0.1, branching_factor=50, n_clusters=2) # threshold = 0.17 works pretty good
            labels = birch.fit_predict(np.arctan(X[['Slope']]))
            df.loc[X.index,f'{type}_Tot_Risk'] = labels
            df[f'{type}_Tot_Risk'] = df[f'{type}_Tot_Risk'].fillna(2) # fill the rest as the third cat
    
    return df

# create log columns of 'Tot_' columns
def log_columns(df):
    tot_cols = [c for c in df.columns if 'Tot_' in c but '_Tot_' not in c]
    for c in tot_cols:
        # get the smallest positive value for the column
        if min(df[c])<=0:
            m = sorted(df[c].apply(lambda x:x if x>0 else 0).unique())[1]
        
        # replace zero or native values by the smallest positive value
        df[c] = df[c].apply(lambda x:x if x>0 else m)

        # taking log and create a new column 'Log_c'
        df[f'Log_{c}'] = np.log(df[c])
    
    return df

# create 1 year lag feautre
def push_one_year(df,curr_cols = ['Log_Tot_Mdcr_Pymt_Amt','Tot_Mdcr_Pymt_Amt','year']):
    # define columns to keep from previous year
    pre_cols = [c for c in df.columns if c not in curr_cols]

    # merge year by year
    for i in range(2014,2024):
        mask_pre = df['year']==i-1
        pre_df = df[mask_pre]
        mask_curr = df['year']==i
        curr_df = df[mask_curr]

        # keep pre_cols from prvious year and curr_cols from current year, add suffixes "_current" for those columns
        # we can also do suffixes '_lag' for pre_cols
        # due to consistency with our other codes and the fact we only have one year lag, we use suffixes "_current" for current_cols
        if i == 2014:
            lag_df = pre_df[pre_cols].merge(curr_df[['Rndrng_NPI'] + curr_cols],on='Rndrng_NPI',how='inner',suffixes=('','_current'))
        else:
            lag_df = pd.concat([lag_df,pre_df[pre_cols].merge(curr_df[['Rndrng_NPI'] + curr_cols],on='Rndrng_NPI',how='inner',suffixes=('','_current'))],axis=0,ignore_index=True)
    
    # change 'year' to 'current_year
    lag_df = lag_df.rename(columns={'year':'current_year'})

    return lag_df