import marimo

__generated_with = "0.11.30"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


@app.cell
def _(np, plt):
    plt.scatter(np.linspace(0, 100, 11), np.linspace(0, 100, 11))
    plt.show()
    return


@app.cell
def _(np):
    print(np.linspace(0, 90, 10))
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
