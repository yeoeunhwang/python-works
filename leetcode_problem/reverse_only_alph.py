def reverse_only_letter(S):
    alp = []
    for c in S:
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            alp.append(c)
    alp = list(reversed(alp))
    changed_s = []
    for c in S:
        changed_s.append(c)
    order = 0
    for i in range(len(changed_s)):
        if changed_s[i] in alp:
            changed_s[i] = alp[order]
            order += 1
    return ''.join(changed_s)


print(reverse_only_letter('ab_cd'))
