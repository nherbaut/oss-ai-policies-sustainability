### Policy for AI Generated Content

Version 0.12.0

### Summary

We recognize the AI tooling ecosystem and underlying models are evolving rapidly. This policy provides guardrails while encouraging transparency about tool usage, so contributors can benefit from AI productivity gains responsibly.

A human must always be in the loop, and humans stay accountable for everything they submit, exactly as they always have. Contributions must be understood by the humans who propose, review, and maintain them. AI-assisted work is held to the same standard as any other contribution. Copyright law continues to apply to all preexisting works. We encourage but don’t require using Open Source AI models trained on content with compatible licensing.

### Five Pillars

This policy rests on five principles. The detailed guidance that follows is meant to illustrate and support these pillars, not to add requirements beyond them.

1.  **AI use is welcomed.** Contributors are free to use the AI tools that work best for them. We neither mandate particular tools nor discourage their use.
2.  **Humans remain accountable.** Every contribution must have an accountable human author who signs off under the Developer Certificate of Origin (DCO), fully understands, and stands behind the work, regardless of how it was produced.
3.  **Material AI use is disclosed.** When AI tools materially shape a contribution, that fact is recorded in the commit metadata using a machine-readable label, so the origin of the work can be understood later if questions arise.
4.  **Results are human-consumable.** Contributions must be understood by the humans who propose, review, and maintain them. The point of engagement is the human community, not the tooling.
5.  **The same standard applies.** Don’t trust AI output implicitly. AI assisted contributions are held to the same quality, correctness, security, and licensing standards as any other contribution. Reviewers may reject low-quality work, but neither a higher nor a lower bar applies because a tool was involved.

### Context

Technology rooted in artificial intelligence (AI) is an actively evolving area with exciting technical possibilities and significant legal uncertainties. The OpenInfra Foundation Governing Board wants to encourage exploration and adoption of new technologies while exercising reasonable caution around potential risks.

### Challenges

- Copyright law in this area is presently an evolving topic with a landscape which will take some time to stabilize. As of March 16th, 2023, Computer Generated work is *not* considered an original work which can be copyrighted in the United States with similar stances being taken in other countries around the world.
- Source training data, and thus resulting material, may come from materials which have unclear or incompatible copyrights and/or licenses. In other cases, copyright of any generated code may be explicitly retained by the vendor operating the AI technology, which is incompatible with contribution to projects. Furthermore, some tools have demonstrated the ability to source context from the contents of a project being worked upon. Ultimately this requires awareness of the End-User License Agreement by the contributor.
- This is an evolving area, and tools will evolve. Contributors need to also be aware, and take action based upon each particular situation, which is the very reason for this document.

### Applicability

All contributions of content committed into source revision control systems by projects housed under the OpenInfra Foundation.

### Policy and Guidance

It is the policy of the OpenInfra Foundation that:

- Contributions must be compatible with the principals of the [Four Opens](/four-opens).
- Contributions created using AI tools are generally permitted if contributors and reviewers follow the checklists below.
- Contributions to OpenInfra Foundation projects are distributed under open source software licenses (Apache 2.0 or other OSI approved licenses), so code or content included in a contribution must be compatible with those licenses. The license of a contribution does not need to be exactly the same as the project's license, being compatible means that the contribution's license grants sufficient rights to allow everything the project's license allows (or allows more), and imposes similar restrictions (or fewer restrictions). Many open source licenses are compatible with other open source licenses, and code or content in the public domain is compatible with all open source licenses. Contributors need to verify they have the right to contribute output from AI tools, just like they do for their own original work, work owned by their employer, work copied or modified from another open source project, or work submitted on behalf of a third party.
  - Where possible, configure the AI tool to operate in modes that respect open source licensing. This will be different for each tool.
  - Any copyrighted materials authored or owned by third parties could be problematic, so make sure they are licensed as open source or public domain, or that you have permission from the copyright holder to release them as open source. Make sure the AI tool doesn’t claim proprietary rights to the code or content generated by the tool.
- We generally expect contributions to be made by a human taking an action, so the contributor has a chance to review their contribution for any technical or legal problems before submitting. Purely autonomous submissions with no identifiable accountable human are not acceptable, not because a tool was used, but because there is no accountable party to maintain the work or follow up on issues. The exception to the rule is that we do allow submissions from well documented automated processes, such as release tooling or for internationalization updates, as long as some individual or team of humans takes responsibility for managing the automated process.
- This policy will be re-evaluated and updated as the law, technology, and open source best practices continue to evolve.

#### Contributor Checklist

As a contributor, you are responsible for the code you submit, whether you use AI tools or write it yourself. Some AI tools offer settings, features, or modes that can help, but these are no substitute for your own review of code quality, correctness, style, security, and licensing.

- With all AI tools, contributors should be mindful of their limitations. Carefully review any suggested or generated code or comments to ensure nothing is inherently harmful, malicious, or outright incorrect.
- OpenInfra projects have adopted the “Generated-By” and “Assisted-By” labels. The “Generated-By” label was first proposed by the Apache Software Foundation as part of their Generative Tooling Guidance. The “Assisted-By” label was adopted later by OpenStack’s Nova, CNCF’s OpenTelemetry, the Linux Kernel, LLVM and other projects, to recognize that AI tools assist developers in many different ways. We recommend using “Assisted-By” moving forward, though “Generated-By” is still approved in this policy, and may be found in the commit history of some OpenInfra projects. These labels are in addition to the “Signed-Off-By” label identifying the contributor who submits the contribution into code review.
  - When available, AI tools should be operated in modes which are compatible with the Open Source Definition as maintained by the OSI.
  - When available, AI features that flag output that resembles publicly available code and provide licensing information should be enabled. Such results should be used to prevent the contribution of incompatibly licensed open source code.
  - When available, AI features that are designed to block output suggestions that match publicly available code should be enabled.
  - Add an “Assisted-By” label to the commit message, and explain in comments or the commit message any prompts or background context the reviewers might need to fully understand the change and how much of the change came from the tool.
- By contributing you are indicating you have the permission and rights to submit the content to a project, so take care in checking that the output of the tool is compatible with the project’s license. The “Signed-Off-By” or “Co-Authored-By” label in your contribution is a statement that a human contributor takes responsibility for the entire contents of the commit, including any parts that were generated or assisted by AI tools or other tools.
- This policy does not supersede any project specific requirements around actions to be taken prior to the submission of changes into review.

#### Reviewer Checklist

- When reviewing contributions with the “Generated-By” or “Assisted-By” labels, verify that the change includes sufficient explanation of the context that the reviewer and future contributors can understand the purpose and origin.
- Hold AI-assisted contributions to the same standard as any other contribution. The disclosure label is not grounds for rejection; it is context. As with any change, reviewers may reject work that does not meet the project’s quality, correctness, security, or licensing bar.
- Code style changes may be necessary to meet project standards and community guidelines, please work with the contributor as-needed
- If the change set is substantially re-worked by human changes during the code review process, consider whether it makes sense to remove the “Generated-By” or “Assisted-By” label prior to committing.

### References

- U.S. Copyright Office Registration Guidance Pertaining to Works Generated by Artificial Intelligence - \<https://www.federalregister.gov/documents/2023/03/16/2023-05321/copyright-registration-guidance-works-containing-material-generated-by-artificial-intelligence\>
- Four Opens - \<https://openinfra.org/four-opens/\>
- Apache Software Foundation Generative Tooling Guidance - \<https://www.apache.org/legal/generative-tooling.html\>

### Change History

| Version | Description | Date | Author |
|----|----|----|----|
| 0.1 | Initial Draft | November 9th, 2023 | J. Kreger |
| 0.2 | Revision including T. Carrez's feedback | February 16, 2024 | J. Kreger & T. Carrez |
| 0.3 | Four opens link and content acceptability | February 22, 2024 | J. Kreger |
| 0.4 | Formatting changes, minor wording changes | February 22, 2024 | J. Kreger on behalf of the working group |
| 0.5 | Revisions from C. Stevenson | February 28, 2024 | C. Stevenson |
| 0.6 | Rewrite the policy section into contributor/reviewer checklist oriented statements to provide clear guidance as action items from board working group discussion, and reformat the change history into a table, and further minor text edits suggested by A. Marrich. | March 14, 2024 | J. Kreger |
| 0.7 | Revisions to make the text both easier to read and more legally precise. | March 26, 2024 | A. Randal |
| 0.8 | Revisions from C. Stevenson | April 8th, 2024 | C. Stevenson |
| 0.8.1 | Minor formatting revision and change for clarity, adoption of suggestion from C. Stevenson. | April 17, 2024 | J. Kreger |
| 0.9.0 | Clarification of Permissively Licensed suggestion from C. Stevenson to Compatible License. | April 23, 2024 | A. Randal |
| 0.9.1 | Change the word "less" to "fewer" in terms of license restrictions. | May 21, 2024 | C. Stevenson |
| 0.9.2 | Revision of contributor guidelines based upon feedback from J. Blair | May 31, 2024 | A. Randal |
| 0.10.0 | Revised content based upon Board and Community discussions, including addition of an assisted-by label. | May 9, 2025 | J. Kreger |
| 0.10.1 | Added a Summary suggestion based upon discussion with A. Marrich | May, 12 2025 | J. Kreger |
| 0.11 | Revision to clarify “Assisted-By” along with further clarifying the Summary and removal of the example commit message from open discussion with A. Marrich, G. Mann, and community members. | June 24, 2025 | J. Kreger on behalf of the working group |
| 0.11.1 | Added clarifications about combining labels and the responsibility of contributors | July 8, 2025 | A. Randal |
| 0.11.2 | Revised Summary text | July 8th, 2025 | E. Glynn |
| 0.12.0 | Revised content based upon OpenInfra AI Policy Working Group discussions and Governing Board review | September 25, 2026 | W. Wilson on behalf of the working group |

#### 

Join the OpenInfra Foundation to learn how you can get involved in initiatives around open infrastructure.

[JOIN](https://openinfra.dev/join/)
