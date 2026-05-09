class Solution:

    def encode(self, strs: List[str]) -> str:
        return "\u200c".join(strs)
    def decode(self, s: str) -> List[str]:
        x = s.split("\u200c")
        if not x:
            return []
        else:
            return x
