# AGENTS.md

Guidance for AI agents and contributors working in this repo.

## What this is

A grammar-only editor extension: TextMate injection grammars that highlight the code
inside JSDoc/TSDoc comments. There is **no TypeScript, no build step, and no runtime
code** — just JSON grammars in `syntaxes/`, contributed via `package.json`. The only
dev dependency is the packaging tool.

## Building the .vsix

```bash
npm run package        # runs: npx --yes @vscode/vsce package
```

This produces `jsdoc-highlight-code-<version>.vsix`. `vsce` reads the name and version
from `package.json`, so bump the version there first. The built `.vsix` is gitignored on
purpose — it is not committed; build it when you need it.

> Note: this repo was originally pinned to `@vscode/vsce@2.15.0`, which is broken on
> current Node (it produces an empty `.vsix`). Use a modern `vsce` (3.x) — the version in
> `devDependencies` — which packages correctly.

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
