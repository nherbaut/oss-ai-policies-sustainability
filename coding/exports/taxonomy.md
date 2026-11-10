![Sustainability coding taxonomy. Dimensions follow the Karlskrona manifesto [@becker2015sustainability], and twenty categories follow Roy et al. [@roy2026taxonomy]. Individual-level categories are provisional.](taxonomy.png)

### Sustainability coding taxonomy

The five high-level dimensions follow the Karlskrona manifesto [@becker2015sustainability]. The twenty categories assigned to the environmental, technical, social and economic dimensions are drawn from Roy et al. [@roy2026taxonomy]. The five individual-level categories are provisional literature-derived extensions whose original definitions require verification. Operational definitions and coding guidance are adaptations by the research team for OSS/GenAI.

| Dimension | Category | Provenance |
|---|---|---|
| Environmental | Carbon Footprint | Roy et al. [@roy2026taxonomy] |
| Environmental | Energy Consumption | Roy et al. [@roy2026taxonomy] |
| Environmental | E-waste | Roy et al. [@roy2026taxonomy] |
| Environmental | Code Sustainability | Roy et al. [@roy2026taxonomy] |
| Environmental | Resource management | Roy et al. [@roy2026taxonomy] |
| Technical | Perdurability | Roy et al. [@roy2026taxonomy] |
| Technical | Longitivity | Roy et al. [@roy2026taxonomy] |
| Technical | Repairability | Roy et al. [@roy2026taxonomy] |
| Technical | Feature Bloat | Roy et al. [@roy2026taxonomy] |
| Technical | Security Concerns | Roy et al. [@roy2026taxonomy] |
| Social | Digital Inclusivity | Roy et al. [@roy2026taxonomy] |
| Social | Equitable Access | Roy et al. [@roy2026taxonomy] |
| Social | Ethical Concerns | Roy et al. [@roy2026taxonomy] |
| Social | Customer social value | Roy et al. [@roy2026taxonomy] |
| Social | Social Engineering | Roy et al. [@roy2026taxonomy] |
| Social | User error protection | Roy et al. [@roy2026taxonomy] |
| Economic | Circular Economy | Roy et al. [@roy2026taxonomy] |
| Economic | Affordability | Roy et al. [@roy2026taxonomy] |
| Economic | Cost efficiency | Roy et al. [@roy2026taxonomy] |
| Economic | Software process evolving intellectual capital | Roy et al. [@roy2026taxonomy] |
| Individual | Health | Provisional literature extension |
| Individual | Lifelong learning | Provisional literature extension |
| Individual | Privacy | Provisional literature extension |
| Individual | Safety | Provisional literature extension |
| Individual | Agency | Provisional literature extension |

Source labels are retained to preserve traceability, including “Longitivity” and “Social Engineering”. The latter has divergent meanings in the source materials, which are documented in its QualCoder memo. Coding distinguishes policy requirements, stated concerns, possible effects and observed effects. Each new code or category receives a memo recording its reference and source location, or its inductive origin and supporting corpus passages.

The complete exported codebook includes the live QualCoder memos, operational definitions, coding guidance and reference details. Regenerate it with `make coding-taxonomy-export`.

### Environmental

“effects of human activities on natural systems”

— Becker et al. (2015), [@becker2015sustainability], Section II, PDF page 4. https://www.cs.toronto.edu/~sme/papers/2015/Beckeretal-ICSE2015.pdf

### Technical

“longevity of information, systems, and infrastructure”

— Becker et al. (2015), [@becker2015sustainability], Section II, PDF page 4. https://www.cs.toronto.edu/~sme/papers/2015/Beckeretal-ICSE2015.pdf

### Social

“societal communities”

— Becker et al. (2015), [@becker2015sustainability], Section II, PDF page 4. https://www.cs.toronto.edu/~sme/papers/2015/Beckeretal-ICSE2015.pdf

### Economic

“assets, capital and added value”

— Becker et al. (2015), [@becker2015sustainability], Section II, PDF page 4. https://www.cs.toronto.edu/~sme/papers/2015/Beckeretal-ICSE2015.pdf

### Individual

“well-being of humans”

— Becker et al. (2015), [@becker2015sustainability], Section II, PDF page 5. https://www.cs.toronto.edu/~sme/papers/2015/Beckeretal-ICSE2015.pdf

### Carbon Footprint

“This is a measure of the total greenhouse gas (GHG) emissions caused directly and indirectly by an individual, organization, event, or product. It is expressed in terms of the amount of carbon dioxide (CO2) or its equivalent of other GHGs. The carbon footprint considers the entire life cycle of a product or activity, from the extraction of raw materials to its final disposal.”

— Sustainability Category Correlations.xlsx, Definitions!A2, entry “Carbon Footprint”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Energy Consumption

“This refers to the total amount of energy utilized in a particular process or by a specific entity, such as a household or a business. It is a critical component of the environmental impact, as energy production, particularly from fossil fuels, is a major source of greenhouse gas emissions. The concept is intrinsically linked to energy efficiency, where higher consumption indicates lower efficiency.”

— Sustainability Category Correlations.xlsx, Definitions!A4, entry “Energy Consumption”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### E-waste

“Short for electronic waste, this term describes discarded electrical or electronic devices. It encompasses a wide array of products, from household appliances to computers and mobile phones, that are no longer considered useful due to malfunction or obsolescence. E-waste is a growing global concern due to the volume of its generation and the presence of toxic materials that can harm human health and the environment if not managed properly.”

— Sustainability Category Correlations.xlsx, Definitions!A6, entry “E-waste”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Code Sustainability

“This concept involves the development of software with a minimal environmental impact. It emphasizes writing efficient code that consumes less energy and optimizing the use of resources throughout the software's lifecycle. The goal is to create software that is not only functional and reliable but also environmentally conscious. This can include practices like code optimization and choosing energy-efficient data centers.”

— Sustainability Category Correlations.xlsx, Definitions!A8, entry “Code Sustainability”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Resource management

“This is the practice of using resources in the most effective way possible while minimizing waste and environmental impact. It involves maximizing the output from a given amount of resources, be it materials, energy, or water. Resource efficiency is a key strategy for achieving sustainable development, as it helps to conserve natural resources and reduce pollution.”

— Sustainability Category Correlations.xlsx, Definitions!A10, entry “Resource Efficiency”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Perdurability

“In the context of software, perdurability refers to the ability of a system to persist and remain effective over a long period, despite changes in its environment or requirements. It is closely related to the concepts of durability and long-term viability.”

— Sustainability Category Correlations.xlsx, Definitions!A12, entry “Perdurability”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Longitivity

“This term emphasizes the lifespan of a product or system. In software, it refers to the length of time a system remains useful and operational before it becomes obsolete or needs to be replaced. Designing for longevity involves creating systems that are adaptable and can evolve with changing needs.”

— Sustainability Category Correlations.xlsx, Definitions!A14, entry “Longevity”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Repairability

“This is the ease with which a product or system can be repaired or maintained. For hardware, it means designing products with accessible components that can be easily replaced. In software, it translates to writing clean, modular, and well-documented code that is easy to debug and modify.”

— Sustainability Category Correlations.xlsx, Definitions!A16, entry “Repairability”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Feature Bloat

“This occurs when a product or software becomes overloaded with excessive features, many of which may be unnecessary for the user. Feature bloat can lead to a more complex and difficult-to-use product, increased resource consumption, and a shorter lifespan as the system becomes unwieldy.”

— Sustainability Category Correlations.xlsx, Definitions!A18, entry “Feature Bloat”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Security Concerns

“This category encompasses the measures taken to protect a system and its users from threats and vulnerabilities. In a sustainability context, a secure system is one that is resilient to attacks and can be trusted by its users over the long term, thus contributing to its overall viability.”

— Sustainability Category Correlations.xlsx, Definitions!A20, entry “Security Concerns”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Digital Inclusivity

“This refers to ensuring that everyone, regardless of their background, ability, or socioeconomic status, has access to and can effectively use digital technologies. It is about bridging the digital divide and creating a more equitable digital society.”

— Sustainability Category Correlations.xlsx, Definitions!A23, entry “Digital Inclusivity”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Equitable Access

“This concept is closely related to digital inclusivity and focuses on the fair distribution of access to technology and its benefits. It addresses the barriers that can prevent certain groups from accessing and benefiting from digital resources.”

— Sustainability Category Correlations.xlsx, Definitions!A25, entry “Equitable Access”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Ethical Concerns

“This broad category covers the moral implications of technology and its use. It includes issues such as data privacy, algorithmic bias, and the potential for technology to be used for malicious purposes. Addressing ethical concerns is crucial for building trust and ensuring that technology serves humanity in a positive way.”

— Sustainability Category Correlations.xlsx, Definitions!A27, entry “Ethical Concerns”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Customer social value

“This refers to the positive social impact that a product or service creates for its customers and the wider community. It goes beyond the direct functional benefits to consider how the product contributes to social well-being and addresses societal needs.”

— Sustainability Category Correlations.xlsx, Definitions!A29, entry “Customer Social Value”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Social Engineering

“In the context of information security, this is the use of deception to manipulate individuals into divulging confidential or personal information that may be used for fraudulent purposes. From a broader social sustainability perspective, it highlights the vulnerability of individuals in the digital realm and the need for education and protection.”

— Sustainability Category Correlations.xlsx, Definitions!A31, entry “Social Engineering”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### User error protection

“This involves designing systems and interfaces that minimize the likelihood of users making errors and that provide clear and helpful guidance when errors do occur. It is about creating a more user-friendly and forgiving digital environment, which contributes to a more positive and less stressful user experience.”

— Sustainability Category Correlations.xlsx, Definitions!A33, entry “User Error Protection”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Circular Economy

“This is an economic model that aims to eliminate waste and promote the continual use of resources. In a circular economy, products are designed to be durable, repairable, and recyclable, so that their materials can be returned to the production cycle at the end of their life.”

— Sustainability Category Correlations.xlsx, Definitions!A35, entry “Circular Economy”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Affordability

“This refers to the ability of individuals and organizations to purchase a product or service without undue financial hardship. In a sustainability context, affordability is about ensuring that sustainable choices are accessible to everyone, not just a privileged few.”

— Sustainability Category Correlations.xlsx, Definitions!A37, entry “Affordability”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Cost efficiency

“This is about maximizing the value derived from a given amount of resources. In software development, it involves optimizing development processes and resource allocation to create high-quality software in a cost-effective manner. Cost efficiency contributes to the economic viability of a project and its long-term sustainability.”

— Sustainability Category Correlations.xlsx, Definitions!A39, entry “Cost Efficiency”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Software process evolving intellectual capital

“This refers to the continuous improvement and adaptation of the processes used to develop and maintain software. It involves learning from experience, adopting new technologies and methodologies, and evolving processes to meet changing needs and challenges. A commitment to process evolution is essential for long-term economic sustainability in the fast-paced world of software development.”

— Sustainability Category Correlations.xlsx, Definitions!A41, entry “Software Process Evolution”. Associated taxonomy: Roy et al. (2026), [@roy2026taxonomy], DOI 10.1145/3786148.3788620.

### Health

“Health”

— Categories & Metrics.docx, table 1, Individual lists in the entries “Requirements engineering for sustainability: an awareness framework for designing software systems for a better tomorrow” (2020) and “Do we really know what we are building? Raising awareness of potential Sustainability Effects of Software Systems in Requirements Engineering” (2019).

### Lifelong learning

“Lifelong learning”

— Categories & Metrics.docx, table 1, Individual lists in the entries “Requirements engineering for sustainability: an awareness framework for designing software systems for a better tomorrow” (2020) and “Do we really know what we are building? Raising awareness of potential Sustainability Effects of Software Systems in Requirements Engineering” (2019).

### Privacy

“Privacy”

— Categories & Metrics.docx, table 1, Individual lists in the entries “Requirements engineering for sustainability: an awareness framework for designing software systems for a better tomorrow” (2020) and “Do we really know what we are building? Raising awareness of potential Sustainability Effects of Software Systems in Requirements Engineering” (2019).

### Safety

“Safety”

— Categories & Metrics.docx, table 1, Individual lists in the entries “Requirements engineering for sustainability: an awareness framework for designing software systems for a better tomorrow” (2020) and “Do we really know what we are building? Raising awareness of potential Sustainability Effects of Software Systems in Requirements Engineering” (2019).

### Agency

“Agency”

— Categories & Metrics.docx, table 1, Individual lists in the entries “Requirements engineering for sustainability: an awareness framework for designing software systems for a better tomorrow” (2020) and “Do we really know what we are building? Raising awareness of potential Sustainability Effects of Software Systems in Requirements Engineering” (2019).

## Bibliographic references

Becker, Christoph, Ruzanna Chitchyan, Leticia Duboc, Steve Easterbrook, Birgit Penzenstadler, Norbert Seyff, and Colin C. Venters. "Sustainability design and software: The Karlskrona manifesto." In 2015 IEEE/ACM 37th IEEE International Conference on Software Engineering, vol. 2, pp. 467–476. IEEE, 2015.
Roy, Mandira, Novarun Deb, Agostino Cortesi, and Nabendu Chaki. "Towards a Taxonomy of Sustainability Requirements for Software Design." In Proceedings of the IEEE/ACM 10th International Workshop on Green and Sustainable Software, pp. 22–27. 2026. DOI 10.1145/3786148.3788620.
