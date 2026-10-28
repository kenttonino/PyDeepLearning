from pathlib import Path
from utils.main import add_new_line
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
    redwine = pd.read_csv(ROOT / "dataset" / "redwine.csv");
    redwine.head();

    add_new_line(1);
    print("# ------------------------- #");
    print("# (1) Input Shape Challenge #");
    print("# ------------------------- #")
    input_shape = [redwine.shape[1] - 1];
    print(input_shape);
    add_new_line(1);
