[![Castle Game Engine Logo](https://castle-engine.io/images/castle_game_engine_icon.svg) Castle Game Engine](/)

- [Download](https://castle-engine.io/download)
- [Features](https://castle-engine.io/features)
- [News](https://castle-engine.io/wp/)
- [Documentation](#)
  - [Tutorial: 3D physics fun](https://castle-engine.io/bad_chess)
  - [Manual](https://castle-engine.io/manual)
  - [Creating Game Data](https://castle-engine.io/creating_data_intro.php)
  - [API Reference](https://castle-engine.io/apidoc/html/index.html)
  - [Why Pascal?](https://castle-engine.io/why_pascal)
  - [Modern Object Pascal Introduction](https://castle-engine.io/modern_pascal)
  - [Overview for Unity Developers](https://castle-engine.io/castle_game_engine_for_unity_developers)
  - [Scene Graph: X3D nodes](https://castle-engine.io/x3d)
  - [Conferences](https://castle-engine.io/conferences)
- [Videos](https://www.youtube.com/c/CastleGameEngine)
- [Model Viewer](https://castle-engine.io/castle-model-viewer "Viewer for glTF, X3D, Collada, sprite sheets and other 3D and 2D model formats")
- [Community](https://castle-engine.io/talk.php "Ask for help, report bugs, discuss features")
- [Gallery](#)
  - [Games](https://castle-engine.io/gallery_games.php)
  - [Tools](https://castle-engine.io/gallery_tools.php)
  - [Additional Components](https://castle-engine.io/additional_components.php)
  - [Assets (3D and 2D Graphics, Sound)](https://castle-engine.io/assets.php)
- 
- [Release notes](https://castle-engine.io/release)

[Donate](https://patreon.com/castleengine) [Book a Meeting](https://calendar.proton.me/bookings#IFp0_KuiKOQDieI7o4imzSQaYVPbmjaG2eL3ihaGop0=)

[Home](/) » [Documentation](https://castle-engine.io/documentation) » [Manual](https://castle-engine.io/manual) » [Helping in engine development](https://castle-engine.io/helping)

[Previous: Coding Conventions](https://castle-engine.io/coding_conventions)

 

Manual

# Using AI when contributing to Castle Game Engine

Table of Contents

- [1. Summary of the summary](#_summary_of_the_summary)
- [2. Summary](#_summary)
- [3. Introduction](#_introduction)
- [4. Requirements](#_requirements)
- [5. Guidelines to use AI successfully (when contributing, or using in your own projects)](#_guidelines_to_use_ai_successfully_when_contributing_or_using_in_your_own_projects)
- [6. Guidelines to successfully develop applications using Castle Game Engine, with or without AI](#_guidelines_to_successfully_develop_applications_using_castle_game_engine_with_or_without_ai)
- [7. Don’t violate copyrights / licenses when using AI](#_dont_violate_copyrights_licenses_when_using_ai)
  - [7.1. Context: why this is a problem](#_context_why_this_is_a_problem)
  - [7.2. Guideline: Do diligence to avoid copyright/license violations](#_guideline_do_diligence_to_avoid_copyrightlicense_violations)
- [8. See also](#_see_also)

## 1. Summary of the summary

**When working to solve the problem, we should be gaining understanding (of the problem, our available tools, solutions…​), not losing it.**

- Don’t use AI in a way that makes you dumber. Don’t make solutions that are unmaintainable, poorly understood, badly designed, mixed with hallucinated docs or assumptions.

- Do use AI in a way that makes you smarter. Reach the right solution by extra information and reviews (that you understand and agree with), reach it faster by suggestions (that you understand, and can confirm they point you in the right direction).

## 2. Summary

This page documents *required rules* when using AI to contribute to *Castle Game Engine*. It also collects our *recommended guidelines* when using AI in your own projects.

- **You are responsible** for everything you submit: code, documentation, commit messages, issue/PR descriptions.

- **Understand everything** you submit. Know the reasons behind it. Do your own research and decision-making.

- **Be critical** of AI suggestions. They may contain hallucinations or unoptimal approaches.

- **Keep AI conversations private**. Don’t clutter issues with your conversations with AI.

A good rule of thumb is to **generate smaller, not larger, pieces of code / documentation**.

- **AI-generated larger pieces of code / documentation are often wrong.** They confuse you (suggesting further work in the wrong direction), they show hallucinated or deprecated APIs, they do not use recommended approaches (e.g. AI often puts everything in one big program file, which makes the application non-[cross-platform](cross_platform) and ignores our [views](views) concept to organize applications), they do not understand the platform-specific and compiler-specific language nuances etc.

- **Do start with small tasks for AI.** Use AI for code completion (and reject without hesitation wrong suggestions). Use agents for smaller tasks that you have an idea how to solve yourself. Ask questions about the codebase "how is X done" (and check the answer).

## 3. Introduction

Note

Unlike most of our engine documentation, parts of this text are written in my personal ([hi, I’m Michalis](https://michalis.xyz/)) voice, sharing my personal experience. I hope this helps you understand the reasoning behind some of the statements.

Also, I’m sorry it’s a long text. Ironically, being too verbose is also a complaint we often have about AI-generated stuff. I can only hope that my human writing is more entertaining / informative :)

From my conversations with fellow developers, I know we’ve all tried using AI, and we all have our share of *success stories* and *failure stories (cautionary tales)*.

- One of my personal early successes was using AI to help me add [Sketchfab Integration](https://castle-engine.io/wp/2023/06/09/import-models-from-sketchfab-using-castle-game-engine-editor/) to our [editor](editor). AI’s knowledge of the Sketchfab API was very helpful, and it was capable of using our [`TCastleDownload`](https://castle-engine.io/apidoc/html/CastleDownload.TCastleDownload.html) for the task, when instructed to use it.

  Since then, I’ve been using AI for many tasks — code completion, code exploration, self reviews…​ I recognize it’s just a probabilistic machine that repeats, with only a certain probability of being right, the "Internet wisdom" — nothing more, nothing less.

- One of my personal failures, quite recent actually (2025), was asking AI for a proof of [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem). AI incorrectly combined a few different ways to go about proving this theorem, and it made a nonsensical step in the middle of the proof, temporarily changing the meaning of the symbols and claiming invalid things about the situation. To make matters worse, this incorrect answer from AI looked *plausible* (if you just scan it quickly without really comprehending each step, you will nod your head and say *"yes, that sounds about right"*), and it was stated with *confidence*. Since AI is trained to produce output that sounds plausible and confident.

  The educational implications of such AI mistakes are worrying. Think about children who want to learn math and ask AI such a question, perhaps because they didn’t understand the proof their teacher showed during a school lesson, so they come home and ask AI for help. If I were 10 years old and used AI to help me understand the Pythagorean theorem proof, I would conclude *"well, one step in this proof doesn’t look right; I’m probably too stupid to understand it"*. It’s only because I’m older (and more confident in my own math skills) that I can see the reality: *"one step in this proof is incorrect; AI is wrong because it’s just a probabilistic machine guessing what to tell me to sound most plausible"*.

With this introduction, let’s jump into recommendations and rules about using AI to contribute to *Castle Game Engine*.

Warning

One last disclaimer: This page doesn’t discuss the aspects of AI beyond *"using AI to write Pascal code in the context of our engine"*. We don’t discuss here the fact that AI was trained on copyrighted data (sometimes non-public) and can regurgitate it when asked, without caring about attribution or licensing. Or various clear abuses of AI, like generating spam (such as on our [forum](https://forum.castle-engine.io/)). Or the existential dread where does this progress lead, thinking years ahead. Or using AI to make good art (2D or 3D). The topic is broad. Let’s focus for now on how to use what you have, right now, to help you write good code.

## 4. Requirements

- The core rule is that you are responsible for every line of code and every sentence in documentation (in code, in issue/PR descriptions) that you submit. If it’s nonsense or unoptimal, you should make it better.

- Do not submit code you don’t understand. If AI has suggested a solution, we expect you to analyze every line of it and adjust if necessary before submitting.

  Consider:

  - Is the proposed solution the right way to solve the problem? Is this how you would go about it, if you forget about AI for a second?

  - Whether it is maintainable (apply software design principles like [DRY (Don’t Repeat Yourself)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) and [KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)).

  - Whether it follows the engine [coding conventions](coding_conventions) and uses the right engine API. And yes, you can help AI by pointing it to our docs. [Our manual is in the AsciiDoctor format](https://github.com/castle-engine/cge-www/tree/master/htdocs/doc) which is just a text with trivial markup and AI can process it effortlessly.

  - Whether it supports all our compilers and platforms. AI is often mistaken about nuances here; our CI/CD helps detect issues.

- The same goes for documentation and issue/PR descriptions. Make sure it’s good documentation, simple, and to the point. Documentation must actually help human developers, not be just *"something you had to provide, so you asked AI to produce something that looks plausible, to pass the review"*.

  Especially watch out for overly long and marketing-style statements. We don’t want long documents with emoticons claiming that *"this is the best solution in the world"*. And while being grammatically correct is nice, it’s not the most important thing we look for in good documentation.

  We look for documentation that is *precise*, *practically helpful* (no marketing buzzwords, just explain the problem and solution), and *concise* (shorter is better).

  See my [own test, using an AI agent to develop MCP](https://github.com/castle-engine/castle-engine/pull/694) where AI produced…​ a useful start, but it required a lot of fixes (to even make this start be correct, as AI tried to extend the test suite, failed, and happily assumed it’s all good; it also implemented 2 solutions, both wrong in different ways, at the beginning). And it’s still far from a useful solution, it cannot be used in a way we need, and it’s only a mockup that isn’t aware of the real project. Yet AI confidently claims in the PR that *"This implementation makes Castle Game Engine the first game engine with comprehensive MCP support"*. It’s a hilariously invalid statement :)

- Don’t fill issues with your conversation with AI. This particularly applies to conversations with *GitHub Copilot*. Yes, GitHub encourages you to use *GitHub Copilot* in various contexts throughout their website (and maintainers [cannot even block it](https://github.com/orgs/community/discussions/159749)) --- but it’s not a good practice. We don’t want to read your conversation with AI (sometimes filled with hallucinations, sometimes overly verbose and off-topic). If you want to talk with AI or iterate on code with AI, do it in your own space, without distracting other developers. For example, use a text editor that has AI integration. Review AI-proposed changes before anything gets committed.

- Don’t respond with AI-generated answers to our questions. We value what *you* think; we value the *real* reasons behind the decisions you made. We don’t value AI justifying the changes in an attempt to convince the human reviewer that *"it’s good, merge it"*.

## 5. Guidelines to use AI successfully (when contributing, or using in your own projects)

- You, as a human programmer, must be in charge.

- Start by *asking AI to help you understand the code*.

  - Ask AI questions about particular code pieces, small or large.

  - Ask AI to find bugs or memory leaks, to proofread your submission.

  - Let AI analyze a codebase and describe how things work.

  - Use AI to search for things (esp. things that are beyond "grep search"; e.g. you don’t know how it is called, but you know that there exists *"something that allows you to add two 3D vectors"*; AI can find it and tell you to `var A, B, C: TVector3; A := B + C;`).

  *Still, never trust the answer without double-checking it. Remember my cautionary tale about the Pythagorean theorem above. When the answer is not obvious, AI will hallucinate (tell you a lie) and be confident about it.*

- Use AI for *code completion*, i.e. suggestions in text editors. This allows AI to augment deterministic code completion (like from our [VS Code extension, which uses Lazarus CodeTools for code completion](https://castle-engine.io/vscode)), and in simple cases, the suggestions may be correct and save you some typing.

  Accept suggestions if they make sense. If you look at the suggestion and you can immediately see *"yes, that’s exactly what I wanted to type, thanks!"*.

  Reject suggestions if they don’t make sense or you’re not sure what they do or why. Don’t hesitate to reject AI work, and don’t over-analyze AI answers to find *"nuggets of truth"* in an incorrect answer. AI is just guessing to please you, based on what it was trained on.

- Use AI for *code reviews*. It’s useful to have another set of eyes look at your code changes. Before committing, you can e.g. ask *"review uncommitted changes"*.

  Don’t blindly trust the review. If AI recommends this or that change, understand why, check whether the recommendations are suitable in this case, check that it’s not hallucinating or misunderstanding how to change the code, in other words judge for yourself.

  That said, such "extra pair of eyes" is often useful in my experience. Some of the things AI can point out during the review are valid. By addressing (some of) the review notes, I make much better commits.

- *AI agents* should be used with caution and only with full understanding.

  Don’t throw a hard task at AI, hoping it will *solve it for you in one shot*. Split the task into smaller pieces (make a "TODO list" for the agent). Specify the conditions for the task (do X using Y and Z, e.g. "communicate with X using its REST API and engine TCastleDownload class", or "introduce a method to class X doing this"). Always consider how to refactor the solution to be simplest and most maintainable. AI output is supposed to be a starting point for you, not the final solution.

  Note

  Special recommendation applies to *starting a new project with AI*. **Do not** tell AI to "just create a new game using Castle Game Engine" — as then it can make a bad starting point, ignoring our [views](views), going against our recommended setup for cross-platform projects, making visual designing impossible etc.

  Instead, **tell AI to create a new project using `castle-engine create empty` command-line** (see our [build tool](build_tool) commands) and then turn this into your desired game.

  Note

  Don’t worry, *visual designing* in our editor doesn’t conflict with editing the project with AI agents. Our designs are just JSON files, and agents are capable of modifying these JSONs. So the agents can cooperate with visual designing effectively.

  In fact, *do not* let agents do all the work by writing Pascal code, when instead they should modify design JSON files. The AI agents tend to solve too many tasks by writing Pascal code, because the AI is happy to write long spaghetti boilerplate code. But this is not good for further modification — the effect of setting up components using Pascal code can only be observed at run-time, you cannot edit the design in the editor. Guide the AI to add/modify components by editing our designs (`.castle-user-interface`, `.castle-transform` JSON files) when possible.

- Look whether there’s an existing solution to your problem outside of AI. For example, create a new project using our [editor’s](editor) *"New Project"* feature (instead of asking AI to start a project). Or look into our [examples](https://github.com/castle-engine/castle-engine/tree/master/examples) for something similar to what you’re trying to do. Starting from something correct (and using an AI agent to customize the solution for your needs) is better than forcing AI to guess a big solution from scratch.

  And again, remember that you are responsible for the solution, both code and documentation. Don’t submit it without reviewing it. Don’t submit any code or documentation that you don’t understand. Don’t use any language constructs that you don’t understand.

  Basically, ask AI to *"fill the gaps"* for you, to help you. If you ask it to do design work (propose a solution for you), be very critical of the answer — maybe it’s a good start, or maybe it requires refactoring to be useful, or maybe it’s best to reject it and try another approach.

## 6. Guidelines to successfully develop applications using Castle Game Engine, with or without AI

Whether you use AI or not, common recommendations apply:

- Learn to use the engine by [watching our tutorials](https://www.youtube.com/@CastleGameEngine), [reading our tutorials](https://castle-engine.io/bad_chess), and [following our manual](manual).

- Use the editor to create a new project and see what API the project is using. Think about how you want to extend it. Look in our [API documentation](https://castle-engine.io/apidoc/html/index.html) to learn what things do.

- Start small. Experiment by creating simple games, that seem like "typical use of the engine". Start with the engine’s *"New Project"* templates. Extend it, reading the necessary documentation along the way.

- Use version control. [Git](https://git-scm.com/) is currently the most popular version control system. Using version control allows you to review your own changes and/or changes proposed by AI.

## 7. Don’t violate copyrights / licenses when using AI

### 7.1. Context: why this is a problem

The AI models have been trained on publicly available data, in many cases on open-source projects, ignoring copyrights and licenses of these projects. AI output doesn’t attribute proper copyrights and so using it may violate licenses (in particular copyleft licenses like GPL).

Strictly speaking, the output of any tool should be covered by the same copyrights / licenses as the input it was processing, that was the rule that was obeyed before AI got popular. Yet AI companies have ignored this, the AI output is a mixture of various sources, without proper attribution or licensing for any of them. And indeed AI output can easily produce code that is identical or very similar to the code it was trained on. Sadly, copyright / licensing has been ignored by AI training and there is no one challenging this in court (successfully).

Watch the talk [AI generated violations of FOSS Licenses](https://www.youtube.com/watch?v=xvuiSgXfqc4) for funny + sad examples.

Note

A special note addressing notions I’ve heard that *"copyright is outdated, we live in a post-copyright world etc."*. No: copyright is essential, in future as in the past.

Without the copyright and licenses, everything (including all open-source code, like our engine, and all proprietary code, like proprietary AI tools and training software) would be in the *public domain*. This means everything you may ever do (code, art) would not be automatically owned by you, thus you cannot e.g. gain from selling it (like selling proprietary software, or selling books!) or protect it (like making sure people are obligated to share improvements to your open-source code, like copyleft licenses do).

Copyright and licenses are still the basis of all work ownership (software and beyond).

### 7.2. Guideline: Do diligence to avoid copyright/license violations

Do **reasonable due diligence to make sure your AI-generated code doesn’t infringe any copyrights or licenses**. This means that if you generate a significant portion of new code → search for similar code, using normal web search, and using AI review, before committing it.

Again, see the [talk linked above](https://www.youtube.com/watch?v=xvuiSgXfqc4) for examples how AI can easily produce code that is identical or similar to the code it was trained on, and omit (or even falsify) the original author and license. The problem is real.

Submitting code that is covered by a specific copyright/license, and not including that copyright/license, and ignoring the license requirements → is a violation of the given license. We require that the code you submit be covered by *your* copyright, and it’s your responsibility to make sure that whatever AI generated can indeed be treated as such.

This is yet another reason to **generate *smaller*, not *larger*, pieces of code**. Code-completing a line of code with AI is probably not infringing any copyright/license, it probably mostly follows your own code a few lines above. On the other hand, generating a complete e.g. "*inverse square root implementation"* is almost certainly a violation that will not be attributed to the actual, well-known author.

## 8. See also

In our engine:

- We have experimented even with *vibe coding* for fun, see [https://github.com/michaliskambi/castle-vibes/](https://github.com/michaliskambi/castle-vibes/) for the complete code and data, screenshots, and a [long README with observations](https://github.com/michaliskambi/castle-vibes/blob/master/README.md). We’ve made a [news post summarizing the conclusions](https://castle-engine.io/wp/2026/02/23/ai-usage-guidelines-and-thoughts-updated-and-test-of-vibe-coding-with-castle-game-engine/).

- See also [example situations in the context of Castle Game Engine how AI hallucinations make bad code/docs](https://github.com/chaoss/wg-ai-alignment/issues/16).

Many other projects have nice guidelines about using AI that we agree with. For example:

- [Zulip contribution guidelines about AI](https://github.com/zulip/zulip/blob/main/CONTRIBUTING.md#ai-use-policy-and-guidelines)

- [Python rules about AI](https://devguide.python.org/getting-started/generative-ai/)

- [Collection of various AI / LLM policies of projects](https://github.com/chaoss/wg-ai-alignment/tree/main/moderation#readme)

- [Linux kernel guidelines about AI](https://docs.kernel.org/process/coding-assistants.html) (in particular with explicit mention of copyright issues)

More opinions I agree with:

- [Kurzgesagt video warning about AI slop](https://www.youtube.com/watch?v=_zfN9wnPvU0). There is a real problem of welcoming hallucinations into our knowledge base (Internet).

- I do think that one answer is we need search engines trying to "filter out" AI slop (not amplify it). I’m a happy user of [Kagi](https://kagi.com/) and [agree with their POV about LLMs](https://blog.kagi.com/llms).

- [Article from Addy Osmani "The 80% Problem in Agentic Coding"](https://substack.com/home/post/p-185933546) is a balanced viewpoint I agree with — highlighting both the hope and the dangers of AI agents in coding.

- [Interview with Pi devs](https://www.youtube.com/watch?v=AEmHcFH1UgQ) has lots of valid observations about AI and coding.

------------------------------------------------------------------------

To improve this documentation just [edit this page](https://github.com/castle-engine/cge-www/blob/master/htdocs/doc/ai.adoc) and create a pull request to [cge-www repository](https://github.com/castle-engine/cge-www).

[Previous: Coding Conventions](https://castle-engine.io/coding_conventions)

 

Manual

[Documentation](https://castle-engine.io/documentation)

1.  [Tutorial: 3D physics fun](https://castle-engine.io/bad_chess)
2.  [Manual](https://castle-engine.io/manual)
    1.  [Install](https://castle-engine.io/install)
    2.  [Build your first application](https://castle-engine.io/build_first)
    3.  [Designing user interface and handling events (press, update) within the view](https://castle-engine.io/view_events)
        1.  [Managing Views](https://castle-engine.io/views)
    4.  [Viewport with scenes, camera, navigation](https://castle-engine.io/viewport_and_scenes)
        1.  [Tutorial: Designing a 3D world](https://castle-engine.io/viewport_3d)
        2.  [Creating 2D games](https://castle-engine.io/viewport_2d)
        3.  [Camera](https://castle-engine.io/camera)
        4.  [Navigation](https://castle-engine.io/navigation)
        5.  [Writing code to modify scenes and transformations](https://castle-engine.io/viewport_and_scenes_from_code)
        6.  [Behaviors](https://castle-engine.io/behaviors)
        7.  [Multiple viewports to display one world](https://castle-engine.io/multiple_viewports_to_display_one_world)
        8.  [Expose scene elements, like children transformations, as TCastleScene children](https://castle-engine.io/expose)
    5.  [User interface](https://castle-engine.io/user_interface)
        1.  [Text and fonts](https://castle-engine.io/text)
        2.  [Localization (translating your application)](https://castle-engine.io/localization)
        3.  [Window size and fullscreen](https://castle-engine.io/window_size)
        4.  [Customize loading image](https://castle-engine.io/loading_image)
        5.  [Advanced: custom drawn 2D controls](https://castle-engine.io/ui_custom_drawn)
    6.  [Editor](https://castle-engine.io/editor)
        1.  [Custom Components in Editor](https://castle-engine.io/custom_components)
        2.  [Components to reuse a design in other designs](https://castle-engine.io/reuse_design)
        3.  [Sketchfab](https://castle-engine.io/sketchfab)
    7.  [URLs, loading (downloading) and saving resources](https://castle-engine.io/url)
        1.  [Data directory and castle-data:/ URL protocol](https://castle-engine.io/data)
        2.  [Multi-player](https://castle-engine.io/multi_player)
    8.  [2D games](https://castle-engine.io/2d_games)
        1.  [Sprite sheets](https://castle-engine.io/sprite_sheets)
        2.  [Images](https://castle-engine.io/using_images)
        3.  [Tiled maps](https://castle-engine.io/tiled_maps)
        4.  [How to render 2D games with images and sprites](https://castle-engine.io/how_to_render_2d)
    9.  [Physics](https://castle-engine.io/physics)
    10. [Shaders](https://castle-engine.io/shaders)
    11. [Sound](https://castle-engine.io/sound)
        1.  [OpenAL](https://castle-engine.io/openal)
        2.  [FMOD](https://castle-engine.io/fmod)
    12. [Persistent data (user preferences, savegames)](https://castle-engine.io/user_preferences_savegames)
    13. [Save screen (screenshot)](https://castle-engine.io/save_screen)
    14. [Logging](https://castle-engine.io/log)
    15. [Cross-platform (desktop, mobile, consoles...) projects](https://castle-engine.io/cross_platform)
        1.  [CastleEngineManifest​.xml](https://castle-engine.io/project_manifest)
        2.  [Customize UI scaling, font, warmup cache by CastleSettings.xml](https://castle-engine.io/data_settings)
        3.  [Build Tool](https://castle-engine.io/build_tool)
        4.  [Touch Input](https://castle-engine.io/touch_input)
        5.  [Game Controllers (Joysticks, Gamepads)](https://castle-engine.io/controllers)
    16. [Platforms details](https://castle-engine.io/platforms)
        1.  [Android](https://castle-engine.io/android)
        2.  [Android FAQ](https://castle-engine.io/android_faq)
        3.  [Android Services (Google Play Games and many more...)](https://castle-engine.io/android_services)
        4.  [Adding New Android Services](https://castle-engine.io/adding_new_android_services)
        5.  [iOS](https://castle-engine.io/ios)
        6.  [iOS Services (Apple Game Center and many more...)](https://castle-engine.io/ios_services)
        7.  [In-App Purchases (Android, iOS)](https://castle-engine.io/in_app_purchases)
        8.  [Nintendo Switch](https://castle-engine.io/nintendo_switch)
        9.  [macOS](https://castle-engine.io/macos)
        10. [Web](https://castle-engine.io/web)
    17. [Optimization](https://castle-engine.io/optimization)
        1.  [Occlusion Culling](https://castle-engine.io/occlusion_culling)
        2.  [Profiling Using Valgrind](https://castle-engine.io/profiling_using_valgrind)
        3.  [Detecting Memory Leaks](https://castle-engine.io/memory_leaks)
    18. [Making rendering prettier](https://castle-engine.io/how_to_make_rendering_prettier)
        1.  [Bump Mapping (Normal Maps)](https://castle-engine.io/bump_mapping)
        2.  [Shadow Volumes](https://castle-engine.io/shadow_volumes)
        3.  [Background (skybox, sky and ground)](https://castle-engine.io/background)
        4.  [Fog](https://castle-engine.io/fog)
        5.  [Blending](https://castle-engine.io/blending)
        6.  [Color Space (Gamma Correction)](https://castle-engine.io/color_space)
        7.  [Alpha Bleeding](https://castle-engine.io/alpha_bleeding)
    19. [Skinned animation (Skin node)](https://castle-engine.io/skin)
    20. [Steam](https://castle-engine.io/steam)
    21. [Engine on a form (VCL, FMX, LCL) using TCastleControl](https://castle-engine.io/control_on_form)
    22. [Automatic Builds (Continuous Integration and Delivery)](https://castle-engine.io/automatic_builds)
        1.  [GitHub Actions (automatic builds for GitHub projects)](https://castle-engine.io/github_actions)
        2.  [GitLab CI/CD (automatic builds for GitLab projects)](https://castle-engine.io/gitlab_ci)
        3.  [Woodpecker CI (automatic builds for Codeberg projects)](https://castle-engine.io/woodpecker)
        4.  [Docker (easily get CGE, compilers, texture compression tools)](https://castle-engine.io/docker)
        5.  [Jenkins (automatic builds by your Jenkins server)](https://castle-engine.io/jenkins)
        6.  [Using Castle Game Engine with any CI](https://castle-engine.io/ci)
    23. [Pascal IDEs](https://castle-engine.io/ide)
        1.  [Lazarus](https://castle-engine.io/lazarus)
        2.  [Delphi](https://castle-engine.io/delphi)
            1.  [Delphi packages](https://castle-engine.io/delphi_packages)
            2.  [Delphi for Android and iOS](https://castle-engine.io/delphi_mobile)
            3.  [Delphi for Linux](https://castle-engine.io/delphi_linux)
            4.  [Delphi for macOS](https://castle-engine.io/delphi_macos)
            5.  [C++ Builder](https://castle-engine.io/cpp_builder)
        3.  [Visual Studio Code](https://castle-engine.io/vscode)
    24. [Miscellaneous](https://castle-engine.io/miscellaneous)
        1.  [Which way is up?](https://castle-engine.io/up)
        2.  [Transformation hierarchy](https://castle-engine.io/transformation_hierarchy)
        3.  [CastleWindow Backends](https://castle-engine.io/castlewindow_backends)
        4.  [Threads](https://castle-engine.io/threads)
        5.  [Compiling from source](https://castle-engine.io/compiling_from_source)
        6.  [Supported compilers and IDEs](https://castle-engine.io/supported_compilers)
        7.  [Coding Traps](https://castle-engine.io/coding_traps)
        8.  [Units Map](https://castle-engine.io/units_map)
        9.  [Dedicated GPU](https://castle-engine.io/dedicated_gpu)
        10. [fpcupdeluxe](https://castle-engine.io/fpcupdeluxe)
        11. [FpMake and FpPkg](https://castle-engine.io/fpmake)
        12. [License](https://castle-engine.io/license)
    25. [Helping in engine development](https://castle-engine.io/helping)
        1.  [Donate](https://castle-engine.io/donate)
        2.  [Roadmap](https://castle-engine.io/roadmap)
        3.  [Coding Conventions](https://castle-engine.io/coding_conventions)
        4.  Using AI
3.  [Creating Game Data](https://castle-engine.io/creating_data_intro.php)
4.  [API Reference](https://castle-engine.io/apidoc/html/index.html)
5.  [Why Pascal?](https://castle-engine.io/why_pascal)
6.  [Modern Object Pascal Introduction](https://castle-engine.io/modern_pascal)
7.  [Overview for Unity Developers](https://castle-engine.io/castle_game_engine_for_unity_developers)
8.  [Scene Graph: X3D nodes](https://castle-engine.io/x3d)
9.  [Conferences](https://castle-engine.io/conferences)

Copyright [Michalis Kamburelis](https://michalis.xyz/) and [Castle Game Engine Contributors](https://github.com/castle-engine/castle-engine/graphs/contributors).

This [webpage is also open-source and we welcome pull requests to improve it](https://github.com/castle-engine/cge-www).

We use cookies for analytics. See our [privacy policy](https://castle-engine.io/privacy_policy). ![Scarf Analytics](https://static.scarf.sh/a.png?x-pxid=8fb63cd5-e9ab-4d27-af9b-a979ff518df1)

\<embed src="//castle-engine.io/piwik/piwik.php?idsite=1&rec=1" style="border:0;" /\>
