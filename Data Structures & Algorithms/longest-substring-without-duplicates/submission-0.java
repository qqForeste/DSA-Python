class Solution {
    public int lengthOfLongestSubstring(String s) {
        // hashmap + sliding window (dynamic)

        int left = 0;
        Map<Character,Integer> charmap = new HashMap<>();
        int longest = 0;


        for (int right = 0; right < s.length(); right++)
        {
            charmap.put(s.charAt(right), charmap.getOrDefault(s.charAt(right), 0) + 1);

            while (charmap.get(s.charAt(right)) > 1)
            {
                 charmap.put(s.charAt(left), charmap.getOrDefault(s.charAt(left), 0) - 1);
                 if (charmap.get(s.charAt(left)) <= 0)
                 {
                    charmap.remove(s.charAt(left));
                 }
                left += 1;
            }

            longest = Math.max(longest, right - left + 1);
        }

        return longest;

    }
}
