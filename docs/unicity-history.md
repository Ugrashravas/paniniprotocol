---
title: Unicity Distance History
nav_order: 3
---

<!-- MathJax for rendering inline/block LaTeX -->
<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>


[⬅️ Back to Overview](index.md)
## The Original Approach: Linear & Arbitrary

We began by using the **same formula** from YD's paper to compute the unicity distance (The relevant section is *2.4.2: "Unicity Distance"*)

YD assumed the following arbitrary increases in equivocation due to conflating:
- Aspirated and unaspirated phonemes: **10%**
- Retroflex and dental phonemes **10%**
- All sibilants: **150%**

We instead used **more conservative estimates**:
- Aspirated and unaspirated phonemes: **20%**
- Retroflex and dental phonemes **20%**
- All sibilants: **200%**

Our assumptions are summarized in this [section](index.md#latin-to-sanskrit-phoneme-class-mapping-jeffersons-key).

Using these, the unicity distance \( U \) was computed as:

$$U = \frac{(26 + 18 × 0.2 + 1 × 2)}{0.7} \approx 45.143$$

Hence, if our "decipherment" of the U.S. Constitution produced *coherent output beyond 46 characters*, it would've met the same standard that Yajnadevam set for his own work.

## The First Revision: Actually Considering the Keyspace

Immediately after we crossed **46** symbols, it was pointed out by one of his followers that a "better formula" was available in his discord server:
<!-- <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Personally I have some doubts on the unicity distance calculation, it seemed off when I read it in your original thread. But it would require me to brush up on the fundamentals and work is going to keep me busy for a couple of weeks<br><br>Yes I saw your argument that you used YD&#39;s…</p>&mdash; The Butter Thief (@TheButterThief) <a href="https://twitter.com/TheButterThief/status/1942934255320916056?ref_src=twsrc%5Etfw">July 9, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>  -->
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">the discord is already public dude, i am not trying to hide anything, anyways here goes <a href="https://t.co/1RgZ7zNndV">pic.twitter.com/1RgZ7zNndV</a></p>&mdash; The Butter Thief (@TheButterThief) <a href="https://twitter.com/TheButterThief/status/1942948814710616119?ref_src=twsrc%5Etfw">July 9, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 


The primary distinguishing feature of this approach is that it actually considers all possible phoneme-combinations that can act as the key, as compared to the previous formula which arbitrarily weighted phoneme classes linearly thus missing the exponential growth in keyspace due to many-many mappings. Even here, one of the formulae used his subjectively reduced list of ciphertext symbols.

So, using our complete ciphertext and our subjectively reduced one due to the allograph table, we end up with two possible unicity distances, again using the same methods as Yajnadevam - namely:

$$\frac{3+\log_2{(2^{26})^{52}}}{0.7\log_2{52}} \approx 339.57$$

and

$$\frac{3+\log_2{(2^{26})^{81}}}{0.7\log_2{81}} \approx 475.225$$

And sure enough, we crossed these distances as well. (Of course, this formula is also faulty as it does not account properly for the phoneme classes arbitrarily chosen by YD. His 48 is not a magic number, and there are a lot many more ways of choosing upto pairs of two phonemes to populate his phoneme classes.)

## The Second Revision

Based on the latest exchange, we expect a second revision of unicity distance:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">However, I anticipate some flaws in your yet-to-come formula already:<br>#1 will be some extra term bce I&#39;ve &quot;included vowels /e/ /ai/ and non-vowel /ay/ in the same class&quot;. However, /ay/ is grammatically the SAME as dipthong /e/, as is explicitly mentioned in sUtra eco&#39;yavAyAvaH.</p>&mdash; उ॒ग्रश्र॑वस् (@Ugrashravas) <a href="https://twitter.com/Ugrashravas/status/1944786561943662935?ref_src=twsrc%5Etfw">July 14, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

It is yet to be seen by how much this will increase the unicity distance.

[⬅️ Back to Overview](index.md)