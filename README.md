### JSDoc syntax highlighting

Adds syntax highlighting to JSDoc comments (JS, TS, HTML, CSS, SCSS).
Supports @example and fenced code blocks.

This is a modified version of this abandoned extension:
[JSDoc Markdown highlighting](https://github.com/mjbvz/vscode-jsdoc-markdown-highlighting) by @mjbvz.

Comments like these should have code syntax highlighting:

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
