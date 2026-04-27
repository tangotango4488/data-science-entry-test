prompt_a = """
I am a marketing manager at a retail company and we have just finished 
a three-month campaign. My team has collected customer feedback through 
an online survey and we now have about 500 responses stored in a 
spreadsheet. Each response includes the customer's age group, the 
product they purchased, their satisfaction rating from 1 to 5, and a 
short written comment. I need to present the findings to our CEO next 
Friday in a way that is easy to understand. Can you analyse this data 
for me, highlight which age groups and products have the lowest 
satisfaction scores, identify the most common complaints from the 
written comments, and summarise everything in a short paragraph I can 
use as an executive summary?
"""

prompt_b = """
Role: You are a data analyst helping a retail marketing team.
Task: Analyse customer survey data from a 3-month campaign.
Data: 500 responses containing age group, product purchased, 
satisfaction rating (1-5), and written comments.
Steps:
1. Identify age groups and products with the lowest satisfaction scores.
2. Extract the most common themes from the written comments.
3. Summarise findings in an executive summary paragraph.
Audience: CEO presentation on Friday.
Constraints: Keep the summary concise and free of technical jargon.
"""


# Task 1
# Read both prompts above carefully, then answer the questions below as comments.

# Q8a: Which prompt do you think will get a better response from an AI?
# Your answer: Prompt B

# Q8b: Give TWO reasons to support your choice.
# Your answer (Reason 1): Prompt B is clearer for the AI to follow with defined labels (e.g age group, product purchased, satisfaction rating, comments), which will help AI to addresses all the necessary components of the task in a logical manner.
# Your answer (Reason 2): Prompt B It defines the audience (CEO) and specific constraints (no jargon, concise), ensuring the tone of the output is professionally aligned with the goal.

# Q8c: What is ONE strength of the prompt you did NOT choose?
# Your answer: Prompt A provides a more natural "narrative" background which can help the AI to understand the context of the task better, making it more relatable and easier to generate a response that fits the scenario.


# Task 2
# Rewrite either prompt by borrowing ONE element from the other
# to make it stronger. Explain what you borrowed and why.
""""

Rewritten Prompt:

Task: Analyse 500 customer survey responses from a 3-month campaign.
Data Details: Each response includes age group, product purchased, satisfaction rating (1-5), and a short written comment.

Steps:
1) Identify age groups and products with the lowest satisfaction scores.
2) Extract the most common themes or complaints from the written comments.
3) Summarise findings in an executive summary paragraph for a CEO presentation this Friday.

Constraints: Keep the summary concise and free of technical jargon.

"""
# I borrowed the specific data attributes (age group, product, rating, comments) from Prompt A and integrated them into the "Data Details" section.
# This addition provides clarity on what exactly is included in the dataset, which can help the AI to focus on analyzing those specific variables, leading to a more accurate and relevant response.
# The structured format of Prompt B combined with the detailed data attributes from Prompt A creates a comprehensive prompt that is both clear and informative for the AI.