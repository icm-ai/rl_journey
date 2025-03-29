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
    def print_evens(x: list[int]) -> None:
        for i in (j for j in x if j % 2 == 0):
            print(i)
    print_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    return (print_evens,)


@app.cell
def _():
    def print_evens_1(x: list[int]) -> None:
        evens = (j for j in x if j % 2 == 0)
        for i in evens:
            print(i)

    print_evens_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    return (print_evens_1,)


@app.cell
def _():
    def print_evens_2(x: list[int]) -> None:
        print(*[i for i in x if i % 2 == 0], sep="\n")

    print_evens_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    return (print_evens_2,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
