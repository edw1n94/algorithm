def solution(s):
    answer = 0
    if len(s) < 2:
        return len(s)

    for n in range(1, int(len(s) / 2) + 1):
        list_str = []
        index = 0
        while (index < len(s)):
            target = s[index:index + n]
            cnt = 0
            for j in range(index, len(s), n):
                if (target == s[j:j + n]):
                    cnt += 1
                else:
                    break

            if cnt > 1:
                list_str.append(str(cnt) + target)
            else:
                list_str.append(target)

            if cnt == 0:
                index += n
            else:
                index += cnt * n

        new_str = (''.join(list_str))
        if answer == 0:
            answer = len(new_str)
        else:
            if len(new_str) < answer:
                answer = len(new_str)

    return answer


s = "ababcdcdababcdcd"
s2 = "aabbaccc"
s3 = "abcabcdede"

answer = solution(s3)
