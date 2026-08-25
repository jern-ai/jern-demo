# Project conventions

jern reads this file and puts it in the agent's system prompt, so it is part
of how the agent behaves — which is why changing it shows up in CI.

- When a test encodes the intended behavior, fix the source, never the test.
- Keep the functions in `src/` pure: no I/O, no globals.
- Make the smallest change that makes the suite pass.
