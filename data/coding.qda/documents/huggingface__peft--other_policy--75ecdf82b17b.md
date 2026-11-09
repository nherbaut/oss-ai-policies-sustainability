PEFT documentation

Contribute to PEFT

# PEFT

🏡 View all docsAWS Trainium & InferentiaAccelerateBitsandbytesCLIChat UIDataset viewerDatasetsDeploying on AWSDiffusersGoogle CloudGoogle TPUsGradioHubHub Python LibraryHuggingface.jsInference Endpoints (dedicated)Inference ProvidersKernelsLeRobotLeaderboardsLightevalMicrosoft AzureOpenEnvOptimumPEFTReachy MiniSafetensorsSentence TransformersTRLTasksText Embeddings InferenceTokenizersTrackioTransformersTransformers.jsXetsmolagentstimm

Search documentation

mainv0.21.0v0.20.0v0.19.0v0.18.0v0.17.0v0.16.0v0.15.0v0.14.0v0.13.0v0.12.0v0.11.0v0.10.0v0.9.0v0.8.2v0.7.1v0.6.2 ARENESFRIDJAKOPTRUTRVIZH

Get started

[🤗 PEFT](/docs/peft/main/en/index)[Quicktour](/docs/peft/main/en/quicktour)[Installation](/docs/peft/main/en/install)

Guides

[Configurations and models](/docs/peft/main/en/guides/peft_model_config)[Integrations](/docs/peft/main/en/guides/peft_integrations)

Distributed Training

[DeepSpeed](/docs/peft/main/en/accelerate/deepspeed)[Fully Sharded Data Parallel](/docs/peft/main/en/accelerate/fsdp)

[Memory Efficient Training](/docs/peft/main/en/developer_guides/memory_efficient_training)[Model merging](/docs/peft/main/en/developer_guides/model_merging)[Quantization](/docs/peft/main/en/developer_guides/quantization)[Custom models](/docs/peft/main/en/developer_guides/custom_models)[Adapter injection](/docs/peft/main/en/developer_guides/low_level_api)[Mixing PEFT methods](/docs/peft/main/en/developer_guides/mixed_models)[torch.compile](/docs/peft/main/en/developer_guides/torch_compile)[Contribute to PEFT](/docs/peft/main/en/developer_guides/contributing)[Troubleshooting](/docs/peft/main/en/developer_guides/troubleshooting)[PEFT checkpoint format](/docs/peft/main/en/developer_guides/checkpoint)

Methods

[Overview](/docs/peft/main/en/methods/overview)

Soft Prompting

[Cartridges](/docs/peft/main/en/package_reference/cartridges)[CPT](/docs/peft/main/en/package_reference/cpt)[Llama-Adapter](/docs/peft/main/en/package_reference/llama_adapter)[P-Tuning](/docs/peft/main/en/package_reference/p_tuning)[Prefix tuning](/docs/peft/main/en/package_reference/prefix_tuning)[Prompt tuning](/docs/peft/main/en/package_reference/prompt_tuning)

Layer Tuning

[BEFT](/docs/peft/main/en/package_reference/beft)[LayerNorm Tuning](/docs/peft/main/en/package_reference/layernorm_tuning)[Trainable Tokens](/docs/peft/main/en/package_reference/trainable_tokens)

Adapters

[AdaLoRA](/docs/peft/main/en/package_reference/adalora)[AdaMSS](/docs/peft/main/en/package_reference/adamss)[BOFT](/docs/peft/main/en/package_reference/boft)[C3A](/docs/peft/main/en/package_reference/c3a)[DEFT](/docs/peft/main/en/package_reference/deft)[DeLoRA](/docs/peft/main/en/package_reference/delora)[FourierFT](/docs/peft/main/en/package_reference/fourierft)[FRoD](/docs/peft/main/en/package_reference/frod)[GLoRA](/docs/peft/main/en/package_reference/glora)[GraLoRA](/docs/peft/main/en/package_reference/gralora)[HiRA](/docs/peft/main/en/package_reference/hira)[HRA](/docs/peft/main/en/package_reference/hra)[IA3](/docs/peft/main/en/package_reference/ia3)[Lily](/docs/peft/main/en/package_reference/lily)[LoHa](/docs/peft/main/en/package_reference/loha)[LoKr](/docs/peft/main/en/package_reference/lokr)

LoRA

[LoRA](/docs/peft/main/en/package_reference/lora)[Variant: BD-LoRA](/docs/peft/main/en/package_reference/lora_variant_bdlora)[Variant: DoRA](/docs/peft/main/en/package_reference/lora_variant_dora)[Variant: KaSA](/docs/peft/main/en/package_reference/lora_variant_kasa)[Variant: MonteCLoRA](/docs/peft/main/en/package_reference/lora_variant_monteclora)[Variant: VeLoRA](/docs/peft/main/en/package_reference/lora_variant_velora)

[MiSS](/docs/peft/main/en/package_reference/miss)[OFT](/docs/peft/main/en/package_reference/oft)[OSF](/docs/peft/main/en/package_reference/osf)[PaCA](/docs/peft/main/en/package_reference/paca)[PEANuT](/docs/peft/main/en/package_reference/peanut)[Polytropon](/docs/peft/main/en/package_reference/poly)[PSOFT](/docs/peft/main/en/package_reference/psoft)[PVeRA](/docs/peft/main/en/package_reference/pvera)[RandLora](/docs/peft/main/en/package_reference/randlora)[RoAd](/docs/peft/main/en/package_reference/road)[ShadowPEFT](/docs/peft/main/en/package_reference/shadow)[SHiRA](/docs/peft/main/en/package_reference/shira)[Super-Tuning](/docs/peft/main/en/package_reference/supertuning)[TinyLoRA](/docs/peft/main/en/package_reference/tinylora)[UniLoRA](/docs/peft/main/en/package_reference/unilora)[VB-LoRA](/docs/peft/main/en/package_reference/vblora)[VeRA](/docs/peft/main/en/package_reference/vera)[WaveFT](/docs/peft/main/en/package_reference/waveft)[X-LoRA](/docs/peft/main/en/package_reference/xlora)

API reference

You are viewing main version, which requires [installation from source](/docs/peft/install#source). If you'd like regular pip install, checkout the latest stable version ([v0.21.0](/docs/peft/v0.21.0/developer_guides/contributing)).

![Hugging Face's logo](/front/assets/huggingface_logo-noborder.svg)

Join the Hugging Face community

and get access to the augmented documentation experience

Collaborate on models, datasets and Spaces

Faster examples with accelerated inference

Switch between documentation themes

Sign Up

to get started

Copy page

# Contribute to PEFT

We are happy to accept contributions to PEFT. If you plan to contribute, please read this to make the process as smooth as possible.

## Discuss and obtain approval before opening a PR

Before opening a pull request (including a draft), open or find an issue in [huggingface/peft](https://github.com/huggingface/peft/issues) and discuss your proposed contribution. If there is an existing issue and someone is already working on it, has declared their intent to work on it, or has an open PR, you should not submit a separate PR. Wait for a PEFT maintainer or Hugging Face member to explicitly approve the proposal. If you open an issue, keep the length and complexity of the description in proportion with the complexity of the issue. Often, a short description with a reproducer is more valuable than a long description.

An approval comment contains the message `/peft-triage approved`. It may additionally state the assigned contributor’s name, for example `/peft-triage approved username` or `/peft-triage approved @username`. Opening a PR for an issue you’re not assigned to will lead to closure of said PR.

Link the approved, open issue in your PR description using `#123`, `huggingface/peft#123`, or `https://github.com/huggingface/peft/issues/123`. As an exception, maintainers may designate specific long-running discussions that can be referenced by their full GitHub URL without a separate approval comment. If you reference several issues or discussions, one valid reference is sufficient.

An automated workflow checks PRs for approved open issues or discussions. PRs without a valid reference are automatically closed with an explanation. You can obtain issue approval, update the PR description, and reopen the same PR; please do not create a replacement. If you believe your PR was closed incorrectly, ping the maintainers on the PR.

The independent stale bot can still close inactive items, even if labeled as `triaged`. If you feel like the maintainers have overlooked your contribution, you may ping them, but not earlier than before two weeks of inactivity.

## Installation

Follow these steps to start contributing:

1.  Fork the [repository](https://github.com/huggingface/peft) by clicking on the ‘Fork’ button on the repository’s page. This creates a copy of the code under your GitHub user account.

2.  Clone your fork to your local disk, and add the base repository as a remote. The following command assumes you have your public SSH key uploaded to GitHub. See the following guide for more [information](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

    Copied

    ``` bash
    git clone git@github.com:<your Github handle>/peft.git
    cd peft
    git remote add upstream https://github.com/huggingface/peft.git
    ```

3.  Create a new branch to hold your development changes, and do this for every new PR you work on.

    Start by synchronizing your `main` branch with the `upstream/main` branch (more details in the [GitHub Docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)):

    Copied

    ``` bash
    git checkout main
    git fetch upstream
    git merge upstream/main
    ```

    Once your `main` branch is synchronized, create a new branch from it:

    Copied

    ``` bash
    git checkout -b a-descriptive-name-for-my-changes
    ```

    **Do not** work on the `main` branch.

4.  Set up a development environment by running the following command in a conda or a virtual environment you’ve created for working on this library:

    Copied

    ``` bash
    pip install -e ".[test]"
    ```

    (If PEFT was already installed in the virtual environment, remove it with `pip uninstall peft` before reinstalling it.)

If you are new to creating a pull request, follow the [Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) guide by GitHub.

## Tests and code quality checks

Regardless of the contribution type (unless it’s only about the docs), you should run tests and code quality checks before creating a PR to ensure your contribution doesn’t break anything and follows the project standards.

### Running test and checks

We provide a Makefile to execute the necessary tests. Run the code below for the unit test:

Copied

``` sh
make test
```

Run one of the following to either only check or check and fix code quality and style:

Copied

``` sh
make quality  # just check
make style  # check and fix
```

Running `make quality` will also check if all methods/classes from PEFT’s public API (i.e. everything that’s mentioned in `peft.__all__`) are mentioned in the docs. These errors cannot be fixed by `make style`, you need to make sure to document new items in the public API in the docs to fix this error.

You can also set up [`pre-commit`](https://pre-commit.com/) to run these fixes automatically as Git commit hooks.

Copied

``` bash
$ pip install pre-commit
$ pre-commit install
```

Running all the tests can take a while, so during development it can be more efficient to only [run tests specific to your change](https://docs.pytest.org/en/6.2.x/usage.html#specifying-tests-selecting-tests), e.g. via:

Copied

``` sh
pytest tests/<test-file-name> -k <name-of-test>
```

This should finish much quicker and allow for faster iteration.

### Adding tests

For a general guide on adding new tests, check `tests/README.md`.

If your change is specific to a hardware setting (e.g., it requires CUDA), take a look at [`tests/test_gpu_examples.py`](https://github.com/huggingface/peft/blob/1c1c7fdaa6e6abaa53939b865dee1eded82ad032/tests/test_gpu_examples.py) and [`tests/test_common_gpu.py`](https://github.com/huggingface/peft/blob/1c1c7fdaa6e6abaa53939b865dee1eded82ad032/tests/test_common_gpu.py) to see if it makes sense to add tests there. If your change could have an effect on saving and loading models, please run the tests with the `--regression` flag to trigger regression tests.

## Stale PRs

It can happen that while you’re working on your PR, the underlying code base changes due to other changes being merged. If that happens – especially when there is a merge conflict – please update your branch with the latest changes. This can be a merge or a rebase, and we’ll squash and merge the PR once it’s ready. **Avoid force pushes** to make reviews easier.

## PR description

When opening a PR, please provide a nice description of the change you’re proposing and reference the approved issue as described above. If it relates to other issues or PRs, please reference them as well. Providing a good description not only helps the reviewers review your code better and faster, it can also be used later (as a basis) for the commit message which helps with long term maintenance of the project.

Keep the length and complexity of the PR description in line with the change. We don’t need ten paragraphs of explanation for a trivial one-line change. Don’t restate what is obvious from looking at the diff (e.g. “Fixed the typo in ‘foobaar’).

If your code makes some non-trivial changes, it may also be a good idea to add comments to the code to explain those changes. For example, if you had to iterate on your implementation multiple times because the most obvious way didn’t work, it’s a good indication that a code comment is needed.

If relevant, indicate how you tested the change, e.g. by showing the `pytest` test command or reproducer code.

## Reviewer feedback

After submitting your PR, a maintainer will typically give feedback within a couple of days. If you don’t get any feedback within two weeks, your PR might have slipped their notice; feel free to ping the maintainers then, but no earlier.

If the reviewer provides in-line comments, don’t mark them as resolved if you addressed them. Leave these comments open, as they are helping the reviewer to resume their work.

After working through reviewer feedback, ping the reviewer so that they know the PR is ready to review.

## Bugfixes

Please give a description of the circumstances that led to the bug. If there is an existing issue, please link to it (e.g., “Resolves \#12345”).

Ideally when a bugfix is provided, it should be accompanied by a test for the bug. The test should fail with the current code and pass with the bugfix. Add a comment to the test that references the issue or PR. Without a test, it is more difficult to prevent regressions in the future.

## Documentation improvements

We are happy to have fixes for broken links and missing or unclear documentation. Taking care of examples, making sure that they are up-to-date and running fine in this fast moving environment is also highly appreciated.

Please refrain from sending pull requests that *only* correct typing errors as these generally create more work than they safe. Such changes are better combined with more substantial fixes (such as fixing broken links or extending/updating documentation).

## Add a new PEFT fine-tuning method

New parameter-efficient fine-tuning methods are developed all the time. If you would like to add a new and promising method to PEFT, please follow these steps.

1.  If you’re *not* an author of the original paper, check for existing implementations and double check with the authors that they don’t plan to submit a PR themselves.
2.  Open a proposal issue and wait for explicit approval as described above, before starting the core integration work listed below.
3.  Check recent commits for new PEFT methods being added to take as inspiration.
4.  After the proposal is approved, it can be useful to open a draft PR early once the method basically works and first tests pass, then ask for feedback. Reference the approved issue in the draft PR description.

### Core integration of a new PEFT method

- [ ] Open an issue on `huggingface/peft` and obtain explicit approval before investing too much work.
- [ ] Link the source of the method, usually the final paper or another stable primary reference. We want to avoid work that is still under review, as the implementation should be stable.
- [ ] Add a new `PeftType` entry in `src/peft/utils/peft_types.py`.
- [ ] Create a new tuner package under `src/peft/tuners/` with the files your method needs (typically: `config.py`, `model.py`, `layer.py`, and `__init__.py`).
- [ ] Register the method in the tuner `__init__.py` with `register_peft_method(...)`.
- [ ] Export the new config/model from `src/peft/tuners/__init__.py` and `src/peft/__init__.py`.
- [ ] If the method needs default target modules for Transformers models, add the mapping in `src/peft/utils/constants.py`.
- [ ] Add the method to the test matrix in `tests/test_custom_models.py` as these are the broadest and quickest tests. Check that the tests pass with `pytest tests/test_custom_models.py -k <method-name> -v`, fix failures if any.
- [ ] Run style/quality checks with `make style` before pushing.
- [ ] In the PR description, explain the method, link the paper, summarize tradeoffs, and list what was added.

### Full PR to add a new PEFT method

- [ ] Ensure that the configuration arguments that are specific to the method are well named and explained, don’t assume that the user knows the paper inside out.
- [ ] Follow the naming and coding conventions of PEFT.
- [ ] Ensure that you didn’t accidentally check in unrelated changes, e.g. the code formatter changing unrelated files.
- [ ] If some implementation choices are non-trivial, document them with a code comment.
- [ ] Complete the full test suite (`test_config.py`, `test_decoder_models.py`, etc.) by adding the PEFT method to the test matrix. Ensure that the tests pass.
- [ ] Add docs in `docs/source/package_reference/` with a short explanation, paper link, usage snippet, and autodoc blocks. Explain the pros and cons compared to other methods like LoRA. Register that doc page in `docs/source/_toctree.yml`.
- [ ] Add a runnable example under `examples/` (can be a copy of an existing example), with a short `README.md`.
- [ ] Check the benchmarks in `method_comparison/` and add experiment settings for your new method. This is a good place to sanity check that the PEFT method trains as expected. Include one or two reasonable benchmark configurations (one default, one optimized for the benchmark).
- [ ] Recommended: Add generic quantization support. Instead of having to explicitly add quantization layer types for each quantization method, support generic quantization. As an example, check how it’s implemented in [BOFT](https://github.com/huggingface/peft/tree/main/src/peft/tuners/boft). Extend [https://github.com/huggingface/peft/blob/main/tests/test_quantization.py](https://github.com/huggingface/peft/blob/main/tests/test_quantization.py) by adding your PEFT method there. Ask maintainers for help if needed.

## Making changes to existing PEFT methods

If you make a change to a PEFT method that could potentially change its outputs, thus invalidating already trained checkpoints, we need to take extra precautions. Please check the description at [https://github.com/huggingface/peft/blob/main/.ai/skills/peft-method-changes/SKILL.md](https://github.com/huggingface/peft/blob/main/.ai/skills/peft-method-changes/SKILL.md) for details. The instructions there are meant for both humans and AI.

## Add other features

First open an issue on GitHub with a proposal to add the new feature and wait for explicit approval as described above. This way, you can discuss with the maintainers if it makes sense to add the feature before spending too much time on implementing it.

New features should generally be accompanied by tests and documentation or examples. Without the latter, users will have a hard time discovering your cool new feature.

Changes to the code should be implemented in a backward-compatible way. For example, existing code should continue to work the same way after the feature is merged.

[*Update* on GitHub](https://github.com/huggingface/peft/blob/main/docs/source/developer_guides/contributing.md)

[←torch.compile](/docs/peft/main/en/developer_guides/torch_compile) [Troubleshooting→](/docs/peft/main/en/developer_guides/troubleshooting)

[Contribute to PEFT](#contribute-to-peft)[Discuss and obtain approval before opening a PR](#discuss-and-obtain-approval-before-opening-a-pr)[Installation](#installation)[Tests and code quality checks](#tests-and-code-quality-checks)[Running test and checks](#running-test-and-checks)[Adding tests](#adding-tests)[Stale PRs](#stale-prs)[PR description](#pr-description)[Reviewer feedback](#reviewer-feedback)[Bugfixes](#bugfixes)[Documentation improvements](#documentation-improvements)[Add a new PEFT fine-tuning method](#add-a-new-peft-fine-tuning-method)[Core integration of a new PEFT method](#core-integration-of-a-new-peft-method)[Full PR to add a new PEFT method](#full-pr-to-add-a-new-peft-method)[Making changes to existing PEFT methods](#making-changes-to-existing-peft-methods)[Add other features](#add-other-features)
