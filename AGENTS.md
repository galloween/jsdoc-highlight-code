# AGENTS.md

Guidance for AI agents and contributors working in this repo.

## What this is

A grammar-only editor extension: TextMate injection grammars that highlight the code
inside JSDoc/TSDoc comments. There is **no TypeScript, no build step, and no runtime
code** — just JSON grammars in `syntaxes/`, contributed via `package.json`. It has no
npm dependencies.

## Building the .vsix

Use the bundled script, **not** `vsce package`:

```bash
npm run package        # runs: python3 build-vsix.py
```

`vsce package` (and `vsce ls`) silently produce an **empty** `.vsix` here: the manifest
is written but every `extension/` file is dropped (a yazl streaming failure under current
Node). `build-vsix.py` assembles the `.vsix` structure directly and validates it. It reads
the name and version from `package.json`, so bump the version there first.

The built `.vsix` is gitignored on purpose — it is not committed. Build it when you need it.

## Releasing

1. Bump `version` in `package.json` and add a `CHANGELOG.md` entry.
2. `npm run package` → produces `jsdoc-highlight-code-<version>.vsix`.
3. Publish to **both** registries so VS Code and Cursor stay in sync:
   - **Microsoft Marketplace** — <https://marketplace.visualstudio.com/manage> (web upload), or `vsce publish`.
   - **Open VSX** (used by Cursor, VSCodium, Windsurf, Gitpod) — <https://open-vsx.org> (web upload), or `ovsx publish jsdoc-highlight-code-<version>.vsix -p <token>`.

## Notes

- Extension id: `galloween.jsdoc-highlight-code`.
- Icon: `media/icon.png` (128×128).
- A maintained fork of <https://github.com/mjbvz/vscode-jsdoc-markdown-highlighting>.
