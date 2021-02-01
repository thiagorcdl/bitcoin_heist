![preview](https://github.com/thiagorcdl/bitcoin_heist/blob/master/assets/social_media_preview.png)

# Bitcoin Heist
[![Released under the MIT license.](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/thiagorcdl/social_media_buzz/blob/master/LICENSE) [![This Repository uses a generated Social Preview from @pqt/social-preview](https://img.shields.io/badge/%E2%9C%93-Social%20Preview-blue)](https://github.com/pqt/social-preview)

### Bitcoin Blockchain Clustering Analysis for Ransomware Detection

This code was developed as a study tool for the **Cluster Analysis, Association Mining, and Model Evaluation** course provided by the University of California Irvine on [Coursera](https://www.coursera.org/learn/cluster-analysis-association-mining-and-model-evaluation).
It utilizes the _BitcoinHeistRansomwareAddress_ data set, available at the UCI Machine Learning Repository.

# Usage

1. Clone repository
1. Fetch dataset ([data.zip](https://archive.ics.uci.edu/ml/machine-learning-databases/00526/))
1. Extract inside `{PROJECT_ROOT}/assets/dataset`so you have the following:
   - `{PROJECT_ROOT}/assets/dataset/BitcoinHeistData.csv`
1. Install requirements:
    - `pip install -r requirements.txt`
1. Run `social_media_buzz` module:
    - `python -m bitcoin_heist`
1. Check results under `/assets/results/`


# Acknowledgements

Special thanks to **Cuneyt Gurcan Akcora** (University of Manitoba), **Yulia Gel** (University of Texas at Dallas), and **Murat kantarcioglu** (University of Texas at Dallas) for providing the data set used here.

I'd also like to thank University of California Irvine for hosting the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets.php), [where the data set](https://archive.ics.uci.edu/ml/datasets/BitcoinHeistRansomwareAddressDataset) can be [downloaded](https://archive.ics.uci.edu/ml/machine-learning-databases/00526/data.zip).
