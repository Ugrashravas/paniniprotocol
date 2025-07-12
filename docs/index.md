<!-- MathJax for rendering inline/block LaTeX -->
<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>

# Pāṇini Protocol

Welcome to the official dashboard for the first decipherment of the United States constitution as Pāṇinian Sanskrit!

<div style="text-align: center;">
<img src="img/paniniprotocol.jpeg" alt="Ugrashravas smiting the dragon of garbled speech with a lightning of pure speech, weapon of the first grammarian Indra" width="80%">
</div>

---
# Background

Yajnadevam (@yajnadevam) has made waves online and in media by claiming to have deciphered the Indus Valley Civilization (IVC) script, a problem that has stumped linguists, epigraphers, and historians for over a century. Unlike traditional approaches rooted in archaeology and linguistics, Yajnadevam claims his method is based on cryptography and information theory, and therefore, "mathematically correct".

However, Yajnadevam’s proposed readings, supposedly in Sanskrit, are riddled with ungrammatical constructions, violating basic rules of Sanskrit grammar. The issues are so fundamental that even beginner-level students of Sanskrit can recognize them as artificial and incorrect. Multiple scholars and enthusiasts have pointed this out, yet he continues to assert the correctness of his "Sanskrit" by citing obscure Vedic usages and far-fetched interpretations of Pāṇini's Aṣṭādhyāyī stretched beyond reasonable bounds.

The truth is simply that, by torturing Pāṇini’s rules in this way, *anything* can be made to look like "Sanskrit." During our long exchanges, I laid out these deficiencies clearly, and even offered constructive suggestions: I showed how his own set-intersection method could be meaningfully adapted, if the goal were actually to decipher a text written in proper Sanskrit.

However, Yajnadevam refused to acknowledge any flaw. In fact, he issued a challenge: if my critique is valid, then I should be able to “decipher” *even the U.S. Constitution* as Sanskrit using his methods.

<div style="text-align: center;">
<img src="img/challenge.jpeg" alt="YD's Challenge" width="400">
</div>

... and, that’s exactly what I’ve done.

This isn’t just a rebuttal. It’s a demonstration of how methodological abuse can produce false “decipherments,” and how mathematical jargon can be used to dazzle rather than to clarify.

---
## Statement of the challenge

What counts as *deciphering* the U.S. Constitution? For the purposes of this demonstration, we shall adopt the **same metric** that Yajnadevam uses to claim that his Indus Valley Civilization (IVC) decipherment is valid: **unicity distance**.

From his own website:

> **"How do we know this is all correct?**  
> The correctness of the decipherment is judged simply by being able to read the corpus beyond the unicity distance. Even if all sign values were derived in a dream, thats the only thing that matters."  
> — [Yajnadevam / ScriptDerivation](https://github.com/yajnadevam/ScriptDerivation)

Thus, to demonstrate a successful “decipherment” of the U.S. Constitution, we must simply **cross this unicity distance** — by Yajnadevam’s own criterion.

We shall use the **same formula** from his paper to compute the unicity distance (The relevant section is *2.4.2: "Unicity Distance"*)

YD assumes a the following increases in equivocation due to conflating:
- Aspirated and unaspirated phonemes: **10%**
- Retroflex and dental phonemes **10%**
- All sibilants: **150%**

We instead use **more conservative estimates**:
- Aspirated and unaspirated phonemes: **20%**
- Retroflex and dental phonemes **20%**
- All sibilants: **200%**

These assumptions are summarized in the following section.

Using these, the unicity distance \( U \) is computed as:

<div style="text-align: center;">
  <code>U = (26 + 18 × 0.2 + 1 × 2) / 0.7 ≈ 45.143</code>
</div>

Hence, if our "decipherment" of the U.S. Constitution produces *coherent output beyond 46 characters*, it meets the same standard that Yajnadevam sets for his own work.

---

## Latin to Sanskrit Phoneme Class Mapping (Jefferson's Key)

Now, to begin our "decipherment" of the U.S. Constitution, we require a mapping from **Latin letters to Sanskrit phonemes**.  Luckily, such a key was revealed by Thomas Jefferson in a dream to Ugraśravas:

<div style="text-align: center;">
<img src="img/revelation.png" alt="Thomas Jefferson revealing the one-key-to-rule-them-all to Ugraśravas in a dream" width="400">
</div>

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

**NOTE 1:**  This mapping is exactly as valid as Yajnadevam's, since, by his own standards, origin doesn't matter as long as the unicity threshold is crossed.

**NOTE 2:** the phoneme classes in this table are nearly replicas of Yajnadevam's own, with very few modifications.

**NOTE 3:** The scheme used to read the constitution using this table is much stricter and more conservative than Yajnadevam's, as we do not perform aribtrary consonant doubling.

---
## [📄 View Translations](translation.md)

---

## Translation Summary

The unicity distance is **46** symbols, indicated by the red marker. As of date, **1000+** have been translated, indicated by the green progress bar. Note that this graphic is not always upto date; for the live count, see the bottom row in the [translation page](translation.md)

<h3>Progress in first 1500 symbols</h3>

<div style="position: relative; width: 100%; max-width: 600px; height: 30px; background: #eee; border-radius: 6px; overflow: hidden; border: 1px solid #ccc;">

  <!-- Green progress bar -->
  <div style="width: 67%; height: 100%; background: #4caf50;"></div>

  <!-- Unicity Distance marker -->
  <div style="
    position: absolute;
    left: 3%;
    top: 0;
    bottom: 0;
    width: 2px;
    background: red;
    z-index: 2;">
  </div>

  <!-- Label for the red marker -->
  <div style="
    position: absolute;
    left: 3%;
    top: 100%;
    transform: translateX(-50%);
    font-size: 0.9rem;
    color: red;
    margin-top: 4px;">
    UD Threshold
  </div>
</div>

<p style="margin-top: 0.5rem;">Current progress: <strong>67.53%</strong>. Last updated: 2025-Jul-12, 21:38 (GMT +5:30)</p>

