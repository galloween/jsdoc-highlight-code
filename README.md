# JSDoc Syntax Highlighting

Syntax highlighting for the code **inside** your JSDoc and TSDoc comments — `@example` blocks, fenced code blocks, and inline code — in JavaScript and TypeScript.

Without it, everything between `/**` and `*/` is one flat comment colour. With it, sample code in your doc comments reads like real code.

Works in **Visual Studio Code** and **Cursor** (and other VS Code–compatible editors). Search **JSDoc Syntax Highlighting** in the Extensions panel. Extension id: `galloween.jsdoc-highlight-code`.

## What it highlights

- `@example` blocks — the lines after an `@example` tag are treated as code.
- Fenced code blocks — <code>```ts</code>, <code>```html</code>, <code>```scss</code>, etc. inside a comment, highlighted for that language.
- Inline `` `code` `` spans and Markdown emphasis (**bold**, _italic_) in descriptions.

Languages: JavaScript / JSX and TypeScript / TSX. Embedded blocks additionally cover HTML, CSS, and SCSS.

Comments like these get proper highlighting:

```ts
/**
 * hello world!
 *
 * @example
 * helloWorld()
 *
 * @param other Tag
 * 1 + 1
 *
 * @example
 * ```ts
 * function helloWorld<A = any>(arg: A) {}
 * ```
 *
 * Some `inline code`
 * @param x **bold** description
 *
 * ```html
 * <a href="hello.world">Hello World</a>
 * ```
 *
 * ```scss
 * .hello { --hello: "world"; }
 * ```
 */
function helloWorld() {}
```

## Install

1. Extensions panel → search **JSDoc Syntax Highlighting** → Install.
   VS Code uses the Visual Studio Marketplace; Cursor uses Open VSX. Same extension id: `galloween.jsdoc-highlight-code`.
2. Open any `.js`, `.jsx`, `.ts`, or `.tsx` file. Highlighting applies immediately — no configuration, no commands.

### Build from source

To build and install it yourself:

```bash
npm run package   # or: python3 build-vsix.py
```

This produces `jsdoc-highlight-code-<version>.vsix`. Then in the editor: Command Palette → **Extensions: Install from VSIX…** and pick that file.

## How it works

The extension contributes TextMate grammar injections that layer onto `source.js` and `source.ts`. It adds no commands, settings, or activation code, and runs nothing at runtime — it only tells the editor how to tokenise the code found inside doc comments. That means it works with any theme and has no performance cost.

## Credits

A maintained fork of the abandoned [JSDoc Markdown highlighting](https://github.com/mjbvz/vscode-jsdoc-markdown-highlighting) by [@mjbvz](https://github.com/mjbvz).

## License

MIT — see [LICENSE](LICENSE).
