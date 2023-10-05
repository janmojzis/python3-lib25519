if __name__ == '__main__':

    from lib25519 import x25519

    pk1, sk1 = x25519.keypair()
    pk2, sk2 = x25519.keypair()
    k1 = x25519.dh(pk1, sk2)
    k2 = x25519.dh(pk2, sk1)
    assert (k1 == k2)

    print('x25519 OK')
