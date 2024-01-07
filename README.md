# RustX3DH

Embeded the [xxxdh](https://github.com/alexyer/xxxdh/tree/master), which iplementation of the Extended Triple Diffie-Hellman key exchange protocol written in Rust, on Python. [xxxdh](https://github.com/alexyer/xxxdh/tree/master) is written by [Olexander Yermakov](https://github.com/alexyer).

Implementation is close to the [Signal Spec](https://signal.org/docs/specifications/x3dh/), but Ristretto point Curve25519 used as a *curve* for the default implementation. Though underlying algorithms could be changed fairly easily.

## Usage

```python
//! Basic example.

from x3dh import x3dh_ser

u1_shared_secret_key, u2_shared_secret_key = x3dh_ser.gen_3xdh_secrets_key_pairs()

print(f"[u1_shared_secret_key]:{u1_shared_secret_key}")
print(f"[u2_shared_secret_key]:{u2_shared_secret_key}")
```
