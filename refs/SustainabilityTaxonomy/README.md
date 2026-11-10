This repository contains **SUPPLMENTARY materials** for the manuscript- **Towards a Taxonomy of Sustainability Requirements for Software Design**. Submitted in 10th GREENS Workshop.


**Categories & Metrics document**- It provides the identified list of categories and metrics, along with references.

**Sustainability Category Correlations**- It provides the identified correlations (Positive and Negative) among different sustainability categories.

**Research papers surveyed for taxonomy document**- It lists out 105 papers used for building the taxonomy and answering the research questions-

****RQ-1 How are sustainability requirements defined and characterized across different domains (e.g., stand-alone software, cloud computing, smart systems, healthcare)?**

**RQ-2 What are the most frequently identified categories of sustainability requirements for different dimensions in the existing state of the art (e.g., inclusivity for social dimension, energy consumption for environmental dimension)?**

**RQ-3 What commonalities and divergences of sustainability requirements across different domains can be identified and recorded within a generic comprehensive taxonomy?****

**Taxonomy_created.csv**- The taxonomy file.

**The following structured prompt was used in taxonomy building:**

"""You are an AI assistant specialized in requirements analysis. You will receive a research document related to sustainability requirements for software or information systems. Your task is to analyze the text carefully and identify all statements that explicitly or implicitly represent sustainability requirements (SRs). Follow these guidelines strictly:

1. Base your analysis only on the information contained in the provided document. Do not use external knowledge or generate any content not supported by the given context.
   
2. If no sustainability requirements are clearly indicated, respond that none are explicitly mentioned rather than making assumptions.
   
3. For each identified SR, extract and present the following details:

        a. A concise description of the sustainability requirement as expressed or implied in the text,
        b. The associated sustainability dimension (Environmental, Social, Economic, Technical, or Individual),
        c. Any contextual information such as system type, domain, or purpose if specified.

4. Return the final output as a structured list or table format. Each entry should directly reference phrases or sentences from the input text that justify the extracted requirement.

Do not infer or hallucinate requirements beyond the content explicitly or implicitly supported by the given document.
"""

**The following structured prompt was used to guide the LLM in generating the correlation matrix:**


"""You are an AI assistant who specializes in analyzing relationships among sustainability categories. You will receive a data set that contains multiple sustainability dimensions (Environmental, Social, Economic, Technical, and Individual), each with a list of categories and their definitions. Your task is to infer possible correlations among these categories by analyzing the meaning and implications of each category. Follow these guidelines:


1. Your reasoning should consider the definitions and descriptions given in the dataset.
   
2. Identify correlations that reflect conceptual, causal, or influence-based relationships between categories (e.g., how improving one category might affect another).
   
3. Represent the correlations in a structured matrix format, where rows and columns correspond to categories, and each cell indicates the type of correlation (Positive, Negative, Neutral, or No Correlation).   

4. {Provide a brief justification (one or two sentences) for each identified correlation based on contextual definitions.
   
5. If a correlation cannot be reasonably established from the provided context, mark it as neutral instead of speculating.

Your final output should be a correlation matrix followed by a concise explanation of the reasoning behind the identified relationships. Avoid hallucinating or adding information not contained in the data set.
"""
