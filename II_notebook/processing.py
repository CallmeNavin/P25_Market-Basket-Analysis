import pandas as pd
df = pd.read_csv("p25_mba/I_raw/basket_analysis.csv")
df_items = df.drop(columns=["id"])
df_bool = df_items.astype(bool)

from mlxtend.frequent_patterns import apriori, association_rules
frequent_itemsets = apriori(df_bool, min_support=0.05, use_colnames=True)
print('Top itemsets by support:')
print(frequent_itemsets.sort_values(by="support", ascending=False).head(10))

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
print("\nTop rules by lift:")
print(rules.sort_values(by="lift", ascending=False)[["antecedents", "consequents", "support", "confidence", "lift"]].head(10))