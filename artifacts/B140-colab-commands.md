# B140 Colab Pro+ reproduction commands

**Execution policy:** run only on a Colab Pro+ CPU/high-RAM runtime. Do not
run `experiments/B140_exact_vandermonde_colab.py` on the local workstation.

After the B140 commit is pushed to `main`, execute these cells in order:

```bash
!git clone --depth 1 --branch main https://github.com/lluiseriksson/hodge-conjecture-research-front.git /content/hodge-conjecture-research-front
!cd /content/hodge-conjecture-research-front && git rev-parse HEAD
```

```bash
!cd /content/hodge-conjecture-research-front && python experiments/B140_exact_vandermonde_colab.py
```

The expected terminal line is `COLAB PASS`, preceded by exact rank
`4t+1` and nullity `1` for every `t=5,...,9`. Record the runtime and commit
SHA after the experiment completes. This stress test is supplementary: the
bounded modular maximal-minor certificate is the decisive finite check.
