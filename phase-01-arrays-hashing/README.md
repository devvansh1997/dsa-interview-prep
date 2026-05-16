# Hashing Mental Notes

- use dict.get() for counts or keeping track of items in dict
- YOU CAN JUST INITIALIZE DICT using ```defaultdict(list)``` and then whenver a key is being looked up and it doesnt exist, python will create one on the spot for that particular line. SUPER CONVENIENT

---

## Top-K Frequent Elements (347) — Bucket Sort Pattern

### When to use bucket sort
- Anytime values fall in a **known, bounded range** → bucket sort becomes possible
- For frequency problems: any element's count is bounded by `len(nums)`, so frequencies live in `[1, n]`
- Beats heap (O(n log k)) and sort (O(n log n)) → **O(n) total**

### The pattern
1. **Build count map** with hashmap — O(n)
2. **Create buckets** where `index = frequency`, `bucket[i] = list of elements appearing i times`
   - `buckets = [[] for _ in range(len(nums) + 1)]`
   - Multiple elements can share an index, so each bucket is a **list**
3. **Iterate buckets backward** (highest frequency first), collect until you have k elements

### Gotchas I hit
- Using `defaultdict(list)` and assigning `0` instead of leaving as empty list — buckets must hold **lists of elements**, not counts
- `range()` doesn't take keyword args — `range(start, stop, step)` is positional. For backward iteration: `range(n, 0, -1)`
- `answer.append(buckets[i])` appends the whole list → got `[[1], [2]]` instead of `[1, 2]`. Use `extend` to add the elements
- Decrement `k` by `len(buckets[i])` (how many elements you actually added), not by 1

### Takeaways
- **Frequency in known range → bucket sort**
- **Bucket index = value, bucket contents = list**
- **Iterate backward when you want "top" something** — saves an explicit sort

---

## Product of Array Except Self (238) — Prefix & Suffix Pattern

### When to use
- Problem asks for "something about all elements **except** this one"
- Range products / sums where you can't use division
- Anywhere you need "everything to the left × everything to the right" per index

### The pattern
1. `prefix[i]` = product of elements **strictly left** of `i`
2. `suffix[i]` = product of elements **strictly right** of `i`
3. `answer[i] = prefix[i] * suffix[i]`

Base cases: `prefix[0] = 1`, `suffix[n-1] = 1` (nothing on that side).

```python
for i in range(1, n):
    prefix[i] = prefix[i-1] * nums[i-1]

for j in range(n-2, -1, -1):
    suffix[j] = suffix[j+1] * nums[j+1]
```

### Gotchas I hit
- Multiplied `nums[i]` instead of `nums[i-1]` — `prefix[i]` is everything **strictly left** of `i`, so use `nums[i-1]`
- Tried dual-pointer (i and j in same loop) — overcomplicated, two separate loops are cleaner
- `prefix[-1]` in Python silently wraps to the last element — start loops at `range(1, n)` to avoid

### Space optimization (O(1) auxiliary)
Interviewers will ask: "Can you do it without the prefix/suffix arrays?"

**Trick:** write prefix products directly into the output array, then walk backward maintaining a single `running_suffix` variable.

```python
answer = [1] * n
for i in range(1, n):
    answer[i] = answer[i-1] * nums[i-1]

running_suffix = 1
for i in range(n-1, -1, -1):
    answer[i] *= running_suffix
    running_suffix *= nums[i]
```

**Why this is O(1) auxiliary:**
- Output array doesn't count (convention)
- Prefix array → folded into output
- Suffix array → replaced with one scalar (you only ever need the suffix at the current index)

### Takeaways
- **"Except self" / "all except this" → prefix-suffix arrays**
- **Two passes (one each direction)** is almost always cleaner than dual-pointer in one loop
- **Folding an array into a running variable** is a common space-optimization trick — applies anywhere you only need one value at a time