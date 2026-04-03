 
class Solution:
    def survivedRobotsHealths(self, positions, healths, directions: str):
        paired = [(i, list(t)) for i, t in sorted(enumerate(zip(positions, healths, directions)), key=lambda x: x[1][0])]
        ans = []

        left = []
        right = []

        for i, n in enumerate(paired):
            if n[1][2] == 'R':
                if left:
                    if paired[left[-1]][1][1] > n[1][1]:
                        paired[left[-1]][1][1] -= 1
                    elif paired[left[-1]][1][1] == n[1][1]:
                        left.pop()
                    else:
                        while left and paired[left[-1]][1][1] < n[1][1]:
                            n[1][1] -= 1
                            left.pop()

                        if not left:
                            right.append(i)
                        else:
                            if paired[left[-1]][1][1] == n[1][1]:
                                left.pop()
                            else: 
                                paired[left[-1]][1][1] -= 1
                else:
                    right.append(i)
            else:
                if right:
                    if paired[right[-1]][1][1] > n[1][1]:
                        paired[right[-1]][1][1] -= 1
                    elif paired[right[-1]][1][1] == n[1][1]:
                        right.pop()
                    else:
                        while right and paired[right[-1]][1][1] < n[1][1]:
                            n[1][1] -= 1
                            right.pop()

                        if not right:
                            ans.append(i)
                        else:
                            if paired[right[-1]][1][1] == n[1][1]:
                                right.pop()
                            else: 
                                paired[right[-1]][1][1] -= 1
                else:
                    ans.append(i)

        ans += left + right

        return [paired[i][1][1] for i in sorted(ans, key=lambda i: paired[i][0])]

if __name__ == "__main__":
    yes = Solution()

    positions  = [3,2,30,24,38,7]
    healths    = [47,12,49,11,47,38]
    directions = "RRLRRR"

    print(yes.survivedRobotsHealths(positions, healths, directions))
