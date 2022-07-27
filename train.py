import torch
import argparse
from autogluon.tabular import TabularDataset, TabularPredictor
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-feature", default='all_feature', type=str, help="choose the feature that would be used for detecting spam review,such as postag,keyword,similar,liwc,postag_liwc,all_feature")
    args = parser.parse_args()
    feature=args.feature
    train_data = TabularDataset('./train_data/{}_train.csv'.format(feature))
    train_data.head()
    label='label'
    save_dir='./save_model/{}'.format(feature)
    predictor = TabularPredictor(label=label,path=save_dir).fit(train_data)
    print(predictor.fit_summary(verbosity=3, show_plot=True))

