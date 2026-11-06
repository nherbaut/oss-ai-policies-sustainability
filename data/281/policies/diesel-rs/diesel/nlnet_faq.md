> Source: https://nlnet.nl/foundation/policies/generativeAI/faq
> Retrieved (UTC): 2026-11-05T21:55:29+00:00
> Publisher: NLnet Foundation. Related to Diesel through its reference to NLnet’s funding policy.
> Companion document: [NLnet GenAI policy, version 2.0](other_policy.md).

# FAQ about the GenAI policy

This FAQ addresses questions about the [Policy on the use of Generative Artificial Intelligence for NLnet-funded projects](https://nlnet.nl/foundation/policies/generativeAI/2.0/). They've been grouped under headers for quick reference.

## Topics

- [Transitional arrangment for NGI Zero programmes](https://nlnet.nl/foundation/policies/generativeAI/faq#transition)
- [Application process](https://nlnet.nl/foundation/policies/generativeAI/faq#application)
- [Pre-existing LLM-generated code on your codebase](https://nlnet.nl/foundation/policies/generativeAI/faq#pre-existing)
- [Project development](https://nlnet.nl/foundation/policies/generativeAI/faq#project-development)
- [Disclosure](https://nlnet.nl/foundation/policies/generativeAI/faq#disclosure)
- [Creation of AI-related projects](https://nlnet.nl/foundation/policies/generativeAI/faq#ai-related)

## FAQs

### Transitional arrangment for NGI and NGI Zero programmes

There is a transitional arrangement for applicants and beneficiaries from programmes which are in a concluding phase (notably [NGI Zero Commons Fund](https://nlnet.nl/commonsfund/), [NGI Taler](https://nlnet.nl/taler/) and [Fediversity](https://nlnet.nl/fediversity/)). Proposals still under evaluation for those funds will be treated as per the previous ([v1.1](https://nlnet.nl/foundation/policies/generativeAI/1.1/)) version of the GenAI policy out of clemency, but may choose to voluntarily follow the new revised policy in the light of future applications.

### Application process

- I've submitted a proposal with the aid of GenAI before the new policy came into force on October 20<sup>th</sup> 2026. Do I need to write a new proposal without GenAI?

  No. We have made a one time exception allowing the use of GenAI for writing the proposal for applications submitted before October 21, 2026. If your project otherwise adheres to the policy, there is no need to resubmit.

- I have submitted a proposal before October 21<sup>st</sup> 2026 that includes use of LLMs in project development which is not in accordance with your policy. Do I need to resubmit?

  Yes. Applications that propose forms of project development which are not in accordance with GenAI policy 2.0, need to be resubmitted to fit the policy.

- How do I resubmit my proposal?

  Simply fill out the application form again. It is appreciated if you mention the fact it's a resubmission in the application and provide the project ID of the old application. (This makes it easier for us to deduplicate, and will speed up processing)

- The policy requires to disclose pre-existing LLM-generated code in my codebase. How do I disclose that in the application form?

  The application form has a section 'AI disclosure' at the bottom. There you can provide a high-level overview of how GenAI was used in your project. Just write a broad, general description of how GenAI was used.

- I worry that you'll think I wrote my application with AI because I use similar style, like using bullet points.

  Don't worry too much; LLMs generating text as bullet points lists is a result of how commonly this type of formatting occurs in training materials.

- Can I use an LLM for translation?

  No. It is okay to use regular machine translation, but not LLMs. We do understand there can be a language barrier, English is not the native language for most of our staff either. But we don't care about spelling or grammar, only about your ideas.

- Is my project eligible if it builds on open-source components/libraries that are made using AI tools?

  This is a good question with a multi-faceted answer:

  - You can use existing, mature components/libraries that have been produced and vetted by others.
  - You can not generate dependencies yourself to create an articifical boundery between your project and AI generated components.
  - If an AI recommends a certain library, make sure you do your own vetting before implementing.

### Pre-existing LLM-generated code on your codebase

- Will my proposal be disqualified if my codebase contains pre-existing LLM-generated code?

  No. But you do need to disclose pre-existing LLM-generated code in the application form. There is an 'AI disclosure' section in the form.

- Our project extends an existing open source codebase. We cannot independently guarantee that third-party contributors never used generative AI when producing the existing code ...

  *(question continues) Could you confirm whether extending or forking an existing codebase is permissible where we are not aware of AI-generated contributions, but cannot guarantee their complete absence?*  
  Answer: Good question. Yes this is permissible. First, because having pre-existing LLM-generated code in the codebase, does not render the project ineligible. And second, we understand it is not always possible to know whether or not there is LLM-generated code in the codebase, so we understand you can not always guarantee it.  
  *(follow-up question) What checks or disclosures would you expect in this situation?*  
  Answer: Just write it down as you have done here: stating that you don't know and why you don't know.

- If significant AI-generated contributions are known to exist in the pre-existing codebase, would this require disclosure and assessment, or would it make the proposed project ineligible?

  It would not render the project ineligible, but it would require disclosure. There is a 'AI disclosure' section in the application form.

### Project development

- AI coding assistants write most of the code and/or documentation in my project, is this compliant with the GenAI policy?

  No. Use of AI is only allowed in a read-only manner. The policy requires you to write your own code and documentation.

- I am using \[brand LLM redacted\] to code but the idea, concept, and design and everything about the project except the code is from me. Does that make my project unfundable?

  Unfortunately it does. It is not allowed to use GenAI for producing artefacts of any kind, including code, design, and documentation. You can only use GenAI in a read-only manner.

- There is an accessibility exception for AI usage in the application process, could a similar exception also be applied to project development?

  Yes, the [accessibility exception](https://nlnet.nl/foundation/policies/generativeAI/2.0/#accessibility) described in the policy is also valid for project development. For instance, if a motor impairment makes typing difficult, it is allowed to use AI as an assisstive technology. Needless to say, other uses of AI that are restricted by the policy, still remain restricted. And all use of GenAI must be disclosed.

- Is it acceptable that some parts of the project that are not in the scope of the grant can be made using AI tools and integrated later in the project?

  Technically we cannot stop you from doing that, but it is not the intent of the policy. You'll need to disclose such intentions in your proposal. We will then weigh it as part of the evaluation.

- Analytical support: Would using an LLM to explain existing code, discuss technical approaches, or identify potential bugs and security issues fall within permitted “read-only usage”...

  *(question continues:) , provided that developers independently assess the output and implement any changes themselves?*  
  Answer: You can have LLM's look at your code and point out flaws. You have to then write the code to fix it up yourself. Asking an LLM what to do next is not allowed, you should yourself build a working solution. Only then can you have it reviewed.

- Could you explain why AI-assisted code generation is prohibited?

  For some background on our reasoning, see the [news item](https://nlnet.nl/news/2026/20261020-AI-policy.html) we published at the time of the release of the policy.

- Is there any flexibility for an applicant who fully discloses extensive use of AI coding tools?

  There is a [transitonal arrangment](https://nlnet.nl/foundation/policies/generativeAI/faq#transition) for applicants and beneficiaries within NGI and NGI Zero programmes. For other programmes there a no exceptions.

- I want to continue using GenAI for project development. Can you make an exception for me?

  There are two general exceptions: for projects within NGI Zero programmes, because these were already in flight during the publication of the version 2.0 of the policy. And an accessibility exception described in the policy. If you do not fall within either of those exceptions, the answer is no.

- We use AI as a coding partner in our development, and we intend to continue doing so. Does our approach make the project ineligible for Open Internet Stack programmes?

  The short answer is yes. AI as a 'coding partner' is not a development method that is compatible with our current programmes and the genAI policy.

- Is reverse-engineering Android applications using LLM in scope of 'read only use'? ...

  *(Question continues:) As a result of this automated reversing the LLM would produce a specification of a proprietary protocol but the open-source implementation of this protocol would then be written by a human.*  
  Answer: Yes. The work method you propose does indeed fall within the read-only use of LLMs, and would be allowed.

- A question about the boundary of permitted “read-only” use...

  *(question continues:) Policy 2.0 states that generative AI may inspect human-written code and identify security issues or flaws, provided that human contributors craft the fixes and write the code themselves. Does permitted read-only use also include reviewing human-authored architecture, tests and documentation; explaining general technical concepts; identifying verifier, portability or security problems; and providing high-level recommendations without generating patches or final wording?*  
  Answer: Yes, all those use cases are permitted.

### Disclosure

- What minimum transparency, disclosure, or evidence is expected for permitted read-only use?

  Provide at the very minimum a high-level description of the use of GenAI. This means summarising the general stance towards generative AI at the project level in the README, man/info pages, and your website. We \*recommend\* a more extensive disclosure. See: https://nlnet.nl/foundation/policies/generativeAI/2.0/#transparency

### Creation of AI-related projects

- Are there limitations to building AI tooling? So not using AI but building it?

  Yes. In certain programmes (notably [Restack](https://nlnet.nl/restack#AI)AI-related projects not within scope. There is one exception: projects that are already widely used throughout society (\> 1 million active human users) and directly relevant to the stack, can apply for funding.

- Restack excludes AI-related projects. I am creating a tool that can be used by humans, but can optionally also be used by AI. Is this is scope?

  Yes. When the AI functionality is an additional feature, the project is in scope for programmes that do not fund AI-related projects.

- The Restack programme excludes AI-related projects. Where is the line for infrastructure that AI systems can consume but that contains no AI itself?

  *(question continues:) For example, would a deterministic library that records content-addressed source references (document, chunk, version, hash) and verifies that a cited passage exists and matches its hash be in scope, if any AI component using it stays outside the funded work?*  
  Answer: If it is also consumable and useful outside of the AI ecosystems, then it would likely be considered.

- My project has an optional local AI, off by default, only for searching documents. Is it in scope for Restack if the grant does not fund the AI part?

  It would likely be in scope.

- When AI-related projects are out of scope, is all automation forbidden?

  No, this stipulation exclusively concerns GenAI and does not regulate other forms of automation. Non-GenAI forms of automation are within scope such as deterministic and reproducible generation of source code, formal and symbolic proofs, fuzz testing, or non-GenAI forms of machine learning.
