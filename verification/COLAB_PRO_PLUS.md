# Colab Pro+ heavy-verification runbook

Heavy or unbounded verification is not run on the local Windows host. The
following cold-clone cell pins the last published commit containing the B140
verifier, installs its declared verification dependencies, imposes a
30-minute wall-clock limit, and records peak memory on a Colab Pro+ CPU/high
RAM runtime.

```bash
%%bash
set -euo pipefail

REMOTE="https://github.com/lluiseriksson/hodge-conjecture-research-front.git"
PINNED_COMMIT="195eb4e6b5e1282243aec2453de1df826fa4b992"
WORKDIR="/content/hodge-conjecture-research-front"

rm -rf -- "$WORKDIR"
git clone --filter=blob:none "$REMOTE" "$WORKDIR"
cd "$WORKDIR"
git checkout --detach "$PINNED_COMMIT"
python -m pip install --disable-pip-version-check -r requirements-verification.txt

timeout --signal=TERM --kill-after=30s 30m \
  /usr/bin/time -v python verification/verify_B140_quintic_linear_floor.py \
  2>&1 | tee /content/B140-colab-pro-plus.log

git status --short
git rev-parse HEAD
sha256sum /content/B140-colab-pro-plus.log
```

The log, checked-out commit, exit status, peak resident memory, and SHA-256
must be copied into a new artifact before B140 is ever promoted on the basis
of this computational check. A green run verifies only the finite arithmetic
assertions in the script; it is not evidence for the Hodge Conjecture.
