# Constraints

These are the ground rules for designing this library:

- This library should be generally interoperable with well-known ML tools, at
  least:
  - Numpy
  - PyTorch/TensorFlow/Jax
- This library should *in concept* be simple to understand to a beginner to the
  field (or at least to someone with intermediate software engineering
  knowledge, even if the implementation is complex.
- This library should expose an opinionated implementation for creating
  neurosymbolic programs but be open to extension or modification.
- Every public interface must be documented in a way that makes its purpose and
  function clear to someone who has never used the library before. 
- The high-level interface for using the library matters more than the low-level
  implementation detail.
  - We should have ease of use similar to Hugging Face's libraries.
  - Practically speaking, a bored high-schooler should be able to use this
    library with minimal assistance.