import pandas as pd
import numpy as np
import random


class FeatureEngineering():
    """AI is creating summary for FeatureEngineering
    """
    def __init__(self) -> None:
        pass

    def mix_numpy_arrays(self,
                         array1: np.ndarray,
                         array2: np.ndarray,
                         amount_first_array: int,
                         amount_second_array: int
                         ) -> np.ndarray:
        """IMPORTANTE A PORCENTAGEM VAI SER BASEADA DO TAMANHO DO OUTPUT

        Args:
            array1 (np.ndarray): [description]
            array2 (np.ndarray): [description]
            reduction_factor (int, optional): [description]. Defaults to 4.

        Returns:
            np.ndarray: [description]
        """
        return np.concatenate([
            np.random.choice(array1, amount_first_array),
            np.random.choice(array2, amount_second_array)
        ])

    def mix_numpy_arrays_comp_list(self,
                                   tuple_arrays: tuple,
                                   tuple_amounts: tuple
                                   ) -> np.ndarray:
        """IMPORTANTE A PORCENTAGEM VAI SER BASEADA DO TAMANHO DO OUTPUT

        Args:
            array1 (np.ndarray): [description]
            array2 (np.ndarray): [description]
            reduction_factor (int, optional): [description]. Defaults to 4.

        Returns:
            np.ndarray: [description]
        """
        return np.concatenate(
            [np.random.choice(arr, amount)
                for arr, amount in zip(tuple_arrays, tuple_amounts)]
        )
