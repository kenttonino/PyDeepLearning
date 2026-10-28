from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

def run_exercise_redwine():
    # Set the matplotlib defaults.
    plt.rc('figure', autolayout=True);
    plt.rc(
            'axes',
            labelweight='bold',
            labelsize='large',
            titleweight='bold',
            titlesize=18,
            titlepad=10
    );

    ROOT = Path(__file__).resolve().parent.parent.parent
    red_wine = pd.read_csv(ROOT / "dataset" / "red-wine.csv");
    red_wine.head();
