import numpy as np
import pandas as pd
from typing import Union
import h2o
from h2o.automl import H2OAutoML

class Modeling():
    """Class responsible for modelization"""
    def __init__(self) -> None:
        pass

    def spliting(self,
                 df: pd.DataFrame,
                 split_ratio: float,
                 target_variable: str,
                 seed: int = 1) -> dict:
        """Splits pandas data frame in 3 h2o Frames.
        The original data frame cut on specific features, and its division on
        train and test, following the split ratio
        Args:
            df (pd.DataFrame): Original data frame that will be splitted.
            split_ratio (float): Ratio to split the original data frame in
            test and train.
            range_features (tuple): columns names that will be used to cut.
            the original data frame, from range_features[0] to
            range_features[1].
            seed (int, optional): [description]. Defaults to 1. Random seed.
        Returns:
            dict: dict with H2OFrames.
        """

        X = h2o.H2OFrame(df)# df.loc[:, df.columns != target_variable]
        y = df.loc[:, target_variable]
        train, test = X.split_frame(ratios=[split_ratio],
                                                  seed=seed)

        return {
            "X": X, "y": y, "train": train, "test": test
        }

    def training(self,
                 model_name: str,
                 target_variable: str,
                 features: list,
                 train: h2o.H2OFrame,
                 test: h2o.H2OFrame,
                 maxmodels: int = 20,
                 seed: int = 1
                 ) -> H2OAutoML:
        """Train a aml object (set of models) to predict a target feature from
        features_names. Receives train and test splitted h2o frames.
        Args:
            model_name (str): name of aml object.
            features_names (list): list of strings with feature names
            used as input to prediction.
            target_feature (str): name of target feature that shall be
            predicted.
            train (h2o.H2OFrame): h2o frame that will be used to train.
            test (h2o.H2OFrame): h2o frame that will be used to test.
            maxmodels (int, optional): [description]. Defaults to 20.
            Number of models that aml object will train.
            seed (int, optional): [description]. Defaults to 1.
            Random seed.
        Returns:
            H2OAutoML: aml object with all models trained.
        """
        aml = H2OAutoML(project_name=model_name,
                        max_models=maxmodels, seed=seed)
        aml.train(x=features,
                  y=target_variable,
                  training_frame=train,
                  leaderboard_frame=test)
        return aml

    def get_predictions_df(self,
                           model: h2o.model,
                           h2o_frame,
                           index: pd.DataFrame.index,
                           kpi: pd.Series) -> pd.DataFrame:
        """Receives model, and configurations to return chats prediction,
        indexed with chats expected for the following index.
        Args:
            model (h2o.model): model to predict values.
            index (pd.DataFrame.index): Index with dates and hours to predict.
            chats (pd.Series): Amount of chats expected on those houres.
        Returns:
            pd.DataFrame: data frame with index as each hour of the week and
            3 columns: chats expectation for each hour as 'chats', attendants
            prediction as 'predict' and predictions rounded as
            'prediction_round'.
        """
        preds = model.predict(h2o_frame).as_data_frame()
        preds.set_index(index, inplace=True)
        preds = preds.join(kpi)
        preds['prediction_round'] = round(preds.predict)

        return preds