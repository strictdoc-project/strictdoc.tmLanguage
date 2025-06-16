# Publishing the StrictDoc VSCode Extension

This document explains how to package and publish the extension to the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/).

## 1. Checklist before publishing

* ✅ Version in `package.json` has been bumped.
* ✅ Only necessary files are included in the `.vsix` package.
* ✅ `.vscodeignore` is up-to-date and excludes:

  * tests/\*\*
  * parse\_syntax.js
  * .github/\*\*
  * assets/\*\*
  * node\_modules/\*\* (if not needed at runtime)
  * any other internal scripts or data

## 2. Bump the version

### 2.1. manually (recommended)

Update `version` in `package.json` (manually):

```json
"version": "0.2.1"
```

> ⚠️ This must be **higher** than the currently published version.

### 2.2. automatically via npm version

You can also use:

```bash
npm version patch|minor|major
```

it will:
  * Update the version number in package.json and package-lock.json;
  * Automatically create a Git commit with a message like v0.2.2;
  * Create a Git tag with the same version name (v0.2.2).

If you want to avoid creating the commit and tag, use the --no-git-tag-version flag:

```bash
npm version patch --no-git-tag-version
```

## 3. Build the extension

Run:

```bash
vsce package
```

This generates a `.vsix` file (e.g., `strictdoc-0.2.1.vsix`).

## 4. Publish to Marketplace

If not logged in:

```bash
vsce login StrictDoc
```

To publish:

```bash
vsce publish
```

## 5. Verify

Check that the version and content appear here (may take a minute or two):

* [https://marketplace.visualstudio.com/items?itemName=StrictDoc.strictdoc](https://marketplace.visualstudio.com/items?itemName=StrictDoc.strictdoc)

---

## Notes

* Images used in `README.md` will be loaded from GitHub if paths are relative.
* You don't need to ship them inside `.vsix`.
* Use the `docs/` folder for internal notes, not visible on Marketplace.
