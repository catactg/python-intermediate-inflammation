#!/usr/bin/env python3
"""Software for managing and analysing patients' inflammation data in our imaginary hospital."""

import argparse
import os
from inflammation import models, views, analysis


def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    infiles = args.infiles
    if not isinstance(infiles, list):
        infiles = [args.infiles]

    for filename in infiles:
        inflammation_data = models.load_csv(filename)

        view_data = {
            "average": models.daily_mean(inflammation_data),
            "max": models.daily_max(inflammation_data),
            "min": models.daily_min(inflammation_data),
        }
        outfile = os.path.basename(filename).replace(".csv", ".png")
        if args.outdir is None:
            outpath = None
        else:
            outpath = os.path.join(args.outdir, outfile)
        views.visualize(view_data, outpath)

    _, extension = os.path.splitext(infiles[0])
    if extension == ".json":
        data_source = analysis.JSONDataSource(os.path.dirname(infiles[0]))
    elif extension == ".csv":
        data_source = analysis.CSVDataSource(os.path.dirname(infiles[0]))
    else:
        raise ValueError(f"Unsupported data file format: {extension}")
    analysis.analyse_data(data_source)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A basic patient inflammation data management system"
    )

    parser.add_argument(
        "infiles",
        nargs="+",
        help="Input CSV(s) containing inflammation series for each patient",
    )

    parser.add_argument(
        "-outdir",
        help="Output directory to save figures as PNG",
    )

    args = parser.parse_args()

    main(args)
