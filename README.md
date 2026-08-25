# jern demo — an agent under repository rules

![A terminal session: the rules in force, a golden session replaying clean, one
line of jern.json changed, and the same check failing with the exact
recorded-vs-actual difference](https://jern.ai/demo.gif)

*Real output from this repository — offline, no model called.*

A deliberately small Python project that shows what
[jern](https://jern.ai) adds to a coding agent: **rules the repository
enforces**, a **receipt** for every run, and a **CI gate that catches
behavior changes**. There is no Lisp anywhere in this repository — the whole
setup is one `jern.json`, one baseline, and one workflow.

## The setup

| File | What it does |
|---|---|
| [`jern.json`](jern.json) | The repo's rules: the agent may only edit `src/` and `tests/`, may run `python3` without asking, may not touch MCP tools, and gets at most 12 model calls. |
| [`.jern/baseline.json`](.jern/baseline.json) | The **protected** rules. CI reads this from the *base* commit, so a pull request cannot weaken it by editing its own copy. |
| [`.jern/golden/`](.jern/golden) | A recorded session — a real run of "fix the failing test", kept as a committed snapshot of how the agent handles it. |
| [`.github/workflows/jern.yml`](.github/workflows/jern.yml) | Replays that snapshot on every pull request. Offline: no API key, no model calls. |
| [`CONVENTIONS.md`](CONVENTIONS.md) | Project conventions. jern puts this in the agent's system prompt — which is why editing it changes agent behavior, and why CI notices. |

## What the pull requests demonstrate

Both are open pull requests in this repository:

1. **[#3 — changing the agent's configuration turns the check red.](../../pull/3)**
   It switches the test runner in `jern.json`. The agent would now run a
   different command, so the check fails with the exact difference:

   ```
   diverged from the recording at tool call #11.
     recorded: …"command":"python3 -m unittest discover -s tests -t ."}}
     actual:   …"command":"python3 -m unittest discover -s tests -t . -v"}}
   ```

   No model was called to find that out.

2. **[#2 — a pull request cannot weaken the rules that judge it.](../../pull/2)**
   It widens `edits_within` in its own `jern.json` *and deletes the
   protected baseline*. The check's comment still shows the baseline, read
   from the base commit, in force. Nothing about the agent's behavior
   changed, so the check itself is green — the point is in the policy
   provenance, not the verdict.

Every run also leaves a **receipt**: model calls against budget, tools used,
files actually written, policy decisions, and the trace they came from.

## What a golden check can and cannot see

It re-executes the *agent* against the recording's model and tool results.
So it catches changes to the agent, its configuration, and the policy — and
it does **not** catch a change to a file the agent reads during the run.
Editing [`CONVENTIONS.md`](CONVENTIONS.md) changes what a live run would
see, but the replay still answers that `read_file` from the recording.
Re-record to capture it. (We learned this the honest way: the first version
of this demo claimed otherwise, and the pull request went green.)

## Try it locally

```bash
curl -fsSL https://jern.ai/install.sh | sh     # or: JERN_VERSION=0.14.4 …
jern policy          # every rule in force, and where each came from
jern golden check    # replay the recording — offline, no API key
jern golden list
```

To see the agent actually work (this one needs a provider key):

```bash
export ANTHROPIC_API_KEY=…     # or OPENAI_API_KEY, or none for ollama
jern run "make fahrenheit_to_celsius round to one decimal place"
```

It will ask before writing, refuse to touch anything outside `src/` and
`tests/`, run the test suite after each edit, and print a receipt at the end.

## What this does not claim

A golden session protects the behavior it captured — it is a snapshot, not a
proof. Re-recording is a legitimate way to approve new behavior, so a PR that
changes recordings is *reporting* a change, not proving it safe; that is why
[`.github/CODEOWNERS`](.github/CODEOWNERS) puts `.jern/golden/` and the
baseline behind review. The honest fine print is in jern's
[security model](https://github.com/jern-ai/jern/blob/main/docs/security-model.md).
