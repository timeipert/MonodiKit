import pickle, os
import sys

sys.path.append('..')
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

import monodikit

class IntervalBigramHeatmap:
    def __init__(self):
        self.corpus_directory = "../../data/*"
        self.corpus_pickle_path = "corpus.pkl"
        self.corpus = self.load_corpus()
        self.neumes_per_chant = []

    def load_corpus(self):
        if not os.path.exists(self.corpus_pickle_path):
            corpus = monodikit.Corpus(self.corpus_directory)
            with open(self.corpus_pickle_path, "wb") as f:
                pickle.dump(corpus, f)
        else:
            with open(self.corpus_pickle_path, "rb") as f:
                corpus = pickle.load(f)
        return corpus

    def create_intervals(self, neumes, filter_division_change=True):
        return [int(interval) for interval in
                monodikit.compute_intervals(neumes, filter_division_change=filter_division_change)]

    @classmethod
    def divide_list(cls, lst, num_parts):
        avg = len(lst) / float(num_parts)
        result = []
        last = 0.0

        while last < len(lst):
            result.append(lst[int(last):int(last + avg)])
            last += avg
        return result

    @classmethod
    def create_interval_dataframe(cls, intervals):
        interval_df = pd.DataFrame({'interval': intervals})
        interval_df['next_interval'] = interval_df['interval'].shift(-1).dropna().astype(int).astype("Int64")
        return interval_df

    @classmethod
    def calculate_heatmap_data(cls, interval_df, normalize=True):
        heatmap_data = interval_df.groupby(['interval', 'next_interval']).size().unstack(fill_value=0)
        if normalize:
            sum_value = heatmap_data.sum().sum()
            heatmap_data = heatmap_data / sum_value
        return heatmap_data

    def calculate_mean_matrix(self, dataframes):
        indices = set()
        columns = set()
        for df in dataframes:
            indices.update(df.index)
            columns.update(df.columns)

        mean_matrix = pd.DataFrame(index=sorted(indices), columns=sorted(columns))

        for row_index in mean_matrix.index:
            for col_index in mean_matrix.columns:
                mean_matrix.loc[row_index, col_index] = self.calculate_mean(dataframes, row_index, col_index)

        return mean_matrix

    def calculate_mean(self, dataframes, row_index, col_index):
        values = []
        for df in dataframes:
            if row_index in df.index and col_index in df.columns:
                value = df.loc[row_index, col_index]
                if not np.isnan(value):
                    values.append(value)
        if values:
            return np.mean(values)
        else:
            return 0

    @classmethod
    def add_missing_intervals(cls, heatmap_sum):
        unique_intervals = {-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        missing_intervals = unique_intervals - set(heatmap_sum.index)
        for interval in missing_intervals:
            heatmap_sum[interval] = 0
        return heatmap_sum

    @classmethod
    def reorder_heatmap(cls, heatmap_sum):
        unique_intervals = {-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        heatmap_sum = heatmap_sum[sorted(unique_intervals)]
        heatmap_sum = heatmap_sum.reindex(sorted(unique_intervals))
        return heatmap_sum

    def compute(self):
        intervals_complete = [self.create_intervals(document.flat_neume_components) for document in
                              self.corpus.documents]
        intervals_chunks = [self.divide_list(self.create_intervals(document.flat_neume_components), 10) for document in
                            self.corpus.documents]
        beginnings = []
        middles = []
        endings = []
        for chant in intervals_chunks:
            chunks = []
            for chunk in chant:
                interval_df = self.create_interval_dataframe(chunk)
                heatmap_data = self.calculate_heatmap_data(interval_df, normalize=True)
                chunks.append(heatmap_data)
            try:
                beginnings.append(chunks[0])
                middles.append(self.calculate_mean_matrix(chunks[1:-2]))
                endings.append(chunks[-1])
            except:
                print(chunks)
        begin_matrix = self.reorder_heatmap(self.add_missing_intervals(self.calculate_mean_matrix(beginnings)))
        middle_matrix = self.reorder_heatmap(self.add_missing_intervals(self.calculate_mean_matrix(middles)))
        end_matrix = self.reorder_heatmap(self.add_missing_intervals(self.calculate_mean_matrix(endings)))

        complete_matrices = []
        for chant in intervals_complete:
            interval_df = self.create_interval_dataframe(chant)
            complete_matrices.append(self.calculate_heatmap_data(interval_df, normalize=True))
        complete_matrix = self.reorder_heatmap(
            self.add_missing_intervals(self.calculate_mean_matrix(complete_matrices)))
        self.plot_composed_figure(complete_matrix, begin_matrix, middle_matrix, end_matrix, "Test")

    def plot_composed_figure(self, heatmap_all,
                             heatmap_begin,
                             heatmap_middle,
                             heatmap_end,
                             title_string):
        fig, axes = plt.subplots(1, 4, figsize=(15, 5))
        cbar_ax = fig.add_axes([.28, .09, .4, .02])
        sns.heatmap(heatmap_all.fillna(0), annot=False, cmap="BuPu", square=True, fmt='d', ax=axes[0],
                    cbar=False, norm=LogNorm())
        sns.heatmap(heatmap_begin.fillna(0), annot=False, cmap="BuPu", square=True, fmt='d', ax=axes[1],
                    cbar=False, norm=LogNorm())
        sns.heatmap(heatmap_middle.fillna(0), annot=False, cmap="BuPu", square=True, fmt='d', ax=axes[2],
                    cbar=False, norm=LogNorm())
        sns.heatmap(heatmap_end.fillna(0), annot=False, cmap="BuPu", square=True, fmt='d', ax=axes[3],
                    cbar=True,
                    cbar_ax=cbar_ax,
                    cbar_kws={"shrink": 0.2, "location": "bottom"},
                    norm=LogNorm()
                    )
        fig.tight_layout(rect=[0, 0, .9, 1])
        axes[0].set_title(f"Complete Chant")
        axes[1].set_title(f"Beginning Part")
        axes[2].set_title(f"Middle Part")
        axes[3].set_title(f"Ending Part")
        ylabel = [ax.set_xlabel("Subsequent Interval") for ax in axes]
        xlabel = [ax.set_ylabel("") for ax in axes]
        axes[0].set_ylabel("Initial Interval")

        plt.savefig(f"{title_string}_figure.png", bbox_inches='tight', pad_inches=0.5)


experiment = IntervalBigramHeatmap()
experiment.compute()
