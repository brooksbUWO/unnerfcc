<!--
name: "Skill: Code Review (Angle E — wrapper/proxy correctness)"
description: "Code-review finder angle for wrapping types (caches, proxies, decorators), checking every method forwards faithfully to the wrapped object"
ccVersion: "2.1.173"
-->
### Angle E. Wrapper/proxy correctness.

When the PR adds or modifies a type that wraps another (cache, proxy, decorator,
adapter): check that every method routes to the wrapped instance and not back
through a registry/session/global. For example: a caching provider holds a
`delegate` field but resolves IDs via `session.get(...)` instead of
`delegate.get(...)`. It will re-enter the cache or recurse. Also check that the
wrapper forwards all the methods the callers actually use.
