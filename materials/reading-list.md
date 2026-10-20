# Reading list: AI for content analysis and qualitative coding

These are the studies on the "What the studies found" slide in Part 3, roughly ordered from "it works" to "be careful". Most used older models (GPT-3 to GPT-4). The models have improved since, but you still need to validate.

## Deductive coding with a codebook

- **Xiao, Z., Yuan, X., Liao, Q. V., Abdelghani, R., & Oudeyer, P.-Y. (2023).** Supporting qualitative analysis with large language models: Combining codebook with GPT-3 for deductive coding. *Companion Proceedings of the 28th International Conference on Intelligent User Interfaces (IUI '23)*. <https://arxiv.org/abs/2304.10548>
  An expert-drafted codebook plus GPT-3 reached fair to substantial agreement with expert coders.

- **Chew, R., Bollenbacher, J., Wenger, M., Speer, J., & Kim, A. (2023).** LLM-assisted content analysis: Using large language models to support deductive coding. *arXiv:2306.14924*. <https://arxiv.org/abs/2306.14924>
  GPT-3.5 often matched human coders. The authors also show how to spot codes where the model is effectively guessing.

## Annotation at scale

- **Gilardi, F., Alizadeh, M., & Kubli, M. (2023).** ChatGPT outperforms crowd workers for text-annotation tasks. *PNAS, 120*(30), e2305016120. <https://doi.org/10.1073/pnas.2305016120>
  Across 6,183 tweets and news articles, zero-shot ChatGPT beat crowd workers on relevance, stance, topic and frame detection.

- **Pangakis, N., Wolken, S., & Fasching, N. (2023).** Automated annotation with generative AI requires validation. *arXiv:2306.00176*. <https://arxiv.org/abs/2306.00176>
  GPT-4 replicated 27 annotation tasks from published social-science studies. Performance varied a lot by task and dataset, so the authors argue for validating against human labels every time.

## Inductive analysis

- **De Paoli, S. (2024).** Performing an inductive thematic analysis of semi-structured interviews with a large language model. *Social Science Computer Review, 42*(4), 997–1019. <https://doi.org/10.1177/08944393231220483>
  GPT-3.5 recovered most of the main themes from two previously analysed interview datasets. Framed as exploratory.

## Bias

- **Ashwin, J., Chhabra, A., & Rao, V. (2025).** Using large language models for qualitative analysis can introduce serious bias. *Sociological Methods & Research*. Preprint: <https://arxiv.org/abs/2309.17147>
  On interviews with Rohingya refugees, LLM coding errors weren't random: they varied with characteristics of the people interviewed. A simpler model trained on careful human codes did better.
