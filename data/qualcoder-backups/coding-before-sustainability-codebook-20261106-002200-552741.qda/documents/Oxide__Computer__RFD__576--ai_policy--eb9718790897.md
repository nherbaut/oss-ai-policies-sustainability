<div class="800:mt-16 relative mt-12 pb-20 print:mt-0" role="main">

<div class="600:px-10 w-full px-5">

<div class="m-auto max-w-300 page-header 800:mb-16 mb-12 600:gap-6 grid grid-cols-12 gap-4">

<div class="800:col-start-2 1200:col-start-3 flex print:hidden">

<a href="https://github.com/oxidecomputer/rfd/pull/964" target="_blank"
rel="noreferrer"><span
class="ox-badge ring ring-inset variant-default text-mono-sm inline-flex h-4 items-center rounded-sm px-0.75 py-px whitespace-nowrap uppercase bg-accent text-accent ring-current/15"><span>published</span></span></a>

</div>

<div class="col-span-12 grid grid-cols-12 items-baseline">

<div class="text-sans-lg text-accent-tertiary 800:col-span-1 800:block 1200:col-span-2 hidden print:hidden">

<span class="1200:inline hidden">RFD</span> 576

</div>

<div class="800:col-span-11 1200:col-span-10 col-span-12 flex items-baseline">

# <span class="hidden print:block">RFD 576</span> Using LLMs at Oxide

</div>

<div class="800:col-span-10 800:col-start-2 800:pr-10 1000:col-span-10 1000:col-start-2 1200:col-start-3 1200:pr-16 col-span-12 mt-4 flex">

<div class="items-top text-sans-md text-notice bg-notice 1200:w-[calc(100%-var(--toc-width))] flex w-full rounded px-3 py-2 pr-6 print:hidden">

<img
src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGNsYXNzPSJ0ZXh0LW5vdGljZS10ZXJ0aWFyeSBtci0yIHNocmluay0wIj48dXNlIGhyZWY9Ii9hc3NldHMvc3ByaXRlLUNPbEpSb0s1LnN2ZyNhY2Nlc3MtMTYiIC8+PC9zdmc+"
class="text-notice-tertiary mr-2 shrink-0" />

<div>

This RFD can be accessed by the following
groups:<span class="text-notice-tertiary ml-1 inline-block">\[</span>public<span class="text-notice-tertiary">\]</span>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="border-secondary border-b print:m-auto print:max-w-300 print:rounded-lg print:border">

<div class="border-secondary print:border-default flex w-full items-center border-t print:py-2 hidden capitalize print:block print:border-t-0">

<div class="600:px-10 w-full px-5">

<div class="m-auto max-w-300 600:gap-6 grid grid-cols-12 gap-4">

<div class="text-mono-sm text-tertiary 800:col-span-1 1200:col-span-2 print:text-raise relative col-span-4 flex h-10 items-center print:col-span-2">

<div class="border-secondary absolute top-2 right-0 bottom-2 hidden w-px border-r print:block">

</div>

State

</div>

<div class="text-sans-md text-default 800:col-span-9 1200:col-span-8 col-span-8 flex h-10 items-center print:col-span-10">

published

</div>

</div>

</div>

</div>

<div class="border-secondary print:border-default flex w-full items-center border-t print:py-2 800:hidden print:hidden">

<div class="600:px-10 w-full px-5">

<div class="m-auto max-w-300 600:gap-6 grid grid-cols-12 gap-4">

<div class="text-mono-sm text-tertiary 800:col-span-1 1200:col-span-2 print:text-raise relative col-span-4 flex h-10 items-center print:col-span-2">

<div class="border-secondary absolute top-2 right-0 bottom-2 hidden w-px border-r print:block">

</div>

RFD

</div>

<div class="text-sans-md text-default 800:col-span-9 1200:col-span-8 col-span-8 flex h-10 items-center print:col-span-10">

576

</div>

</div>

</div>

</div>

<div class="border-secondary print:border-default flex w-full items-center border-t print:py-2">

<div class="600:px-10 w-full px-5">

<div class="m-auto max-w-300 600:gap-6 grid grid-cols-12 gap-4">

<div class="text-mono-sm text-tertiary 800:col-span-1 1200:col-span-2 print:text-raise relative col-span-4 flex h-10 items-center print:col-span-2">

<div class="border-secondary absolute top-2 right-0 bottom-2 hidden w-px border-r print:block">

</div>

Authors

</div>

<div class="text-sans-md text-default 800:col-span-9 1200:col-span-8 col-span-8 flex h-10 items-center print:col-span-10">

<div>

<a href="/?author=bryan%40oxide.computer"
class="link-with-underline inline-block" data-discover="true">Bryan
Cantrill</a>

</div>

</div>

</div>

</div>

</div>

<div class="border-secondary print:border-default flex w-full items-center border-t print:py-2">

<div class="600:px-10 w-full px-5">

<div class="m-auto max-w-300 600:gap-6 grid grid-cols-12 gap-4">

<div class="text-mono-sm text-tertiary 800:col-span-1 1200:col-span-2 print:text-raise relative col-span-4 flex h-10 items-center print:col-span-2">

<div class="border-secondary absolute top-2 right-0 bottom-2 hidden w-px border-r print:block">

</div>

Updated

</div>

<div class="text-sans-md text-default 800:col-span-9 1200:col-span-8 col-span-8 flex h-10 items-center print:col-span-10">

<div testid="timestamp">

<div class="bg-tertiary h-4 w-32 rounded">

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="600:px-10 w-full px-5">

<div class="m-auto max-w-300 800:mt-16 mt-12 600:gap-6 grid grid-cols-12 gap-4">

<div class="800:col-span-10 800:col-start-2 1200:col-span-10 1200:col-start-3 col-span-12 flex">

<div id="preamble" lineno="13">

<div class="sectionbody">

<div class="paragraph" lineno="13">

Large language models (LLMs) are an indisputable breakthrough of the
last five years, potentially profoundly changing the way that we work.
As with any extraordinarily powerful tool, LLM use has both promise and
peril — and that they are so general-purpose leaves real questions about
how and when they should be used. The landscape is shifting so rapidly
that static prescription is unlikely — but that LLMs are evolving so
quickly also gives urgency to the question: **how should LLMs be used at
Oxide**?

</div>

</div>

</div>

<div class="sect1">

## <span id="_values_in_llm_usage" class="anchor" aria-hidden="true"></span><a href="#_values_in_llm_usage" class="link group">Values in LLM
usage<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="sectionbody">

<div class="paragraph" lineno="23">

As is our wont, it’s helpful to look at LLM use through the lens of our
values, several of which come to mind, listed here in priority order:

</div>

<div class="ulist" lineno="26">

- **Responsibility**: In terms of LLM use at Oxide, our lodestar is our
  sense of responsibility. However powerful they may be, LLMs are but a
  tool, ultimately acting at the behest of a human. Oxide employees bear
  responsibility for the artifacts we create, whatever automation we
  might employ to create them. That is, human judgement remains firmly
  in the loop: even if or as an LLM is generating an artifact that we
  will use (writing, test cases, documentation, code, etc.), their
  output is the responsibility of the human using them.

- **Rigor**: LLMs are double-edged with respect to rigor. On the one
  hand, wielded carefully, they can help us sharpen our own thinking by
  pointing out holes in our own reasoning or otherwise providing
  thought-provoking suggestions. On the other, if used recklessly or
  thoughtlessly, they can have the opposite effect, replacing crisp
  thinking with generated flotsam. LLMs are useful in as much as they
  promote and reinforce our rigor.

- **Empathy**: Be we readers or writers, there are humans on the other
  end of our language use. As we use LLMs, we must keep in mind our
  empathy for that human, be they the one who is consuming our writing,
  or the one who has written what we are reading.

- **Teamwork**: We are working together on a shared endeavor, and we
  must be sure that our LLM use does not undermine our sense of
  teamwork. Specifically, we must be careful to not use LLMs in such a
  way as to undermine the trust that we have in one another. In some
  cases, LLM usage is going to be warranted (or otherwise expected), and
  in others it won’t be. Note this isn’t as simple as disclosure of
  usage: in some contexts, volunteering that an LLM has been used to
  generate work product may implicitly distance oneself from the
  responsibility for the content — and erode the trust that is essential
  for teamwork.

- **Urgency**: Urgency seems natural with a tool that can seemingly do
  so much knowledge work so quickly, but with respect to LLM use, too
  many organizations have seemingly enshrined urgency over all else.
  These organizations treat LLMs as an opportunity to increase pace over
  all else, seemingly without regard for setting direction. Urgency is
  certainly important, and LLMs absolutely afford an opportunity to do
  work more quickly — but that pace must not come at the expense of our
  responsibility, rigor, empathy and teamwork.

</div>

</div>

</div>

<div class="sect1">

## <span id="_uses_of_llms" class="anchor" aria-hidden="true"></span><a href="#_uses_of_llms" class="link group">Uses of LLMs<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="sectionbody">

<div class="paragraph" lineno="66">

LLM use varies widely, and the ramifications of those uses vary
accordingly; it’s worth taking apart several of the (many) uses for
LLMs.

</div>

<div class="sect2">

### <span id="_llms_as_readers" class="anchor" aria-hidden="true"></span><a href="#_llms_as_readers" class="link group">LLMs as readers<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="paragraph" lineno="71">

LLMs are superlative at reading comprehension, able to process and
meaningfully comprehend documents effectively instantly. This can be
extraordinarily powerful for summarizing documents — or of answering
more specific questions of a large document like a datasheet or
specification. (Ironically, LLMs are especially good at evaluating
documents to assess the degree that an LLM assisted their creation!)

</div>

<div class="paragraph" lineno="78">

While use of LLMs to assist comprehension has little downside, it does
come with an important caveat: when uploading a document to a hosted LLM
(ChatGPT, Claude, Gemini, etc.), there must be assurance of **data
privacy** — and specifically, assurance that the model will not use the
document to train future iterations of itself. Note that this may be
opt-out (that is, by default, a model may reserve the right to train on
uploaded documents), but can generally be controlled via
preferences — albeit occasionally via euphemism. (OpenAI shamelessly
calls this checked-by-default setting "Improve the model for everyone",
making anyone who doesn’t wish the model to train on their data feel as
if they suffer from a kind of reactionary avarice.)

</div>

<div class="paragraph" lineno="89">

A final cautionary note: using LLMs to assist comprehension should not
substitute for actually reading a document where such reading is
socially expected. More concretely: while LLMs can be a useful tool to
assist in the evaluating of candidate materials per
<a href="/rfd/0003" data-discover="true">[rfd3]</a>, their use should be
restricted to be as a tool, not as a substitute for human eyes (and
brain!).

</div>

</div>

<div class="sect2">

### <span id="_llms_as_researchers" class="anchor" aria-hidden="true"></span><a href="#_llms_as_researchers" class="link group">LLMs as
researchers<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="paragraph" lineno="97">

LLMs can be useful researchers. LLMs are well-suited for the kind of
light research tasks for which one would historically use an internet
search engine, especially as LLM hallucination has been attenuated and
sourcing has improved (and, frankly, as the quality of Google search
results has declined).

</div>

<div class="paragraph" lineno="103">

For more involved research, LLMs are still useful, but with a cautionary
note: the quality of results can vary widely based on model, level of
reasoning, quality of prompt, etc., and one should be careful about
drawing too much confidence from the lengthy, well-formatted nature of
an LLM-powered report. Even if a report appears well-sourced, one
shouldn’t assume that the sources themselves are correct; as
LLM-authored content is increasingly found in the wild, a seemingly
authoritative source found by an LLM may itself be an LLM hallucination!
(In particular, it is not uncommon to find LLM-derived research that
makes fantastical claims about Oxide, including products we don’t offer
or capabilities we don’t have.)

</div>

<div class="paragraph" lineno="114">

When engaging LLMs as researchers, one should select a model with deep
research capabilities enabled, following its citation links to learn
more from the original sources. One should not trust or share
LLM-researched content without checking it first; it should be treated
as a jumping off point to kickstart one’s own research efforts rather
than a finished product.

</div>

<div class="paragraph" lineno="120">

Finally, as with any other use of LLMs, the responsibility for the
artifact lies with the person using the LLM to aid their research, not
with the LLM itself.

</div>

</div>

<div class="sect2">

### <span id="_llms_as_editors" class="anchor" aria-hidden="true"></span><a href="#_llms_as_editors" class="link group">LLMs as editors<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="paragraph" lineno="126">

LLMs can be excellent editors. Engaging an LLM late in the creative
process (that is, with a document already written and broadly polished),
allows for LLMs to provide helpful feedback on structure, phrasing,
etc. — all without danger of losing one’s own voice. A cautionary note
here: LLMs are infamous pleasers — and you may find that the breathless
praise from an LLM is in fact more sycophancy than analysis. This
becomes more perilous the earlier one uses an LLM in the writing
process: the less polish a document already has, the more likely it is
that an LLM will steer to something wholly different — at once praising
your groundbreaking genius while offering to rewrite it for you.

</div>

</div>

<div class="sect2">

### <span id="_llms_as_writers" class="anchor" aria-hidden="true"></span><a href="#_llms_as_writers" class="link group">LLMs as writers<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="paragraph" lineno="138">

While LLMs are adept at reading and can be terrific at editing, their
writing is much more mixed. At best, writing from LLMs is hackneyed and
cliché-ridden; at worst, it brims with tells that reveal that the prose
is in fact automatically generated.

</div>

<div class="paragraph" lineno="143">

What’s so bad about this? First, to those who can recognize an LLM’s
reveals (an expanding demographic!), it’s just embarrassing — it’s as if
the writer is walking around with their [intellectual fly
open](https://bcantrill.dtrace.org/2025/12/05/your-intellectual-fly-is-open/).
But there are deeper problems: LLM-generated writing undermines the
authenticity of not just one’s writing but of the thinking behind it as
well. If the prose is automatically generated, might the ideas be too?
The reader can’t be sure — and increasingly, the hallmarks of LLM
generation cause readers to turn off (or worse).

</div>

<div class="paragraph" lineno="153">

Finally, LLM-generated prose undermines a social contract of sorts:
absent LLMs, it is presumed that of the reader and the writer, it is the
writer that has undertaken the greater intellectual exertion. (That is,
it is more work to write than to read!) For the reader, this is
important: should they struggle with an idea, they can reasonably assume
that the writer themselves understands it — and it is the least a reader
can do to labor to make sense of it.

</div>

<div class="paragraph" lineno="160">

If, however, prose is LLM-generated, this social contract becomes ripped
up: a reader cannot assume that the writer understands their ideas
because they might not so much have read the product of the LLM that
they tasked to write it. If one is lucky, these are LLM hallucinations:
obviously wrong and quickly discarded. If one is unlucky, however, it
will be a kind of LLM-induced cognitive dissonance: a puzzle in which
pieces don’t fit because there is in fact no puzzle at all. This can
leave a reader frustrated: why should they spend more time reading prose
than the writer spent writing it?

</div>

<div class="paragraph" lineno="169">

This can be navigated, of course, but it is truly perilous: our writing
is an important vessel for building trust — and that trust can be
quickly eroded if we are not speaking with our own voice. For us at
Oxide, there is a more mechanical reason to be jaundiced about using
LLMs to write: because our hiring process very much selects for writers,
we know that everyone at Oxide **can** write — and we have the luxury of
demanding of ourselves the kind of writing that we know that we are all
capable of.

</div>

<div class="paragraph" lineno="177">

So our guideline is to generally **not** use LLMs to write — but there
is nuance here, and different kinds of writing merit some elaboration.

</div>

<div class="sect3">

#### <span id="_llms_in_public_writing" class="anchor" aria-hidden="true"></span><a href="#_llms_in_public_writing" class="link group">LLMs in public
writing<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="paragraph" lineno="182">

The prevalence of LLM-infused writing (and the concomitant loss of
reader trust) has made the potential consequences of LLM use in public
writing much more dire: if the reader believes text to be LLM-authored,
they are increasingly likely to not only stop reading, but to question
the writer. And when the writer is representing Oxide — as is the case
for public writing like a company blog post, press release, social media
post, or public RFD — it is the authenticity of Oxide’s voice itself
that becomes suspect.

</div>

<div class="paragraph" lineno="190">

We must not endanger the Oxide voice that we have all worked so hard to
build: for any public Oxide writing, not only must an LLM not be used to
write, but it must be **further** true that the text not be read as
LLM-authored. This is a higher bar, and arguably a weirder one: not only
must it be human written, it must be unimpeachably so.

</div>

<div class="paragraph" lineno="196">

Fortunately, tools can help. We use Pangram at Oxide, and have found its
false positive rate to be extremely
low.<a href="https://arxiv.org/abs/2607.27183" target="_blank"
rel="noopener">[pangram4]</a> Before publication, Pangram should report
that the writing is entirely human-written. Note that it is
possible — though in our experience, highly unlikely — that
human-authored text will need to be slightly re-worked to achieve this.
(Much more likely, however, is that Pangram successfully identifies
clauses or paragraphs that were indeed LLM-authored, if perhaps as the
innocent result of accepting an LLM’s suggestion during the editing
process.)

</div>

</div>

<div class="sect3">

#### <span id="_llms_in_personal_writing" class="anchor" aria-hidden="true"></span><a href="#_llms_in_personal_writing" class="link group">LLMs in personal
writing<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="paragraph" lineno="207">

For any writing where the expectation is clearly direct personal
communication — e.g., chat, review comments, e-mail — LLMs should never
be used to write. This is not to say that LLMs will not be used at all:
they can be used to inform (in the case of review comments) or edit
(e-mails) — but they should never be used to write text that the reader
is very clearly expecting to be human-authored.

</div>

</div>

<div class="sect3">

#### <span id="_llms_in_operational_writing" class="anchor" aria-hidden="true"></span><a href="#_llms_in_operational_writing" class="link group">LLMs in
operational writing<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="paragraph" lineno="216">

If the guidelines for LLM use in public writing and personal writing are
clear (namely: don’t), it’s quite a bit murkier for the workhorse
writing that serves to get a job done. This is *operational writing*: it
is neither highfalutin prose nor quotidian correspondence, but rather
the kind of writing that documents an aspect of the system or contains
the detailed response to an RFP. For operational writing, accuracy and
completeness trump all else: the reader’s expectation is correctness,
not authorship. (Indeed, a hallmark of operational writing is that its
attribution to an author is incidental, if it’s attributed at all.) As a
result, LLMs may find use in the mechanics of operational writing
(including the generation of text), but the human author remains
accountable: correctness must be verified — and responsibility to the
reader is paramount.

</div>

</div>

</div>

<div class="sect2">

### <span id="_llms_as_code_reviewers" class="anchor" aria-hidden="true"></span><a href="#_llms_as_code_reviewers" class="link group">LLMs as code
reviewers<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="paragraph" lineno="230">

As with reading comprehension and editing, LLMs can make for good code
reviewers. But they can also make nonsense suggestions or otherwise miss
larger issues. LLMs should be used for review (and can be very helpful
when targeted to look for a particular kind of issue), but that review
should not be accepted as a human substitute.

</div>

</div>

<div class="sect2">

### <span id="_llms_as_debuggers" class="anchor" aria-hidden="true"></span><a href="#_llms_as_debuggers" class="link group">LLMs as debuggers<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="paragraph" lineno="238">

LLMs can be surprisingly helpful debugging problems, but perhaps only
because our expectations for them would be so low. While LLMs shouldn’t
be relied upon (clearly?) to debug a problem, they can serve as a kind
of animatronic [rubber
duck](https://en.wikipedia.org/wiki/Rubber_duck_debugging), helping to
inspire the next questions to ask. (And they can be surprising: LLMs
have been known to debug I2C issues from the screenshot of a scope
capture!) When debugging a vexing problem one has little to lose by
using an LLM (provided, of course, it does not displace interactions
with one’s colleagues to collaboratively debug!) — but perhaps also
little to gain.

</div>

</div>

<div class="sect2">

### <span id="_llms_as_programmers" class="anchor" aria-hidden="true"></span><a href="#_llms_as_programmers" class="link group">LLMs as
programmers<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="paragraph" lineno="250">

LLMs are amazingly good at writing code — so much so that there is
borderline mass hysteria about LLMs entirely eliminating software
engineering as a craft. As with using an LLM to write prose, there is
obvious peril here! Unlike prose, however (which really should be handed
in a polished form to an LLM to maximize the LLM’s efficacy), LLMs can
be quite effective writing code *de novo*. This is especially valuable
for code that is experimental or auxiliary or otherwise throwaway. The
closer code is to the system that we ship, the greater care needs to be
shown when using LLMs. Even with something that seems natural for LLM
contribution (e.g., writing tests), one should still be careful: it’s
easy for LLMs to spiral into nonsense on even simple tasks.

</div>

<div class="paragraph" lineno="261">

As with so many things, using LLMs to aid in programming requires
judgement and balance: they can be extraordinarily useful across an
entire spectrum of software activity, and shouldn’t be dismissed out of
hand. But any implicit dependency on an LLM to comprehend or evolve a
system must also be strenuously resisted: we do not want to become as
gavage geese, being force-fed unnecessary complexity in hopes that an
LLM will somehow spare us from asphyxiation.

</div>

<div class="paragraph" lineno="268">

Wherever LLM-generated code is used, it becomes the responsibility of
the engineer. As part of this process of taking responsibility,
**self-review** becomes essential: LLM-generated code should not be
reviewed by others if the responsible engineer has not themselves
reviewed it. Moreover, once in the loop of peer review, generation
should more or less be removed: if code review comments are addressed by
wholesale re-generation, iterative review becomes impossible.

</div>

<div class="paragraph" lineno="276">

In short, where LLMs are used to generate code, responsibility, rigor,
empathy and teamwork must remain top of mind.

</div>

</div>

</div>

</div>

<div class="sect1">

## <span id="_llm_anti_patterns" class="anchor" aria-hidden="true"></span><a href="#_llm_anti_patterns" class="link group">LLM anti-patterns<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="sectionbody">

<div class="paragraph" lineno="281">

There are some obvious pitfalls of LLM usage that are worth calling out,
not because we at Oxide are in any particular danger of falling into
them, but because others are (or seem to be) — and they constitute
behavior that we absolutely want to avoid.

</div>

<div class="sect2">

### <span id="_llm_mandates" class="anchor" aria-hidden="true"></span><a href="#_llm_mandates" class="link group">LLM mandates<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="paragraph" lineno="288">

LLMs are certainly valuable tools, but some organizations — either out
of executive capriciousness, misguided micromanagement, or something
darker — have mandated (or otherwise strongly incentivized) their
organization’s use of LLMs. Such decrees are absurd: they undermine the
autonomy and mastery essential in our work. As with any tool, we should
feel empowered to use LLMs, but not obligated to do so: we trust
ourselves to choose the best tool for the job, be it LLM or no.

</div>

<div class="paragraph" lineno="296">

Executive fiats with respect to LLM usage will not be forthcoming.

</div>

</div>

<div class="sect2">

### <span id="_llm_shaming" class="anchor" aria-hidden="true"></span><a href="#_llm_shaming" class="link group">LLM shaming<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="paragraph" lineno="300">

Conversely, some have decided that they not only oppose LLM use for
themselves, but wish to out or otherwise shame those that are making use
of LLMs. Aside from the impracticalities of this position (e.g., as LLMs
become the foundation for technologies like search, it will become
increasingly difficult to attest to one’s own purity), such strident
opposition undermines teamwork.

</div>

<div class="paragraph" lineno="306">

In this regard, LLM use may be viewed as a dietary choice: one may
choose to (say) not eat meat — and at Oxide we wish to empathize with
that disposition by making sure that vegetarian options are available
when we eat together. But just as we accommodate those choices, those
who make them must understand that others will make different
decisions — and it is decidedly anti-social to interrupt someone’s meal
to register disapproval with their choice of entrée.

</div>

</div>

<div class="sect2">

### <span id="_llm_anthropomorphization" class="anchor" aria-hidden="true"></span><a href="#_llm_anthropomorphization" class="link group">LLM
anthropomorphization<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="paragraph" lineno="315">

LLMs can (obviously) feel human-like, which has inspired some to close
the loop entirely, explicitly anthropomorphizing LLMs with a prompt that
constitutes a persona. Especially when coupled with realistic
(LLM-powered!) voice generation, the result can be uncanny — and
perilous: an LLM is (emphatically!) not a person, and in particular
cannot be held accountable; to anthropomorphize an LLM is to imply a
responsibility that they cannot take. (For an amusing — and
horrifying — treatment of the absolute chaos this can unleash, see the
<a href="https://www.shellgame.co" target="_blank" rel="noopener">Shell
Game podcast</a>.)

</div>

<div class="paragraph" lineno="324">

However tempting anthropomorphizing LLMs may be, it’s not a practice
that we will engage in at Oxide.

</div>

</div>

</div>

</div>

<div class="sect1">

## <span id="_mechanics" class="anchor" aria-hidden="true"></span><a href="#_mechanics" class="link group">Mechanics<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="sectionbody">

<div class="paragraph" lineno="329">

Mechanical details of using LLMs — along with many specific tips and
links — can be found in the (internal) [LLMs at
Oxide](https://github.com/oxidecomputer/meta/tree/master/engineering/llms)
document.

</div>

</div>

</div>

<div class="sect1">

## <span id="_determinations" class="anchor" aria-hidden="true"></span><a href="#_determinations" class="link group">Determinations<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="sectionbody">

<div class="paragraph" lineno="336">

Broadly speaking, LLM use is encouraged at Oxide, but that use must
always be consistent with our deeply-held sense of responsibility: our
responsibility to our product, our responsibility to our customers — and
our responsibility to one another.

</div>

</div>

</div>

<div class="sect1">

## <span id="_external_references" class="anchor" aria-hidden="true"></span><a href="#_external_references" class="link group">External
References<img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld2JveD0iMCAwIDE2IDE2IiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LWFjY2VudC1zZWNvbmRhcnkgbWwtMiBoaWRkZW4gZ3JvdXAtaG92ZXI6aW5saW5lLWJsb2NrIj48ZyBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Im02LjU4NiAxMi4yNDMgMS41OS0xLjU5MWEuNzUuNzUgMCAwIDEgMS4wNjEgMGwuMzU0LjM1M2EuNzUuNzUgMCAwIDEgMCAxLjA2TDggMTMuNjU4QTQgNCAwIDAgMSAyLjM0MyA4bDEuNTkxLTEuNTkxYS43NS43NSAwIDAgMSAxLjA2IDBsLjM1NC4zNTRhLjc1Ljc1IDAgMCAxIDAgMS4wNmwtMS41OSAxLjU5MWEyIDIgMCAxIDAgMi44MjggMi44MjlNMTIuMDY2IDkuNTkxYS43NS43NSAwIDAgMS0xLjA2IDBsLS4zNTQtLjM1NGEuNzUuNzUgMCAwIDEgMC0xLjA2bDEuNTktMS41OTFhMiAyIDAgMSAwLTIuODI4LTIuODI5bC0xLjU5IDEuNTkxYS43NS43NSAwIDAgMS0xLjA2MSAwbC0uMzU0LS4zNTNhLjc1Ljc1IDAgMCAxIDAtMS4wNkw4IDIuMzQyQTQgNCAwIDAgMSAxMy42NTcgOHoiIC8+PHBhdGggZD0iTTkuOTQ1IDUuNzAyYS43NS43NSAwIDAgMC0xLjA2MSAwTDUuNzAyIDguODg0YS43NS43NSAwIDAgMCAwIDEuMDZsLjM1My4zNTRhLjc1Ljc1IDAgMCAwIDEuMDYxIDBsMy4xODItMy4xODJhLjc1Ljc1IDAgMCAwIDAtMS4wNnoiIC8+PC9nPjwvc3ZnPg=="
class="text-accent-secondary ml-2 hidden group-hover:inline-block" /></a>

<div class="sectionbody">

<div class="ulist bibliography" lineno="344">

- <span id="rfd3"></span>\[rfd3\] Oxide Computer Company. RFD 3 Oxide
  Hiring Process. <a href="/rfd/0003" class="bare"
  data-discover="true">https://rfd.shared.oxide.computer/rfd/0003</a>.

- <span id="pangram4"></span>\[pangram4\] Ben Glickenhaus, Katherine
  Thai, Jenna Russell, Elyas Masrour, Yue Han, Max Spero, and Bradley
  Emi, *Pangram 4 Technical Report*,
  [arXiv:2607.27183](https://arxiv.org/abs/2607.27183), 2026.

- <span id="shell-game"></span>\[Shell Game\] *Shell Game*, Season 2.
  <a href="https://www.shellgame.co"
  class="bare">https://www.shellgame.co</a>

</div>

</div>

</div>

<div class="1200:sticky 1200:block top-[calc(2rem+(var(--header-height)))] hidden max-h-[calc(100vh-(var(--header-height)+3rem))] w-(--toc-width) shrink-0 grow overflow-auto print:hidden">

- <a href="#_values_in_llm_usage"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1rem">Values in LLM usage</a>
- <a href="#_uses_of_llms"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1rem">Uses of LLMs</a>
- <a href="#_llms_as_readers"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1.5rem">LLMs as readers</a>
- <a href="#_llms_as_researchers"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1.5rem">LLMs as researchers</a>
- <a href="#_llms_as_editors"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1.5rem">LLMs as editors</a>
- <a href="#_llms_as_writers"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1.5rem">LLMs as writers</a>
- <a href="#_llms_in_public_writing"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:2rem">LLMs in public writing</a>
- <a href="#_llms_in_personal_writing"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:2rem">LLMs in personal writing</a>
- <a href="#_llms_in_operational_writing"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:2rem">LLMs in operational writing</a>
- <a href="#_llms_as_code_reviewers"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1.5rem">LLMs as code reviewers</a>
- <a href="#_llms_as_debuggers"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1.5rem">LLMs as debuggers</a>
- <a href="#_llms_as_programmers"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1.5rem">LLMs as programmers</a>
- <a href="#_llm_anti_patterns"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1rem">LLM anti-patterns</a>
- <a href="#_llm_mandates"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1.5rem">LLM mandates</a>
- <a href="#_llm_shaming"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1.5rem">LLM shaming</a>
- <a href="#_llm_anthropomorphization"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1.5rem">LLM anthropomorphization</a>
- <a href="#_mechanics"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1rem">Mechanics</a>
- <a href="#_determinations"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1rem">Determinations</a>
- <a href="#_external_references"
  class="block border-l py-[4px] pr-4 text-tertiary border-secondary hover:text-secondary"
  style="padding-left:1rem">External References</a>

</div>

<div class="fixed inset-x-0 bottom-0 z-10 *:mb-0">

<div class="toc bg-default border-secondary sticky top-[calc(var(--header-height)-1px)] z-10 -mt-px mb-10 block w-full border-t border-b print:hidden 1200:hidden block"
orientation="vertical">

<div state="closed" orientation="vertical">

### Table of Contents <img
src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMiIgaGVpZ2h0PSIxMiIgdmlld2JveD0iMCAwIDEyIDEyIiByb2xlPSJpbWciIGNsYXNzPSJ0ZXh0LXRlcnRpYXJ5IHRyYW5zaXRpb24tYWxsIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik04LjgwNyA2LjU5N2EuNjY3LjY2NyAwIDAgMCAwLTEuMTk0bC01Ljg0Mi0yLjkyQS42NjcuNjY3IDAgMCAwIDIgMy4wNzl2NS44NDJjMCAuNDk2LjUyMi44MTguOTY1LjU5NnoiIC8+PC9zdmc+"
class="text-tertiary transition-all" />

<div id="radix-_R_3apj5_"
class="animated-accordion hydrated border-secondary max-h-[60vh] w-full overflow-y-scroll border-t px-(--container-px)"
state="closed" hidden="" role="region" aria-labelledby="radix-_R_1apj5_"
orientation="vertical"
style="--radix-accordion-content-height:var(--radix-collapsible-content-height);--radix-accordion-content-width:var(--radix-collapsible-content-width)">

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>
