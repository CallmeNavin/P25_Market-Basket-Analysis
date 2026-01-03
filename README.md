# Retail Site Selection Analytics

**VERSION 1 - DESCRIPTIVE ANALYSIS**

**A. Project Overview**

- This project demonstrates a basic Market Basket Analysis workflow using the Apriori algorithm.
- This exercise focuses on understanding the algorithmic flow rather than deriving real-world business insights.

**B. Dataset Information**

**Source**

- Market Basket Analysis Data (from Kaggle): https://www.kaggle.com/datasets/ahmtcnbs/datasets-for-appiori
- The dataset is already one-hot encoded at transaction level. After removing the transaction identifier and ensuring boolean input, frequent itemsets are generated based on minimum support. Association rules are then derived and ranked by lift to highlight meaningful co-purchase patterns. 

**D. Key Findings and Actionable Plans**

**I. Key Findings**

- Single products such as chocolate, butter, and yogurt show high support (~40%), indicating core items.
- High-support single items rarely appear in top high-lift pairs, indicating that popular products tend to be purchased independently across diverse contexts, while strong co-purchase relationships are more likely among niche or context-specific items.
- Association rules with high lift (>1.7) reveal meaningful co-occurrence patterns between product combinations, even though their overall frequency (support ~5–6%) is relatively low.

**II. Actionable Plans**

- Differentiate roles of products: Treat high-support single items as traffic or volume drivers, not primary targets for bundle or cross-sell strategies.
- Focus cross-sell efforts on high-lift pairs. However, these pairs are suitable candidates for small-scale experiments, minimizing risk while testing potential uplift.

**E. Appendix**

Top itemsets by support:
     support        itemsets
15  0.421421     (chocolate)
2   0.420420        (Butter)
14  0.420420        (Yogurt)
7   0.410410     (Ice cream)
12  0.409409         (Sugar)
8   0.408408  (Kidney Beans)
4   0.407407          (Corn)
9   0.405405          (Milk)
3   0.404404        (Cheese)
11  0.403403         (Onion)

Top rules by lift:
                antecedents            consequents   support  confidence      lift
5639         (Dill, Cheese)  (Kidney Beans, Onion)  0.055055    0.310734  1.826022
5634  (Kidney Beans, Onion)         (Dill, Cheese)  0.055055    0.323529  1.826022
6643        (Unicorn, Dill)     (Onion, chocolate)  0.060060    0.357143  1.820335
6646     (Onion, chocolate)        (Unicorn, Dill)  0.060060    0.306122  1.820335
5662   (Kidney Beans, Dill)    (chocolate, Cheese)  0.057057    0.331395  1.779914
5667    (chocolate, Cheese)   (Kidney Beans, Dill)  0.057057    0.306452  1.779914
3931          (Corn, Sugar)       (Unicorn, Apple)  0.055055    0.294118  1.770021
3926       (Unicorn, Apple)          (Corn, Sugar)  0.055055    0.331325  1.770021
4250  (Kidney Beans, Bread)           (Corn, Milk)  0.057057    0.341317  1.766715
4251           (Corn, Milk)  (Kidney Beans, Bread)  0.057057    0.295337  1.766715

_**About Me**_

Hi, I'm Navin (Bao Vy) – an aspiring Data Analyst passionate about turning raw data into actionable business insights.
I’m eager to contribute to data-driven decision making and help organizations translate analytics into business impact.
For more details, please reach out at:

🌐 LinkedIn: https://www.linkedin.com/in/navin826/

📂 Portfolio: https://github.com/CallmeNavin/