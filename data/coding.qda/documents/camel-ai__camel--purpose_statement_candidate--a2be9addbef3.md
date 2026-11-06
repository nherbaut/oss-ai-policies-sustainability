[![Banner](docs/images/banner.png)](https://www.camel-ai.org/)

[![Documentation](https://img.shields.io/badge/Documentation-EB3ECC)](https://camel-ai.github.io/camel/index) [![Discord](https://img.shields.io/discord/1082486657678311454?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb)](https://discord.camel-ai.org/) [![X](https://img.shields.io/twitter/follow/CamelAIOrg?style=social)](https://x.com/CamelAIOrg) [![Reddit](https://img.shields.io/reddit/subreddit-subscribers/CamelAI?style=plastic&logo=reddit&label=r%2FCAMEL&labelColor=white)](https://www.reddit.com/r/CamelAI/) [![Wechat](https://img.shields.io/badge/WeChat-CamelAIOrg-brightgreen?logo=wechat&logoColor=white)](https://ghli.org/camel/wechat.png) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-CAMEL--AI-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/camel-ai) [![Star](https://img.shields.io/github/stars/camel-ai/camel?label=stars&logo=github&color=brightgreen)](https://github.com/camel-ai/camel/stargazers) [![Package License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/camel-ai/camel/blob/master/licenses/LICENSE) [![PyPI Download](https://img.shields.io/pypi/dm/camel-ai)](https://pypi.org/project/camel-ai) [![](https://img.shields.io/badge/Join%20Us-yellow?style=plastic)](https://eigent-ai.notion.site/eigent-ai-careers)

[![camel-ai/camel \| Trendshift](https://trendshift.io/api/badge/repositories/649)](https://trendshift.io/repositories/649)

[English](README.md) \| [简体中文](README.zh.md) \| [日本語](README.ja.md)

------------------------------------------------------------------------

#### 

[Community](https://github.com/camel-ai/camel#community) \| [Installation](https://github.com/camel-ai/camel#installation) \| [Examples](https://github.com/camel-ai/camel/tree/HEAD/examples) \| [Paper](https://arxiv.org/abs/2303.17760) \| [Citation](https://github.com/camel-ai/camel#citation) \| [Contributing](https://github.com/camel-ai/camel#contributing-to-camel-) \| [CAMEL-AI](https://www.camel-ai.org/)

🐫 CAMEL is an open-source community dedicated to finding the scaling laws of agents. We believe that studying these agents on a large scale offers valuable insights into their behaviors, capabilities, and potential risks. To facilitate research in this field, we implement and support various types of agents, tasks, prompts, models, and simulated environments.

Join us ([*Discord*](https://discord.camel-ai.org/) or [*WeChat*](https://ghli.org/camel/wechat.png)) in pushing the boundaries of finding the scaling laws of agents.

🌟 Star CAMEL on GitHub and be instantly notified of new releases.

![Star](docs/images/stars.gif)

[![](https://camel-ai.github.io/camel_asset/graphics/join_us.png)](https://eigent-ai.notion.site/eigent-ai-careers)

Table of contents

- [CAMEL Framework Design Principles](#camel-framework-design-principles)
- [Why Use CAMEL for Your Research?](#why-use-camel-for-your-research)
- [What Can You Build With CAMEL?](#what-can-you-build-with-camel)
  - [Data Generation](#1-data-generation)
  - [Task Automation](#2-task-automation)
  - [World Simulation](#3-world-simulation)
- [Quick Start](#quick-start)
  - [Starting with ChatAgent](#starting-with-chatagent)
  - [Seeking Help](#seeking-help)
- [Tech Stack](#tech-stack)
- [Research](#research)
- [Synthetic Datasets](#synthetic-datasets)
- [Cookbooks (Usecases)](#cookbooks-usecases)
  - [Basic Concepts](#1-basic-concepts)
  - [Advanced Features](#2-advanced-features)
  - [Model Training & Data Generation](#3-model-training--data-generation)
  - [Multi-Agent Systems & Applications](#4-multi-agent-systems--applications)
  - [Data Processing](#5-data-processing)
- [Real-World Usecases](#real-world-usecases)
- [🧱 Built with CAMEL (Real-world Producs & Research)](#-built-with-camel-real-world-producs--research)
  - [Research Projects](#research-projects)
  - [Product Projects](#product-projects)
- [🗓️ Events](#️-events)
- [Contributing to CAMEL](#contributing-to-camel)
- [Community & Contact](#community--contact)
- [Citation](#citation)
- [Acknowledgment](#acknowledgment)
- [License](#license)

#### 

## CAMEL Framework Design Principles

### 🧬 Evolvability

The framework enables multi-agent systems to continuously evolve by generating data and interacting with environments. This evolution can be driven by reinforcement learning with verifiable rewards or supervised learning.

### 📈 Scalability

The framework is designed to support systems with millions of agents, ensuring efficient coordination, communication, and resource management at scale.

### 💾 Statefulness

Agents maintain stateful memory, enabling them to perform multi-step interactions with environments and efficiently tackle sophisticated tasks.

### 📖 Code-as-Prompt

Every line of code and comment serves as a prompt for agents. Code should be written clearly and readably, ensuring both humans and agents can interpret it effectively.

## Why Use CAMEL for Your Research?

We are a community-driven research collective comprising over 100 researchers dedicated to advancing frontier research in Multi-Agent Systems. Researchers worldwide choose CAMEL for their studies based on the following reasons.

|  |  |  |
|:---|:---|:---|
|  |  |  |
| ✅ | Large-Scale Agent System | Simulate up to 1M agents to study emergent behaviors and scaling laws in complex, multi-agent environments. |
| ✅ | Dynamic Communication | Enable real-time interactions among agents, fostering seamless collaboration for tackling intricate tasks. |
| ✅ | Stateful Memory | Equip agents with the ability to retain and leverage historical context, improving decision-making over extended interactions. |
| ✅ | Support for Multiple Benchmarks | Utilize standardized benchmarks to rigorously evaluate agent performance, ensuring reproducibility and reliable comparisons. |
| ✅ | Support for Different Agent Types | Work with a variety of agent roles, tasks, models, and environments, supporting interdisciplinary experiments and diverse research applications. |
| ✅ | Data Generation and Tool Integration | Automate the creation of large-scale, structured datasets while seamlessly integrating with multiple tools, streamlining synthetic data generation and research workflows. |

## What Can You Build With CAMEL?

### 1. Data Generation

[![CoT Data Generation](docs/images/cot.png)](https://github.com/camel-ai/camel/blob/master/camel/datagen/cot_datagen.py)

[![Self-Instruct Data Generation](docs/images/self_instruct.png)](https://github.com/camel-ai/camel/tree/master/camel/datagen/self_instruct)

[![Source2Synth Data Generation](docs/images/source2synth.png)](https://github.com/camel-ai/camel/tree/master/camel/datagen/source2synth)

[![Self-Improving Data Generation](docs/images/self_improving.png)](https://github.com/camel-ai/camel/blob/master/camel/datagen/self_improving_cot.py)

### 2. Task Automation

[![Role Playing](docs/images/role_playing.png)](https://github.com/camel-ai/camel/blob/master/camel/societies/role_playing.py)

[![Workforce](docs/images/workforce.png)](https://github.com/camel-ai/camel/tree/master/camel/societies/workforce)

[![RAG Pipeline](docs/images/rag_pipeline.png)](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_rag)

### 3. World Simulation

[![Oasis Case](docs/images/oasis_case.png)](https://github.com/camel-ai/oasis)

## Quick Start

Installing CAMEL is a breeze thanks to its availability on PyPI. Simply open your terminal and run:

``` bash
pip install camel-ai
```

### Starting with ChatAgent

This example demonstrates how to create a `ChatAgent` using the CAMEL framework and perform a search query using DuckDuckGo.

1.  **Install the tools package:**

``` bash
pip install 'camel-ai[web_tools]'
```

2.  **Set up your OpenAI API key:**

``` bash
export OPENAI_API_KEY='your_openai_api_key'
```

Alternatively, use a `.env` file:

``` bash
cp .env.example .env
# then edit .env and add your keys
```

3.  **Run the following Python code:**

``` python
from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType
from camel.agents import ChatAgent
from camel.toolkits import SearchToolkit

model = ModelFactory.create(
  model_platform=ModelPlatformType.OPENAI,
  model_type=ModelType.GPT_4O,
  model_config_dict={"temperature": 0.0},
)

search_tool = SearchToolkit().search_duckduckgo

agent = ChatAgent(model=model, tools=[search_tool])

response_1 = agent.step("What is CAMEL-AI?")
print(response_1.msgs[0].content)
# CAMEL-AI is the first LLM (Large Language Model) multi-agent framework
# and an open-source community focused on finding the scaling laws of agents.
# ...

response_2 = agent.step("What is the Github link to CAMEL framework?")
print(response_2.msgs[0].content)
# The GitHub link to the CAMEL framework is
# [https://github.com/camel-ai/camel](https://github.com/camel-ai/camel).
```

4.  **(Optional) Enable model request/response logs:**

``` bash
export CAMEL_MODEL_LOG_ENABLED=true
export CAMEL_MODEL_LOG_MODEL_CONFIG_ENABLED=true
export CAMEL_LOG_DIR=camel_logs
```

- `CAMEL_MODEL_LOG_ENABLED`: Enables request/response JSON logs.
- `CAMEL_MODEL_LOG_MODEL_CONFIG_ENABLED`: Controls whether `model_config_dict` is logged under `request.model_config_dict`. When unset, it defaults to the same value as `CAMEL_MODEL_LOG_ENABLED`.
- `CAMEL_LOG_DIR`: Directory for generated log files (default: `camel_logs`).
- Logs are written as UTF-8 JSON with multilingual text preserved (for example Chinese, Japanese, Arabic) without Unicode escape noise.

For more detailed instructions and additional configuration options, check out the [installation section](https://github.com/camel-ai/camel/blob/master/docs/get_started/installation.md).

After running, you can explore our CAMEL Tech Stack and Cookbooks at [docs.camel-ai.org](https://docs.camel-ai.org) to build powerful multi-agent systems.

We provide a [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1AzP33O8rnMW__7ocWJhVBXjKziJXPtim?usp=sharing) demo showcasing a conversation between two ChatGPT agents playing roles as a python programmer and a stock trader collaborating on developing a trading bot for stock market.

Explore different types of agents, their roles, and their applications.

- **[Creating Your First Agent](https://docs.camel-ai.org/cookbooks/basic_concepts/create_your_first_agent)**
- **[Creating Your First Agent Society](https://docs.camel-ai.org/cookbooks/basic_concepts/create_your_first_agents_society)**
- **[Critic Agents](https://docs.camel-ai.org/cookbooks/advanced_features/critic_agents_and_tree_search)**

### Seeking Help

Please reach out to us on [CAMEL discord](https://discord.camel-ai.org/) if you encounter any issue set up CAMEL.

## Tech Stack

[![TechStack](https://camel-ai.github.io/camel_asset/graphics/techstack.png)](https://docs.camel-ai.org)

### Key Modules

Core components and utilities to build, operate, and enhance CAMEL-AI agents and societies.

| Module | Description |
|:---|:---|
| **[Agents](https://docs.camel-ai.org/key_modules/agents)** | Core agent architectures and behaviors for autonomous operation. |
| **[Agent Societies](https://docs.camel-ai.org/key_modules/society)** | Components for building and managing multi-agent systems and collaboration. |
| **[Data Generation](https://docs.camel-ai.org/key_modules/datagen)** | Tools and methods for synthetic data creation and augmentation. |
| **[Models](https://docs.camel-ai.org/key_modules/models)** | Model architectures and customization options for agent intelligence. |
| **[Tools](https://docs.camel-ai.org/key_modules/tools)** | Tools integration for specialized agent tasks. |
| **[Memory](https://docs.camel-ai.org/key_modules/memory)** | Memory storage and retrieval mechanisms for agent state management. |
| **[Storage](https://docs.camel-ai.org/key_modules/storages)** | Persistent storage solutions for agent data and states. |
| **[Benchmarks](https://github.com/camel-ai/camel/tree/master/camel/benchmarks)** | Performance evaluation and testing frameworks. |
| **[Interpreters](https://docs.camel-ai.org/key_modules/interpreters)** | Code and command interpretation capabilities. |
| **[Data Loaders](https://docs.camel-ai.org/key_modules/loaders)** | Data ingestion and preprocessing tools. |
| **[Retrievers](https://docs.camel-ai.org/key_modules/retrievers)** | Knowledge retrieval and RAG components. |
| **[Runtime](https://github.com/camel-ai/camel/tree/master/camel/runtime)** | Execution environment and process management. |
| **[Human-in-the-Loop](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_human_in_loop_and_tool_approval)** | Interactive components for human oversight and intervention. |

------------------------------------------------------------------------

## Research

We believe that studying these agents on a large scale offers valuable insights into their behaviors, capabilities, and potential risks.

**Explore our research projects:**

[![OWL](docs/images/owl.png)](https://github.com/camel-ai/owl)

[![OASIS](docs/images/oasis.png)](https://oasis.camel-ai.org/)

[![CRAB](docs/images/crab.png)](https://crab.camel-ai.org/)

[![Loong](docs/images/loong.png)](https://github.com/camel-ai/loong)

[![Agent Trust](docs/images/agent_trust.png)](https://agent-trust.camel-ai.org/)

[![Emos](docs/images/emos.png)](https://emos-project.github.io/)

> ### Research with US
>
> We warmly invite you to use CAMEL for your impactful research.
>
> Rigorous research takes time and resources. We are a community-driven research collective with 100+ researchers exploring the frontier research of Multi-agent Systems. Join our ongoing projects or test new ideas with us, [reach out via email](mailto:camel-ai@eigent.ai) for more information.
>
> ![Partners](docs/images/partners.png)

## Synthetic Datasets

### 1. Utilize Various LLMs as Backends

For more details, please see our [`Models Documentation`](https://docs.camel-ai.org/key_modules/models#).

> **Data (Hosted on Hugging Face)**

| Dataset | Chat format | Instruction format | Chat format (translated) |
|----|----|----|----|
| **AI Society** | [Chat format](https://huggingface.co/datasets/camel-ai/ai_society/blob/main/ai_society_chat.tar.gz) | [Instruction format](https://huggingface.co/datasets/camel-ai/ai_society/blob/main/ai_society_instructions.json) | [Chat format (translated)](https://huggingface.co/datasets/camel-ai/ai_society_translated) |
| **Code** | [Chat format](https://huggingface.co/datasets/camel-ai/code/blob/main/code_chat.tar.gz) | [Instruction format](https://huggingface.co/datasets/camel-ai/code/blob/main/code_instructions.json) | x |
| **Math** | [Chat format](https://huggingface.co/datasets/camel-ai/math) | x | x |
| **Physics** | [Chat format](https://huggingface.co/datasets/camel-ai/physics) | x | x |
| **Chemistry** | [Chat format](https://huggingface.co/datasets/camel-ai/chemistry) | x | x |
| **Biology** | [Chat format](https://huggingface.co/datasets/camel-ai/biology) | x | x |

### 2. Visualizations of Instructions and Tasks

| Dataset | Instructions | Tasks |
|----|----|----|
| **AI Society** | [Instructions](https://atlas.nomic.ai/map/3a559a06-87d0-4476-a879-962656242452/db961915-b254-48e8-8e5c-917f827b74c6) | [Tasks](https://atlas.nomic.ai/map/cb96f41b-a6fd-4fe4-ac40-08e101714483/ae06156c-a572-46e9-8345-ebe18586d02b) |
| **Code** | [Instructions](https://atlas.nomic.ai/map/902d6ccb-0bbb-4294-83a8-1c7d2dae03c8/ace2e146-e49f-41db-a1f4-25a2c4be2457) | [Tasks](https://atlas.nomic.ai/map/efc38617-9180-490a-8630-43a05b35d22d/2576addf-a133-45d5-89a9-6b067b6652dd) |
| **Misalignment** | [Instructions](https://atlas.nomic.ai/map/5c491035-a26e-4a05-9593-82ffb2c3ab40/2bd98896-894e-4807-9ed8-a203ccb14d5e) | [Tasks](https://atlas.nomic.ai/map/abc357dd-9c04-4913-9541-63e259d7ac1f/825139a4-af66-427c-9d0e-f36b5492ab3f) |

## Cookbooks (Usecases)

Practical guides and tutorials for implementing specific functionalities in CAMEL-AI agents and societies.

### 1. Basic Concepts

| Cookbook | Description |
|:---|:---|
| **[Creating Your First Agent](https://docs.camel-ai.org/cookbooks/basic_concepts/create_your_first_agent)** | A step-by-step guide to building your first agent. |
| **[Creating Your First Agent Society](https://docs.camel-ai.org/cookbooks/basic_concepts/create_your_first_agents_society)** | Learn to build a collaborative society of agents. |
| **[Message Cookbook](https://docs.camel-ai.org/cookbooks/basic_concepts/agents_message)** | Best practices for message handling in agents. |

### 2. Advanced Features

| Cookbook | Description |
|:---|:---|
| **[Tools Cookbook](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_tools)** | Integrating tools for enhanced functionality. |
| **[Memory Cookbook](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_memory)** | Implementing memory systems in agents. |
| **[RAG Cookbook](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_rag)** | Recipes for Retrieval-Augmented Generation. |
| **[Graph RAG Cookbook](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_graph_rag)** | Leveraging knowledge graphs with RAG. |
| **[Track CAMEL Agents with AgentOps](https://docs.camel-ai.org/cookbooks/advanced_features/agents_tracking)** | Tools for tracking and managing agents in operations. |

### 3. Model Training & Data Generation

| Cookbook | Description |
|:---|:---|
| **[Data Generation with CAMEL and Finetuning with Unsloth](https://docs.camel-ai.org/cookbooks/data_generation/sft_data_generation_and_unsloth_finetuning_Qwen2_5_7B)** | Learn how to generate data with CAMEL and fine-tune models effectively with Unsloth. |
| **[Data Gen with Real Function Calls and Hermes Format](https://docs.camel-ai.org/cookbooks/data_generation/data_gen_with_real_function_calls_and_hermes_format)** | Explore how to generate data with real function calls and the Hermes format. |
| **[CoT Data Generation and Upload Data to Huggingface](https://docs.camel-ai.org/cookbooks/data_generation/distill_math_reasoning_data_from_deepseek_r1)** | Uncover how to generate CoT data with CAMEL and seamlessly upload it to Huggingface. |
| **[CoT Data Generation and SFT Qwen with Unsolth](https://docs.camel-ai.org/cookbooks/data_generation/cot_data_gen_sft_qwen_unsolth_upload_huggingface)** | Discover how to generate CoT data using CAMEL and SFT Qwen with Unsolth, and seamlessly upload your data and model to Huggingface. |

### 4. Multi-Agent Systems & Applications

| Cookbook | Description |
|:---|:---|
| **[Role-Playing Scraper for Report & Knowledge Graph Generation](https://docs.camel-ai.org/cookbooks/applications/roleplaying_scraper)** | Create role-playing agents for data scraping and reporting. |
| **[Create A Hackathon Judge Committee with Workforce](https://docs.camel-ai.org/cookbooks/multi_agent_society/workforce_judge_committee)** | Building a team of agents for collaborative judging. |
| **[Dynamic Knowledge Graph Role-Playing: Multi-Agent System with dynamic, temporally-aware knowledge graphs](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_dkg)** | Builds dynamic, temporally-aware knowledge graphs for financial applications using a multi-agent system. It processes financial reports, news articles, and research papers to help traders analyze data, identify relationships, and uncover market insights. The system also utilizes diverse and optional element node deduplication techniques to ensure data integrity and optimize graph structure for financial decision-making. |
| **[Customer Service Discord Bot with Agentic RAG](https://docs.camel-ai.org/cookbooks/applications/customer_service_Discord_bot_using_SambaNova_with_agentic_RAG)** | Learn how to build a robust customer service bot for Discord using Agentic RAG. |
| **[Customer Service Discord Bot with Local Model](https://docs.camel-ai.org/cookbooks/applications/customer_service_Discord_bot_using_local_model_with_agentic_RAG)** | Learn how to build a robust customer service bot for Discord using Agentic RAG which supports local deployment. |

### 5. Data Processing

| Cookbook | Description |
|:---|:---|
| **[Video Analysis](https://docs.camel-ai.org/cookbooks/data_processing/video_analysis)** | Techniques for agents in video data analysis. |
| **[3 Ways to Ingest Data from Websites with Firecrawl](https://docs.camel-ai.org/cookbooks/data_processing/ingest_data_from_websites_with_Firecrawl)** | Explore three methods for extracting and processing data from websites using Firecrawl. |
| **[Create AI Agents that work with your PDFs](https://docs.camel-ai.org/cookbooks/data_processing/agent_with_chunkr_for_pdf_parsing)** | Learn how to create AI agents that work with your PDFs using Chunkr and Mistral AI. |

## Real-World Usecases

Real-world usecases demonstrating how CAMEL’s multi-agent framework enables real business value across infrastructure automation, productivity workflows, retrieval-augmented conversations, intelligent document/video analysis, and collaborative research.

### 1 Infrastructure Automation

| Usecase | Description |
|:---|:---|
| **[ACI MCP](https://github.com/camel-ai/camel/tree/master/examples/usecases/aci_mcp)** | Real-world usecases demonstrating how CAMEL’s multi-agent framework enables real business value across infrastructure automation, productivity workflows, retrieval-augmented conversations, intelligent document/video analysis, and collaborative research. |
| **[Cloudflare MCP CAMEL](https://github.com/camel-ai/camel/tree/master/examples/usecases/cloudfare_mcp_camel)** | Intelligent agents manage Cloudflare resources dynamically, enabling scalable and efficient cloud security and performance tuning. |

### 2 Productivity & Business Workflows

| Usecase | Description |
|:---|:---|
| **[Airbnb MCP](https://github.com/camel-ai/camel/tree/master/examples/usecases/airbnb_mcp)** | Coordinate agents to optimize and manage Airbnb listings and host operations. |
| **[PPTX Toolkit Usecase](https://github.com/camel-ai/camel/tree/master/examples/usecases/pptx_toolkit_usecase)** | Analyze PowerPoint documents and extract structured insights through multi-agent collaboration. |

### 3 Retrieval-Augmented Multi-Agent Chat

| Usecase | Description |
|:---|:---|
| **[Chat with GitHub](https://github.com/camel-ai/camel/tree/master/examples/usecases/chat_with_github)** | Query and understand GitHub codebases through CAMEL agents leveraging RAG-style workflows, accelerating developer onboarding and codebase navigation. |
| **[Chat with YouTube](https://github.com/camel-ai/camel/tree/master/examples/usecases/chat_with_youtube)** | Conversational agents extract and summarize video transcripts, enabling faster content understanding and repurposing. |

### 4 Video & Document Intelligence

| Usecase | Description |
|:---|:---|
| **[YouTube OCR](https://github.com/camel-ai/camel/tree/master/examples/usecases/youtube_ocr)** | Agents perform OCR on video screenshots to summarize visual content, supporting media monitoring and compliance. |
| **[Mistral OCR](https://github.com/camel-ai/camel/tree/master/examples/usecases/mistral_OCR)** | CAMEL agents use OCR with Mistral to analyze documents, reducing manual effort in document understanding workflows. |

### 5 Research & Collaboration

| Usecase | Description |
|:---|:---|
| **[Multi-Agent Research Assistant](https://github.com/camel-ai/camel/tree/master/examples/usecases/multi_agent_research_assistant)** | Simulates a team of research agents collaborating on literature review, improving efficiency in exploratory analysis and reporting. |

## 🧱 Built with CAMEL (Real-world Producs & Research)

[![Built with CAMEL](docs/images/built_with_CAMEL.png)](https://www.camel-ai.org/)

### Research Projects

| Name | Description |
|:---|:---|
| **[ChatDev](https://github.com/OpenBMB/ChatDev/tree/main/camel)** | Communicative Agents for software Development |
| **[Paper2Poster](https://github.com/Paper2Poster/Paper2Poster)** | Multimodal poster automation from scientific papers |
| **[Paper2Video](https://github.com/showlab/Paper2Video)** | Automatic video generation from scientific papers |

### Product Projects

| Name | Description |
|:---|:---|
| **[Eigent](https://www.eigent.ai/)** | The World First Multi-agent Workforce |

## 🗓️ Events

We are actively involved in community events including:

- 🎙️ **Community Meetings** — Weekly virtual syncs with the CAMEL team
- 🏆 **Competitions** — Hackathons, Bounty Tasks and coding challenges hosted by CAMEL
- 🤝 **Volunteer Activities** — Contributions, documentation drives, and mentorship
- 🌍 **Ambassador Programs** — Represent CAMEL in your university or local tech groups

> Want to host or participate in a CAMEL event? Join our [Discord](https://discord.com/invite/CNcNpquyDc) or want to be part of [Ambassador Program](https://www.camel-ai.org/ambassador).

## Contributing to CAMEL

> For those who'd like to contribute code, we appreciate your interest in contributing to our open-source initiative. Please take a moment to review our [contributing guidelines](https://github.com/camel-ai/camel/blob/master/CONTRIBUTING.md) to get started on a smooth collaboration journey.🚀
>
> We also welcome you to help CAMEL grow by sharing it on social media, at events, or during conferences. Your support makes a big difference!

## Contributors

[![](https://contrib.rocks/image?repo=camel-ai/camel)](https://github.com/camel-ai/camel/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks).

## Acknowledgment

Special thanks to [Nomic AI](https://home.nomic.ai/) for giving us extended access to their data set exploration tool (Atlas).

We would also like to thank Haya Hammoud for designing the initial logo of our project.

We implemented amazing research ideas from other works for you to build, compare and customize your agents. If you use any of these modules, please kindly cite the original works: - `TaskCreationAgent` and `TaskPrioritizationAgent` from *Nakajima et al.*: [Task-Driven Autonomous Agent](https://yoheinakajima.com/task-driven-autonomous-agent-utilizing-gpt-4-pinecone-and-langchain-for-diverse-applications/).

- `PersonaHub` from *Tao Ge et al.*: [Scaling Synthetic Data Creation with 1,000,000,000 Personas](https://arxiv.org/pdf/2406.20094). \[[Example](https://github.com/camel-ai/camel/blob/master/examples/personas/personas_generation.py)\]

- `Self-Instruct` from *Yizhong Wang et al.*: [SELF-INSTRUCT: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/pdf/2212.10560). \[[Example](https://github.com/camel-ai/camel/blob/master/examples/datagen/self_instruct/self_instruct.py)\]

## License

The source code is licensed under Apache 2.0.

## Citation

    @inproceedings{li2023camel,
      title={CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society},
      author={Li, Guohao and Hammoud, Hasan Abed Al Kader and Itani, Hani and Khizbullin, Dmitrii and Ghanem, Bernard},
      booktitle={Thirty-seventh Conference on Neural Information Processing Systems},
      year={2023}
    }

Here is an example of how to cite our work:

    We use the CAMEL framework \cite{li2023camel} to develop the agents used in our experiments.

## Community & Contact

For more information please contact camel-ai@eigent.ai

- **GitHub Issues:** Report bugs, request features, and track development. [Submit an issue](https://github.com/camel-ai/camel/issues)

- **Discord:** Get real-time support, chat with the community, and stay updated. [Join us](https://discord.camel-ai.org/)

- **X (Twitter):** Follow for updates, AI insights, and key announcements. [Follow us](https://x.com/CamelAIOrg)

- **Ambassador Project:** Advocate for CAMEL-AI, host events, and contribute content. [Learn more](https://www.camel-ai.org/community)

- **WeChat Community:** Scan the QR code below to join our WeChat community.

  ![WeChat QR Code](misc/wechat.jpeg)
