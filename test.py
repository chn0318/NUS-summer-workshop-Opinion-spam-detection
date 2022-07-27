from autogluon.tabular import TabularDataset, TabularPredictor
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("-feature", default='all_feature', type=str, help="choose the feature that would be used for detecting spam review,such as postag,keyword,similar,liwc,postag_liwc,all_feature")
    args = parser.parse_args()
    feature=args.feature
    test_data = TabularDataset('./test_data/{}_test.csv'.format(feature))
    label='label'
    save_dir='./save_model/{}'.format(feature)
    y_test = test_data[label]
    test_data_nolab = test_data.drop(columns=[label])
    print(test_data_nolab.head())
    predictor=TabularPredictor.load(save_dir)
    y_pred = predictor.predict(test_data_nolab)
    print("Predictions:  \n", y_pred)
    print(predictor.evaluate_predictions(y_true=y_test, y_pred=y_pred, auxiliary_metrics=True))
    print(predictor.leaderboard(test_data, silent=True)) 