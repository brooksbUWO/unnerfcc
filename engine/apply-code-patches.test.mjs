// node --test engine/apply-code-patches.test.mjs
// Regression: minified names may contain `$`. A replacement STRING passed to
// String.replace re-interprets `$2` as capture group 2, so the 2.1.258 guard
// `if(o==="max"&&!$2(n))o="high"` became `if(o==="max"&&!o(n))o="xhigh"` and the
// Skill tool crashed with `o is not a function ('o' is "max")` on any skill whose
// frontmatter says `effort: max`.
import { test } from "node:test";
import assert from "node:assert/strict";
import { applyCodePatches } from "./apply-code-patches.mjs";

const STOCK_2_1_258 =
  'function x(e,n){let o=e;if(typeof o==="string"&&jk(o))o=AU(o,n);' +
  'if(o==="max"&&!$2(n))o="high";if(o==="xhigh"&&!F2(n))o="high";return o}' +
  'function v(e){if(e==="low"||e==="medium"||e==="high"||e==="xhigh")return e;return"high"}';

test("cascade-max-fallback keeps a $-named capability guard intact", () => {
  const { js } = applyCodePatches(STOCK_2_1_258, {});
  assert.match(js, /if\(o==="max"&&!\$2\(n\)\)o="xhigh"/, "guard must still call $2, not the effort string");
  assert.doesNotMatch(js, /!o\(n\)/, "the effort variable must never be called as a function");
});

test("validator-accepts-max survives a $ in the captured parameter name", () => {
  const src = STOCK_2_1_258.replace(/\be==="low"\|\|e==="medium"\|\|e==="high"\|\|e==="xhigh"\)return e/,
    '$1==="low"||$1==="medium"||$1==="high"||$1==="xhigh")return $1');
  const { js } = applyCodePatches(src, {});
  assert.match(js, /\$1==="xhigh"\|\|\$1==="max"\)return/, "validator chain must name the captured param verbatim");
});
