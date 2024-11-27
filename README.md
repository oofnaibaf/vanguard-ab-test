# vanguard-ab-test

## Overview

Vanguard is a leading American investment firm, managing 9.3 btrillion in global assets and Vanguard is commited to investor-centric principles and cost-effective investment solutions. Therefore, this project focuses on analyzing the results of a digital experiment conducted by Vanguard, to assess whether a redesigned user interface (UI) leads to higher completion rates of an online process.

The experiment consists of two groups of clients: a Control group using the old UI and a Test group using the new UI. The objective is to evaluate the performance of both groups and assess whether the new design enhances completion rates.

## Key Objectives

The project aims to assess whether the new UI improves completion rates compared to the old UI, while also evaluating its cost-effectiveness and potential demographic differences in adoption and success. This will involve Exploratory Data Analysis (EDA), hypothesis testing, performance evaluation, and data visualization using Python and Tableau.

## Datasets

The analysis relies on three key datasets:

Client Profiles (df_final_demo): Demographics such as age, gender, account details of Vanguard clients.
Digital Footprints (df_final_web_data): A detailed trace of client interactions online, divided into two parts: pt_1 and pt_2.
Experiment Roster (df_final_experiment_clients): A list revealing which clients participated in the experiment.

## Results and Key Insights
The project aims to determine:

- Whether the new digital UI leads to a higher completion rate for Vanguard clients?
  
Null Hypothesis (H_0): The completion rate for the Test group (new design) is equal to the completion rate for the Control group (old design).

Alternative Hypothesis (H_a): The completion rate for the Test group (new design) is not equal to the completion rate for the Control group (old design).

Our analysis showed that the test group has a higher completion rate compared to the control group. The test group achieved a completion rate of 0.60, while the control group had a rate of 0.51, indicating a statistically significant improvement in performance for the test group. Therfore, we reject the Null Hypothesis.

- Whether the observed increase meets the 5% cost-effectiveness threshold?
  
Null Hypothesis (H_0): The completion rate for the Test group (new design) is equal to or greater than the completion rate for the Control group (old design) increased by 5%.

Alternative Hypothesis (H_a): The completion rate for the Test group (new design) is lower than the completion rate for the Control group (old design) increased by 5%.
  
Our analysis confirmed that the observed increase in completion rate meets the 5% cost-effectiveness threshold. In fact, the improvement is even greater, with the test group showing approximately a 16% higher completion rate compared to the control group. This substantial increase demonstrates a strong and cost-effective result. Here, we can confirm the Null Hypothesis.

- If any demographic factors influence the completion rates for either the Control or Test group?

Based on our analysis, we observed that males in both the Test and Control groups have higher completion rates compared to females. Additionally, individuals aged 45 to 65 exhibited higher error rates, particularly with an increased number of backward steps, indicating that this age group may face more challenges during the task.


## Conclusion

This project analyzes the effectiveness of Vanguard’s new digital UI in improving client engagement through an A/B test. In conclusion, the new digital UI significantly improves the completion rate for Vanguard clients, surpassing the 5% cost-effectiveness threshold, and thus supports the effectiveness of the new design.

## Presentation

https://www.canva.com/design/DAGW75AGohE/HsU9HSBLG_PpUpjYUP85MQ/edit
