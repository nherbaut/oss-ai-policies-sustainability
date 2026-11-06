<div id="main" role="main">

<div id="general-coding-guidelines" class="section">

# General coding guidelines<a href="#general-coding-guidelines" class="headerlink"
title="Link to this heading">¶</a>

<div id="use-of-generative-ai" class="section">

<span id="id1"></span>

## Use of generative AI<a href="#use-of-generative-ai" class="headerlink"
title="Link to this heading">¶</a>

AI assistance when working on Wagtail is permitted. Purely AI-generated
contributions are not - if we wanted those, we would prompt an AI agent
ourselves.

As a contributor to the project, we would like you to consider what
value you are providing beyond your ability to paste a bug report into
an LLM. Even if you are not familiar with the Wagtail codebase, your
experience as a Wagtail user or site builder is still valuable for
providing guidance on how a feature should behave, how and where it
should be documented, or manually replicating an issue and verifying
that it has been fixed, perhaps with screenshots. All of this is
information that we would like to see in a PR, as it demonstrates that a
human has understood and thought about the issue being fixed.

For this reason, we ask you to write the pull request description
yourself, and not offload that task to an AI agent.

If you use generative AI for your contribution, please fill in the “AI
usage” portion of the PR description. For example:

> <div>
>
> *“This pull request includes code written by Claude Code. I have
> verified in-browser that this fixes the issue.”*
>
> </div>

<div id="acceptable-uses" class="section">

### Acceptable uses<a href="#acceptable-uses" class="headerlink"
title="Link to this heading">¶</a>

- Gaining understanding of the existing Wagtail code

- Assistance with written English for code comments, documentation and
  pull request descriptions

- Supplementing contributor knowledge for code, tests, and documentation

</div>

<div id="unacceptable-uses" class="section">

### Unacceptable uses<a href="#unacceptable-uses" class="headerlink"
title="Link to this heading">¶</a>

- Entire work (code changes, documentation update, pull request
  descriptions) are LLM-generated without there being a clear
  understanding of the solution implementation from the contributor.

- Responding to questions asked during code review by pasting those
  questions into an LLM

- Allowing an LLM to make unchecked false statements through the use of
  stock phrases, such as claiming to have manually tested a bugfix, or
  claiming to have experience of an issue through a real-world project

We will close those pull requests and issues that are unproductive, so
we can focus our limited maintainer capacity elsewhere.

</div>

</div>

<div id="language" class="section">

## Language<a href="#language" class="headerlink"
title="Link to this heading">¶</a>

British English is preferred for user-facing text; this text should also
be marked for translation (using the
<span class="pre">`django.utils.translation.gettext`</span> function and
<span class="pre">`{%`</span>` `<span class="pre">`translate`</span>` `<span class="pre">`%}`</span>
template tag, for example).

User-facing errors or field validation should use a well-formed sentence
with a period (full stop) at the end.

However, identifiers within code should use American English if the
British or international spelling would conflict with built-in language
keywords; for example, CSS code should consistently use the spelling
<span class="pre">`color`</span> to avoid inconsistencies like
<span class="pre">`background-color:`</span>` `<span class="pre">`$colour-red`</span>.
American English is also the preferred spelling style when writing
documentation.

Learn more about our documentation writing style in
<a href="documentation_guidelines.html#writing-style-guide"
class="reference internal"><span class="std std-ref">Writing style
guide</span></a>.

Learn more about how to make content suitable for translations in
<a href="translations.html#contributing-translations"
class="reference internal"><span
class="std std-ref">Translations</span></a>.

</div>

<div id="file-names" class="section">

## File names<a href="#file-names" class="headerlink"
title="Link to this heading">¶</a>

Where practical, try to adhere to the existing convention of file names
within the folder where added.

Examples:

- Django templates - <span class="pre">`lower_snake_case.html`</span>

- Documentation - <span class="pre">`lower_snake_case.md`</span>

</div>

<div id="naming-conventions" class="section">

## Naming conventions<a href="#naming-conventions" class="headerlink"
title="Link to this heading">¶</a>

<div id="use-classname-in-python-html-template-tag-variables"
class="section">

### Use <span class="pre">`classname`</span> in Python / HTML template tag variables<a href="#use-classname-in-python-html-template-tag-variables"
class="headerlink" title="Link to this heading">¶</a>

<span class="pre">`classname`</span> is preferred for any API /
interface or Django template variables that need to output an HTML
class.

<div id="django-template-tag" class="section">

#### Django template tag<a href="#django-template-tag" class="headerlink"
title="Link to this heading">¶</a>

Example template tag definition

<div class="highlight-python notranslate">

<div class="highlight">

    @register.inclusion_tag("wagtailadmin/shared/dialog/dialog_toggle.html")
    def dialog_toggle(dialog_id, classname="", text=None):
        return {
            "classname": classname,
            "text": text,
        }

</div>

</div>

Example template

<div class="highlight-html+django notranslate">

<div class="highlight">

    {% comment "text/markdown" %}

        Variables accepted by this template:

        - `classname` - {string?} if present, adds classname to button
        - `dialog_id` - {string} unique id to use to reference the modal which will be triggered

    {% endcomment %}

    <button type="button" class="{{ classname }}" data-a11y-dialog-show="{{ dialog_id }}">
        {{ text }}
    </button>

</div>

</div>

Example usage

<div class="highlight-html+django notranslate">

<div class="highlight">

    {% dialog_toggle classname='button button-primary' %}

</div>

</div>

</div>

</div>

<div id="python-django-class-driven-content" class="section">

### Python / Django class driven content<a href="#python-django-class-driven-content" class="headerlink"
title="Link to this heading">¶</a>

<div class="highlight-python notranslate">

<div class="highlight">

    class Panel:
        def __init__(self, heading="", classname="", help_text="", base_form_class=None):
            self.heading = heading
            self.classname = classname

</div>

</div>

<div id="details" class="section">

#### Details<a href="#details" class="headerlink" title="Link to this heading">¶</a>

| Convention | Usage |
|----|----|
| <span class="pre">`classname`</span> | ✅ Preferred for any new code. |
| <span class="pre">`class`</span> | ✳️ Only if used as part of a generic <span class="pre">`attrs`</span>-like dict; however avoid due to conflicts with Python <span class="pre">`class`</span> keyword. |
| <span class="pre">`classnames`</span> | ❌ Avoid for new code. |
| <span class="pre">`class_name`</span> | ❌ Avoid for new code. |
| <span class="pre">`class_names`</span> | ❌ Avoid for new code. |
| <span class="pre">`className`</span> | ❌ Avoid for new code. |
| <span class="pre">`classNames`</span> | ❌ Avoid for new code. |

</div>

</div>

</div>

</div>

</div>
