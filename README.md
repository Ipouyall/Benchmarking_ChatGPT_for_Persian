# <p align="center">Benchmarking Large Language Models for Persian: A Preliminary Study Focusing on ChatGPT</p>

<h2 align="center">
  <p><a href="https://lrec-coling-2024.org/">[LREC-COLING 2024]</a> Benchmarking Large Language Models for Persian: A Preliminary Study Focusing on ChatGPT</p>
</h2>

<p align="center">
  <br>
  <a href="https://arxiv.org/abs/2404.02403"><img alt="Paper" src="https://img.shields.io/badge/📃-Paper-808080"></a>
  <a href="#"><img alt="Video" src="https://img.shields.io/badge/​-Video-red?logo=youtube&logoColor=FF0000"></a>
  <a href="#"><img alt="Slides" src="https://img.shields.io/badge/​-Slides-FFBB00?logo=googlesheets&logoColor=FFBB00"></a>
</p>

## Intro
This repo covers the implementation of the following paper:  **[Benchmarking Large Language Models for Persian: A Preliminary Study Focusing on ChatGPT]()** by Amirhossein Abaskohi, Sara Baruni, Mostafa Masoudi, Nesa Abbasi, Mohammad Hadi Babalou, Ali Edalat, Sepehr Kamahi, Samin Mahdizadeh Sani, Nikoo Naghavian, Danial Namazifard, Pouya Sadeghi and Yadollah Yaghoobzadeh , accepted to LREC-COLING 2024.

## Abstract
This paper explores the efficacy of large language models (LLMs) for Persian. 
While ChatGPT and consequent LLMs have shown remarkable performance in English, their efficiency for more low-resource languages remains an open question. 
We present  the first comprehensive benchmarking study of LLMs across diverse Persian language tasks.
Our primary focus is on GPT-3.5-turbo, but we also include GPT-4 and OpenChat-3.5 to provide a more holistic evaluation. Our assessment encompasses a diverse set of tasks categorized into classic, reasoning, and knowledge-based domains. To enable a thorough comparison, we evaluate LLMs against existing task-specific fine-tuned models.
Given the limited availability of Persian datasets for reasoning tasks, we introduce two new benchmarks: one based on elementary school math questions and another derived from the entrance exams for 7th and 10th grades.
Our findings reveal that while LLMs, especially GPT-4, excel in tasks requiring reasoning abilities and a broad understanding of general knowledge, they often lag behind smaller pre-trained models fine-tuned specifically for particular tasks. Additionally, we observe improved performance when test sets are translated to English before inputting them into GPT-3.5.
These results highlight the significant potential for enhancing LLM performance in the Persian language. This is particularly noteworthy due to the unique attributes of Persian, including its distinct alphabet and writing styles.

![results_overview_chart](https://github.com/AmirAbaskohi/Benchmarking_ChatGPT_for_Persian/assets/50926437/5f9e7087-8171-44ab-8299-2038b7804289)


## Datasets

The `benchmarks` and `prompts` used in our paper can be found in `Benchmarks` directory. 
In it for each task there are three files available:
- `.jsonl` file which includes the test samples
- `prompt.py` file which includes our prompts both in English and Farsi(Persian)
- `sample.ipynb` which is a sample notebook for getting the evaluation results.

For the new benchmarks introduced in the paper you find them using the following links:

* [Elementry Schools Questions Dataset](https://github.com/AmirAbaskohi/Benchmarking_ChatGPT_for_Persian/blob/main/Experiments/ChatGPT/Elemntry%20School%20Questions/elem_q.xlsx)
* [Mathematical Problems Dataset](https://github.com/AmirAbaskohi/Benchmarking_ChatGPT_for_Persian/blob/main/Experiments/ChatGPT/Mathematical%20Problems/math_dataset.csv)

For the other datasets, checkout the paper for the used datasets.

## Results

We evaluated GPT-3.5, GPT-4, and OpenChat 13 tasks. The results are as followed:

|                         |            |               |        GPT-3.5         |        GPT-4        |           |
|-------------------------|------------|---------------|:----------------------:|:-------------------:|-----------|
|                         |            |               | Persian Prompt (N-shot) | English Prompt (N-shot) |           |
| Category                | Task       | Metric        | 0      | 1      | 3      | 0      | 1      | 3      | SOTA | Random |
| Classic                 |  Sentiment  | Macro F1      | .725   | .804   | .791   | .786   | .798   | .761   | .891 | .403   |
| Classic                 |  Emotion    | Macro F1      | .492   | .513   | .537   | .562   | .568   | .589   | .699 | .117   |
| Classic                 |  NER        | Macro F1      | .578   | .472   | .589   | .617   | .620   | .625   | .988 | .041   |
| Classic                 | MT (En → Fa) | Bleu | 7.5    | 6.9    | 7.3    | 7.0    | 7.3    | 7.0    | 6.2  | -      |
| Classic                 | MT (Fa → En) | Bleu | 10.5   | 10.8   | 11.0   | 11.0   | 11.0   | 10.8   | 11.7 | -      |
| Classic                 | Reading    | F1            | .535   | .643   | .642   | .588   | .644   | .644   | .691 | -      |
| Reasoning               | Textual    | Macro F1      | .375   | .318   | .320   | .536   | .541   | .516   | .690 | .360   |
| Reasoning               | Textual    | Macro F1      | .348   | .356   | .368   | .418   | .426   | .441   | .524 | .294   |
| Reasoning               | Multi-choice QA (math & logic) | Acc | .450   | .450   | .435   | .445   | .435   | .415   | .725 | -      |
| Reasoning               | Elementary | Acc           | .535   | .435   | .565   | .590   | .520   | .545   | .740 | -      |
| Reasoning               | Math       | Math          | .209   | .375   | .503   | .194   | .348   | .408   | .564 | -      |
| Know                    | Multi-choice QA (literature) | Acc | .280 | .295   | .275   | .310   | .305   | .290   | .460 | .335   |
| Know                    | Multi-choice QA (common) | Acc | .385 | .395   | .445   | .425   | .430   | .430   | .635 | .250   |

|                         |            |               |        OpenChat         |           |
|-------------------------|------------|---------------|-------------------------|-----------|
|                         |            |               | Persian Prompt (N-shot) | English Prompt (N-shot) |
| Category                | Task       | Metric        | 0      | 1      | 3      | 0      | 1      | 3      |
| Classic                 | Sentiment  | Macro F1      | .460   | .484   | .439   | .485   | .466   | .468   |
| Classic                 | Emotion    | Macro F1      | .186   | .327   | .400   | .464   | .456   | .454   |
| Classic                 | NER        | Macro F1      | .241   | .603   | .606   | .536   | .563   | .588   |
| Classic                 | MT (En → Fa) | Bleu | 5.7    | 6.3    | 6.5    | 5.9    | 6.7    | 6.8    |
| Classic                 | MT (Fa → En) | Bleu | 9.1    | 9.1    | 9.1    | 9.1    | 9.6    | 9.6    |
| Classic                 | Reading    | F1            | .506   | .528   | .568   | .595   | .589   | .613   |
| Reasoning               | Textual    | Macro F1      | .338   | .468   | .443   | .432   | .612   | .554   |
| Reasoning               | Textual    | Macro F1      | .370   | .415   | .445   | .515   | .555   | .555   |
| Reasoning               | Multi-choice QA (math & logic) | Acc | .180   | .260   | .300   | .275   | .215   | .245   |
| Reasoning               | Elementary | Acc           | .555   | .455   | .520   | .585   | .540   | .535   |
| Reasoning               | Math       | Math          | .128   | .229   | .241   | .113   | .168   | .214   |
| Know                    | Multi-choice QA (literature) | Acc | .215 | .275   | .240   | .265   | .205   | .265   |
| Know                    | Multi-choice QA (common) | Acc | .345 | .310   | .300   | .305   | .360   | .325   |


## SOTA Models

The SOTA models used as a baseline in the paper are as follows:

| Task                     | Models                                                                                    |
|--------------------------|-------------------------------------------------------------------------------------------|
| Sentiment Classification | [mt5-small-parsinlu-sentiment-analysis](https://huggingface.co/persiannlp/mt5-small-parsinlu-sentiment-analysis) |
|                          | **[mt5-base-parsinlu-sentiment-analysis](https://huggingface.co/persiannlp/mt5-base-parsinlu-sentiment-analysis)** |
|                          | [mt5-large-parsinlu-sentiment-analysis](https://huggingface.co/persiannlp/mt5-large-parsinlu-sentiment-analysis) |
| Textual Entailment (ParsiNLU) | [wikibert-base-parsinlu-entailment](https://huggingface.co/persiannlp/wikibert-base-parsinlu-entailment) |
|                          | [mt5-base-parsinlu-snli-entailment](https://huggingface.co/persiannlp/mt5-base-parsinlu-snli-entailment) |
|                          | **[mt5-large-parsinlu-snli-entailment](https://huggingface.co/persiannlp/mt5-large-parsinlu-snli-entailment)** |
|                          | [parsbert-base-parsinlu-entailment](https://huggingface.co/persiannlp/parsbert-base-parsinlu-entailment) |
|                          | [mbert-base-parsinlu-entailment](https://huggingface.co/persiannlp/mbert-base-parsinlu-entailment) |
| Textual Entailment (ConjNLI) | **[xlm-roberta-large](https://huggingface.co/FacebookAI/xlm-roberta-large)** |
|                          | [bert-base-multilingual-cased](https://huggingface.co/google-bert/bert-base-multilingual-cased) |
|                          | [mt5-large](https://huggingface.co/google/mt5-large) |
| Named Entity Recognition | **[Bert-fa-base-uncased-ner-arman](https://huggingface.co/HooshvareLab/bert-fa-base-uncased-ner-arman)** |
| Multiple-Choice QA       | **[mt5-small-parsinlu-multiple-choice](https://huggingface.co/persiannlp/mt5-small-parsinlu-multiple-choice)** (best on literature) |
|                          | [mt5-base-parsinlu-multiple-choice](https://huggingface.co/persiannlp/mt5-base-parsinlu-multiple-choice) |
|                          | **[mt5-large-parsinlu-multiple-choice](https://huggingface.co/persiannlp/mt5-large-parsinlu-multiple-choice)** (best on math&logic) |
|                          | [mt5-small-parsinlu-arc-comqa-obqa-multiple-choice](https://huggingface.co/persiannlp/mt5-small-parsinlu-arc-comqa-obqa-multiple-choice) |
|                          | [mt5-base-parsinlu-arc-comqa-obqa-multiple-choice](https://huggingface.co/persiannlp/mt5-base-parsinlu-arc-comqa-obqa-multiple-choice) |
|                          | **[mt5-large-parsinlu-arc-comqa-obqa-multiple-choice](https://huggingface.co/persiannlp/mt5-large-parsinlu-arc-comqa-obqa-multiple-choice)** (best on com-know) |
| Reading Comprehension    | [mt5-small-parsinlu-squad-reading-comprehension](https://huggingface.co/persiannlp/mt5-small-parsinlu-squad-reading-comprehension) |
|                          | [mt5-base-parsinlu-squad-reading-comprehension](https://huggingface.co/persiannlp/mt5-base-parsinlu-squad-reading-comprehension) |
|                          | **[mt5-large-parsinlu-squad-reading-comprehension](https://huggingface.co/persiannlp/mt5-large-parsinlu-squad-reading-comprehension)** |
| Emotion Classification   | [distilbert-base-multilingual-cased-finetuned-emotion](https://huggingface.co/Toshifumi/distilbert-base-multilingual-cased-finetuned-emotion) |
|                          | [xlm-emo-t](https://huggingface.co/MilaNLProc/xlm-emo-t) |
|                          | **[ParsBERT-and-Imbalanced-Data-Handling-Approaches](https://github.com/AmirAbaskohi/Persian-Emotion-Detection-using-ParsBERT-and-Imbalanced-Data-Handling-Approaches)** |
|                          | [bert-base-multilingual-cased-finetuned-emotion](https://huggingface.co/Toshifumi/bert-base-multilingual-cased-finetuned-emotion) |
| Translation              | [mt5-small-parsinlu-opus-translation_fa_en](https://huggingface.co/persiannlp/mt5-small-parsinlu-opus-translation_fa_en) |
|                          | [mt5-base-parsinlu-opus-translation_fa_en](https://huggingface.co/persiannlp/mt5-base-parsinlu-opus-translation_fa_en) |
|                          | **[mt5-large-parsinlu-opus-translation_fa_en](https://huggingface.co/persiannlp/mt5-large-parsinlu-opus-translation_fa_en)** (Persian to English) |
|                          | [mt5-small-parsinlu-translation_en_fa](https://huggingface.co/persiannlp/mt5-small-parsinlu-translation_en_fa) |
|                          | [mt5-base-parsinlu-translation_en_fa](https://huggingface.co/persiannlp/mt5-base-parsinlu-translation_en_fa) |
|                          | **[mt5-large-parsinlu-translation_en_fa](https://huggingface.co/persiannlp/mt5-large-parsinlu-translation_en_fa)** (English to Persian) |

## How to run?

For each experiment, there as notebook in the paper where you can follow them step by step. Remember to replace you `API-KEY` for the models. In addition, for `ChatGPT` experiments, as mentioned in the paper we used two different versions. For GPT-3.5 we used `gpt-3.5-turbo-0125` and for GPT-4 we used `gpt-4-0125-preview`.

## Citation

```
@misc{abaskohi2024benchmarking,
      title={Benchmarking Large Language Models for Persian: A Preliminary Study Focusing on ChatGPT}, 
      author={Amirhossein Abaskohi and Sara Baruni and Mostafa Masoudi and Nesa Abbasi and Mohammad Hadi Babalou and Ali Edalat and Sepehr Kamahi and Samin Mahdizadeh Sani and Nikoo Naghavian and Danial Namazifard and Pouya Sadeghi and Yadollah Yaghoobzadeh},
      year={2024},
      eprint={2404.02403},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
