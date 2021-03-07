import argparse
import pandas as pd
import numpy as np
import itertools
from collections import defaultdict

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n_teams", type=int)
    parser.add_argument("periods", type=int)
    parser.add_argument("--output", type=str, default="season.csv")
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()

    np.random.seed(args.seed)
    teams = np.arange(args.n_teams)
    pairs = list(itertools.combinations(teams, 2))
    season = {
        "period": [],
        "p1": [],
        "p2": []
    }
    for period in np.arange(args.periods):
        matched = set()
        while len(matched) < args.n_teams:
            remaining = [x for x in pairs if x[0] not in matched and x[1] not in matched]
            pair = remaining[np.random.choice(len(remaining))]
            matched.add(pair[0])
            matched.add(pair[1])

            season["period"].append(period)
            season["p1"].append(pair[0])
            season["p2"].append(pair[1])

    df = pd.DataFrame(season)
    df.to_csv(args.output, index=None)

if __name__ == '__main__':
    main()