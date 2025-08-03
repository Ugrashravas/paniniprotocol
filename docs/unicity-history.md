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

Our assumptions are summarized in this table:

<table border="1" cellpadding="6" cellspacing="0">
  <thead>
    <tr>
      <th>Latin Symbol</th>
      <th>Sanskrit Phoneme Class</th>
      <th>Assumed Increase in Equivocation</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>E</td><td>अ, आ</td><td>20%</td></tr>
    <tr><td>T</td><td>श, ष, स, ह</td><td>200%</td></tr>
    <tr><td>A</td><td>त, थ, ट, ठ</td><td>20%</td></tr>
    <tr><td>O</td><td>इ, ई, य्</td><td>20%</td></tr>
    <tr><td>I, J</td><td>न</td><td>0%</td></tr>
    <tr><td>N</td><td>र, ऋ, ॠ</td><td>20%</td></tr>
    <tr><td>S, Z</td><td>व</td><td>0%</td></tr>
    <tr><td>H, X</td><td>म</td><td>0%</td></tr>
    <tr><td>R</td><td>य</td><td>0%</td></tr>
    <tr><td>D</td><td>द, ध, ड, ढ</td><td>20%</td></tr>
    <tr><td>L</td><td>ए, ऐ, अय्</td><td>20%</td></tr>
    <tr><td>U</td><td>उ, ऊ, व्</td><td>20%</td></tr>
    <tr><td>C</td><td>प, फ</td><td>20%</td></tr>
    <tr><td>M</td><td>क, ख</td><td>20%</td></tr>
    <tr><td>W</td><td>ओ, औ, अव्</td><td>20%</td></tr>
    <tr><td>F</td><td>ब, भ</td><td>20%</td></tr>
    <tr><td>G, Q</td><td>च, छ</td><td>20%</td></tr>
    <tr><td>Y</td><td>अस्, अः</td><td>20%</td></tr>
    <tr><td>P</td><td>अन्, अं, ङ्, ञ्</td><td>20%</td></tr>
    <tr><td>B</td><td>ग, घ</td><td>20%</td></tr>
    <tr><td>V</td><td>ज, झ</td><td>20%</td></tr>
    <tr><td>K</td><td>ल, ऌ</td><td>20%</td></tr>
  </tbody>
</table>


Using these, the unicity distance \( U \) was computed as:

$$U = \frac{(26 + 18 × 0.2 + 1 × 2)}{0.7} \approx 45.143$$

Hence, if our "decipherment" of the U.S. Constitution produced *coherent output beyond 46 characters*, it would've met the same standard that Yajnadevam set for his own work.

## The First Revision: Actually Considering the Keyspace

Immediately after we crossed **46** symbols, it was pointed out by one of his followers that a "better formula" was available in his discord server:
<!-- <blockquote class="twitter-tweet"><p lang="en" dir="ltr">Personally I have some doubts on the unicity distance calculation, it seemed off when I read it in your original thread. But it would require me to brush up on the fundamentals and work is going to keep me busy for a couple of weeks<br><br>Yes I saw your argument that you used YD&#39;s…</p>&mdash; The Butter Thief (@TheButterThief) <a href="https://twitter.com/TheButterThief/status/1942934255320916056?ref_src=twsrc%5Etfw">July 9, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>  -->
<div style="text-align: center;">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">the discord is already public dude, i am not trying to hide anything, anyways here goes <a href="https://t.co/1RgZ7zNndV">pic.twitter.com/1RgZ7zNndV</a></p>&mdash; The Butter Thief (@TheButterThief) <a href="https://twitter.com/TheButterThief/status/1942948814710616119?ref_src=twsrc%5Etfw">July 9, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
</div>
<br>

The primary distinguishing feature of this approach is that it actually considers all possible phoneme-combinations that can act as the key, as compared to the previous formula which arbitrarily weighted phoneme classes linearly thus missing the exponential growth in keyspace due to many-many mappings. Even here, one of the formulae used his subjectively reduced list of ciphertext symbols.

So, using our complete ciphertext and our subjectively reduced one due to the allograph table, we end up with two possible unicity distances, again using the same methods as Yajnadevam - namely:

$$\frac{3+\log_2{(2^{26})^{52}}}{0.7\log_2{52}} \approx 339.57$$

and

$$\frac{3+\log_2{(2^{26})^{81}}}{0.7\log_2{81}} \approx 475.225$$

And sure enough, we crossed these distances as well.

## The Second Revision

Based on the latest exchange, we expect a second revision of unicity distance:

<div style="text-align: center;">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">However, I anticipate some flaws in your yet-to-come formula already:<br>#1 will be some extra term bce I&#39;ve &quot;included vowels /e/ /ai/ and non-vowel /ay/ in the same class&quot;. However, /ay/ is grammatically the SAME as dipthong /e/, as is explicitly mentioned in sUtra eco&#39;yavAyAvaH.</p>&mdash; उ॒ग्रश्र॑वस् (@Ugrashravas) <a href="https://twitter.com/Ugrashravas/status/1944786561943662935?ref_src=twsrc%5Etfw">July 14, 2025</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
</div>
<br>

~~It is yet to be seen by how much this will increase the unicity distance.~~

## Final Note

Apart from the fact that [Unicity Distance is not a measure of correctness](methodology-flaws.md), all formualtions used by Yajnadevam for finding unicity distance are faulty as they use constructs developed for ciphers with reversible keys. In Shannon's own words (emphasis added):

> A secrecy system is defined abstractly as a set of transformations of one space (the set of possible messages) into a second space (the set of possible cryptograms). Each particular transformation of the set corresponds to enciphering with a particular key. The transformations are supposed **reversible** (non-singular) so that **unique deciphering is possible when the key is known**.
>
> — [Communication Theory of Secrecy Systems](https://www.andrew.cmu.edu/course/18-330/2025s/reading/shannon1949.pdf), Pg 657

As we've seen, Yajnadevam's key is not reversible. Knowing the key does not allow us to create a unique ciphertext or recover a unique plaintext. The same message (say रव) can be encoded as many different cryptograms (<img src="img/symbols/va1.png" height="25"><img src="img/symbols/ra1.png" height="25">, <img src="img/symbols/va2.png" height="25"><img src="img/symbols/ra2.png" height="25">, <img src="img/symbols/va3.png" height="25"><img src="img/symbols/ra3.png" height="25">, and $$267$$ others) and the same cryptogram (say <img src="img/symbols/ta1.png" height="25"><img src="img/symbols/sa1.png" height="25">) can be deciphered as many different messages (सट, षत, स्थ, हट्ठ, and $$92$$ others).


Finally, the redundancy of the "language" generated by abusing the very liberal rules of Pāṇini is likely much lower than the 0.7 for most real languages. This was [pointed out by us at the very beginning](https://x.com/Ugrashravas/status/1945699993891053864), but was met with dismissal. Presently, however, Yajnadevam seems to have entered a fascinating state where he simultaneously believes and denies it:

> 3. Panini redundancy may need to be accounted for. Depending on the number of kridantas used etc. I have speculated that Panini redundancy is much lower than the 0.7 for most languages.
>
> — [Yajnadevam, Jul 17 4:13 AM](https://x.com/yajnadevam/status/1945615379222376841)

> "If you torture Panini, you can read anything" is a Bollywood rendition of "Panini grammar has a very low redundancy". Of course you can't read anything. You can't read एएएएएए. The redundancy is not close to zero. It is closer to 0.7 than it is to 0.
>
> — [Also   Yajnadevam, Jul 17 10:23 AM](https://x.com/yajnadevam/status/1945708422218821663)

## Summary

We had anticipated Yajnadevam to start adjusting and negotiating the unicity distance upward a couple times before finally devolving into [word salad and goalpost shifts](dancing-goalposts.md). In that spirit, we visualized the history of UD values: earlier ones are shown in pink, while the most recent value provided by Yajnadevam appears in red. 

The red marker has moved **2** times as of date. Presently, Yajnadevam seems to have given up on hard math and shifted to [fuzzy word salad](dancing-goalposts.md).

As of date, the unicity distance is **475**, and **508+** symbols have been translated (green bar). This may be outdated — see the [translation page](translation.md) for live numbers.

<h3>Progress in first 1000 symbols</h3>

<div style="position: relative; width: 100%; max-width: 600px; height: 30px; background: #eee; border-radius: 6px; overflow: hidden; border: 1px solid #ccc;">

  <!-- Green progress bar -->
  <div style="width: 51%; height: 100%; background: #4caf50;"></div>

  <!-- Unicity Distance marker -->
  <div style="
    position: absolute;
    left: 5%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: pink;
    z-index: 2;">
  </div>
  <!-- Unicity Distance marker -->
  <div style="
    position: absolute;
    left: 34%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: pink;
    z-index: 2;">
  </div>
  <!-- Unicity Distance marker -->
  <div style="
    position: absolute;
    left: 48%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: red;
    z-index: 2;">
  </div>

</div>

<p style="margin-top: 0.5rem;">Current progress: <strong>50.80%</strong>. Last updated: 2025-Jul-14, 21:49 (GMT +5:30)</p>

[⬅️ Back to Overview](index.md)