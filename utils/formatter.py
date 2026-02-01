def format_top_features(feature_names, importances, k=3):
    pairs = list(zip(feature_names, importances))
    pairs.sort(key=lambda x: x[1], reverse=True)

    return pairs[:k]
