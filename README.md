# StrictDoc Markup syntax highlighting using TextMate grammar in JSON format

This repository contains a TextMate grammar package that enables syntax
highlighting for the StrictDoc markup language.

[StrictDoc](https://github.com/strictdoc-project/strictdoc) is:

> Software for technical documentation and requirements management. 

## Demos

### PyCharm

![](assets/PyCharm/Screenshot_PyCharm_1.png)

## Installing in PyCharm

Clone this repository to a good place under your file system:

```bash
git clone git@github.com:strictdoc-project/strictdoc.tmLanguage.git
```

Go to `Preferences / Editor / TextMate Bundles`.

![](assets/PyCharm/Screenshot_PyCharm_2.png)

Click "+". Find and specify the `strictdoc.tmLanguage.git` folder. The folder
should appear in the list bundles. Note: the folder first appears at the bottom
of the list but then goes up when you open the `TextMate Bundles` next time.

![](assets/PyCharm/Screenshot_PyCharm_3.png)

When the settings are saved via `Apply` or `OK`, the syntax of all
open `.sdoc` files should become highlighted right away.
