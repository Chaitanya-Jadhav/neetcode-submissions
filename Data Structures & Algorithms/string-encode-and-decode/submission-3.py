class Solution:

    def encode(self, strs: List[str]) -> str:
        return "\u200c".join(strs)
    def decode(self, s: str) -> List[str]:
        return s.split("\u200c")
