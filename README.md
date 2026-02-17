# Medicare-Project

**Team Member**: Emmanuel Ameh, Blessing Adeleye, Aly Boyd, Malsha Jayasinghe, Junqing Qian

## Dataset
Our main dataset is [Medicare Physician & Other Practitioners - by Provider
](https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider) from the [Data.CMS.gov](https://data.cms.gov/) website. We will use data from year 2013 to year 2023 for this project.

## Backgrounds and Objectives
Medicare is the U.S. federal health insurance program mainly for people 65 and above (and some younger people with disabilities). Medicare Part B primarily covers outpatient and “medical” services, like doctor/physician services, outpatient hospital care, many preventive services, durable medical equipment, ambulance, some home health, and limited outpatient drugs (e.g., certain infusions). The premium for Medicare Part B has in a rising trend, which has direct impact for beneficiaries. Providers care about adequate equipment for patient care, appropriate staffing conditions and schedulings. The federal government cares about limiting the budget of medicare to sustain it for future years and regulating drug costs.

We want to use the medicare provider datasets from 2013 to 2023 to predict medicare part B total spending in furture years, i.e. year 2024, 2025, and 2026. We will have an enrollment trend from the past 10 years that we will use for 2024, 2025, and 2026 enrollment. We plan to use available total part B spendings for year 2024 and year 2025 as our validation measure. 

We will not address current or past policy changes that may affect the cost of medicare as well as pharmaceutical company incentives. We are also not addressing medicare spending impacted by geographic features by population size such as being rural or urban. We do include geographic features at the state level. We are also not considering beneficiaries's diagnostic details and demographic background in general.