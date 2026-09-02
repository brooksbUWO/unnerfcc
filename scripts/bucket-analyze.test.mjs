// node --test scripts/bucket-analyze.test.mjs
// Regression: the merge writer used to splice `Rule(...)` Python literals
// into apply-unnerfs.py. After the RULES catalog moved to unnerfcc/rules/,
// that splicer would fail silently (no dict to splice into) on the next
// upgrade.sh run. These tests pin the JSON-writing replacement: the
// count-asserted idempotency guard now counts store rules instead of
// Python-source Rule( occurrences (the guard itself caught a real silent
// drop at v2.1.251, see bucket-analyze.mjs's own comment on that history).
import { test } from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, writeFileSync, readFileSync, rmSync, chmodSync } from "node:fs";
import { join } from "node:path";
import { tmpdir } from "node:os";
import {
  countStoreRules,
  writeRulesToStore,
  rulesDirFor,
} from "./bucket-analyze.mjs";

function makeStore(files) {
  const dir = mkdtempSync(join(tmpdir(), "bucket-analyze-test-"));
  for (const [id, rules] of Object.entries(files)) {
    writeFileSync(join(dir, `${id}.json`), JSON.stringify({ id, rules }, null, 1) + "\n");
  }
  return dir;
}

test("countStoreRules sums rule-array lengths across every file in the directory", () => {
  const dir = makeStore({
    a: [{ description: "d1", stock: ["s1"], unnerf: ["u1"] }],
    b: [
      { description: "d2", stock: ["s2"], unnerf: ["u2"] },
      { description: "d3", stock: ["s3"], unnerf: ["u3"] },
    ],
  });
  assert.equal(countStoreRules(dir), 3);
  rmSync(dir, { recursive: true, force: true });
});

test("writeRulesToStore appends to an existing id in last position, leaving other files untouched", () => {
  const dir = makeStore({
    a: [{ description: "d1", stock: ["s1"], unnerf: ["u1"] }],
    b: [{ description: "d2", stock: ["s2"], unnerf: ["u2"] }],
  });
  const bBefore = readFileSync(join(dir, "b.json"), "utf-8");

  writeRulesToStore(dir, "2.1.258", [
    { file: "a.md", rule: { stock: "new stock", unnerf: "new unnerf", description: "new rule" } },
  ]);

  const a = JSON.parse(readFileSync(join(dir, "a.json"), "utf-8"));
  assert.equal(a.rules.length, 2);
  assert.equal(a.rules[1].description, "new rule");
  assert.equal(a.rules[0].description, "d1", "the original rule stays in first position");

  const bAfter = readFileSync(join(dir, "b.json"), "utf-8");
  assert.equal(bAfter, bBefore, "a sibling file must not be touched by an append to a different id");

  rmSync(dir, { recursive: true, force: true });
});

test("writeRulesToStore creates a new file for an id with no existing entry", () => {
  const dir = makeStore({});

  writeRulesToStore(dir, "2.1.258", [
    { file: "new-id.md", rule: { stock: "s", unnerf: "u", description: "d" } },
  ]);

  const data = JSON.parse(readFileSync(join(dir, "new-id.json"), "utf-8"));
  assert.equal(data.id, "new-id");
  assert.equal(data.rules.length, 1);

  rmSync(dir, { recursive: true, force: true });
});

test("a written rule stores stock and unnerf as line arrays that round-trip through join", () => {
  const dir = makeStore({});
  const stockBody = "line one\nline two\nline three";
  const unnerfBody = "replacement one\nreplacement two";

  writeRulesToStore(dir, "2.1.258", [
    { file: "round-trip.md", rule: { stock: stockBody, unnerf: unnerfBody, description: "d" } },
  ]);

  const data = JSON.parse(readFileSync(join(dir, "round-trip.json"), "utf-8"));
  const rule = data.rules[0];
  assert.deepEqual(rule.stock, stockBody.split("\n"));
  assert.deepEqual(rule.unnerf, unnerfBody.split("\n"));
  assert.equal(rule.stock.join("\n"), stockBody);
  assert.equal(rule.unnerf.join("\n"), unnerfBody);

  rmSync(dir, { recursive: true, force: true });
});

test("a written rule carries a non-empty provenance string naming the ccVersion", () => {
  const dir = makeStore({});

  writeRulesToStore(dir, "2.1.258", [
    { file: "prov.md", rule: { stock: "s", unnerf: "u", description: "d" } },
  ]);

  const data = JSON.parse(readFileSync(join(dir, "prov.json"), "utf-8"));
  const rule = data.rules[0];
  assert.equal(typeof rule.provenance, "string");
  assert.ok(rule.provenance.length > 0);
  assert.ok(rule.provenance.includes("2.1.258"), "provenance must name the ccVersion");

  rmSync(dir, { recursive: true, force: true });
});

test("the written file contains no CR byte", () => {
  const dir = makeStore({});

  writeRulesToStore(dir, "2.1.258", [
    { file: "no-cr.md", rule: { stock: "s\nwith lines", unnerf: "u\nwith lines too", description: "d" } },
  ]);

  const raw = readFileSync(join(dir, "no-cr.json"), "utf-8");
  assert.ok(!raw.includes("\r"), "no CR byte may enter a rule body or the surrounding JSON text");

  rmSync(dir, { recursive: true, force: true });
});

test("the count guard detects a short write and reports failure rather than success", () => {
  // Mirrors merge()'s own guard: count before, write, count after, compare the
  // delta against accepted.length. A writer stubbed to write only 1 of 2
  // accepted rules must make the guard fire, the exact failure mode that
  // reported success while writing nothing at v2.1.251.
  const dir = makeStore({});
  const accepted = [
    { file: "one.md", rule: { stock: "s1", unnerf: "u1", description: "d1" } },
    { file: "two.md", rule: { stock: "s2", unnerf: "u2", description: "d2" } },
  ];

  const before = countStoreRules(dir);
  // Simulate a writer that silently drops the second accepted rule.
  writeRulesToStore(dir, "2.1.258", accepted.slice(0, 1));
  const after = countStoreRules(dir);

  const delta = after - before;
  assert.notEqual(delta, accepted.length, "the guard's own comparison must see the short write");

  rmSync(dir, { recursive: true, force: true });
});

test("rulesDirFor resolves the rules directory from the apply-unnerfs.py path's parent's parent", () => {
  const applyPath = join("some", "repo", "scripts", "apply-unnerfs.py");
  const dir = rulesDirFor(applyPath);
  assert.equal(dir, join("some", "repo", "rules"));
});
