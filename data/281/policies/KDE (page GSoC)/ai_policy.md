## Guidance for GSoC Contributors using AI tooling in GSoC 2026 

**It is vital that you read through the GSoC organization’s documentation paying very close attention to their guidance on whether any AI tooling is allowed in their community. We have asked the orgs to make it very clear what their expectations are for GSoC participants.** 

Each organization has their own opinion on when/if using AI tooling is appropriate. 

**Some organizations do not allow any use of AI tooling, including in the writing of proposals. Others won’t allow any code generated from LLMs into their code base.** 

_Below are some of the things to consider when using AI tooling in general. Again, this guidance isn’t comprehensive for each org - you must read through each org’s GSoC guidance to understand what they will/won’t accept._ 

## Mentor Advice on when to use AI tools 

#### **1. Always Validate and Fully Understand the Code** 

This is the most critical and frequently repeated piece of advice. The human contributor retains **100% responsibility** for the work, which necessitates complete understanding and verification. 

- Always validate what the AI generates, and if you don't understand it or are not sure, don't use it until you are able to figure it out. 

#### **2. Use AI for Research and Learning, Not Core Logic** 

The best use case is seen as a rapid learning or information retrieval tool, rather than a code generator for the most important parts of the project. 

- Use AI tools mostly for **research** and less for code generation 

- Use AI tools for **understanding** and to explore new areas. 

#### **3. Offload Tedious or "Grunt" Work (Boilerplate, Tests, Debugging)** 

AI is encouraged for tasks that are repetitive, time-consuming, or related to fixing existing 

issues, allowing the contributor to focus their time on intellectual challenges. 

- Use to write the **boilerplate** and to refactor 

- Use for only **grunt work** , like adding all file names or changing some imports 

- Help automate some of the more **tedious parts** of their project, or to help **code up some tests** , or to help **debugging** 

- User needs to define the test scope to then use AI tools 

#### **4. Licensing Concerns** 

<mark>Always be sure to verify directly with your org if they allow AI generated code in their code base. There is a lot of discussion on this topic and each org will have their own viewpoint and potential GSoC contributors will need to follow their org's specific guidance.</mark> 

## Concerns from Mentors and GSoC orgs around AI tooling 

# **1) Hindrance to Learning and Skill Development** 

This is the most prevalent concern. Mentors worry that using AI to generate solutions prevents students from developing fundamental skills in programming, problem-solving, and thinking properly. 

# **2) Blind Trust and Lack of Understanding/Verification** 

Often contributors accept AI-generated output (code and text) blindly, without verifying its correctness, logic, or applicability. When developers **blindly use AI tools** to generate code they often don't understand what was generated. 

# **3) Low Code/Output Quality** 

AI generated code is often of **poor quality** , not following guidelines, includes bugs, is hard to maintain, or leads to extra work for mentors. 

- generally low code quality (leading to increased maintainer workload) 

- generate meaningless, long-winded prose 

# **4) Licensing and Copyright Issues** 

The legal implications of AI-generated code are a serious concern for organizations and mentors. 

- Some Org’s Commit Guidelines prohibit committing code generated via large language model because it can possibly violate OSS licenses 

- Copyright issues 

# **5) Inability to Use AI Effectively** 

Some concerns weren't about the AI itself, but the _contributor's lack of skill_ in leveraging it, especially in complex or novel project contexts. 

- Using AI effectively for coding requires skill and experience 

- Contributors sometimes won’t understand the topic of the project, therefore they do not know what to ask from the AI to get the correct information 

# **6) Environmental Impact** 

The massive amount of energy consumption used for large AI models 

### **7) AI's Limitations in Specific or Complex Tasks** 

Mentors noted that AI tools often fail when the problem is complex, unique, or deals with new technology, which is common in a learning environment like GSoC. 

- Tools are good at solving problems that have been solved often before. Our mission is teaching students to solve complex problems that have not been solved before. 

- AI is terrible at writing anything other than simple code in a limited context 

- The projects can use tech that AI doesn't know 


