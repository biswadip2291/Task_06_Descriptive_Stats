# Task 06 — Descriptive Statistics and Large Language Models  

This repository documents the research project for Task 5, which explores the capabilities and limitations of Large Language Models (LLMs) in performing descriptive statistical analysis on a sports dataset.  

**Researcher:** Biswadip Bhattacharyya  
**Report Date:** August 15, 2024  
**Dataset:** 2025 Syracuse Women's Lacrosse (stats as of May 12, 2025)  
**LLM Used:** ChatGPT-4 with Advanced Data Analysis (simulated interaction)  

---

## 1. Project Objective  

The goal of this research is to challenge a Large Language Model with natural language questions about a small dataset, progressing from simple factual queries to a complex, inferential coaching recommendation.  

The focus is on:  
- Prompt engineering  
- Metric definition  
- Documenting the LLM's successes and failures in a multi-stage analytical task  

---

## 2. Phase 1 Recap (Work from July 31st Report)  

In the first research period, the project was successfully initiated.  

**Key accomplishments included:**  

**Data Preparation:**  
- Stats from the provided image were transcribed into two machine-readable CSV files:  
  - `player_stats_2025.csv`  
  - `game_results_2025.csv`  

**Initial LLM Interaction:**  
- LLM successfully ingested the data and accurately answered simple factual questions (e.g., win–loss record, top scorer)  

**Basic Prompt Engineering:**  
- A subjective question (“Who is the most efficient scorer?”) was answered by defining “efficiency” as Shooting Percentage and providing the LLM with a clear, multi-step process for calculation  

**Conclusion from Phase 1:**  
- LLM is strong in executing well-defined instructions  
- User must provide the analytical framework  

---

## 3. Phase 2 — Answering the Coaching Recommendation (Work for August 15th Report)  

This phase focused on the main objective:  

> “To win two more games, should I focus on offense or defense, and who is the one player I should work with to be a game changer?”

This required decomposing the question into a logical sequence of prompts (“prompt chaining”), where the output of one analysis informs the next.  

---

### Step 1: Analyzing Performance in Losses  

**Prompt:** See `prompts/04_analysis_of_losses.txt`  

**LLM Findings:**  

| Metric               | Season Average | Average in 9 Losses | Performance Gap |
|----------------------|----------------|---------------------|-----------------|
| Goals Scored         | 12.37          | 8.67                 | -3.70           |
| Goals Against        | 11.63          | 13.22                | +1.59           |

**Insight:**  
- The team’s offense collapses in losses, scoring nearly 4 fewer goals per game.  
- Defensive performance also drops, but the offensive decline is more than twice as severe.  

---

### Step 2: Determining the Strategic Focus  

**Prompt:** See `prompts/05_strategic_focus.txt`  

**LLM Recommendation:**  
- Focus should be on **offense**  

**Justification:**  
> "The data shows that your team's identity is built around its high-scoring offense... In losses, your defense only gives up about 1.5 extra goals, but your offense scores nearly 4 fewer goals... Closing the offensive gap is the most direct, data-supported path to converting these losses into wins."  

---

### Step 3: Identifying a "Game Changer" Player  

**Prompt:** See `prompts/06_identify_game_changer.txt`  

**LLM Findings:**  
- Team shooting percentage: **43.7%**  
- High-volume shooters (≥ 40 shots) below team average:  

| Player           | Shots | Goals | Shooting Pct | Below Team Avg? |
|------------------|-------|-------|--------------|-----------------|
| Emma Ward        | 77    | 30    | 39.0%        | Yes             |
| Joely Caramelli  | 46    | 16    | 34.8%        | Yes             |

**LLM Recommendation:**  
- Selected: **#33 Joely Caramelli**  

**Justification:**  
> "Joely Caramelli is already a core part of the offense, taking the 6th most shots on the team (46). However, her shooting percentage of 34.8% is the lowest among all high-volume shooters... A small improvement in her conversion rate could yield a large increase in goals."  

---

### Step 4: Synthesizing the Final Recommendation  

**Prompt:** See `prompts/07_final_recommendation.txt`  

**Final Synthesized Answer:**  
> "Coach, to win two more games next season, your primary focus should be on boosting your offense. Our analysis shows that in your losses, the team's offensive production falls by a staggering 3.7 goals per game, a drop-off far more significant than any defensive struggles. The key to closing this gap lies with #33 Joely Caramelli. She is already a vital playmaker, generating a high volume of shots (46), but her conversion rate is the lowest among your core offensive group. By working with her specifically on shot selection and finishing, even a modest improvement in her efficiency would translate directly into the extra goals needed to turn your toughest losses into wins."  

---

## 4. Research Experience and Reflections  

**The User as the Analyst:**  
- The LLM did not “decide” the approach — it executed the analytical steps I designed.  
- Quality of the output depended on my ability to decompose the problem and design prompts.  

**Power of Prompt Chaining:**  
- The loss analysis fed into the strategic focus step, which narrowed the player identification search.  

**Synthesis is a Key Strength:**  
- LLM excelled at merging all findings into a coherent narrative in the final step.  

---

## 5. Conclusion and Future Work  

This research demonstrated that LLMs can be guided to produce **complex, data-driven insights** from a small dataset when:  
- Metrics are clearly defined  
- Problems are broken into steps  
- Outputs are validated by the analyst  

**Future Direction:**  
- As suggested by Professor Strome, present findings in a more narrative, accessible format (e.g., **“AI Street Interview”**)  

---
