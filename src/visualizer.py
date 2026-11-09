
import matplotlib.pyplot as plt


def plot_histogram(df, column):
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.hist(df[column].dropna(), bins=20, edgecolor="black")
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

    fig.tight_layout()
    return fig


def plot_boxplot(df, column):
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.boxplot(df[column].dropna())
    ax.set_title(f"Box Plot of {column}")
    ax.set_ylabel(column)

    fig.tight_layout()
    return fig


def plot_bar_chart(df, column):
    counts = df[column].value_counts().head(15)

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(counts.index.astype(str), counts.values)
    ax.set_title(f"Frequency of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    ax.tick_params(axis="x", rotation=45)

    fig.tight_layout()
    return fig


def plot_correlation_heatmap(df):
    numerical_df = df.select_dtypes(include="number")

    if numerical_df.shape[1] < 2:
        return None

    correlation = numerical_df.corr()

    fig, ax = plt.subplots(figsize=(10, 7))

    image = ax.imshow(
        correlation,
        cmap="coolwarm",
        interpolation="nearest"
    )

    fig.colorbar(image, ax=ax, label="Correlation")

    ax.set_xticks(range(len(correlation.columns)))
    ax.set_xticklabels(correlation.columns, rotation=45, ha="right")

    ax.set_yticks(range(len(correlation.columns)))
    ax.set_yticklabels(correlation.columns)

    ax.set_title("Correlation Heatmap")

    fig.tight_layout()
    return fig
