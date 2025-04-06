# Parkinson's Disease Detection Dataset

## Dataset Description
This dataset contains biomedical voice measurements and TQWT (Tunable Q-factor Wavelet Transform) based features from individuals with and without Parkinson's disease (PD). The data is used to predict the presence of Parkinson's disease based on various speech signal processing and wavelet-transformed features.

**Source**: [GeeksforGeeks Parkinson's Dataset](https://media.geeksforgeeks.org/wp-content/uploads/20250122143413596644/parkinson_disease.csv)  
**File Name**: `parkinson_disease.csv`  
**Format**: CSV (Comma-Separated Values)

## About Parkinson's Disease
Parkinson's disease is a progressive nervous system disorder that affects movement. Symptoms start gradually, sometimes with a barely noticeable tremor in just one hand. This dataset focuses on vocal impairments which are common in PD patients.

## Key Features (After Feature Selection)
The dataset contains multiple features, with the following being particularly important for prediction:

### TQWT (Tunable Q-factor Wavelet Transform) Features:
1. **tqwt_kurtosisValue_dec_28** - Kurtosis value of the 28th decomposition level
2. **tqwt_kurtosisValue_dec_26** - Kurtosis value of the 26th decomposition level  
3. **tqwt_kurtosisValue_dec_25** - Kurtosis value of the 25th decomposition level
4. **tqwt_entropy_shannon_dec_15** - Shannon entropy of the 15th decomposition level
5. **tqwt_entropy_shannon_dec_11** - Shannon entropy of the 11th decomposition level
6. **tqwt_energy_dec_27** - Energy of the 27th decomposition level
7. **tqwt_energy_dec_14** - Energy of the 14th decomposition level
8. **tqwt_energy_dec_12** - Energy of the 12th decomposition level
9. **tqwt_energy_dec_11** - Energy of the 11th decomposition level

### Demographic Feature:
- **gender** - Gender of the subject (may be encoded as 0/1)

### Original Key Features (from MDVP analysis):
1. **MDVP:Fo(Hz)** - Average vocal fundamental frequency
2. **MDVP:Fhi(Hz)** - Maximum vocal fundamental frequency
3. **MDVP:Flo(Hz)** - Minimum vocal fundamental frequency
4. **MDVP:Jitter(%)**, **MDVP:Jitter(Abs)**, etc.
5. **MDVP:Shimmer**, **Shimmer(dB)**, etc.
6. **HNR** - Harmonics-to-noise ratio
7. **RPDE** - Recurrence period density entropy
8. **DFA** - Detrended fluctuation analysis
9. **spread1**, **spread2**, **PPE**

### Target Variable:
- **class** - Health status of the subject (1 = Parkinson's, 0 = healthy)

## Intended Use
This dataset is suitable for:
- Binary classification tasks
- Medical diagnosis prediction
- Feature importance analysis

## Potential Applications
1. Building machine learning models to detect Parkinson's disease from voice recordings
2. Comparing different classification algorithms
3. Feature selection studies
4. Medical research on early PD detection

## Important Notes
- The TQWT features represent advanced signal processing transformations of the original voice measurements
- Kurtosis values indicate the "tailedness" of the probability distribution
- Energy and entropy features capture different aspects of the signal's characteristics
- Gender may be an important demographic factor in PD detection.
