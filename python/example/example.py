from rustx3dh import x3dh_ser

u1_shared_secret_key, u2_shared_secret_key = x3dh_ser.gen_3xdh_secrets_key_pairs()

print(f"[u1_shared_secret_key]:{u1_shared_secret_key}")
print(f"[u2_shared_secret_key]:{u2_shared_secret_key}")