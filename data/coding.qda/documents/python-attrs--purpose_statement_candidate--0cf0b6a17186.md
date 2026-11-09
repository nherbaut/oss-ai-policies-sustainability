[![attrs](https://raw.githubusercontent.com/python-attrs/attrs/main/docs/_static/attrs_logo.svg)](https://www.attrs.org/)

[![Documentation](https://img.shields.io/badge/Docs-RTD-black)](https://www.attrs.org/en/stable/) [![](https://bestpractices.coreinfrastructure.org/projects/6482/badge)](https://bestpractices.coreinfrastructure.org/projects/6482) [![No AI slop inside.](https://img.shields.io/badge/no-slop-purple)](https://github.com/python-attrs/attrs/blob/main/.github/AI_POLICY.md) [![](https://img.shields.io/pypi/v/attrs)](https://pypi.org/project/attrs/) [![Downloads per month](https://static.pepy.tech/personalized-badge/attrs?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads%20/%20Month)](https://pepy.tech/project/attrs)

*attrs* is the Python package that will bring back the **joy** of **writing classes** by relieving you from the drudgery of implementing object protocols (aka [dunder methods](https://www.attrs.org/en/latest/glossary.html#term-dunder-methods)). Trusted by NASA for [Mars missions since 2020](https://github.com/readme/featured/nasa-ingenuity-helicopter)!

Its main goal is to help you to write **concise** and **correct** software without slowing down your code.

## Sponsors

*attrs* would not be possible without our [amazing sponsors](https://github.com/sponsors/hynek). Especially those generously supporting us at the *The Organization* tier and higher:

[![](docs/_static/sponsors/Variomedia.svg "Variomedia AG")](https://www.variomedia.de/) [![](docs/_static/sponsors/Tidelift.svg "Tidelift")](https://tidelift.com/?utm_source=lifter&utm_medium=referral&utm_campaign=hynek) [![](docs/_static/sponsors/Kraken.svg "Kraken Tech")](https://kraken.tech/) [![](docs/_static/sponsors/Privacy-Solutions.svg "Privacy Solutions")](https://privacy-solutions.org/) [![](docs/_static/sponsors/Klaviyo.svg "Klaviyo")](https://klaviyo.com/) [![](docs/_static/sponsors/FilePreviews.svg "FilePreviews")](https://filepreviews.io/) [![](docs/_static/sponsors/TestMu-AI.svg "TestMu AI")](https://www.testmuai.com/?utm_medium=sponsor&utm_source=structlog) [![](docs/_static/sponsors/Polar.svg "Polar")](https://polar.sh/)

**Please consider [joining them](https://github.com/sponsors/hynek) to help make *attrs*’s maintenance more sustainable!**

## Example

*attrs* gives you a class decorator and a way to declaratively define the attributes on that class:

``` pycon
>>> from attrs import asdict, define, make_class, Factory

>>> @define
... class SomeClass:
...     a_number: int = 42
...     list_of_numbers: list[int] = Factory(list)
...
...     def hard_math(self, another_number):
...         return self.a_number + sum(self.list_of_numbers) * another_number


>>> sc = SomeClass(1, [1, 2, 3])
>>> sc
SomeClass(a_number=1, list_of_numbers=[1, 2, 3])

>>> sc.hard_math(3)
19
>>> sc == SomeClass(1, [1, 2, 3])
True
>>> sc != SomeClass(2, [3, 2, 1])
True

>>> asdict(sc)
{'a_number': 1, 'list_of_numbers': [1, 2, 3]}

>>> SomeClass()
SomeClass(a_number=42, list_of_numbers=[])

>>> C = make_class("C", ["a", "b"])
>>> C("foo", "bar")
C(a='foo', b='bar')
```

After *declaring* your attributes, *attrs* gives you:

- a concise and explicit overview of the class's attributes,
- a nice human-readable `__repr__`,
- equality-checking methods,
- an initializer,
- and much more,

*without* writing dull boilerplate code again and again and *without* runtime performance penalties.

------------------------------------------------------------------------

This example uses *attrs*'s modern APIs that have been introduced in version 20.1.0, and the *attrs* package import name that has been added in version 21.3.0. The classic APIs (`@attr.s`, `attr.ib`, plus their serious-business aliases) and the `attr` package import name will remain **indefinitely**.

Check out [*On The Core API Names*](https://www.attrs.org/en/latest/names.html) for an in-depth explanation!

### Hate Type Annotations!?

No problem! Types are entirely **optional** with *attrs*. Simply assign `attrs.field()` to the attributes instead of annotating them with types:

``` python
from attrs import define, field


@define
class SomeClass:
    a_number = field(default=42)
    list_of_numbers = field(factory=list)
```

## Data Classes

On the tin, *attrs* might remind you of `dataclasses` (and indeed, `dataclasses` [are a descendant](https://hynek.me/articles/import-attrs/) of *attrs*). In practice it does a lot more and is more flexible. For instance, it allows you to define [special handling of NumPy arrays for equality checks](https://www.attrs.org/en/stable/comparison.html#customization), allows more ways to [plug into the initialization process](https://www.attrs.org/en/stable/init.html#hooking-yourself-into-initialization), has a replacement for `__init_subclass__`, and allows for stepping through the generated methods using a debugger.

For more details, please refer to our [comparison page](https://www.attrs.org/en/stable/why.html#data-classes), but generally speaking, we are more likely to commit crimes against nature to make things work that one would expect to work, but that are quite complicated in practice.

## Project Information

- [**Changelog**](https://www.attrs.org/en/stable/changelog.html)
- [**Documentation**](https://www.attrs.org/)
- [**PyPI**](https://pypi.org/project/attrs/)
- [**Source Code**](https://github.com/python-attrs/attrs)
- [**Contributing**](https://github.com/python-attrs/attrs/blob/main/.github/CONTRIBUTING.md)
- [**Third-party Extensions**](https://github.com/python-attrs/attrs/wiki/Extensions-to-attrs)
- **Get Help**: use the `python-attrs` tag on [Stack Overflow](https://stackoverflow.com/questions/tagged/python-attrs)

### *attrs* for Enterprise

Available as part of the [Tidelift Subscription](https://tidelift.com/?utm_source=lifter&utm_medium=referral&utm_campaign=hynek).

The maintainers of *attrs* and thousands of other packages are working with Tidelift to deliver commercial support and maintenance for the open source packages you use to build your applications. Save time, reduce risk, and improve code health, while paying the maintainers of the exact packages you use.
