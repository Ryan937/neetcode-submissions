class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length)
            return false

        const dict: number[] = Array(26).fill(0);

        for (let i = 0; i < s.length; i++) {
            dict[s[i].charCodeAt(0) - 'a'.charCodeAt(0)]++;
            dict[t[i].charCodeAt(0) - 'a'.charCodeAt(0)]--;
        }

        for (const num of dict) {
            if (num !== 0)
                return false;
        }

        return true
    }
}
