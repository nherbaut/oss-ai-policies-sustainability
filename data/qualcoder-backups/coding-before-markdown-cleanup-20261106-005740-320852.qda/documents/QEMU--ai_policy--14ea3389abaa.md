<div class="document" role="main" itemscope="itemscope"
itemtype="http://schema.org/Article">

<div itemprop="articleBody">

<div id="code-provenance" class="section">

<span id="id1"></span>

# Code provenance<a href="#code-provenance" class="headerlink"
title="Link to this heading"></a>

<div id="certifying-patch-submissions" class="section">

## Certifying patch submissions<a href="#certifying-patch-submissions" class="headerlink"
title="Link to this heading"></a>

The QEMU community **mandates** all contributors to certify provenance
of patch submissions they make to the project. To put it another way,
contributors must indicate that they are legally permitted to contribute
to the project.

Certification is achieved with a low overhead by adding a single line to
the bottom of every git commit:

<div class="highlight-default notranslate">

<div class="highlight">

    Signed-off-by: YOUR NAME <YOUR@EMAIL>

</div>

</div>

The addition of this line asserts that the author of the patch is
contributing in accordance with the clauses specified in the
<a href="https://developercertificate.org"
class="reference external">Developer’s Certificate of Origin</a>:

> <div>
>
> Developer’s Certificate of Origin 1.1
>
> By making a contribution to this project, I certify that:
>
> 1.  The contribution was created in whole or in part by me and I have
>     the right to submit it under the open source license indicated in
>     the file; or
>
> 2.  The contribution is based upon previous work that, to the best of
>     my knowledge, is covered under an appropriate open source license
>     and I have the right under that license to submit that work with
>     modifications, whether created in whole or in part by me, under
>     the same open source license (unless I am permitted to submit
>     under a different license), as indicated in the file; or
>
> 3.  The contribution was provided directly to me by some other person
>     who certified (a), (b) or (c) and I have not modified it.
>
> 4.  I understand and agree that this project and the contribution are
>     public and that a record of the contribution (including all
>     personal information I submit with it, including my sign-off) is
>     maintained indefinitely and may be redistributed consistent with
>     this project or the open source license(s) involved.
>
> </div>

The name used with “Signed-off-by” does not need to be your legal name,
nor birth name, nor appear on any government ID. It is the identity you
choose to be known by in the community, but should not be anonymous, nor
misrepresent whom you are.

It is generally expected that the name and email addresses used in one
of the <span class="pre">`Signed-off-by`</span> lines, matches that of
the git commit <span class="pre">`Author`</span> field. It’s okay if you
subscribe or contribute to the list via more than one address, but using
multiple addresses in one commit just confuses things.

If the person sending the mail is not one of the patch authors, they are
nonetheless expected to add their own
<span class="pre">`Signed-off-by`</span> to comply with the DCO clause
(c).

</div>

<div id="multiple-authorship" class="section">

## Multiple authorship<a href="#multiple-authorship" class="headerlink"
title="Link to this heading"></a>

It is not uncommon for a patch to have contributions from multiple
authors. In this scenario, git commits will usually be expected to have
a <span class="pre">`Signed-off-by`</span> line for each contributor
involved in creation of the patch. Some edge cases:

> <div>
>
> - The non-primary author’s contributions were so trivial that they can
>   be considered not subject to copyright. In this case the secondary
>   authors need not include a <span class="pre">`Signed-off-by`</span>.
>
>   This case most commonly applies where QEMU reviewers give short
>   snippets of code as suggested fixes to a patch. The reviewers don’t
>   need to have their own <span class="pre">`Signed-off-by`</span>
>   added unless their code suggestion was unusually large, but it is
>   common to add <span class="pre">`Suggested-by`</span> as a credit
>   for non-trivial code.
>
> - Both contributors work for the same employer and the employer
>   requires copyright assignment.
>
>   It can be said that in this case a
>   <span class="pre">`Signed-off-by`</span> is indicating that the
>   person has permission to contribute from their employer who is the
>   copyright holder. It is nonetheless still preferable to include a
>   <span class="pre">`Signed-off-by`</span> for each contributor, as in
>   some countries employees are not able to assign copyright to their
>   employer, and it also covers any time invested outside working
>   hours.
>
> </div>

When multiple <span class="pre">`Signed-off-by`</span> tags are present,
they should be strictly kept in order of authorship, from oldest to
newest.

</div>

<div id="other-commit-tags" class="section">

## Other commit tags<a href="#other-commit-tags" class="headerlink"
title="Link to this heading"></a>

While the <span class="pre">`Signed-off-by`</span> tag is mandatory,
there are a number of other tags that are commonly used during QEMU
development:

> <div>
>
> - **Reviewed-by**: when a QEMU community member reviews a patch on the
>   mailing list, if they consider the patch acceptable, they should
>   send an email reply containing a
>   <span class="pre">`Reviewed-by`</span> tag. Subsystem maintainers
>   who review a patch should add this even if they are also adding
>   their <span class="pre">`Signed-off-by`</span> to the same commit.
>
> - **Acked-by**: when a QEMU subsystem maintainer approves a patch that
>   touches their subsystem, but intends to allow a different maintainer
>   to queue it and send a pull request, they would send a mail
>   containing a <span class="pre">`Acked-by`</span> tag. Where a patch
>   touches multiple subsystems, <span class="pre">`Acked-by`</span>
>   only implies review of the maintainers’ own areas of responsibility.
>   If a maintainer wants to indicate they have done a full review they
>   should use a <span class="pre">`Reviewed-by`</span> tag.
>
> - **Tested-by**: when a QEMU community member has functionally tested
>   the behaviour of the patch in some manner, they should send an email
>   reply containing a <span class="pre">`Tested-by`</span> tag.
>
> - **Reported-by**: when a QEMU community member reports a problem via
>   the mailing list, or some other informal channel that is not the
>   issue tracker, it is good practice to credit them by including a
>   <span class="pre">`Reported-by`</span> tag on any patch fixing the
>   issue. When the problem is reported via the GitLab issue tracker,
>   however, it is sufficient to just include a link to the issue.
>
> - **Suggested-by**: when a reviewer or other 3rd party makes
>   non-trivial suggestions for how to change a patch, it is good
>   practice to credit them by including a
>   <span class="pre">`Suggested-by`</span> tag.
>
> </div>

</div>

<div id="subsystem-maintainer-requirements" class="section">

## Subsystem maintainer requirements<a href="#subsystem-maintainer-requirements" class="headerlink"
title="Link to this heading"></a>

When a subsystem maintainer accepts a patch from a contributor, in
addition to the normal code review points, they are expected to validate
the presence of suitable <span class="pre">`Signed-off-by`</span> tags.

At the time they queue the patch in their subsystem tree, the maintainer
**must** also then add their own
<span class="pre">`Signed-off-by`</span> to indicate that they have done
the aforementioned validation. This is in addition to any of their own
<span class="pre">`Reviewed-by`</span> tags the subsystem maintainer may
wish to include.

When the maintainer modifies the patch after pulling into their tree,
they should record their contribution. This is typically done via a note
in the commit message, just prior to the maintainer’s
<span class="pre">`Signed-off-by`</span>:

<div class="highlight-default notranslate">

<div class="highlight">

    Signed-off-by: Cory Contributor <cory.contributor@example.com>
    [Comment rephrased for clarity]
    Signed-off-by: Mary Maintainer <mary.maintainer@mycorp.test>

</div>

</div>

</div>

<div id="tools-for-adding-signed-off-by" class="section">

## Tools for adding <span class="pre">`Signed-off-by`</span><a href="#tools-for-adding-signed-off-by" class="headerlink"
title="Link to this heading"></a>

There are a variety of ways tools can support adding
<span class="pre">`Signed-off-by`</span> tags for patches, avoiding the
need for contributors to manually type in this repetitive text each
time.

<div id="git-commands" class="section">

### git commands<a href="#git-commands" class="headerlink"
title="Link to this heading"></a>

When creating, or amending, a commit the <span class="pre">`-s`</span>
flag to
<span class="pre">`git`</span>` `<span class="pre">`commit`</span> will
append a suitable line matching the configured git author details.

If preparing patches using the
<span class="pre">`git`</span>` `<span class="pre">`format-patch`</span>
tool, the <span class="pre">`-s`</span> flag can be used to append a
suitable line in the emails it creates, without modifying the local
commits. Alternatively to modify all the local commits on a branch:

<div class="highlight-default notranslate">

<div class="highlight">

    git rebase master -x 'git commit --amend --no-edit -s'

</div>

</div>

</div>

<div id="emacs" class="section">

### emacs<a href="#emacs" class="headerlink" title="Link to this heading"></a>

In the file <span class="pre">`$HOME/.emacs.d/abbrev_defs`</span> add:

<div class="highlight-elisp notranslate">

<div class="highlight">

    (define-abbrev-table 'global-abbrev-table
      '(
        ("8rev" "Reviewed-by: YOUR NAME <your@email.addr>" nil 1)
        ("8ack" "Acked-by: YOUR NAME <your@email.addr>" nil 1)
        ("8test" "Tested-by: YOUR NAME <your@email.addr>" nil 1)
        ("8sob" "Signed-off-by: YOUR NAME <your@email.addr>" nil 1)
       ))

</div>

</div>

with this change, if you type (for example)
<span class="pre">`8rev`</span> followed by
<span class="pre">`<space>`</span> or <span class="pre">`<enter>`</span>
it will expand to the whole phrase.

</div>

<div id="vim" class="section">

### vim<a href="#vim" class="headerlink" title="Link to this heading"></a>

In the file <span class="pre">`$HOME/.vimrc`</span> add:

<div class="highlight-default notranslate">

<div class="highlight">

    iabbrev 8rev Reviewed-by: YOUR NAME <your@email.addr>
    iabbrev 8ack Acked-by: YOUR NAME <your@email.addr>
    iabbrev 8test Tested-by: YOUR NAME <your@email.addr>
    iabbrev 8sob Signed-off-by: YOUR NAME <your@email.addr>

</div>

</div>

with this change, if you type (for example)
<span class="pre">`8rev`</span> followed by
<span class="pre">`<space>`</span> or <span class="pre">`<enter>`</span>
it will expand to the whole phrase.

</div>

</div>

<div id="re-starting-abandoned-work" class="section">

## Re-starting abandoned work<a href="#re-starting-abandoned-work" class="headerlink"
title="Link to this heading"></a>

For a variety of reasons there are some patches that get submitted to
QEMU but never merged. An unrelated contributor may decide (months or
years later) to continue working from the abandoned patch and re-submit
it with extra changes.

The general principles when picking up abandoned work are:

> <div>
>
> - Continue to credit the original author for their work, by
>   maintaining their original <span class="pre">`Signed-off-by`</span>
>
> - Indicate where the original patch was obtained from (mailing list,
>   bug tracker, author’s git repo, etc) when sending it for review
>
> - Acknowledge the extra work of the new contributor by including their
>   <span class="pre">`Signed-off-by`</span> in the patch in addition to
>   the original author’s
>
> - Indicate who is responsible for what parts of the patch. This is
>   typically done via a note in the commit message, just prior to the
>   new contributor’s <span class="pre">`Signed-off-by`</span>:
>
>   <div class="highlight-default notranslate">
>
>   <div class="highlight">
>
>       Signed-off-by: Some Person <some.person@example.com>
>       [Rebased and added support for 'foo']
>       Signed-off-by: New Person <new.person@mycorp.test>
>
>   </div>
>
>   </div>
>
> </div>

In complicated cases, or if otherwise unsure, ask for advice on the
project mailing list.

It is also recommended to attempt to contact the original author to let
them know you are interested in taking over their work, in case they
still intended to return to the work, or had any suggestions about the
best way to continue.

</div>

<div id="inclusion-of-generated-files" class="section">

## Inclusion of generated files<a href="#inclusion-of-generated-files" class="headerlink"
title="Link to this heading"></a>

Files in patches contributed to QEMU are generally expected to be
provided only in the preferred format for making modifications. The
implication of this is that the output of code generators or compilers
is usually not appropriate to contribute to QEMU.

For reasons of practicality there are some exceptions to this rule,
where generated code is permitted, provided it is also accompanied by
the corresponding preferred source format. This is done where it is
impractical to expect those building QEMU to run the code generation or
compilation process. A non-exhaustive list of examples is:

> <div>
>
> - Images: where an bitmap image is created from a vector file it is
>   common to include the rendered bitmaps at desired resolution(s),
>   since subtle changes in the rasterization process / tools may affect
>   quality. The original vector file is expected to accompany any
>   generated bitmaps.
>
> - Firmware: QEMU includes pre-compiled binary ROMs for a variety of
>   guest firmwares. When such binary ROMs are contributed, the
>   corresponding source must also be provided, either directly, or
>   through a git submodule link.
>
> - Dockerfiles: the majority of the dockerfiles are automatically
>   generated from a canonical list of build dependencies maintained in
>   tree, together with the libvirt-ci git submodule link. The generated
>   dockerfiles are included in tree because it is desirable to be able
>   to directly build container images from a clean git checkout.
>
> - eBPF: QEMU includes some generated eBPF machine code, since the
>   required eBPF compilation tools are not broadly available on all
>   targeted OS distributions. The corresponding eBPF C code for the
>   binary is also provided. This is a time-limited exception until the
>   eBPF toolchain is sufficiently broadly available in distros.
>
> </div>

In all cases above, the existence of generated files must be
acknowledged and justified in the commit that introduces them.

Tools which perform changes to existing code with deterministic
algorithmic manipulation, driven by user specified inputs, are not
generally considered to be “generators”.

For instance, using Coccinelle to convert code from one pattern to
another pattern, or fixing documentation typos with a spell checker, or
transforming code using sed / awk / etc, are not considered to be acts
of code generation. Where an automated manipulation is performed on
code, however, this should be declared in the commit message.

At times contributors may use or create scripts/tools to generate an
initial boilerplate code template which is then filled in to produce the
final patch. The output of such a tool would still be considered the
“preferred format”, since it is intended to be a foundation for further
human authored changes. Such tools are acceptable to use, provided there
is clearly defined copyright and licensing for their output. Note in
particular the caveats applying to AI content generators below.

</div>

<div id="use-of-ai-generated-content" class="section">

## Use of AI-generated content<a href="#use-of-ai-generated-content" class="headerlink"
title="Link to this heading"></a>

TL;DR:

> <div>
>
> **Current QEMU project policy is to DECLINE any contributions which
> are believed to include or derive from AI generated content. This
> includes ChatGPT, Claude, Copilot, Llama and similar tools.**
>
> **This policy does not apply to other uses of AI, such as researching
> APIs or algorithms, static analysis, or debugging, provided their
> output is not included in contributions.**
>
> </div>

The increasing prevalence of AI-assisted software development results in
a number of difficult legal questions and risks for software projects,
including QEMU. Of particular concern is content generated by
<a href="https://en.wikipedia.org/wiki/Large_language_model"
class="reference external">Large Language Models</a> (LLMs).

The QEMU community requires that contributors certify their patch
submissions are made in accordance with the rules of the
<a href="#dco" class="reference internal"><span
class="std std-ref">Developer's Certificate of Origin (DCO)</span></a>.

To satisfy the DCO, the patch contributor has to fully understand the
copyright and license status of content they are contributing to QEMU.
With AI content generators, the copyright and license status of the
output is ill-defined with no generally accepted, settled legal
foundation.

Where the training material is known, it is common for it to include
large volumes of material under restrictive licensing/copyright terms.
Even where the training material is all known to be under open source
licenses, it is likely to be under a variety of terms, not all of which
will be compatible with QEMU’s licensing requirements.

How contributors could comply with DCO terms (b) or (c) for the output
of AI content generators commonly available today is unclear. The QEMU
project is not willing or able to accept the legal risks of
non-compliance.

The QEMU project thus requires that contributors refrain from using AI
content generators on patches intended to be submitted to the project,
and will decline any contribution if use of AI is either known or
suspected.

Examples of tools impacted by this policy includes GitHub’s CoPilot,
OpenAI’s ChatGPT, Anthropic’s Claude, and Meta’s Code Llama, and
code/content generation agents which are built on top of such tools.

This policy may evolve as AI tools mature and the legal situation is
clarified.

<div id="exceptions" class="section">

### Exceptions<a href="#exceptions" class="headerlink"
title="Link to this heading"></a>

The QEMU project welcomes discussion on any exceptions to this policy,
or more general revisions. This can be done by contacting the qemu-devel
mailing list with details of a proposed tool, model, usage scenario,
etc. that is beneficial to QEMU, while still mitigating issues around
compliance with the DCO. After discussion, any exception will be listed
below.

Exceptions do not remove the need for authors to comply with all other
requirements for contribution. In particular, the “Signed-off-by” label
in a patch submission is a statement that the author takes
responsibility for the entire contents of the patch, including any parts
that were generated or assisted by AI tools or other tools.

</div>

</div>

</div>

</div>

</div>
