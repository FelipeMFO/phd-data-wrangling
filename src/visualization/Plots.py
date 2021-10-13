import matplotlib.pyplot as plt


class Plots():
    """Creates a new class that will be used for rendering the plots .
    """

    def __init__(self) -> None:
        pass

    def plot_spectrum(self, dfs_dict:dict, title: str,
                      size: tuple = (16,12), ncols:int = 2) -> None:
        """Plot the spectrum of the given dictionary .

        Args:
            dfs_dict (dict): [description]
            ncols (int, optional): [description]. Defaults to 2.
        """
        nrows = (len(dfs_dict)//ncols) + 1
        fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=size)
        for i in dfs_dict.keys():

        pass
    
    def 