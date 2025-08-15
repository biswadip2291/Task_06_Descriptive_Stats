Task 06 Descriptive Statistics and Large Language Models
This repository documents the research project for Task 5, which explores the capabilities and limitations of Large Language Models (LLMs) in performing descriptive statistical analysis on a sports dataset.
Researcher: Biswadip Bhattacharyya
Report Date: August 15, 2024
Dataset: 2025 Syracuse Women's Lacrosse (stats as of May 12, 2025)
LLM Used: ChatGPT-4 with Advanced Data Analysis (simulated interaction)
1. Project Objective
The goal of this research is to challenge a Large Language Model with natural language questions about a small dataset, progressing from simple factual queries to a complex, inferential coaching recommendation. The focus is on the process of prompt engineering, metric definition, and documenting the LLM's successes and failures in a multi-stage analytical task.
2. Phase 1 Recap (Work from July 31st Report)
In the first research period, the project was successfully initiated. Key accomplishments included:
Data Preparation: The stats from the provided image were transcribed into two machine-readable CSV files (player_stats_2025.csv and game_results_2025.csv).
Initial LLM Interaction: The LLM successfully ingested the data and accurately answered simple factual questions (e.g., win-loss record, top scorer).
Basic Prompt Engineering: A subjective question ("Who is the most efficient scorer?") was successfully answered by engineering a prompt that defined "efficiency" as Shooting Percentage and provided the LLM with a clear, multi-step process for its calculation.
This initial phase confirmed the LLM's strength in executing well-defined instructions but highlighted the user's responsibility to provide the analytical framework.
3. Phase 2: Answering the Coaching Recommendation (Work for August 15th Report)
This research period focused on completing the main objective: using the LLM to derive a data-driven answer to the complex coaching question: "To win two more games, should I focus on offense or defense, and who is the one player I should work with to be a game changer?"
This required decomposing the question into a logical sequence of prompts, a technique known as "prompt chaining," where the output of one analysis informs the input for the next.
Step 1: Analyzing Performance in Losses
To decide where to focus coaching efforts, I first tasked the LLM with analyzing what goes wrong in the games the team loses.
Prompt: See prompts/04_analysis_of_losses.txt
LLM Findings: The LLM correctly calculated and compared the team's season averages against their performance in the 9 losses. The results were stark:
Metric	Season Average	Average in 9 Losses	Performance Gap
Goals Scored (Offense)	12.37	8.67	-3.70
Goals Against (Defense)	11.63	13.22	+1.59
Insight: The team's offense collapses in losses, scoring nearly 4 fewer goals per game. The defense also performs worse, but the offensive drop-off is more than twice as severe.
Step 2: Determining the Strategic Focus
With the data from Step 1, I asked the LLM to make a strategic recommendation.
Prompt: See prompts/05_strategic_focus.txt
LLM Recommendation: The LLM concluded the focus should be on offense.
Justification (from LLM): "The data shows that your team's identity is built around its high-scoring offense... In losses, your defense only gives up about 1.5 extra goals, but your offense scores nearly 4 fewer goals... Closing the offensive gap is the most direct, data-supported path to converting these losses into wins."
Step 3: Identifying a "Game Changer" Player
With the focus narrowed to offense, the next step was to identify a player with the highest potential for improvement. I engineered a prompt to find a high-volume shooter with a below-average shooting percentage.
Prompt: See prompts/06_identify_game_changer.txt
LLM Findings: The LLM first calculated the team's overall shooting percentage (43.7%) and then analyzed the high-volume shooters (>= 40 shots).
Player	Shots	Goals	Shooting Pct	Below Team Avg?
Emma Ward	77	30	39.0%	Yes
...	...	...	...	...
Joely Caramelli	46	16	34.8%	Yes
LLM Recommendation: The model identified #33 Joely Caramelli.
Justification (from LLM): "Joely Caramelli is already a core part of the offense, taking the 6th most shots on the team (46). However, her shooting percentage of 34.8% is the lowest among all high-volume shooters... A small improvement in her conversion rate could yield a large increase in goals."
Step 4: Synthesizing the Final Recommendation
Finally, I asked the LLM to combine all these findings into a single, actionable paragraph for a coach.
Prompt: See prompts/07_final_recommendation.txt
Final Synthesized Answer:
"Coach, to win two more games next season, your primary focus should be on boosting your offense. Our analysis shows that in your losses, the team's offensive production falls by a staggering 3.7 goals per game, a drop-off far more significant than any defensive struggles. The key to closing this gap lies with #33 Joely Caramelli. She is already a vital playmaker, generating a high volume of shots (46), but her conversion rate is the lowest among your core offensive group. By working with her specifically on shot selection and finishing, even a modest improvement in her efficiency would translate directly into the extra goals needed to turn your toughest losses into wins."

5. Research Experience and Reflections
This second phase provided deeper insights into the practical use of LLMs for data analysis:
The User as the Analyst: The LLM did not "decide" how to solve the problem. It acted as a powerful, high-speed data processor that executed a series of analytical steps I designed. The quality of the final recommendation was entirely dependent on my ability to decompose the problem and engineer the right sequence of prompts.
Power of Prompt Chaining: This project demonstrated that the true power of LLMs in analysis comes from chaining prompts. The conclusion from the "loss analysis" prompt became the premise for the "strategic focus" prompt, which in turn narrowed the search space for the "player identification" prompt.
Synthesis is a Key Strength: While the LLM needed guidance for the step-by-step analysis, its ability to synthesize all the quantitative findings into a coherent, well-written narrative in the final step was impressive and highly valuable.

6. Conclusion and Future Work
This research task successfully demonstrated that a Large Language Model can be guided to produce complex, data-driven insights from a small dataset. The process requires a human analyst to define metrics, decompose problems, and validate outputs.
For future work, as suggested by Professor Strome, these findings could be presented in a more narrative format, such as an "AI Street Interview," to make the data story more accessible and engaging.