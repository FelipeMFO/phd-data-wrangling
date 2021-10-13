import pandas as pd
import numpy as np
import random


class FeatureEngineering():
    """AI is creating summary for FeatureEngineering
    """
    def __init__(self) -> None:
        pass

    def mix_numpy_arrays(self,
                         array1:np.ndarray,
                         array2:np.ndarray,
                         amount_first_array: int,
                         amount_second_array: int
                        #  output_size: int,
                        #  fration_of_first: float = 0.5,
                        #  fration_of_second: float = 0.5
                         ) -> np.ndarray:
        """IMPORTANTE A PORCENTAGEM VAI SER BASEADA DO TAMANHO DO OUTPUT

        Args:
            array1 (np.ndarray): [description]
            array2 (np.ndarray): [description]
            reduction_factor (int, optional): [description]. Defaults to 4.

        Returns:
            np.ndarray: [description]
        """
        # np.random.shuffle(array1)
        # np.random.shuffle(array2)
        return np.concatenate([
            np.random.choice(array1, amount_first_array),
            np.random.choice(array2, amount_second_array)
        ])
        # ans = []
        # ans.append(array1.tolist()[:int(output_size*fration_of_first)])
        # ans.append(array2.tolist()[:int(output_size*fration_of_second)])

        # return ans

    def mix_lists(self,
                  list1: list,
                  list2: list,
                  output_size: int,
                  fration_of_first: float = 0.5,
                  fration_of_second: float = 0.5) -> list:
        """IMPORTANTE A PORCENTAGEM VAI SER BASEADA DO TAMANHO DO OUTPUT

        Args:
            array1 (np.ndarray): [description]
            array2 (np.ndarray): [description]
            reduction_factor (int, optional): [description]. Defaults to 4.

        Returns:
            np.ndarray: [description]
        """
        random.shuffle(list1)
        random.shuffle(list2)        
        ans = []
        ans.append(list1[:int(output_size*fration_of_first)])
        ans.append(list2[:int(output_size*fration_of_second)])

        return ans
    
    
    